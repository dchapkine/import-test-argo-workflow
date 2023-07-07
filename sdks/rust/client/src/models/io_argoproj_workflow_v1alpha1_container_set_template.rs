/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojWorkflowV1alpha1ContainerSetTemplate {
    #[serde(rename = "containers")]
    pub containers: Vec<crate::models::IoArgoprojWorkflowV1alpha1ContainerNode>,
    #[serde(rename = "retryStrategy", skip_serializing_if = "Option::is_none")]
    pub retry_strategy: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1ContainerSetRetryStrategy>>,
    #[serde(rename = "volumeMounts", skip_serializing_if = "Option::is_none")]
    pub volume_mounts: Option<Vec<crate::models::VolumeMount>>,
}

impl IoArgoprojWorkflowV1alpha1ContainerSetTemplate {
    pub fn new(containers: Vec<crate::models::IoArgoprojWorkflowV1alpha1ContainerNode>) -> IoArgoprojWorkflowV1alpha1ContainerSetTemplate {
        IoArgoprojWorkflowV1alpha1ContainerSetTemplate {
            containers,
            retry_strategy: None,
            volume_mounts: None,
        }
    }
}


