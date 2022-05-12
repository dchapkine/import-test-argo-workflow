package util

import (
	"fmt"
	"hash/fnv"
	"os"

	"github.com/argoproj/argo-workflows/v3/pkg/apis/workflow/v1alpha1"
	"github.com/argoproj/argo-workflows/v3/workflow/common"
)

const (
	maxK8sResourceNameLength = 253
	k8sNamingHashLength      = 10
)

// PodNameVersion stores which type of pod names should be used.
// v1 represents the node id.
// v2 is the combination of a node id and template name.
type PodNameVersion string

const (
	// PodNameV1 is the v1 name that uses node ids for pod names
	PodNameV1 PodNameVersion = "v1"
	// PodNameV2 is the v2 name that uses node id combined with
	// the template name
	PodNameV2             PodNameVersion = "v2"
	DefaultPodNameVersion PodNameVersion = PodNameV2
)

// String stringifies the pod name version
func (v PodNameVersion) String() string {
	return string(v)
}

// GetPodNameVersion returns the pod name version to be used
func GetPodNameVersion() PodNameVersion {
	switch os.Getenv("POD_NAMES") {
	case "v2":
		fmt.Println("GetPodNameVersion: v2 is set")
		return PodNameV2
	case "v1":
		fmt.Println("GetPodNameVersion: v1 is set")
		return PodNameV1
	default:
		fmt.Println("default PodNameVersion is v2")
		return DefaultPodNameVersion
	}
}

// PodName return a deterministic pod name
func PodName(workflowName, nodeName, templateName, nodeID string, version PodNameVersion) string {
	if version == PodNameV1 {
		fmt.Printf("pod name set to v1: %s\n", nodeID)
		return nodeID
	}

	if workflowName == nodeName {
		fmt.Printf("workflowName == nodeName, so using %s\n", workflowName)
		return workflowName
	}

	prefix := fmt.Sprintf("%s-%s", workflowName, templateName)
	prefix = ensurePodNamePrefixLength(prefix)

	h := fnv.New32a()
	_, _ = h.Write([]byte(nodeName))

	fmt.Printf("pod name set to v2: %s, nodename='%s', sum32=%v\n", fmt.Sprintf("%s-%v", prefix, h.Sum32()), nodeName, h.Sum32())
	return fmt.Sprintf("%s-%v", prefix, h.Sum32())

}

func ensurePodNamePrefixLength(prefix string) string {
	maxPrefixLength := maxK8sResourceNameLength - k8sNamingHashLength

	if len(prefix) > maxPrefixLength-1 {
		return prefix[0 : maxPrefixLength-1]
	}

	return prefix
}

// GetWorkflowPodNameVersion gets the pod name version from the annotation of a
// given workflow
func GetWorkflowPodNameVersion(wf *v1alpha1.Workflow) PodNameVersion {
	annotations := wf.GetAnnotations()
	fmt.Printf("annotations: %v\n", annotations)
	version := annotations[common.AnnotationKeyPodNameVersion]

	switch version {
	case PodNameV1.String():
		return PodNameV1
	case PodNameV2.String():
		return PodNameV2
	default:
		return DefaultPodNameVersion
	}
}
