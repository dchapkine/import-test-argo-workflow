// Code generated by mockery v1.0.0. DO NOT EDIT.

package mocks

import (
	context "context"

	clusterworkflowtemplate "github.com/argoproj/argo/pkg/apiclient/clusterworkflowtemplate"

	grpc "google.golang.org/grpc"

	mock "github.com/stretchr/testify/mock"

	v1alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
)

// ClusterWorkflowTemplateServiceClient is an autogenerated mock type for the ClusterWorkflowTemplateServiceClient type
type ClusterWorkflowTemplateServiceClient struct {
	mock.Mock
}

// CreateClusterWorkflowTemplate provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) CreateClusterWorkflowTemplate(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateCreateRequest, opts ...grpc.CallOption) (*v1alpha1.ClusterWorkflowTemplate, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *v1alpha1.ClusterWorkflowTemplate
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateCreateRequest, ...grpc.CallOption) *v1alpha1.ClusterWorkflowTemplate); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.ClusterWorkflowTemplate)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateCreateRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// DeleteClusterWorkflowTemplate provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) DeleteClusterWorkflowTemplate(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateDeleteRequest, opts ...grpc.CallOption) (*clusterworkflowtemplate.ClusterWorkflowTemplateDeleteResponse, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *clusterworkflowtemplate.ClusterWorkflowTemplateDeleteResponse
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateDeleteRequest, ...grpc.CallOption) *clusterworkflowtemplate.ClusterWorkflowTemplateDeleteResponse); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*clusterworkflowtemplate.ClusterWorkflowTemplateDeleteResponse)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateDeleteRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetClusterWorkflowTemplate provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) GetClusterWorkflowTemplate(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateGetRequest, opts ...grpc.CallOption) (*v1alpha1.ClusterWorkflowTemplate, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *v1alpha1.ClusterWorkflowTemplate
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateGetRequest, ...grpc.CallOption) *v1alpha1.ClusterWorkflowTemplate); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.ClusterWorkflowTemplate)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateGetRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// LintClusterWorkflowTemplate provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) LintClusterWorkflowTemplate(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateLintRequest, opts ...grpc.CallOption) (*v1alpha1.ClusterWorkflowTemplate, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *v1alpha1.ClusterWorkflowTemplate
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateLintRequest, ...grpc.CallOption) *v1alpha1.ClusterWorkflowTemplate); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.ClusterWorkflowTemplate)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateLintRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ListClusterWorkflowTemplates provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) ListClusterWorkflowTemplates(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateListRequest, opts ...grpc.CallOption) (*v1alpha1.ClusterWorkflowTemplateList, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *v1alpha1.ClusterWorkflowTemplateList
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateListRequest, ...grpc.CallOption) *v1alpha1.ClusterWorkflowTemplateList); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.ClusterWorkflowTemplateList)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateListRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// UpdateClusterWorkflowTemplate provides a mock function with given fields: ctx, in, opts
func (_m *ClusterWorkflowTemplateServiceClient) UpdateClusterWorkflowTemplate(ctx context.Context, in *clusterworkflowtemplate.ClusterWorkflowTemplateUpdateRequest, opts ...grpc.CallOption) (*v1alpha1.ClusterWorkflowTemplate, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *v1alpha1.ClusterWorkflowTemplate
	if rf, ok := ret.Get(0).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateUpdateRequest, ...grpc.CallOption) *v1alpha1.ClusterWorkflowTemplate); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.ClusterWorkflowTemplate)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *clusterworkflowtemplate.ClusterWorkflowTemplateUpdateRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
