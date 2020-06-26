// Code generated by mockery v1.1.1. DO NOT EDIT.

package mocks

import (
	v1alpha1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	mock "github.com/stretchr/testify/mock"
)

// MemoizationCache is an autogenerated mock type for the MemoizationCache type
type MemoizationCache struct {
	mock.Mock
}

// Load provides a mock function with given fields: key
func (_m *MemoizationCache) Load(key string) (*v1alpha1.Outputs, bool) {
	ret := _m.Called(key)

	var r0 *v1alpha1.Outputs
	if rf, ok := ret.Get(0).(func(string) *v1alpha1.Outputs); ok {
		r0 = rf(key)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*v1alpha1.Outputs)
		}
	}

	var r1 bool
	if rf, ok := ret.Get(1).(func(string) bool); ok {
		r1 = rf(key)
	} else {
		r1 = ret.Get(1).(bool)
	}

	return r0, r1
}

// Save provides a mock function with given fields: key, value
func (_m *MemoizationCache) Save(key string, value *v1alpha1.Outputs) bool {
	ret := _m.Called(key, value)

	var r0 bool
	if rf, ok := ret.Get(0).(func(string, *v1alpha1.Outputs) bool); ok {
		r0 = rf(key, value)
	} else {
		r0 = ret.Get(0).(bool)
	}

	return r0
}
