[![slack](https://img.shields.io/badge/slack-argoproj-brightgreen.svg?logo=slack)](https://argoproj.github.io/community/join-slack)

# ArgoProj - Get stuff done with Kubernetes

![Argo Image](argo.png)

## News

We are thrilled that BlackRock has developed an eventing framework for Argo and has decided to contribute it to the Argo Community. Please check out the new project and try [Argo Events](https://github.com/argoproj/argo-events)!

If you actively use Argo in your organization and believe that your organization may be interested in actively participating in the Argo Community, please ask a representative to contact saradhi_sreegiriraju@intuit.com for additional information.

## What is ArgoProj?

ArgoProj is a collection of tools for getting work done with Kubernetes.
* [Argo Workflows](https://github.com/argoproj/argo) - Container-native Workflow Engine
* [Argo CD](https://github.com/argoproj/argo-cd) - Declarative GitOps Continuous Delivery
* [Argo Events](https://github.com/argoproj/argo-events) - Event-based Dependency Manager
* [Argo CI](https://github.com/argoproj/argo-ci) - Simple CI based on GitHUb and Argo Workflows


## What is Argo Workflows?
Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. Argo Workflows is implemented as a Kubernetes CRD (Custom Resource Definition).

* Define workflows where each step in the workflow is a container.
* Model multi-step workflows as a sequence of tasks or capture the dependencies between tasks using a graph (DAG).
* Easily run compute intensive jobs for machine learning or data processing in a fraction of the time using Argo Workflows on Kubernetes.
* Run CI/CD pipelines natively on Kubernetes without configuring complex software development products.

## Why Argo Workflows?
* Designed from the ground up for containers without the overhead and limitations of legacy VM and server-based environments.
* Cloud agnostic and can run on any kubernetes cluster.
* Easily ochestrate highly parallel jobs on Kubernets.
* Argo Workflows puts a cloud-scale supercomputer at your fingertips!

## Documentation
* [Get started here](demo.md)
* [How to write Argo Workflow specs](examples/README.md)
* [How to configure your artifact repository](ARTIFACT_REPO.md)

## Features
* DAG or Steps based declaration of workflows
* Artifact support (S3, Artifactory, HTTP, Git, raw)
* Step level input & outputs (artifacts/parameters)
* Loops
* Parameterization
* Conditionals
* Timeouts (step & workflow level)
* Retry (step & workflow level)
* Resubmit (memoized)
* Suspend & Resume
* Cancellation
* K8s resource orchestration
* Exit Hooks (notifications, cleanup)
* Garbage collection of completed workflow
* Scheduling (affinity/tolerations/node selectors)
* Volumes (ephemeral/existing)
* Parallelism limits
* Daemoned steps
* DinD (docker-in-docker)
* Script steps

## Who uses Argo?
As the Argo Community grows, we'd like to keep track of our users. Please send a PR with your organization name.

Currently **officially** using Argo:

1. [Adobe](https://www.adobe.com/) 
1. [BlackRock](https://www.blackrock.com/)
1. [CoreFiling](https://www.corefiling.com/)
1. [Cratejoy](https://www.cratejoy.com/)
1. [Cyrus Biotechnology](https://cyrusbio.com/)
1. [Datadog](https://www.datadoghq.com/)
1. [Equinor](https://www.equinor.com/)
1. [Gladly](https://gladly.com/)
1. [GitHub](https://github.com/)
1. [Google](https://www.google.com/intl/en/about/our-company/)
1. [Interline Technologies](https://www.interline.io/blog/scaling-openstreetmap-data-workflows/)
1. [Intuit](https://www.intuit.com/)
1. [KintoHub](https://www.kintohub.com/)
1. [Localytics](https://www.localytics.com/)
1. [NVIDIA](https://www.nvidia.com/)
1. [Preferred Networks](https://www.preferred-networks.jp/en/)
1. [SAP Hybris](https://cx.sap.com/)
1. [Styra](https://www.styra.com/)
1. [Quantibio](http://quantibio.com/us/en/)

## Community Blogs and Presentations
* [Open Source Model Management Roundup: Polyaxon, Argo, and Seldon](https://www.anaconda.com/blog/developer-blog/open-source-model-management-roundup-polyaxon-argo-and-seldon/)
* [Producing 200 OpenStreetMap extracts in 35 minutes using a scalable data workflow](https://www.interline.io/blog/scaling-openstreetmap-data-workflows/)
* [Argo integration review](http://dev.matt.hillsdon.net/2018/03/24/argo-integration-review.html)
* TGI Kubernetes with Joe Beda: [Argo workflow system](https://www.youtube.com/watch?v=M_rxPPLG8pU&start=859)
* [Community meeting minutes and recordings](https://docs.google.com/document/d/16aWGQ1Te5IRptFuAIFtg3rONRQqHC1Z3X9rdDHYhYfE)

## Project Resources
* Argo GitHub:  https://github.com/argoproj
* Argo Slack:   [click here to join](https://join.slack.com/t/argoproj/shared_invite/enQtMzExODU3MzIyNjYzLTA5MTFjNjI0Nzg3NzNiMDZiNmRiODM4Y2M1NWQxOGYzMzZkNTc1YWVkYTZkNzdlNmYyZjMxNWI3NjY2MDc1MzI)
* Argo website: https://argoproj.github.io/
