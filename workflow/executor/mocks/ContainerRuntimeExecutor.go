// Code generated by mockery v1.1.1. DO NOT EDIT.

package mocks

import (
	context "context"

	io "io"

	mock "github.com/stretchr/testify/mock"
)

// ContainerRuntimeExecutor is an autogenerated mock type for the ContainerRuntimeExecutor type
type ContainerRuntimeExecutor struct {
	mock.Mock
}

// CopyFile provides a mock function with given fields: containerName, sourcePath, destPath, compressionLevel
func (_m *ContainerRuntimeExecutor) CopyFile(containerName string, sourcePath string, destPath string, compressionLevel int) error {
	ret := _m.Called(containerName, sourcePath, destPath, compressionLevel)

	var r0 error
	if rf, ok := ret.Get(0).(func(string, string, string, int) error); ok {
		r0 = rf(containerName, sourcePath, destPath, compressionLevel)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// GetExitCode provides a mock function with given fields: ctx, containerName
func (_m *ContainerRuntimeExecutor) GetExitCode(ctx context.Context, containerName string) (string, error) {
	ret := _m.Called(ctx, containerName)

	var r0 string
	if rf, ok := ret.Get(0).(func(context.Context, string) string); ok {
		r0 = rf(ctx, containerName)
	} else {
		r0 = ret.Get(0).(string)
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, string) error); ok {
		r1 = rf(ctx, containerName)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetFileContents provides a mock function with given fields: containerName, sourcePath
func (_m *ContainerRuntimeExecutor) GetFileContents(containerName string, sourcePath string) (string, error) {
	ret := _m.Called(containerName, sourcePath)

	var r0 string
	if rf, ok := ret.Get(0).(func(string, string) string); ok {
		r0 = rf(containerName, sourcePath)
	} else {
		r0 = ret.Get(0).(string)
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string, string) error); ok {
		r1 = rf(containerName, sourcePath)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetOutputStream provides a mock function with given fields: ctx, containerName, combinedOutput
func (_m *ContainerRuntimeExecutor) GetOutputStream(ctx context.Context, containerName string, combinedOutput bool) (io.ReadCloser, error) {
	ret := _m.Called(ctx, containerName, combinedOutput)

	var r0 io.ReadCloser
	if rf, ok := ret.Get(0).(func(context.Context, string, bool) io.ReadCloser); ok {
		r0 = rf(ctx, containerName, combinedOutput)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(io.ReadCloser)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, string, bool) error); ok {
		r1 = rf(ctx, containerName, combinedOutput)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// Kill provides a mock function with given fields: ctx, containerNames
func (_m *ContainerRuntimeExecutor) Kill(ctx context.Context, containerNames []string) error {
	ret := _m.Called(ctx, containerNames)

	var r0 error
	if rf, ok := ret.Get(0).(func(context.Context, []string) error); ok {
		r0 = rf(ctx, containerNames)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// Wait provides a mock function with given fields: ctx, containerNames, sidecarNames
func (_m *ContainerRuntimeExecutor) Wait(ctx context.Context, containerNames []string, sidecarNames []string) error {
	ret := _m.Called(ctx, containerNames, sidecarNames)

	var r0 error
	if rf, ok := ret.Get(0).(func(context.Context, []string, []string) error); ok {
		r0 = rf(ctx, containerNames, sidecarNames)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}
