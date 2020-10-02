package sync

import (
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	v1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes/fake"
	"k8s.io/utils/pointer"
	"sigs.k8s.io/yaml"

	argoErr "github.com/argoproj/argo/v3/errors"
	wfv1 "github.com/argoproj/argo/v3/pkg/apis/workflow/v1alpha1"
	fakewfclientset "github.com/argoproj/argo/v3/pkg/client/clientset/versioned/fake"
)

const configMap = `
apiVersion: v1
kind: ConfigMap
metadata:
 name: my-config
data:
 workflow: "1"
 template: "1"
`
const wfWithStatus = `
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  creationTimestamp: "2020-06-19T17:37:05Z"
  generateName: hello-world-
  generation: 4
  labels:
    workflows.argoproj.io/phase: Running
  name: hello-world-prtl9
  namespace: default
  resourceVersion: "844854"
  selfLink: /apis/argoproj.io/v1alpha1/namespaces/default/workflows/hello-world-prtl9
  uid: 790f5c47-211f-4a3b-8949-514ae916633b
spec:
  arguments: {}
  entrypoint: whalesay
  synchronization:
    semaphore:
      configMapKeyRef:
        key: workflow
        name: my-config
  templates:
  - arguments: {}
    container:
      args:
      - hello world
      command:
      - cowsay
      image: docker/whalesay:latest
      name: ""
      resources: {}
    inputs: {}
    metadata: {}
    name: whalesay
    outputs: {}
status:
  finishedAt: null
  nodes:
    hello-world-prtl9:
      displayName: hello-world-prtl9
      finishedAt: null
      hostNodeName: docker-desktop
      id: hello-world-prtl9
      message: ContainerCreating
      name: hello-world-prtl9
      phase: Pending
      startedAt: "2020-06-19T17:37:05Z"
      templateName: whalesay
      templateScope: local/hello-world-prtl9
      type: Pod
  phase: Running
  startedAt: "2020-06-19T17:37:05Z"
  synchronization:
    semaphore:
      holding:
      - holders:
        - hello-world-prtl9
        semaphore: default/configmap/my-config/workflow
`
const wfWithSemaphore = `
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
 name: hello-world
 namespace: default
spec:
 entrypoint: whalesay
 synchronization:
   semaphore:
     configMapKeyRef:
       name: my-config
       key: workflow
 templates:
 - name: whalesay
   container:
     image: docker/whalesay:latest
     command: [cowsay]
     args: ["hello world"]
`

