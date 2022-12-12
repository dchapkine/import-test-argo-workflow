package controller

import (
	apiv1 "k8s.io/api/core/v1"
	"k8s.io/utils/env"

	wfv1 "github.com/argoproj/argo-workflows/v3/pkg/apis/workflow/v1alpha1"
	wfretry "github.com/argoproj/argo-workflows/v3/workflow/util/retry"
)

// RetryTweak is a 2nd order function interface for tweaking the retry
type RetryTweak = func(retryStrategy wfv1.RetryStrategy, nodes wfv1.Nodes, pod *apiv1.Pod)

// FindRetryNode locates the closest retry node ancestor to nodeID.
// If boundaryID is set on the node we get the template name of the boundary node and try to find a node of type retry with
// the same template name
// If boundaryID is not set we get the template of the node and try to find a node of type retry with the name name as the template
func (woc *wfOperationCtx) FindRetryNode(nodes wfv1.Nodes, nodeID string) *wfv1.NodeStatus {
	node, ok := nodes[nodeID]
	if !ok {
		return nil
	}

	boundaryID := node.BoundaryID

	if boundaryID != "" {
		boundaryNode, ok := nodes[boundaryID]
		if !ok {
			return nil
		}
		templateName := boundaryNode.TemplateName
		for _, node := range nodes {
			if node.Type == wfv1.NodeTypeRetry && node.TemplateName == templateName {
				return &node
			}
		}
		return nil
	}
	// if we can't find it with boundaryID try getting it from the node template
	template, err := woc.GetNodeTemplate(&node)
	if err != nil || template == nil {
		return nil
	}
	for _, node := range nodes {
		if node.Type == wfv1.NodeTypeRetry && node.TemplateName == template.Name {
			return &node
		}
	}
	return nil
}

// RetryOnDifferentHost append affinity with fail host to pod
func RetryOnDifferentHost(retryNodeName string) RetryTweak {
	return func(retryStrategy wfv1.RetryStrategy, nodes wfv1.Nodes, pod *apiv1.Pod) {
		if retryStrategy.Affinity == nil {
			return
		}
		hostNames := wfretry.GetFailHosts(nodes, retryNodeName)
		hostLabel := env.GetString("RETRY_HOST_NAME_LABEL_KEY", "kubernetes.io/hostname")
		if hostLabel != "" && len(hostNames) > 0 {
			pod.Spec.Affinity = wfretry.AddHostnamesToAffinity(hostLabel, hostNames, pod.Spec.Affinity)
		}
	}
}
