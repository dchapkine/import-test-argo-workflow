package auth

import (
	"context"
	"encoding/base64"
	"testing"

	"github.com/stretchr/testify/assert"
	"google.golang.org/grpc/metadata"
	"k8s.io/client-go/kubernetes/fake"
	"k8s.io/client-go/rest"

	wfv1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	fakewfclientset "github.com/argoproj/argo/pkg/client/clientset/versioned/fake"
)

func TestServer_GetWFClient(t *testing.T) {
	wfClient := &fakewfclientset.Clientset{}
	kubeClient := &fake.Clientset{}
	restConfig := &rest.Config{}

	testUser := wfv1.User{Name: "test"}
	t.Run("ServerAuth", func(t *testing.T) {
		s := NewGatekeeper("server", wfClient, kubeClient, nil, testUser)
		ctx, err := authAndHandle(s, context.TODO())
		if assert.NoError(t, err) {
			assert.Equal(t, wfClient, GetWfClient(*ctx))
			assert.Equal(t, kubeClient, GetKubeClient(*ctx))
			assert.Equal(t, testUser, GetUser(*ctx))
		}
	})
	t.Run("ClientAuth", func(t *testing.T) {
		t.SkipNow() // TODO
		s := NewGatekeeper("client", wfClient, kubeClient, restConfig, testUser)
		t.Run("AuthorizationHeader", func(t *testing.T) {
			ctx, err := authAndHandle(s, metadata.NewIncomingContext(context.Background(), metadata.Pairs("authorization", base64.StdEncoding.EncodeToString([]byte("anything")))))
			if assert.NoError(t, err) {
				assert.NotEqual(t, wfClient, GetWfClient(*ctx))
				assert.NotEqual(t, kubeClient, GetKubeClient(*ctx))
				assert.NotEqual(t, testUser, GetUser(*ctx))
			}
		})
		t.Run("Cookie", func(t *testing.T) {
			ctx, err := authAndHandle(s, metadata.NewIncomingContext(context.Background(), metadata.Pairs("grpcgateway-cookie", "authorization="+base64.StdEncoding.EncodeToString([]byte("anything")))))
			if assert.NoError(t, err) {
				assert.NotEqual(t, wfClient, GetWfClient(*ctx))
				assert.NotEqual(t, kubeClient, GetKubeClient(*ctx))
				assert.NotEqual(t, testUser, GetUser(*ctx))
			}
		})
	})
	t.Run("HybridAuth", func(t *testing.T) {
		t.SkipNow() // TODO
		s := NewGatekeeper("hybrid", wfClient, kubeClient, restConfig, testUser)
		t.Run("clientAuth", func(t *testing.T) {
			ctx, err := authAndHandle(s, metadata.NewIncomingContext(context.Background(), metadata.Pairs("authorization", base64.StdEncoding.EncodeToString([]byte("{anything}")))))
			if assert.NoError(t, err) {
				assert.NotEqual(t, wfClient, GetWfClient(*ctx))
				assert.NotEqual(t, kubeClient, GetKubeClient(*ctx))
				assert.NotEqual(t, testUser, GetUser(*ctx))
			}
		})
		t.Run("ServerAuth", func(t *testing.T) {
			ctx, err := authAndHandle(s, context.TODO())
			if assert.NoError(t, err) {
				assert.Equal(t, wfClient, GetWfClient(*ctx))
				assert.Equal(t, kubeClient, GetKubeClient(*ctx))
				assert.Equal(t, testUser, GetUser(*ctx))
			}
		})

	})
}

func authAndHandle(s Gatekeeper, ctx context.Context) (*context.Context, error) {
	var usedCtx *context.Context
	_, err := s.UnaryServerInterceptor()(ctx, nil, nil, func(ctx context.Context, req interface{}) (i interface{}, err error) {
		usedCtx = &ctx
		return nil, nil
	})
	return usedCtx, err
}