const wfWithTmplSemaphore = `
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: semaphore-tmpl-level-xjvln
  namespace: default
spec:
  arguments: {}
  entrypoint: semaphore-tmpl-level-example
  templates:
  - arguments: {}
    inputs: {}
    metadata: {}
    name: semaphore-tmpl-level-example
    outputs: {}
    steps:
    - - arguments: {}
        name: generate
        template: gen-number-list
    - - arguments:
          parameters:
          - name: seconds
            value: '{{item}}'
        name: sleep
        template: sleep-n-sec
        withParam: '{{steps.generate.outputs.result}}'
  - arguments: {}
    inputs: {}
    metadata: {}
    name: gen-number-list
    outputs: {}
    script:
      command:
      - python
      image: python:alpine3.6
      name: ""
      resources: {}
      source: |
        import json
        import sys
        json.dump([i for i in range(1, 3)], sys.stdout)
  - arguments: {}
    container:
      args:
      - echo sleeping for {{inputs.parameters.seconds}} seconds; sleep 10; echo done
      command:
      - sh
      - -c
      image: alpine:latest
      name: ""
      resources: {}
    inputs:
      parameters:
      - name: seconds
    metadata: {}
    name: sleep-n-sec
    outputs: {}
    synchronization:
      semaphore:
        configMapKeyRef:
          key: template
          name: my-config
status:
  finishedAt: null
  nodes:
    semaphore-tmpl-level-xjvln:
      children:
      - semaphore-tmpl-level-xjvln-2790796867
      displayName: semaphore-tmpl-level-xjvln
      finishedAt: null
      id: semaphore-tmpl-level-xjvln
      name: semaphore-tmpl-level-xjvln
      phase: Running
      startedAt: "2020-06-04T19:55:11Z"
      templateName: semaphore-tmpl-level-example
      templateScope: local/semaphore-tmpl-level-xjvln
      type: Steps
    semaphore-tmpl-level-xjvln-5807216:
      boundaryID: semaphore-tmpl-level-xjvln
      children:
      - semaphore-tmpl-level-xjvln-2858054438
      displayName: generate
      finishedAt: "2020-06-04T19:55:25Z"
      hostNodeName: k3d-k3s-default-server
      id: semaphore-tmpl-level-xjvln-5807216
      name: semaphore-tmpl-level-xjvln[0].generate
      outputs:
        artifacts:
        - archiveLogs: true
          name: main-logs
          s3:
            accessKeySecret:
              key: accesskey
              name: my-minio-cred
            bucket: my-bucket
            endpoint: minio:9000
            insecure: true
            key: semaphore-tmpl-level-xjvln/semaphore-tmpl-level-xjvln-5807216/main.log
            secretKeySecret:
              key: secretkey
              name: my-minio-cred
        exitCode: "0"
        result: '[1, 2]'
      phase: Succeeded
      resourcesDuration:
        cpu: 9
        memory: 9
      startedAt: "2020-06-04T19:55:11Z"
      templateName: gen-number-list
      templateScope: local/semaphore-tmpl-level-xjvln
      type: Pod
    semaphore-tmpl-level-xjvln-1607747183:
      boundaryID: semaphore-tmpl-level-xjvln
      displayName: sleep(1:2)
      finishedAt: null
      hostNodeName: k3d-k3s-default-server
      id: semaphore-tmpl-level-xjvln-1607747183
      inputs:
        parameters:
        - name: seconds
          value: "2"
      message: ContainerCreating
      name: semaphore-tmpl-level-xjvln[1].sleep(1:2)
      phase: Pending
      startedAt: "2020-06-04T19:55:56Z"
      templateName: sleep-n-sec
      templateScope: local/semaphore-tmpl-level-xjvln
      type: Pod
    semaphore-tmpl-level-xjvln-2790796867:
      boundaryID: semaphore-tmpl-level-xjvln
      children:
      - semaphore-tmpl-level-xjvln-5807216
      displayName: '[0]'
      finishedAt: "2020-06-04T19:55:56Z"
      id: semaphore-tmpl-level-xjvln-2790796867
      name: semaphore-tmpl-level-xjvln[0]
      phase: Succeeded
      startedAt: "2020-06-04T19:55:11Z"
      templateName: semaphore-tmpl-level-example
      templateScope: local/semaphore-tmpl-level-xjvln
      type: StepGroup
    semaphore-tmpl-level-xjvln-2858054438:
      boundaryID: semaphore-tmpl-level-xjvln
      children:
      - semaphore-tmpl-level-xjvln-3448864205
      - semaphore-tmpl-level-xjvln-1607747183
      displayName: '[1]'
      finishedAt: null
      id: semaphore-tmpl-level-xjvln-2858054438
      name: semaphore-tmpl-level-xjvln[1]
      phase: Running
      startedAt: "2020-06-04T19:55:56Z"
      templateName: semaphore-tmpl-level-example
      templateScope: local/semaphore-tmpl-level-xjvln
      type: StepGroup
    semaphore-tmpl-level-xjvln-3448864205:
      boundaryID: semaphore-tmpl-level-xjvln
      displayName: sleep(0:1)
      finishedAt: null
      hostNodeName: k3d-k3s-default-server
      id: semaphore-tmpl-level-xjvln-3448864205
      inputs:
        parameters:
        - name: seconds
          value: "1"
      message: ContainerCreating
      name: semaphore-tmpl-level-xjvln[1].sleep(0:1)
      phase: Pending
      startedAt: "2020-06-04T19:55:56Z"
      templateName: sleep-n-sec
      templateScope: local/semaphore-tmpl-level-xjvln
      type: Pod
  phase: Running
  startedAt: "2020-06-04T19:55:11Z"
`

func unmarshalWF(yamlStr string) *wfv1.Workflow {
	var wf wfv1.Workflow
	err := yaml.Unmarshal([]byte(yamlStr), &wf)
	if err != nil {
		panic(err)
	}
	return &wf
}

func GetSyncLimitFunc(kube *fake.Clientset) func(string) (int, error) {
	syncLimitConfig := func(lockName string) (int, error) {
		items := strings.Split(lockName, "/")
		if len(items) < 4 {
			return 0, argoErr.New(argoErr.CodeBadRequest, "Invalid Config Map Key")
		}

		configMap, err := kube.CoreV1().ConfigMaps(items[0]).Get(items[2], metav1.GetOptions{})

		if err != nil {
			return 0, err
		}

		value, found := configMap.Data[items[3]]

		if !found {
			return 0, argoErr.New(argoErr.CodeBadRequest, "Invalid Sync configuration Key")
		}
		return strconv.Atoi(value)
	}
	return syncLimitConfig
}

