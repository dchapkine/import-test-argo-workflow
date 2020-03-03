// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: pkg/apiclient/workflowarchive/workflow-archive.proto

package workflowarchive

import (
	context "context"
	fmt "fmt"
	v1alpha1 "github.com/argoproj/argo/v2/pkg/apis/workflow/v1alpha1"
	_ "github.com/gogo/protobuf/gogoproto"
	proto "github.com/gogo/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	io "io"
	_ "k8s.io/api/core/v1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	math "math"
	math_bits "math/bits"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

type ListArchivedWorkflowsRequest struct {
	ListOptions          *v1.ListOptions `protobuf:"bytes,1,opt,name=listOptions,proto3" json:"listOptions,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *ListArchivedWorkflowsRequest) Reset()         { *m = ListArchivedWorkflowsRequest{} }
func (m *ListArchivedWorkflowsRequest) String() string { return proto.CompactTextString(m) }
func (*ListArchivedWorkflowsRequest) ProtoMessage()    {}
func (*ListArchivedWorkflowsRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_95ca9a2d33e8bb19, []int{0}
}
func (m *ListArchivedWorkflowsRequest) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *ListArchivedWorkflowsRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_ListArchivedWorkflowsRequest.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *ListArchivedWorkflowsRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListArchivedWorkflowsRequest.Merge(m, src)
}
func (m *ListArchivedWorkflowsRequest) XXX_Size() int {
	return m.Size()
}
func (m *ListArchivedWorkflowsRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ListArchivedWorkflowsRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ListArchivedWorkflowsRequest proto.InternalMessageInfo

func (m *ListArchivedWorkflowsRequest) GetListOptions() *v1.ListOptions {
	if m != nil {
		return m.ListOptions
	}
	return nil
}

type GetArchivedWorkflowRequest struct {
	Uid                  string   `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetArchivedWorkflowRequest) Reset()         { *m = GetArchivedWorkflowRequest{} }
func (m *GetArchivedWorkflowRequest) String() string { return proto.CompactTextString(m) }
func (*GetArchivedWorkflowRequest) ProtoMessage()    {}
func (*GetArchivedWorkflowRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_95ca9a2d33e8bb19, []int{1}
}
func (m *GetArchivedWorkflowRequest) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *GetArchivedWorkflowRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_GetArchivedWorkflowRequest.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *GetArchivedWorkflowRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetArchivedWorkflowRequest.Merge(m, src)
}
func (m *GetArchivedWorkflowRequest) XXX_Size() int {
	return m.Size()
}
func (m *GetArchivedWorkflowRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetArchivedWorkflowRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetArchivedWorkflowRequest proto.InternalMessageInfo

func (m *GetArchivedWorkflowRequest) GetUid() string {
	if m != nil {
		return m.Uid
	}
	return ""
}

type DeleteArchivedWorkflowRequest struct {
	Uid                  string   `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeleteArchivedWorkflowRequest) Reset()         { *m = DeleteArchivedWorkflowRequest{} }
func (m *DeleteArchivedWorkflowRequest) String() string { return proto.CompactTextString(m) }
func (*DeleteArchivedWorkflowRequest) ProtoMessage()    {}
func (*DeleteArchivedWorkflowRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_95ca9a2d33e8bb19, []int{2}
}
func (m *DeleteArchivedWorkflowRequest) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *DeleteArchivedWorkflowRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_DeleteArchivedWorkflowRequest.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *DeleteArchivedWorkflowRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeleteArchivedWorkflowRequest.Merge(m, src)
}
func (m *DeleteArchivedWorkflowRequest) XXX_Size() int {
	return m.Size()
}
func (m *DeleteArchivedWorkflowRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_DeleteArchivedWorkflowRequest.DiscardUnknown(m)
}

var xxx_messageInfo_DeleteArchivedWorkflowRequest proto.InternalMessageInfo

func (m *DeleteArchivedWorkflowRequest) GetUid() string {
	if m != nil {
		return m.Uid
	}
	return ""
}

type ArchivedWorkflowDeletedResponse struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ArchivedWorkflowDeletedResponse) Reset()         { *m = ArchivedWorkflowDeletedResponse{} }
func (m *ArchivedWorkflowDeletedResponse) String() string { return proto.CompactTextString(m) }
func (*ArchivedWorkflowDeletedResponse) ProtoMessage()    {}
func (*ArchivedWorkflowDeletedResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_95ca9a2d33e8bb19, []int{3}
}
func (m *ArchivedWorkflowDeletedResponse) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *ArchivedWorkflowDeletedResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_ArchivedWorkflowDeletedResponse.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *ArchivedWorkflowDeletedResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ArchivedWorkflowDeletedResponse.Merge(m, src)
}
func (m *ArchivedWorkflowDeletedResponse) XXX_Size() int {
	return m.Size()
}
func (m *ArchivedWorkflowDeletedResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ArchivedWorkflowDeletedResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ArchivedWorkflowDeletedResponse proto.InternalMessageInfo

func init() {
	proto.RegisterType((*ListArchivedWorkflowsRequest)(nil), "workflowarchive.ListArchivedWorkflowsRequest")
	proto.RegisterType((*GetArchivedWorkflowRequest)(nil), "workflowarchive.GetArchivedWorkflowRequest")
	proto.RegisterType((*DeleteArchivedWorkflowRequest)(nil), "workflowarchive.DeleteArchivedWorkflowRequest")
	proto.RegisterType((*ArchivedWorkflowDeletedResponse)(nil), "workflowarchive.ArchivedWorkflowDeletedResponse")
}

func init() {
	proto.RegisterFile("pkg/apiclient/workflowarchive/workflow-archive.proto", fileDescriptor_95ca9a2d33e8bb19)
}

var fileDescriptor_95ca9a2d33e8bb19 = []byte{
	// 475 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x54, 0xcd, 0x8a, 0xd4, 0x40,
	0x10, 0x26, 0x2a, 0x82, 0xbd, 0x07, 0xa5, 0xc5, 0x1f, 0xc2, 0x38, 0xae, 0x39, 0x2d, 0xca, 0x54,
	0x9b, 0x75, 0x11, 0x2f, 0x1e, 0x56, 0x17, 0xbc, 0x2c, 0x08, 0xb3, 0x07, 0xc1, 0x5b, 0x4f, 0x52,
	0xdb, 0xd3, 0x4e, 0x26, 0x1d, 0xbb, 0x3b, 0x19, 0x44, 0xbc, 0xf8, 0x0a, 0xde, 0x3d, 0x79, 0x13,
	0xdf, 0xc3, 0xa3, 0xe0, 0x0b, 0xc8, 0xe0, 0x83, 0x48, 0x7a, 0x92, 0xcd, 0x90, 0x64, 0x67, 0x84,
	0xbd, 0x55, 0x75, 0x57, 0x7d, 0xdf, 0x57, 0xf5, 0xa5, 0x43, 0x0e, 0xb2, 0x99, 0x60, 0x3c, 0x93,
	0x51, 0x22, 0x31, 0xb5, 0x6c, 0xa1, 0xf4, 0xec, 0x34, 0x51, 0x0b, 0xae, 0xa3, 0xa9, 0x2c, 0xf0,
	0x2c, 0x1f, 0x55, 0x07, 0x90, 0x69, 0x65, 0x15, 0xbd, 0xde, 0xaa, 0xf3, 0x47, 0x42, 0xda, 0x69,
	0x3e, 0x81, 0x48, 0xcd, 0x99, 0x50, 0x42, 0x31, 0x57, 0x37, 0xc9, 0x4f, 0x5d, 0xe6, 0x12, 0x17,
	0xad, 0xfa, 0xfd, 0x81, 0x50, 0x4a, 0x24, 0x58, 0x12, 0x33, 0x9e, 0xa6, 0xca, 0x72, 0x2b, 0x55,
	0x6a, 0xaa, 0xdb, 0x83, 0xd9, 0x33, 0x03, 0x52, 0x95, 0xb7, 0x73, 0x1e, 0x4d, 0x65, 0x8a, 0xfa,
	0x03, 0xab, 0x74, 0x1a, 0x36, 0x47, 0xcb, 0x59, 0x11, 0x32, 0x81, 0x29, 0x6a, 0x6e, 0x31, 0xae,
	0xba, 0x5e, 0xae, 0x49, 0xe0, 0xda, 0x91, 0xbe, 0x73, 0x41, 0xd3, 0x5a, 0xab, 0x66, 0x45, 0xc8,
	0x93, 0x6c, 0xca, 0xbb, 0x20, 0x41, 0x43, 0xcd, 0x22, 0xa5, 0xb1, 0x87, 0x28, 0x30, 0x64, 0x70,
	0x2c, 0x8d, 0x3d, 0x5c, 0x8d, 0x1e, 0xbf, 0xa9, 0x40, 0xcd, 0x18, 0xdf, 0xe7, 0x68, 0x2c, 0x3d,
	0x21, 0x3b, 0x89, 0x34, 0xf6, 0x75, 0xe6, 0x66, 0xba, 0xeb, 0xed, 0x7a, 0x7b, 0x3b, 0xfb, 0x21,
	0xac, 0x90, 0x61, 0x7d, 0x28, 0xc8, 0x66, 0xa2, 0x3c, 0x30, 0x50, 0x0e, 0x05, 0x45, 0x08, 0xc7,
	0x4d, 0xe3, 0x78, 0x1d, 0x25, 0x00, 0xe2, 0xbf, 0xc2, 0x0e, 0x67, 0x4d, 0x79, 0x83, 0x5c, 0xce,
	0x65, 0xec, 0xa8, 0xae, 0x8d, 0xcb, 0x30, 0x08, 0xc9, 0xbd, 0x23, 0x4c, 0xd0, 0xe2, 0xff, 0xb7,
	0x3c, 0x20, 0xf7, 0xdb, 0xc5, 0x2b, 0x88, 0x78, 0x8c, 0x26, 0x53, 0xa9, 0xc1, 0xfd, 0xaf, 0x57,
	0xc8, 0x9d, 0x76, 0xcd, 0x09, 0xea, 0x42, 0x46, 0x48, 0x7f, 0x78, 0xe4, 0x56, 0xef, 0x5e, 0xe8,
	0x08, 0x5a, 0x9f, 0x0b, 0x6c, 0xda, 0x9f, 0x7f, 0x08, 0x8d, 0x93, 0x50, 0x3b, 0xe9, 0x82, 0x66,
	0x5f, 0x35, 0x20, 0xd4, 0x4e, 0x42, 0x0d, 0x53, 0x42, 0x07, 0xc1, 0xe7, 0xdf, 0x7f, 0xbf, 0x5c,
	0x1a, 0x50, 0xdf, 0x19, 0x59, 0x84, 0xac, 0x22, 0x8e, 0x47, 0x8b, 0x33, 0x55, 0xdf, 0x3d, 0x72,
	0xb3, 0x67, 0xa5, 0xf4, 0x51, 0x47, 0xed, 0xf9, 0x8b, 0xf7, 0x9f, 0x5f, 0x48, 0x6b, 0xb0, 0xe7,
	0x74, 0x06, 0x74, 0xf7, 0x7c, 0x9d, 0xec, 0x63, 0x2e, 0xe3, 0x4f, 0xf4, 0x9b, 0x47, 0x6e, 0xf7,
	0x1b, 0x4a, 0xa1, 0x23, 0x78, 0xa3, 0xf3, 0xfe, 0xe3, 0x4e, 0xfd, 0x16, 0xdb, 0x6b, 0x99, 0x0f,
	0xb7, 0xca, 0x7c, 0x71, 0xf4, 0x73, 0x39, 0xf4, 0x7e, 0x2d, 0x87, 0xde, 0x9f, 0xe5, 0xd0, 0x7b,
	0xfb, 0x74, 0xdb, 0x93, 0xec, 0xff, 0xeb, 0x4c, 0xae, 0xba, 0x87, 0xf6, 0xe4, 0x5f, 0x00, 0x00,
	0x00, 0xff, 0xff, 0x61, 0x99, 0xcf, 0x20, 0x9d, 0x04, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// ArchivedWorkflowServiceClient is the client API for ArchivedWorkflowService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type ArchivedWorkflowServiceClient interface {
	ListArchivedWorkflows(ctx context.Context, in *ListArchivedWorkflowsRequest, opts ...grpc.CallOption) (*v1alpha1.WorkflowList, error)
	GetArchivedWorkflow(ctx context.Context, in *GetArchivedWorkflowRequest, opts ...grpc.CallOption) (*v1alpha1.Workflow, error)
	DeleteArchivedWorkflow(ctx context.Context, in *DeleteArchivedWorkflowRequest, opts ...grpc.CallOption) (*ArchivedWorkflowDeletedResponse, error)
}

type archivedWorkflowServiceClient struct {
	cc *grpc.ClientConn
}

func NewArchivedWorkflowServiceClient(cc *grpc.ClientConn) ArchivedWorkflowServiceClient {
	return &archivedWorkflowServiceClient{cc}
}

func (c *archivedWorkflowServiceClient) ListArchivedWorkflows(ctx context.Context, in *ListArchivedWorkflowsRequest, opts ...grpc.CallOption) (*v1alpha1.WorkflowList, error) {
	out := new(v1alpha1.WorkflowList)
	err := c.cc.Invoke(ctx, "/workflowarchive.ArchivedWorkflowService/ListArchivedWorkflows", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *archivedWorkflowServiceClient) GetArchivedWorkflow(ctx context.Context, in *GetArchivedWorkflowRequest, opts ...grpc.CallOption) (*v1alpha1.Workflow, error) {
	out := new(v1alpha1.Workflow)
	err := c.cc.Invoke(ctx, "/workflowarchive.ArchivedWorkflowService/GetArchivedWorkflow", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *archivedWorkflowServiceClient) DeleteArchivedWorkflow(ctx context.Context, in *DeleteArchivedWorkflowRequest, opts ...grpc.CallOption) (*ArchivedWorkflowDeletedResponse, error) {
	out := new(ArchivedWorkflowDeletedResponse)
	err := c.cc.Invoke(ctx, "/workflowarchive.ArchivedWorkflowService/DeleteArchivedWorkflow", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ArchivedWorkflowServiceServer is the server API for ArchivedWorkflowService service.
type ArchivedWorkflowServiceServer interface {
	ListArchivedWorkflows(context.Context, *ListArchivedWorkflowsRequest) (*v1alpha1.WorkflowList, error)
	GetArchivedWorkflow(context.Context, *GetArchivedWorkflowRequest) (*v1alpha1.Workflow, error)
	DeleteArchivedWorkflow(context.Context, *DeleteArchivedWorkflowRequest) (*ArchivedWorkflowDeletedResponse, error)
}

// UnimplementedArchivedWorkflowServiceServer can be embedded to have forward compatible implementations.
type UnimplementedArchivedWorkflowServiceServer struct {
}

func (*UnimplementedArchivedWorkflowServiceServer) ListArchivedWorkflows(ctx context.Context, req *ListArchivedWorkflowsRequest) (*v1alpha1.WorkflowList, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListArchivedWorkflows not implemented")
}
func (*UnimplementedArchivedWorkflowServiceServer) GetArchivedWorkflow(ctx context.Context, req *GetArchivedWorkflowRequest) (*v1alpha1.Workflow, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetArchivedWorkflow not implemented")
}
func (*UnimplementedArchivedWorkflowServiceServer) DeleteArchivedWorkflow(ctx context.Context, req *DeleteArchivedWorkflowRequest) (*ArchivedWorkflowDeletedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteArchivedWorkflow not implemented")
}

func RegisterArchivedWorkflowServiceServer(s *grpc.Server, srv ArchivedWorkflowServiceServer) {
	s.RegisterService(&_ArchivedWorkflowService_serviceDesc, srv)
}

func _ArchivedWorkflowService_ListArchivedWorkflows_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListArchivedWorkflowsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ArchivedWorkflowServiceServer).ListArchivedWorkflows(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/workflowarchive.ArchivedWorkflowService/ListArchivedWorkflows",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ArchivedWorkflowServiceServer).ListArchivedWorkflows(ctx, req.(*ListArchivedWorkflowsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ArchivedWorkflowService_GetArchivedWorkflow_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetArchivedWorkflowRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ArchivedWorkflowServiceServer).GetArchivedWorkflow(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/workflowarchive.ArchivedWorkflowService/GetArchivedWorkflow",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ArchivedWorkflowServiceServer).GetArchivedWorkflow(ctx, req.(*GetArchivedWorkflowRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ArchivedWorkflowService_DeleteArchivedWorkflow_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteArchivedWorkflowRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ArchivedWorkflowServiceServer).DeleteArchivedWorkflow(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/workflowarchive.ArchivedWorkflowService/DeleteArchivedWorkflow",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ArchivedWorkflowServiceServer).DeleteArchivedWorkflow(ctx, req.(*DeleteArchivedWorkflowRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _ArchivedWorkflowService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "workflowarchive.ArchivedWorkflowService",
	HandlerType: (*ArchivedWorkflowServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListArchivedWorkflows",
			Handler:    _ArchivedWorkflowService_ListArchivedWorkflows_Handler,
		},
		{
			MethodName: "GetArchivedWorkflow",
			Handler:    _ArchivedWorkflowService_GetArchivedWorkflow_Handler,
		},
		{
			MethodName: "DeleteArchivedWorkflow",
			Handler:    _ArchivedWorkflowService_DeleteArchivedWorkflow_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pkg/apiclient/workflowarchive/workflow-archive.proto",
}

func (m *ListArchivedWorkflowsRequest) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *ListArchivedWorkflowsRequest) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *ListArchivedWorkflowsRequest) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if m.ListOptions != nil {
		{
			size, err := m.ListOptions.MarshalToSizedBuffer(dAtA[:i])
			if err != nil {
				return 0, err
			}
			i -= size
			i = encodeVarintWorkflowArchive(dAtA, i, uint64(size))
		}
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *GetArchivedWorkflowRequest) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *GetArchivedWorkflowRequest) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *GetArchivedWorkflowRequest) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.Uid) > 0 {
		i -= len(m.Uid)
		copy(dAtA[i:], m.Uid)
		i = encodeVarintWorkflowArchive(dAtA, i, uint64(len(m.Uid)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *DeleteArchivedWorkflowRequest) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *DeleteArchivedWorkflowRequest) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *DeleteArchivedWorkflowRequest) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.Uid) > 0 {
		i -= len(m.Uid)
		copy(dAtA[i:], m.Uid)
		i = encodeVarintWorkflowArchive(dAtA, i, uint64(len(m.Uid)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *ArchivedWorkflowDeletedResponse) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *ArchivedWorkflowDeletedResponse) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *ArchivedWorkflowDeletedResponse) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	return len(dAtA) - i, nil
}

func encodeVarintWorkflowArchive(dAtA []byte, offset int, v uint64) int {
	offset -= sovWorkflowArchive(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *ListArchivedWorkflowsRequest) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.ListOptions != nil {
		l = m.ListOptions.Size()
		n += 1 + l + sovWorkflowArchive(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *GetArchivedWorkflowRequest) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.Uid)
	if l > 0 {
		n += 1 + l + sovWorkflowArchive(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *DeleteArchivedWorkflowRequest) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.Uid)
	if l > 0 {
		n += 1 + l + sovWorkflowArchive(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *ArchivedWorkflowDeletedResponse) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func sovWorkflowArchive(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozWorkflowArchive(x uint64) (n int) {
	return sovWorkflowArchive(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *ListArchivedWorkflowsRequest) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowWorkflowArchive
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: ListArchivedWorkflowsRequest: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: ListArchivedWorkflowsRequest: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field ListOptions", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowWorkflowArchive
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.ListOptions == nil {
				m.ListOptions = &v1.ListOptions{}
			}
			if err := m.ListOptions.Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipWorkflowArchive(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *GetArchivedWorkflowRequest) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowWorkflowArchive
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: GetArchivedWorkflowRequest: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: GetArchivedWorkflowRequest: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Uid", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowWorkflowArchive
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Uid = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipWorkflowArchive(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *DeleteArchivedWorkflowRequest) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowWorkflowArchive
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: DeleteArchivedWorkflowRequest: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: DeleteArchivedWorkflowRequest: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Uid", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowWorkflowArchive
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Uid = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipWorkflowArchive(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *ArchivedWorkflowDeletedResponse) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowWorkflowArchive
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: ArchivedWorkflowDeletedResponse: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: ArchivedWorkflowDeletedResponse: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		default:
			iNdEx = preIndex
			skippy, err := skipWorkflowArchive(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthWorkflowArchive
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipWorkflowArchive(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	depth := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowWorkflowArchive
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowWorkflowArchive
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
		case 1:
			iNdEx += 8
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowWorkflowArchive
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthWorkflowArchive
			}
			iNdEx += length
		case 3:
			depth++
		case 4:
			if depth == 0 {
				return 0, ErrUnexpectedEndOfGroupWorkflowArchive
			}
			depth--
		case 5:
			iNdEx += 4
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
		if iNdEx < 0 {
			return 0, ErrInvalidLengthWorkflowArchive
		}
		if depth == 0 {
			return iNdEx, nil
		}
	}
	return 0, io.ErrUnexpectedEOF
}

var (
	ErrInvalidLengthWorkflowArchive        = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowWorkflowArchive          = fmt.Errorf("proto: integer overflow")
	ErrUnexpectedEndOfGroupWorkflowArchive = fmt.Errorf("proto: unexpected end of group")
)
