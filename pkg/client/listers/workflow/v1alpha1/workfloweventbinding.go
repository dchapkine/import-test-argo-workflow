// Code generated by lister-gen. DO NOT EDIT.

package v1alpha1

import (
	v1alpha1 "github.com/argoproj/argo/v3/pkg/apis/workflow/v1alpha1"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/labels"
	"k8s.io/client-go/tools/cache"
)

// WorkflowEventBindingLister helps list WorkflowEventBindings.
// All objects returned here must be treated as read-only.
type WorkflowEventBindingLister interface {
	// List lists all WorkflowEventBindings in the indexer.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1alpha1.WorkflowEventBinding, err error)
	// WorkflowEventBindings returns an object that can list and get WorkflowEventBindings.
	WorkflowEventBindings(namespace string) WorkflowEventBindingNamespaceLister
	WorkflowEventBindingListerExpansion
}

// workflowEventBindingLister implements the WorkflowEventBindingLister interface.
type workflowEventBindingLister struct {
	indexer cache.Indexer
}

// NewWorkflowEventBindingLister returns a new WorkflowEventBindingLister.
func NewWorkflowEventBindingLister(indexer cache.Indexer) WorkflowEventBindingLister {
	return &workflowEventBindingLister{indexer: indexer}
}

// List lists all WorkflowEventBindings in the indexer.
func (s *workflowEventBindingLister) List(selector labels.Selector) (ret []*v1alpha1.WorkflowEventBinding, err error) {
	err = cache.ListAll(s.indexer, selector, func(m interface{}) {
		ret = append(ret, m.(*v1alpha1.WorkflowEventBinding))
	})
	return ret, err
}

// WorkflowEventBindings returns an object that can list and get WorkflowEventBindings.
func (s *workflowEventBindingLister) WorkflowEventBindings(namespace string) WorkflowEventBindingNamespaceLister {
	return workflowEventBindingNamespaceLister{indexer: s.indexer, namespace: namespace}
}

// WorkflowEventBindingNamespaceLister helps list and get WorkflowEventBindings.
// All objects returned here must be treated as read-only.
type WorkflowEventBindingNamespaceLister interface {
	// List lists all WorkflowEventBindings in the indexer for a given namespace.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1alpha1.WorkflowEventBinding, err error)
	// Get retrieves the WorkflowEventBinding from the indexer for a given namespace and name.
	// Objects returned here must be treated as read-only.
	Get(name string) (*v1alpha1.WorkflowEventBinding, error)
	WorkflowEventBindingNamespaceListerExpansion
}

// workflowEventBindingNamespaceLister implements the WorkflowEventBindingNamespaceLister
// interface.
type workflowEventBindingNamespaceLister struct {
	indexer   cache.Indexer
	namespace string
}

// List lists all WorkflowEventBindings in the indexer for a given namespace.
func (s workflowEventBindingNamespaceLister) List(selector labels.Selector) (ret []*v1alpha1.WorkflowEventBinding, err error) {
	err = cache.ListAllByNamespace(s.indexer, s.namespace, selector, func(m interface{}) {
		ret = append(ret, m.(*v1alpha1.WorkflowEventBinding))
	})
	return ret, err
}

// Get retrieves the WorkflowEventBinding from the indexer for a given namespace and name.
func (s workflowEventBindingNamespaceLister) Get(name string) (*v1alpha1.WorkflowEventBinding, error) {
	obj, exists, err := s.indexer.GetByKey(s.namespace + "/" + name)
	if err != nil {
		return nil, err
	}
	if !exists {
		return nil, errors.NewNotFound(v1alpha1.Resource("workfloweventbinding"), name)
	}
	return obj.(*v1alpha1.WorkflowEventBinding), nil
}