func TestSemaphoreWfLevel(t *testing.T) {
	kube := fake.NewSimpleClientset()
	var cm v1.ConfigMap
	err := yaml.Unmarshal([]byte(configMap), &cm)
	assert.NoError(t, err)
	_, err = kube.CoreV1().ConfigMaps("default").Create(&cm)
	assert.NoError(t, err)
	syncLimitFunc := GetSyncLimitFunc(kube)
	t.Run("InitializeSynchronization", func(t *testing.T) {
		concurrenyMgr := NewLockManager(syncLimitFunc, func(key string) {
		})
		wf := unmarshalWF(wfWithStatus)
		wfclientset := fakewfclientset.NewSimpleClientset(wf)

		wfList, err := wfclientset.ArgoprojV1alpha1().Workflows("default").List(metav1.ListOptions{})
		assert.NoError(t, err)
		concurrenyMgr.Initialize(wfList.Items)
		assert.Equal(t, 1, len(concurrenyMgr.syncLockMap))
	})
	t.Run("InitializeSynchronizationWithInvalid", func(t *testing.T) {
		concurrenyMgr := NewLockManager(syncLimitFunc, func(key string) {

		})
		wf := unmarshalWF(wfWithStatus)
		invalidSync := []wfv1.SemaphoreHolding{{Semaphore: "default/configmap/my-config1/workflow", Holders: []string{"hello-world-vcrg5"}}}
		wf.Status.Synchronization.Semaphore.Holding = invalidSync
		wfclientset := fakewfclientset.NewSimpleClientset(wf)
		wfList, err := wfclientset.ArgoprojV1alpha1().Workflows("default").List(metav1.ListOptions{})
		assert.NoError(t, err)
		concurrenyMgr.Initialize(wfList.Items)
		assert.Equal(t, 0, len(concurrenyMgr.syncLockMap))
	})

	t.Run("WfLevelAcquireAndRelease", func(t *testing.T) {
		var nextKey string
		concurrenyMgr := NewLockManager(syncLimitFunc, func(key string) {
			nextKey = key
		})
		wf := unmarshalWF(wfWithSemaphore)
		wf1 := wf.DeepCopy()
		wf2 := wf.DeepCopy()
		wf3 := wf.DeepCopy()
		status, wfUpdate, msg, err := concurrenyMgr.TryAcquire(wf, "", wf.Spec.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore.Holding)
		assert.Equal(t, wf.Name, wf.Status.Synchronization.Semaphore.Holding[0].Holders[0])

		// Try to acquire again
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf, "", wf.Spec.Synchronization)
		assert.NoError(t, err)
		assert.True(t, status)
		assert.Empty(t, msg)
		assert.False(t, wfUpdate)

		wf1.Name = "two"
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf1, "", wf1.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		wf2.Name = "three"
		wf2.Spec.Priority = pointer.Int32Ptr(5)
		holderKey2 := getHolderKey(wf2, "")
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf2, "", wf2.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		wf3.Name = "four"
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf3, "", wf3.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		concurrenyMgr.Release(wf, "", wf.Spec.Synchronization)
		assert.Equal(t, holderKey2, nextKey)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.Equal(t, 0, len(wf.Status.Synchronization.Semaphore.Holding[0].Holders))

		// Low priority workflow try to acquire the lock
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf1, "", wf1.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		// High Priority workflow acquires the lock
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf2, "", wf2.Spec.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf2.Status.Synchronization)
		assert.NotNil(t, wf2.Status.Synchronization.Semaphore)
		assert.Equal(t, wf2.Name, wf2.Status.Synchronization.Semaphore.Holding[0].Holders[0])

		concurrenyMgr.ReleaseAll(wf2)
		assert.Nil(t, wf2.Status.Synchronization)
	})
}

