// Code generated by mockery v1.0.0. DO NOT EDIT.

package mocks

import (
	context "context"

	grpc "google.golang.org/grpc"

	info "github.com/argoproj/argo/pkg/apiclient/info"

	mock "github.com/stretchr/testify/mock"
)

// InfoServiceClient is an autogenerated mock type for the InfoServiceClient type
type InfoServiceClient struct {
	mock.Mock
}

// GetInfo provides a mock function with given fields: ctx, in, opts
func (_m *InfoServiceClient) GetInfo(ctx context.Context, in *info.GetInfoRequest, opts ...grpc.CallOption) (*info.InfoResponse, error) {
	_va := make([]interface{}, len(opts))
	for _i := range opts {
		_va[_i] = opts[_i]
	}
	var _ca []interface{}
	_ca = append(_ca, ctx, in)
	_ca = append(_ca, _va...)
	ret := _m.Called(_ca...)

	var r0 *info.InfoResponse
	if rf, ok := ret.Get(0).(func(context.Context, *info.GetInfoRequest, ...grpc.CallOption) *info.InfoResponse); ok {
		r0 = rf(ctx, in, opts...)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*info.InfoResponse)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(context.Context, *info.GetInfoRequest, ...grpc.CallOption) error); ok {
		r1 = rf(ctx, in, opts...)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
