/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// IoArgoprojWorkflowV1alpha1OAuth2Auth : OAuth2Auth holds all information for client authentication via OAuth2 tokens



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojWorkflowV1alpha1OAuth2Auth {
    #[serde(rename = "clientIDSecret", skip_serializing_if = "Option::is_none")]
    pub client_id_secret: Option<Box<crate::models::SecretKeySelector>>,
    #[serde(rename = "clientSecretSecret", skip_serializing_if = "Option::is_none")]
    pub client_secret_secret: Option<Box<crate::models::SecretKeySelector>>,
    #[serde(rename = "endpointParams", skip_serializing_if = "Option::is_none")]
    pub endpoint_params: Option<Vec<crate::models::IoArgoprojWorkflowV1alpha1OAuth2EndpointParam>>,
    #[serde(rename = "scopes", skip_serializing_if = "Option::is_none")]
    pub scopes: Option<Vec<String>>,
    #[serde(rename = "tokenURLSecret", skip_serializing_if = "Option::is_none")]
    pub token_url_secret: Option<Box<crate::models::SecretKeySelector>>,
}

impl IoArgoprojWorkflowV1alpha1OAuth2Auth {
    /// OAuth2Auth holds all information for client authentication via OAuth2 tokens
    pub fn new() -> IoArgoprojWorkflowV1alpha1OAuth2Auth {
        IoArgoprojWorkflowV1alpha1OAuth2Auth {
            client_id_secret: None,
            client_secret_secret: None,
            endpoint_params: None,
            scopes: None,
            token_url_secret: None,
        }
    }
}


