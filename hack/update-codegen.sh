#!/bin/bash
set -eux -o pipefail

# @0.17.2
go install k8s.io/code-generator/cmd/client-gen
go install k8s.io/code-generator/cmd/informer-gen
go install k8s.io/code-generator/cmd/lister-gen

${GOPATH}/src/k8s.io/code-generator/generate-groups.sh \
  "deepcopy,client,informer,lister" \
  github.com/argoproj/argo/pkg/client github.com/argoproj/argo/pkg/apis \
  workflow:v1alpha1 \
  --go-header-file ./hack/custom-boilerplate.go.txt
