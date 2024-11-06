// Code generated by mockery v2.42.2. DO NOT EDIT.

package mocks

import (
	mock "github.com/stretchr/testify/mock"

	time "time"

	v1alpha1 "github.com/argoproj/argo-workflows/v3/pkg/apis/workflow/v1alpha1"
)

// Throttler is an autogenerated mock type for the Throttler type
type Throttler struct {
	mock.Mock
}

// Add provides a mock function with given fields: key, priority, creationTime
func (_m *Throttler) Add(key string, priority int32, creationTime time.Time) {
	_m.Called(key, priority, creationTime)
}

// Admit provides a mock function with given fields: key
func (_m *Throttler) Admit(key string) bool {
	ret := _m.Called(key)

	if len(ret) == 0 {
		panic("no return value specified for Admit")
	}

	var r0 bool
	if rf, ok := ret.Get(0).(func(string) bool); ok {
		r0 = rf(key)
	} else {
		r0 = ret.Get(0).(bool)
	}

	return r0
}

// Init provides a mock function with given fields: wfs
func (_m *Throttler) Init(wfs []v1alpha1.Workflow) error {
	ret := _m.Called(wfs)

	if len(ret) == 0 {
		panic("no return value specified for Init")
	}

	var r0 error
	if rf, ok := ret.Get(0).(func([]v1alpha1.Workflow) error); ok {
		r0 = rf(wfs)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// Remove provides a mock function with given fields: key
func (_m *Throttler) Remove(key string) {
	_m.Called(key)
}

// RemoveParallelismLimit provides a mock function with given fields: key
func (_m *Throttler) RemoveParallelismLimit(key string) {
	_m.Called(key)
}

// NewThrottler creates a new instance of Throttler. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
// The first argument is typically a *testing.T value.
func NewThrottler(t interface {
	mock.TestingT
	Cleanup(func())
}) *Throttler {
	mock := &Throttler{}
	mock.Mock.Test(t)

	t.Cleanup(func() { mock.AssertExpectations(t) })

	return mock
}