func TestResizeSemaphoreSize(t *testing.T) {
	kube := fake.NewSimpleClientset()
	var cm v1.ConfigMap
	err := yaml.Unmarshal([]byte(configMap), &cm)
	assert.NoError(t, err)
	_, err = kube.CoreV1().ConfigMaps("default").Create(&cm)
	assert.NoError(t, err)
	syncLimitFunc := GetSyncLimitFunc(kube)
	t.Run("WfLevelAcquireAndRelease", func(t *testing.T) {
		concurrenyMgr := NewLockManager(syncLimitFunc, func(key string) {
		})
		wf := unmarshalWF(wfWithSemaphore)
		wf.CreationTimestamp = metav1.Time{Time: time.Now()}
		wf1 := wf.DeepCopy()
		wf2 := wf.DeepCopy()
		status, wfUpdate, msg, err := concurrenyMgr.TryAcquire(wf, "", wf.Spec.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore)
		assert.Equal(t, wf.Name, wf.Status.Synchronization.Semaphore.Holding[0].Holders[0])

		wf1.Name = "two"
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf1, "", wf1.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		wf2.Name = "three"
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf2, "", wf2.Spec.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.False(t, status)
		assert.True(t, wfUpdate)

		// Increase the semaphore Size
		cm, err := kube.CoreV1().ConfigMaps("default").Get("my-config", metav1.GetOptions{})
		assert.NoError(t, err)
		cm.Data["workflow"] = "3"
		_, err = kube.CoreV1().ConfigMaps("default").Update(cm)
		assert.NoError(t, err)

		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf1, "", wf1.Spec.Synchronization)
		assert.NoError(t, err)
		assert.True(t, status)
		assert.Empty(t, msg)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf1.Status.Synchronization)
		assert.NotNil(t, wf1.Status.Synchronization.Semaphore)
		assert.Equal(t, wf1.Name, wf1.Status.Synchronization.Semaphore.Holding[0].Holders[0])

		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf2, "", wf2.Spec.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf2.Status.Synchronization)
		assert.NotNil(t, wf2.Status.Synchronization.Semaphore)
		assert.Equal(t, wf2.Name, wf2.Status.Synchronization.Semaphore.Holding[0].Holders[0])

	})
}

func TestSemaphoreTmplLevel(t *testing.T) {
	kube := fake.NewSimpleClientset()
	var cm v1.ConfigMap
	err := yaml.Unmarshal([]byte(configMap), &cm)
	assert.NoError(t, err)
	_, err = kube.CoreV1().ConfigMaps("default").Create(&cm)
	assert.NoError(t, err)
	syncLimitFunc := GetSyncLimitFunc(kube)
	t.Run("TemplateLevelAcquireAndRelease", func(t *testing.T) {
		//var nextKey string
		concurrenyMgr := NewLockManager(syncLimitFunc, func(key string) {
			//nextKey = key
		})
		wf := unmarshalWF(wfWithTmplSemaphore)
		tmpl := wf.Spec.Templates[2]

		status, wfUpdate, msg, err := concurrenyMgr.TryAcquire(wf, "semaphore-tmpl-level-xjvln-3448864205", tmpl.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore)
		assert.Equal(t, "semaphore-tmpl-level-xjvln-3448864205", wf.Status.Synchronization.Semaphore.Holding[0].Holders[0])

		// Try to acquire again
		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf, "semaphore-tmpl-level-xjvln-3448864205", tmpl.Synchronization)
		assert.NoError(t, err)
		assert.True(t, status)
		assert.False(t, wfUpdate)
		assert.Empty(t, msg)

		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf, "semaphore-tmpl-level-xjvln-1607747183", tmpl.Synchronization)
		assert.NoError(t, err)
		assert.NotEmpty(t, msg)
		assert.True(t, wfUpdate)
		assert.False(t, status)

		concurrenyMgr.Release(wf, "semaphore-tmpl-level-xjvln-3448864205", tmpl.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore)
		assert.Empty(t, wf.Status.Synchronization.Semaphore.Holding[0].Holders)

		status, wfUpdate, msg, err = concurrenyMgr.TryAcquire(wf, "semaphore-tmpl-level-xjvln-1607747183", tmpl.Synchronization)
		assert.NoError(t, err)
		assert.Empty(t, msg)
		assert.True(t, status)
		assert.True(t, wfUpdate)
		assert.NotNil(t, wf.Status.Synchronization)
		assert.NotNil(t, wf.Status.Synchronization.Semaphore)
		assert.Equal(t, "semaphore-tmpl-level-xjvln-1607747183", wf.Status.Synchronization.Semaphore.Holding[0].Holders[0])

	})
}
