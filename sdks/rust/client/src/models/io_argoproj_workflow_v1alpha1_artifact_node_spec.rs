/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// IoArgoprojWorkflowV1alpha1ArtifactNodeSpec : ArtifactNodeSpec specifies the Artifacts that need to be deleted for a given Node



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojWorkflowV1alpha1ArtifactNodeSpec {
    #[serde(rename = "archiveLocation", skip_serializing_if = "Option::is_none")]
    pub archive_location: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1ArtifactLocation>>,
    /// Artifacts maps artifact name to Artifact description
    #[serde(rename = "artifacts", skip_serializing_if = "Option::is_none")]
    pub artifacts: Option<::std::collections::HashMap<String, crate::models::IoArgoprojWorkflowV1alpha1Artifact>>,
}

impl IoArgoprojWorkflowV1alpha1ArtifactNodeSpec {
    /// ArtifactNodeSpec specifies the Artifacts that need to be deleted for a given Node
    pub fn new() -> IoArgoprojWorkflowV1alpha1ArtifactNodeSpec {
        IoArgoprojWorkflowV1alpha1ArtifactNodeSpec {
            archive_location: None,
            artifacts: None,
        }
    }
}


