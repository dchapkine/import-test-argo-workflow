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
pub struct IoArgoprojEventsV1alpha1ArtifactLocation {
    #[serde(rename = "configmap", skip_serializing_if = "Option::is_none")]
    pub configmap: Option<Box<crate::models::ConfigMapKeySelector>>,
    #[serde(rename = "file", skip_serializing_if = "Option::is_none")]
    pub file: Option<Box<crate::models::IoArgoprojEventsV1alpha1FileArtifact>>,
    #[serde(rename = "git", skip_serializing_if = "Option::is_none")]
    pub git: Option<Box<crate::models::IoArgoprojEventsV1alpha1GitArtifact>>,
    #[serde(rename = "inline", skip_serializing_if = "Option::is_none")]
    pub inline: Option<String>,
    #[serde(rename = "resource", skip_serializing_if = "Option::is_none")]
    pub resource: Option<Box<crate::models::IoArgoprojEventsV1alpha1Resource>>,
    #[serde(rename = "s3", skip_serializing_if = "Option::is_none")]
    pub s3: Option<Box<crate::models::IoArgoprojEventsV1alpha1S3Artifact>>,
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<Box<crate::models::IoArgoprojEventsV1alpha1UrlArtifact>>,
}

impl IoArgoprojEventsV1alpha1ArtifactLocation {
    pub fn new() -> IoArgoprojEventsV1alpha1ArtifactLocation {
        IoArgoprojEventsV1alpha1ArtifactLocation {
            configmap: None,
            file: None,
            git: None,
            inline: None,
            resource: None,
            s3: None,
            url: None,
        }
    }
}


