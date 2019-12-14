package fixtures

import (
	"bufio"
	"fmt"
	alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	v12 "k8s.io/client-go/kubernetes/typed/core/v1"
	"os"
	"path/filepath"
	"time"

	log "github.com/sirupsen/logrus"
	"github.com/stretchr/testify/suite"
	v1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"sigs.k8s.io/yaml"

	// load the gcp plugin (required to authenticate against GKE clusters).
	_ "k8s.io/client-go/plugin/pkg/client/auth/gcp"

	"github.com/argoproj/argo/cmd/argo/commands"
	"github.com/argoproj/argo/pkg/client/clientset/versioned/typed/workflow/v1alpha1"
)

var kubeConfig = os.Getenv("KUBECONFIG")

func init() {
	if kubeConfig == "" {
		kubeConfig = filepath.Join(os.Getenv("HOME"), ".kube", "config")
	}
	_ = commands.NewCommand()
}

type E2ESuite struct {
	suite.Suite
	client     v1alpha1.WorkflowInterface
	kubeClient kubernetes.Interface
}

func (s *E2ESuite) SetupSuite() {
	_, err := os.Stat(kubeConfig)
	if os.IsNotExist(err) {
		s.T().Skip("Skipping test: " + err.Error())
	}
}

func (s *E2ESuite) BeforeTest(_, _ string) {
	config, err := clientcmd.BuildConfigFromFlags("", kubeConfig)
	if err != nil {
		panic(err)
	}
	s.kubeClient, err = kubernetes.NewForConfig(config)
	if err != nil {
		panic(err)
	}
	s.client = commands.InitWorkflowClient()
	// delete all workflows
	log.WithFields(log.Fields{"test": s.T().Name()}).Info("Deleting all existing workflows")
	err = s.client.DeleteCollection(nil, metav1.ListOptions{})
	if err != nil {
		panic(err)
	}
	// wait for workflow pods to be deleted
	for {
		pods, err := s.kubeClient.CoreV1().Pods("argo").List(metav1.ListOptions{LabelSelector: "workflows.argoproj.io/workflow"})
		if err != nil {
			panic(err)
		}
		if len(pods.Items) == 0 {
			break
		}
		log.WithFields(log.Fields{"test": s.T().Name()}).Info("Waiting for workflow pods to go away")
		time.Sleep(1 * time.Second)
	}
}

func (s *E2ESuite) AfterTest(_, _ string) {
	// TODO - only on failure?
	if s.T().Failed() || true {
		s.printDiagnostics()
	}
}

func (s *E2ESuite) printDiagnostics() {
	wfs, err := s.client.List(metav1.ListOptions{})
	if err != nil {
		s.T().Fatal(err)
	}
	for _, wf := range wfs.Items {
		s.printWorkflowDiagnostics(wf)
	}
}

func (s *E2ESuite) printWorkflowDiagnostics(wf alpha1.Workflow) {
	logCtx := log.WithFields(log.Fields{"test": s.T().Name(), "workflow": wf.Name})
	logCtx.Info("Workflow status:")
	s.printJSON(wf.Status)
	// print logs
	workflow, err := s.client.Get(wf.Name, metav1.GetOptions{})
	if err != nil {
		s.T().Fatal(err)
	}
	for _, node := range workflow.Status.Nodes {
		if node.Type != "Pod" {
			continue
		}
		logCtx := logCtx.WithFields(log.Fields{"node": node.DisplayName})
		s.printPodDiagnostics(logCtx, workflow.Namespace, node.ID)
	}
}

func (s *E2ESuite) printJSON(obj interface{}) {
	// print status
	bytes, err := yaml.Marshal(obj)
	if err != nil {
		s.T().Fatal(err)
	}
	fmt.Println("---")
	fmt.Println(string(bytes))
	fmt.Println("---")
}

func (s *E2ESuite) printPodDiagnostics(logCtx *log.Entry, namespace string, podName string) {
	logCtx = logCtx.WithFields(log.Fields{"pod": podName})
	pods := s.kubeClient.CoreV1().Pods(namespace)
	pod, err := pods.Get(podName, metav1.GetOptions{})
	if err != nil {
		logCtx.Error("Cannot get pod")
		return
	}
	logCtx.Info("Pod manifest:")
	s.printJSON(pod)
	for _, container := range append(pod.Status.InitContainerStatuses, pod.Status.ContainerStatuses...) {
		s.printPodLogs(logCtx, container, pods, podName)
	}
}

func (s *E2ESuite) printPodLogs(logCtx *log.Entry, container v1.ContainerStatus, pods v12.PodInterface, podName string) {
	logCtx = logCtx.WithFields(log.Fields{"container": container.Name, "image": container.Image})
	stream, err := pods.GetLogs(podName, &v1.PodLogOptions{Container: container.Name}).Stream()
	if err != nil {
		logCtx.WithField("err", err).Error("Cannot get logs")
		return
	}
	defer func() { _ = stream.Close() }()
	logCtx.Info("Container logs:")
	scanner := bufio.NewScanner(stream)
	fmt.Println("---")
	for scanner.Scan() {
		fmt.Println("  " + scanner.Text())
	}
	fmt.Println("---")
}

func (s *E2ESuite) Given() *Given {
	return &Given{
		t:      s.T(),
		client: s.client,
	}
}
