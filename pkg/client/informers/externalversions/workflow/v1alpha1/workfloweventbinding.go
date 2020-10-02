// Code generated by informer-gen. DO NOT EDIT.

package v1alpha1

import (
	time "time"

	workflowv1alpha1 "github.com/argoproj/argo/v3/pkg/apis/workflow/v1alpha1"
	versioned "github.com/argoproj/argo/v3/pkg/client/clientset/versioned"
	internalinterfaces "github.com/argoproj/argo/v3/pkg/client/informers/externalversions/internalinterfaces"
	v1alpha1 "github.com/argoproj/argo/v3/pkg/client/listers/workflow/v1alpha1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	runtime "k8s.io/apimachinery/pkg/runtime"
	watch "k8s.io/apimachinery/pkg/watch"
	cache "k8s.io/client-go/tools/cache"
)

// WorkflowEventBindingInformer provides access to a shared informer and lister for
// WorkflowEventBindings.
type WorkflowEventBindingInformer interface {
	Informer() cache.SharedIndexInformer
	Lister() v1alpha1.WorkflowEventBindingLister
}

type workflowEventBindingInformer struct {
	factory          internalinterfaces.SharedInformerFactory
	tweakListOptions internalinterfaces.TweakListOptionsFunc
	namespace        string
}

// NewWorkflowEventBindingInformer constructs a new informer for WorkflowEventBinding type.
// Always prefer using an informer factory to get a shared informer instead of getting an independent
// one. This reduces memory footprint and number of connections to the server.
func NewWorkflowEventBindingInformer(client versioned.Interface, namespace string, resyncPeriod time.Duration, indexers cache.Indexers) cache.SharedIndexInformer {
	return NewFilteredWorkflowEventBindingInformer(client, namespace, resyncPeriod, indexers, nil)
}

// NewFilteredWorkflowEventBindingInformer constructs a new informer for WorkflowEventBinding type.
// Always prefer using an informer factory to get a shared informer instead of getting an independent
// one. This reduces memory footprint and number of connections to the server.
func NewFilteredWorkflowEventBindingInformer(client versioned.Interface, namespace string, resyncPeriod time.Duration, indexers cache.Indexers, tweakListOptions internalinterfaces.TweakListOptionsFunc) cache.SharedIndexInformer {
	return cache.NewSharedIndexInformer(
		&cache.ListWatch{
			ListFunc: func(options v1.ListOptions) (runtime.Object, error) {
				if tweakListOptions != nil {
					tweakListOptions(&options)
				}
				return client.ArgoprojV1alpha1().WorkflowEventBindings(namespace).List(options)
			},
			WatchFunc: func(options v1.ListOptions) (watch.Interface, error) {
				if tweakListOptions != nil {
					tweakListOptions(&options)
				}
				return client.ArgoprojV1alpha1().WorkflowEventBindings(namespace).Watch(options)
			},
		},
		&workflowv1alpha1.WorkflowEventBinding{},
		resyncPeriod,
		indexers,
	)
}

func (f *workflowEventBindingInformer) defaultInformer(client versioned.Interface, resyncPeriod time.Duration) cache.SharedIndexInformer {
	return NewFilteredWorkflowEventBindingInformer(client, f.namespace, resyncPeriod, cache.Indexers{cache.NamespaceIndex: cache.MetaNamespaceIndexFunc}, f.tweakListOptions)
}

func (f *workflowEventBindingInformer) Informer() cache.SharedIndexInformer {
	return f.factory.InformerFor(&workflowv1alpha1.WorkflowEventBinding{}, f.defaultInformer)
}

func (f *workflowEventBindingInformer) Lister() v1alpha1.WorkflowEventBindingLister {
	return v1alpha1.NewWorkflowEventBindingLister(f.Informer().GetIndexer())
}
