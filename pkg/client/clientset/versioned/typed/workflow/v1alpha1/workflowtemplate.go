// Code generated by client-gen. DO NOT EDIT.

package v1alpha1

import (
	"time"

	v1alpha1 "github.com/argoproj/argo/v2/pkg/apis/workflow/v1alpha1"
	scheme "github.com/argoproj/argo/v2/pkg/client/clientset/versioned/scheme"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	rest "k8s.io/client-go/rest"
)

// WorkflowTemplatesGetter has a method to return a WorkflowTemplateInterface.
// A group's client should implement this interface.
type WorkflowTemplatesGetter interface {
	WorkflowTemplates(namespace string) WorkflowTemplateInterface
}

// WorkflowTemplateInterface has methods to work with WorkflowTemplate resources.
type WorkflowTemplateInterface interface {
	Create(*v1alpha1.WorkflowTemplate) (*v1alpha1.WorkflowTemplate, error)
	Update(*v1alpha1.WorkflowTemplate) (*v1alpha1.WorkflowTemplate, error)
	Delete(name string, options *v1.DeleteOptions) error
	DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error
	Get(name string, options v1.GetOptions) (*v1alpha1.WorkflowTemplate, error)
	List(opts v1.ListOptions) (*v1alpha1.WorkflowTemplateList, error)
	Watch(opts v1.ListOptions) (watch.Interface, error)
	Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1alpha1.WorkflowTemplate, err error)
	WorkflowTemplateExpansion
}

// workflowTemplates implements WorkflowTemplateInterface
type workflowTemplates struct {
	client rest.Interface
	ns     string
}

// newWorkflowTemplates returns a WorkflowTemplates
func newWorkflowTemplates(c *ArgoprojV1alpha1Client, namespace string) *workflowTemplates {
	return &workflowTemplates{
		client: c.RESTClient(),
		ns:     namespace,
	}
}

// Get takes name of the workflowTemplate, and returns the corresponding workflowTemplate object, and an error if there is any.
func (c *workflowTemplates) Get(name string, options v1.GetOptions) (result *v1alpha1.WorkflowTemplate, err error) {
	result = &v1alpha1.WorkflowTemplate{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("workflowtemplates").
		Name(name).
		VersionedParams(&options, scheme.ParameterCodec).
		Do().
		Into(result)
	return
}

// List takes label and field selectors, and returns the list of WorkflowTemplates that match those selectors.
func (c *workflowTemplates) List(opts v1.ListOptions) (result *v1alpha1.WorkflowTemplateList, err error) {
	var timeout time.Duration
	if opts.TimeoutSeconds != nil {
		timeout = time.Duration(*opts.TimeoutSeconds) * time.Second
	}
	result = &v1alpha1.WorkflowTemplateList{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("workflowtemplates").
		VersionedParams(&opts, scheme.ParameterCodec).
		Timeout(timeout).
		Do().
		Into(result)
	return
}

// Watch returns a watch.Interface that watches the requested workflowTemplates.
func (c *workflowTemplates) Watch(opts v1.ListOptions) (watch.Interface, error) {
	var timeout time.Duration
	if opts.TimeoutSeconds != nil {
		timeout = time.Duration(*opts.TimeoutSeconds) * time.Second
	}
	opts.Watch = true
	return c.client.Get().
		Namespace(c.ns).
		Resource("workflowtemplates").
		VersionedParams(&opts, scheme.ParameterCodec).
		Timeout(timeout).
		Watch()
}

// Create takes the representation of a workflowTemplate and creates it.  Returns the server's representation of the workflowTemplate, and an error, if there is any.
func (c *workflowTemplates) Create(workflowTemplate *v1alpha1.WorkflowTemplate) (result *v1alpha1.WorkflowTemplate, err error) {
	result = &v1alpha1.WorkflowTemplate{}
	err = c.client.Post().
		Namespace(c.ns).
		Resource("workflowtemplates").
		Body(workflowTemplate).
		Do().
		Into(result)
	return
}

// Update takes the representation of a workflowTemplate and updates it. Returns the server's representation of the workflowTemplate, and an error, if there is any.
func (c *workflowTemplates) Update(workflowTemplate *v1alpha1.WorkflowTemplate) (result *v1alpha1.WorkflowTemplate, err error) {
	result = &v1alpha1.WorkflowTemplate{}
	err = c.client.Put().
		Namespace(c.ns).
		Resource("workflowtemplates").
		Name(workflowTemplate.Name).
		Body(workflowTemplate).
		Do().
		Into(result)
	return
}

// Delete takes name of the workflowTemplate and deletes it. Returns an error if one occurs.
func (c *workflowTemplates) Delete(name string, options *v1.DeleteOptions) error {
	return c.client.Delete().
		Namespace(c.ns).
		Resource("workflowtemplates").
		Name(name).
		Body(options).
		Do().
		Error()
}

// DeleteCollection deletes a collection of objects.
func (c *workflowTemplates) DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error {
	var timeout time.Duration
	if listOptions.TimeoutSeconds != nil {
		timeout = time.Duration(*listOptions.TimeoutSeconds) * time.Second
	}
	return c.client.Delete().
		Namespace(c.ns).
		Resource("workflowtemplates").
		VersionedParams(&listOptions, scheme.ParameterCodec).
		Timeout(timeout).
		Body(options).
		Do().
		Error()
}

// Patch applies the patch and returns the patched workflowTemplate.
func (c *workflowTemplates) Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1alpha1.WorkflowTemplate, err error) {
	result = &v1alpha1.WorkflowTemplate{}
	err = c.client.Patch(pt).
		Namespace(c.ns).
		Resource("workflowtemplates").
		SubResource(subresources...).
		Name(name).
		Body(data).
		Do().
		Into(result)
	return
}
