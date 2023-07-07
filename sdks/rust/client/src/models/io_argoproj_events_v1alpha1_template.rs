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
pub struct IoArgoprojEventsV1alpha1Template {
    #[serde(rename = "affinity", skip_serializing_if = "Option::is_none")]
    pub affinity: Option<Box<crate::models::Affinity>>,
    #[serde(rename = "container", skip_serializing_if = "Option::is_none")]
    pub container: Option<Box<crate::models::Container>>,
    #[serde(rename = "imagePullSecrets", skip_serializing_if = "Option::is_none")]
    pub image_pull_secrets: Option<Vec<crate::models::LocalObjectReference>>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<Box<crate::models::IoArgoprojEventsV1alpha1Metadata>>,
    #[serde(rename = "nodeSelector", skip_serializing_if = "Option::is_none")]
    pub node_selector: Option<::std::collections::HashMap<String, String>>,
    #[serde(rename = "priority", skip_serializing_if = "Option::is_none")]
    pub priority: Option<i32>,
    #[serde(rename = "priorityClassName", skip_serializing_if = "Option::is_none")]
    pub priority_class_name: Option<String>,
    #[serde(rename = "securityContext", skip_serializing_if = "Option::is_none")]
    pub security_context: Option<Box<crate::models::PodSecurityContext>>,
    #[serde(rename = "serviceAccountName", skip_serializing_if = "Option::is_none")]
    pub service_account_name: Option<String>,
    #[serde(rename = "tolerations", skip_serializing_if = "Option::is_none")]
    pub tolerations: Option<Vec<crate::models::Toleration>>,
    #[serde(rename = "volumes", skip_serializing_if = "Option::is_none")]
    pub volumes: Option<Vec<crate::models::Volume>>,
}

impl IoArgoprojEventsV1alpha1Template {
    pub fn new() -> IoArgoprojEventsV1alpha1Template {
        IoArgoprojEventsV1alpha1Template {
            affinity: None,
            container: None,
            image_pull_secrets: None,
            metadata: None,
            node_selector: None,
            priority: None,
            priority_class_name: None,
            security_context: None,
            service_account_name: None,
            tolerations: None,
            volumes: None,
        }
    }
}


