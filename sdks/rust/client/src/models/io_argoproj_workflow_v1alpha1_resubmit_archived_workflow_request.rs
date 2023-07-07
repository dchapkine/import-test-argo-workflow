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
pub struct IoArgoprojWorkflowV1alpha1ResubmitArchivedWorkflowRequest {
    #[serde(rename = "memoized", skip_serializing_if = "Option::is_none")]
    pub memoized: Option<bool>,
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "namespace", skip_serializing_if = "Option::is_none")]
    pub namespace: Option<String>,
    #[serde(rename = "parameters", skip_serializing_if = "Option::is_none")]
    pub parameters: Option<Vec<String>>,
    #[serde(rename = "uid", skip_serializing_if = "Option::is_none")]
    pub uid: Option<String>,
}

impl IoArgoprojWorkflowV1alpha1ResubmitArchivedWorkflowRequest {
    pub fn new() -> IoArgoprojWorkflowV1alpha1ResubmitArchivedWorkflowRequest {
        IoArgoprojWorkflowV1alpha1ResubmitArchivedWorkflowRequest {
            memoized: None,
            name: None,
            namespace: None,
            parameters: None,
            uid: None,
        }
    }
}


