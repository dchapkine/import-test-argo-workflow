// Code generated by informer-gen. DO NOT EDIT.

package v1alpha1

import (
	internalinterfaces "github.com/argoproj/argo/v2/pkg/client/informers/externalversions/internalinterfaces"
)

// Interface provides access to all the informers in this group version.
type Interface interface {
	// CronWorkflows returns a CronWorkflowInformer.
	CronWorkflows() CronWorkflowInformer
	// Workflows returns a WorkflowInformer.
	Workflows() WorkflowInformer
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

// CronWorkflows returns a CronWorkflowInformer.
func (v *version) CronWorkflows() CronWorkflowInformer {
	return &cronWorkflowInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// Workflows returns a WorkflowInformer.
func (v *version) Workflows() WorkflowInformer {
	return &workflowInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}

// WorkflowTemplates returns a WorkflowTemplateInformer.
func (v *version) WorkflowTemplates() WorkflowTemplateInformer {
	return &workflowTemplateInformer{factory: v.factory, namespace: v.namespace, tweakListOptions: v.tweakListOptions}
}
