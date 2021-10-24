package k8s_utils

import (
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
	v1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/labels"
	kubefake "k8s.io/client-go/kubernetes/fake"

	"github.com/argoproj/argo-workflows/v3/workflow/common"
)

func checkServiceAccountExists(saList []*v1.ServiceAccount, name string) bool {
	for _, sa := range saList {
		if sa.Name == name {
			return true
		}
	}
	return false
}

func TestServer_K8sUtilsCache(t *testing.T) {
	_ = os.Setenv("KUBECONFIG", "/dev/null")
	defer func() { _ = os.Unsetenv("KUBECONFIG") }()
	kubeClient := kubefake.NewSimpleClientset(
		&v1.ServiceAccount{
			ObjectMeta: metav1.ObjectMeta{
				Name: "sa1", Namespace: "ns1",
				Annotations: map[string]string{
					common.AnnotationKeyRBACRule:           "'other-group' in groups",
					common.AnnotationKeyRBACRulePrecedence: "0",
				},
			},
			Secrets: []v1.ObjectReference{{Name: "my-secret"}},
		},
		&v1.ServiceAccount{
			ObjectMeta: metav1.ObjectMeta{
				Name: "sa2", Namespace: "ns1",
				Annotations: map[string]string{
					common.AnnotationKeyRBACRule:           "'my-group' in groups",
					common.AnnotationKeyRBACRulePrecedence: "1",
				},
			},
			Secrets: []v1.ObjectReference{{Name: "my-secret"}},
		},
		&v1.ServiceAccount{
			ObjectMeta: metav1.ObjectMeta{
				Name: "sa3", Namespace: "ns2",
				Annotations: map[string]string{
					common.AnnotationKeyRBACRule:           "'my-group' in groups",
					common.AnnotationKeyRBACRulePrecedence: "2",
				},
			},
			Secrets: []v1.ObjectReference{{Name: "user-secret"}},
		})
	cache := NewK8sCache(kubeClient)

	t.Run("List Service Accounts in different namespaces", func(t *testing.T) {
		sa, _ := cache.ServiceAccountLister.ServiceAccounts("ns1").List(labels.Everything())
		assert.Equal(t, len(sa), 2)
		assert.True(t, checkServiceAccountExists(sa, "sa1"))
		assert.True(t, checkServiceAccountExists(sa, "sa2"))

		sa, _ = cache.ServiceAccountLister.ServiceAccounts("ns2").List(labels.Everything())
		assert.Equal(t, len(sa), 1)
		assert.True(t, checkServiceAccountExists(sa, "sa3"))
	})
}
