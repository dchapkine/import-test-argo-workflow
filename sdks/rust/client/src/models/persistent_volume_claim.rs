/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// PersistentVolumeClaim : PersistentVolumeClaim is a user's request for and claim to a persistent volume



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PersistentVolumeClaim {
    /// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    #[serde(rename = "apiVersion", skip_serializing_if = "Option::is_none")]
    pub api_version: Option<String>,
    /// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    #[serde(rename = "kind", skip_serializing_if = "Option::is_none")]
    pub kind: Option<String>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<Box<crate::models::ObjectMeta>>,
    #[serde(rename = "spec", skip_serializing_if = "Option::is_none")]
    pub spec: Option<Box<crate::models::PersistentVolumeClaimSpec>>,
    #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
    pub status: Option<Box<crate::models::PersistentVolumeClaimStatus>>,
}

impl PersistentVolumeClaim {
    /// PersistentVolumeClaim is a user's request for and claim to a persistent volume
    pub fn new() -> PersistentVolumeClaim {
        PersistentVolumeClaim {
            api_version: None,
            kind: None,
            metadata: None,
            spec: None,
            status: None,
        }
    }
}


