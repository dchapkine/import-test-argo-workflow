// Code generated by informer-gen. DO NOT EDIT.

package v1alpha1

import (
	internalinterfaces "github.com/argoproj/argo-workflows/v3/pkg/client/informers/externalversions/internalinterfaces"
)

// Interface provides access to all the informers in this group version.
type Interface interface {
	// ClusterWorkflowTemplates returns a ClusterWorkflowTemplateInformer.
	ClusterWorkflowTemplates() ClusterWorkflowTemplateInformer
	// CronWorkflows returns a CronWorkflowInformer.
	CronWorkflows() CronWorkflowInformer
	// Workflows returns a WorkflowInformer.
	Workflows() WorkflowInformer
	// WorkflowAgents returns a WorkflowAgentInformer.
	WorkflowAgents() WorkflowAgentInformer
	// WorkflowEventBindings returns a WorkflowEventBindingInformer.
	WorkflowEventBindings() WorkflowEventBindingInformer
	// WorkflowNodes returns a WorkflowNodeInformer.
	WorkflowNodes() WorkflowNodeInformer
	// WorkflowTemplates returns a WorkflowTemplateInformer.
	WorkflowTemplates() WorkflowTemplateInformer
}

type version struct {
	factory          internalinterfaces.SharedInformerFactory
	namespace        string
	tweakListOptions internalinterfaces.TweakListOptionsFunc
}

// New returns a new Interface.
func New(f internalinterfaces.SharedInformerFactory, namespace string, tweakListOptions internalinterfaces.TweakListOptionsFunc) Interface {
	return &version{factory: f, namespace: namespace, tweakListOptions: tweakListOptions}
}

// ClusterWorkflowTemplates returns a ClusterWorkflowTemplateInformer.
func (v *version) ClusterWorkflowTemplates() ClusterWorkflowTemplateInformer {
	return &clusterWorkflowTemplateInformer{factory: v.factory, tweakListOptions: v.tweakListOptions}
}

// CronWorkflows returns a CronWorkflowInformer.
func (v *version) CronWorkflows() CronWorkflowInformer {
	return &cronWorkflowInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// Workflows returns a WorkflowInformer.
func (v *version) Workflows() WorkflowInformer {
	return &workflowInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// WorkflowAgents returns a WorkflowAgentInformer.
func (v *version) WorkflowAgents() WorkflowAgentInformer {
	return &workflowAgentInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// WorkflowEventBindings returns a WorkflowEventBindingInformer.
func (v *version) WorkflowEventBindings() WorkflowEventBindingInformer {
	return &workflowEventBindingInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// WorkflowNodes returns a WorkflowNodeInformer.
func (v *version) WorkflowNodes() WorkflowNodeInformer {
	return &workflowNodeInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// WorkflowTemplates returns a WorkflowTemplateInformer.
func (v *version) WorkflowTemplates() WorkflowTemplateInformer {
	return &workflowTemplateInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}
