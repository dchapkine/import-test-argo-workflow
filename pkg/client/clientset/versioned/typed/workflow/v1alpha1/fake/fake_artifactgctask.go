// Code generated by client-gen. DO NOT EDIT.

package fake

import (
	"context"

	v1alpha1 "github.com/argoproj/argo-workflows/v3/pkg/apis/workflow/v1alpha1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	labels "k8s.io/apimachinery/pkg/labels"
	schema "k8s.io/apimachinery/pkg/runtime/schema"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	testing "k8s.io/client-go/testing"
)

// FakeArtifactGCTasks implements ArtifactGCTaskInterface
type FakeArtifactGCTasks struct {
	Fake *FakeArgoprojV1alpha1
	ns   string
}

var artifactgctasksResource = schema.GroupVersionResource{Group: "argoproj.io", Version: "v1alpha1", Resource: "artifactgctasks"}

var artifactgctasksKind = schema.GroupVersionKind{Group: "argoproj.io", Version: "v1alpha1", Kind: "ArtifactGCTask"}

// Get takes name of the artifactGCTask, and returns the corresponding artifactGCTask object, and an error if there is any.
func (c *FakeArtifactGCTasks) Get(ctx context.Context, name string, options v1.GetOptions) (result *v1alpha1.WorkflowArtifactGCTaskSet, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewGetAction(artifactgctasksResource, c.ns, name), &v1alpha1.WorkflowArtifactGCTaskSet{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.WorkflowArtifactGCTaskSet), err
}

// List takes label and field selectors, and returns the list of ArtifactGCTasks that match those selectors.
func (c *FakeArtifactGCTasks) List(ctx context.Context, opts v1.ListOptions) (result *v1alpha1.ArtifactGCTaskList, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewListAction(artifactgctasksResource, artifactgctasksKind, c.ns, opts), &v1alpha1.ArtifactGCTaskList{})

	if obj == nil {
		return nil, err
	}

	label, _, _ := testing.ExtractFromListOptions(opts)
	if label == nil {
		label = labels.Everything()
	}
	list := &v1alpha1.ArtifactGCTaskList{ListMeta: obj.(*v1alpha1.ArtifactGCTaskList).ListMeta}
	for _, item := range obj.(*v1alpha1.ArtifactGCTaskList).Items {
		if label.Matches(labels.Set(item.Labels)) {
			list.Items = append(list.Items, item)
		}
	}
	return list, err
}

// Watch returns a watch.Interface that watches the requested artifactGCTasks.
func (c *FakeArtifactGCTasks) Watch(ctx context.Context, opts v1.ListOptions) (watch.Interface, error) {
	return c.Fake.
		InvokesWatch(testing.NewWatchAction(artifactgctasksResource, c.ns, opts))

}

// Create takes the representation of a artifactGCTask and creates it.  Returns the server's representation of the artifactGCTask, and an error, if there is any.
func (c *FakeArtifactGCTasks) Create(ctx context.Context, artifactGCTask *v1alpha1.WorkflowArtifactGCTaskSet, opts v1.CreateOptions) (result *v1alpha1.WorkflowArtifactGCTaskSet, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewCreateAction(artifactgctasksResource, c.ns, artifactGCTask), &v1alpha1.WorkflowArtifactGCTaskSet{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.WorkflowArtifactGCTaskSet), err
}

// Update takes the representation of a artifactGCTask and updates it. Returns the server's representation of the artifactGCTask, and an error, if there is any.
func (c *FakeArtifactGCTasks) Update(ctx context.Context, artifactGCTask *v1alpha1.WorkflowArtifactGCTaskSet, opts v1.UpdateOptions) (result *v1alpha1.WorkflowArtifactGCTaskSet, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateAction(artifactgctasksResource, c.ns, artifactGCTask), &v1alpha1.WorkflowArtifactGCTaskSet{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.WorkflowArtifactGCTaskSet), err
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().
func (c *FakeArtifactGCTasks) UpdateStatus(ctx context.Context, artifactGCTask *v1alpha1.WorkflowArtifactGCTaskSet, opts v1.UpdateOptions) (*v1alpha1.WorkflowArtifactGCTaskSet, error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateSubresourceAction(artifactgctasksResource, "status", c.ns, artifactGCTask), &v1alpha1.WorkflowArtifactGCTaskSet{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.WorkflowArtifactGCTaskSet), err
}

// Delete takes name of the artifactGCTask and deletes it. Returns an error if one occurs.
func (c *FakeArtifactGCTasks) Delete(ctx context.Context, name string, opts v1.DeleteOptions) error {
	_, err := c.Fake.
		Invokes(testing.NewDeleteAction(artifactgctasksResource, c.ns, name), &v1alpha1.WorkflowArtifactGCTaskSet{})

	return err
}

// DeleteCollection deletes a collection of objects.
func (c *FakeArtifactGCTasks) DeleteCollection(ctx context.Context, opts v1.DeleteOptions, listOpts v1.ListOptions) error {
	action := testing.NewDeleteCollectionAction(artifactgctasksResource, c.ns, listOpts)

	_, err := c.Fake.Invokes(action, &v1alpha1.ArtifactGCTaskList{})
	return err
}

// Patch applies the patch and returns the patched artifactGCTask.
func (c *FakeArtifactGCTasks) Patch(ctx context.Context, name string, pt types.PatchType, data []byte, opts v1.PatchOptions, subresources ...string) (result *v1alpha1.WorkflowArtifactGCTaskSet, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceAction(artifactgctasksResource, c.ns, name, pt, data, subresources...), &v1alpha1.WorkflowArtifactGCTaskSet{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.WorkflowArtifactGCTaskSet), err
}
