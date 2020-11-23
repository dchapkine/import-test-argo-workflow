// Code generated by mockery v1.1.1. DO NOT EDIT.

package mocks

import (
	persist "github.com/argoproj/argo/persist"
	mock "github.com/stretchr/testify/mock"

	v1alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
)

// OffloadNodeStatusRepo is an autogenerated mock type for the OffloadNodeStatusRepo type
type OffloadNodeStatusRepo struct {
	mock.Mock
}

// Delete provides a mock function with given fields: uid, version
func (_m *OffloadNodeStatusRepo) Delete(uid string, version string) error {
	ret := _m.Called(uid, version)

	var r0 error
	if rf, ok := ret.Get(0).(func(string, string) error); ok {
		r0 = rf(uid, version)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// Get provides a mock function with given fields: uid, version
func (_m *OffloadNodeStatusRepo) Get(uid string, version string) (v1alpha1.Nodes, error) {
	ret := _m.Called(uid, version)

	var r0 v1alpha1.Nodes
	if rf, ok := ret.Get(0).(func(string, string) v1alpha1.Nodes); ok {
		r0 = rf(uid, version)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(v1alpha1.Nodes)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string, string) error); ok {
		r1 = rf(uid, version)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// IsEnabled provides a mock function with given fields:
func (_m *OffloadNodeStatusRepo) IsEnabled() bool {
	ret := _m.Called()

	var r0 bool
	if rf, ok := ret.Get(0).(func() bool); ok {
		r0 = rf()
	} else {
		r0 = ret.Get(0).(bool)
	}

	return r0
}

// List provides a mock function with given fields: namespace
func (_m *OffloadNodeStatusRepo) List(namespace string) (map[persist.UUIDVersion]v1alpha1.Nodes, error) {
	ret := _m.Called(namespace)

	var r0 map[persist.UUIDVersion]v1alpha1.Nodes
	if rf, ok := ret.Get(0).(func(string) map[persist.UUIDVersion]v1alpha1.Nodes); ok {
		r0 = rf(namespace)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(map[persist.UUIDVersion]v1alpha1.Nodes)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string) error); ok {
		r1 = rf(namespace)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ListOldOffloads provides a mock function with given fields: namespace
func (_m *OffloadNodeStatusRepo) ListOldOffloads(namespace string) ([]persist.UUIDVersion, error) {
	ret := _m.Called(namespace)

	var r0 []persist.UUIDVersion
	if rf, ok := ret.Get(0).(func(string) []persist.UUIDVersion); ok {
		r0 = rf(namespace)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).([]persist.UUIDVersion)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string) error); ok {
		r1 = rf(namespace)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// Save provides a mock function with given fields: uid, namespace, nodes
func (_m *OffloadNodeStatusRepo) Save(uid string, namespace string, nodes v1alpha1.Nodes) (string, error) {
	ret := _m.Called(uid, namespace, nodes)

	var r0 string
	if rf, ok := ret.Get(0).(func(string, string, v1alpha1.Nodes) string); ok {
		r0 = rf(uid, namespace, nodes)
	} else {
		r0 = ret.Get(0).(string)
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string, string, v1alpha1.Nodes) error); ok {
		r1 = rf(uid, namespace, nodes)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
