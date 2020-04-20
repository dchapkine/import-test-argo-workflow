// Code generated by mockery v1.0.0. DO NOT EDIT.

package mocks

import (
	context "context"

	v1alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	mock "github.com/stretchr/testify/mock"

	workflowarchive "github.com/argoproj/argo/pkg/apiclient/workflowarchive"
)

// ArchivedWorkflowServiceServer is an autogenerated mock type for the ArchivedWorkflowServiceServer type
type ArchivedWorkflowServiceServer struct {
	mock.Mock
}

// DeleteArchivedWorkflow provides a mock function with given fields: _a0, _a1
func (_m *ArchivedWorkflowServiceServer) DeleteArchivedWorkflow(_a0 context.Context, _a1 *workflowarchive.DeleteArchivedWorkflowRequest) (*workflowarchive.ArchivedWorkflowDeletedResponse, error) {
	ret := _m.Called(_a0, _a1)

	var r0 *workflowarchive.ArchivedWorkflowDeletedResponse
	if rf, ok := ret.Get(0).(func(context.Context, *workflowarchive.DeleteArchivedWorkflowRequest) *workflowarchive.ArchivedWorkflowDeletedResponse); ok {
		r0 = rf(_a0, _a1)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*workflowarchive.ArchivedWorkflowDeletedResponse)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *workflowarchive.DeleteArchivedWorkflowRequest) error); ok {
		r1 = rf(_a0, _a1)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetArchivedWorkflow provides a mock function with given fields: _a0, _a1
func (_m *ArchivedWorkflowServiceServer) GetArchivedWorkflow(_a0 context.Context, _a1 *workflowarchive.GetArchivedWorkflowRequest) (*v1alpha1.Workflow, error) {
	ret := _m.Called(_a0, _a1)

	var r0 *v1alpha1.Workflow
	if rf, ok := ret.Get(0).(func(context.Context, *workflowarchive.GetArchivedWorkflowRequest) *v1alpha1.Workflow); ok {
		r0 = rf(_a0, _a1)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.Workflow)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *workflowarchive.GetArchivedWorkflowRequest) error); ok {
		r1 = rf(_a0, _a1)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ListArchivedWorkflows provides a mock function with given fields: _a0, _a1
func (_m *ArchivedWorkflowServiceServer) ListArchivedWorkflows(_a0 context.Context, _a1 *workflowarchive.ListArchivedWorkflowsRequest) (*v1alpha1.WorkflowList, error) {
	ret := _m.Called(_a0, _a1)

	var r0 *v1alpha1.WorkflowList
	if rf, ok := ret.Get(0).(func(context.Context, *workflowarchive.ListArchivedWorkflowsRequest) *v1alpha1.WorkflowList); ok {
		r0 = rf(_a0, _a1)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.WorkflowList)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *workflowarchive.ListArchivedWorkflowsRequest) error); ok {
		r1 = rf(_a0, _a1)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
