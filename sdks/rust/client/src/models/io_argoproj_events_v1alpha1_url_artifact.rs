/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// IoArgoprojEventsV1alpha1UrlArtifact : URLArtifact contains information about an artifact at an http endpoint.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojEventsV1alpha1UrlArtifact {
    #[serde(rename = "path", skip_serializing_if = "Option::is_none")]
    pub path: Option<String>,
    #[serde(rename = "verifyCert", skip_serializing_if = "Option::is_none")]
    pub verify_cert: Option<bool>,
}

impl IoArgoprojEventsV1alpha1UrlArtifact {
    /// URLArtifact contains information about an artifact at an http endpoint.
    pub fn new() -> IoArgoprojEventsV1alpha1UrlArtifact {
        IoArgoprojEventsV1alpha1UrlArtifact {
            path: None,
            verify_cert: None,
        }
    }
}


