// Code generated by client-gen. DO NOT EDIT.

package v1alpha1

import (
	"context"
	"time"

	v1alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	scheme "github.com/argoproj/argo/pkg/client/clientset/versioned/scheme"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	rest "k8s.io/client-go/rest"
)

// WorkflowEventBindingsGetter has a method to return a WorkflowEventBindingInterface.
// A group's client should implement this interface.
type WorkflowEventBindingsGetter interface {
	WorkflowEventBindings(namespace string) WorkflowEventBindingInterface
}

// WorkflowEventBindingInterface has methods to work with WorkflowEventBinding resources.
type WorkflowEventBindingInterface interface {
	Create(ctx context.Context, workflowEventBinding *v1alpha1.WorkflowEventBinding, opts v1.CreateOptions) (*v1alpha1.WorkflowEventBinding, error)
	Update(ctx context.Context, workflowEventBinding *v1alpha1.WorkflowEventBinding, opts v1.UpdateOptions) (*v1alpha1.WorkflowEventBinding, error)
	Delete(ctx context.Context, name string, opts v1.DeleteOptions) error
	DeleteCollection(ctx context.Context, opts v1.DeleteOptions, listOpts v1.ListOptions) error
	Get(ctx context.Context, name string, opts v1.GetOptions) (*v1alpha1.WorkflowEventBinding, error)
	List(ctx context.Context, opts v1.ListOptions) (*v1alpha1.WorkflowEventBindingList, error)
	Watch(ctx context.Context, opts v1.ListOptions) (watch.Interface, error)
	Patch(ctx context.Context, name string, pt types.PatchType, data []byte, opts v1.PatchOptions, subresources ...string) (result *v1alpha1.WorkflowEventBinding, err error)
	WorkflowEventBindingExpansion
}

// workflowEventBindings implements WorkflowEventBindingInterface
type workflowEventBindings struct {
	client rest.Interface
	ns     string
}

// newWorkflowEventBindings returns a WorkflowEventBindings
func newWorkflowEventBindings(c *ArgoprojV1alpha1Client, namespace string) *workflowEventBindings {
	return &workflowEventBindings{
		client: c.RESTClient(),
		ns:     namespace,
	}
}

// Get takes name of the workflowEventBinding, and returns the corresponding workflowEventBinding object, and an error if there is any.
func (c *workflowEventBindings) Get(ctx context.Context, name string, options v1.GetOptions) (result *v1alpha1.WorkflowEventBinding, err error) {
	result = &v1alpha1.WorkflowEventBinding{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		Name(name).
		VersionedParams(&options, scheme.ParameterCodec).
		Do(ctx).
		Into(result)
	return
}

// List takes label and field selectors, and returns the list of WorkflowEventBindings that match those selectors.
func (c *workflowEventBindings) List(ctx context.Context, opts v1.ListOptions) (result *v1alpha1.WorkflowEventBindingList, err error) {
	var timeout time.Duration
	if opts.TimeoutSeconds != nil {
		timeout = time.Duration(*opts.TimeoutSeconds) * time.Second
	}
	result = &v1alpha1.WorkflowEventBindingList{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		VersionedParams(&opts, scheme.ParameterCodec).
		Timeout(timeout).
		Do(ctx).
		Into(result)
	return
}

// Watch returns a watch.Interface that watches the requested workflowEventBindings.
func (c *workflowEventBindings) Watch(ctx context.Context, opts v1.ListOptions) (watch.Interface, error) {
	var timeout time.Duration
	if opts.TimeoutSeconds != nil {
		timeout = time.Duration(*opts.TimeoutSeconds) * time.Second
	}
	opts.Watch = true
	return c.client.Get().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		VersionedParams(&opts, scheme.ParameterCodec).
		Timeout(timeout).
		Watch(ctx)
}

// Create takes the representation of a workflowEventBinding and creates it.  Returns the server's representation of the workflowEventBinding, and an error, if there is any.
func (c *workflowEventBindings) Create(ctx context.Context, workflowEventBinding *v1alpha1.WorkflowEventBinding, opts v1.CreateOptions) (result *v1alpha1.WorkflowEventBinding, err error) {
	result = &v1alpha1.WorkflowEventBinding{}
	err = c.client.Post().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		VersionedParams(&opts, scheme.ParameterCodec).
		Body(workflowEventBinding).
		Do(ctx).
		Into(result)
	return
}

// Update takes the representation of a workflowEventBinding and updates it. Returns the server's representation of the workflowEventBinding, and an error, if there is any.
func (c *workflowEventBindings) Update(ctx context.Context, workflowEventBinding *v1alpha1.WorkflowEventBinding, opts v1.UpdateOptions) (result *v1alpha1.WorkflowEventBinding, err error) {
	result = &v1alpha1.WorkflowEventBinding{}
	err = c.client.Put().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		Name(workflowEventBinding.Name).
		VersionedParams(&opts, scheme.ParameterCodec).
		Body(workflowEventBinding).
		Do(ctx).
		Into(result)
	return
}

// Delete takes name of the workflowEventBinding and deletes it. Returns an error if one occurs.
func (c *workflowEventBindings) Delete(ctx context.Context, name string, opts v1.DeleteOptions) error {
	return c.client.Delete().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		Name(name).
		Body(&opts).
		Do(ctx).
		Error()
}

// DeleteCollection deletes a collection of objects.
func (c *workflowEventBindings) DeleteCollection(ctx context.Context, opts v1.DeleteOptions, listOpts v1.ListOptions) error {
	var timeout time.Duration
	if listOpts.TimeoutSeconds != nil {
		timeout = time.Duration(*listOpts.TimeoutSeconds) * time.Second
	}
	return c.client.Delete().
		Namespace(c.ns).
		Resource("workfloweventbindings").
		VersionedParams(&listOpts, scheme.ParameterCodec).
		Timeout(timeout).
		Body(&opts).
		Do(ctx).
		Error()
}

// Patch applies the patch and returns the patched workflowEventBinding.
func (c *workflowEventBindings) Patch(ctx context.Context, name string, pt types.PatchType, data []byte, opts v1.PatchOptions, subresources ...string) (result *v1alpha1.WorkflowEventBinding, err error) {
	result = &v1alpha1.WorkflowEventBinding{}
	err = c.client.Patch(pt).
		Namespace(c.ns).
		Resource("workfloweventbindings").
		Name(name).
		SubResource(subresources...).
		VersionedParams(&opts, scheme.ParameterCodec).
		Body(data).
		Do(ctx).
		Into(result)
	return
}
