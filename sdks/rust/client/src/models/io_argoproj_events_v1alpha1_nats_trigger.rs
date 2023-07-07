/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// IoArgoprojEventsV1alpha1NatsTrigger : NATSTrigger refers to the specification of the NATS trigger.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojEventsV1alpha1NatsTrigger {
    #[serde(rename = "parameters", skip_serializing_if = "Option::is_none")]
    pub parameters: Option<Vec<crate::models::IoArgoprojEventsV1alpha1TriggerParameter>>,
    #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<Vec<crate::models::IoArgoprojEventsV1alpha1TriggerParameter>>,
    /// Name of the subject to put message on.
    #[serde(rename = "subject", skip_serializing_if = "Option::is_none")]
    pub subject: Option<String>,
    #[serde(rename = "tls", skip_serializing_if = "Option::is_none")]
    pub tls: Option<Box<crate::models::IoArgoprojEventsV1alpha1TlsConfig>>,
    /// URL of the NATS cluster.
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<String>,
}

impl IoArgoprojEventsV1alpha1NatsTrigger {
    /// NATSTrigger refers to the specification of the NATS trigger.
    pub fn new() -> IoArgoprojEventsV1alpha1NatsTrigger {
        IoArgoprojEventsV1alpha1NatsTrigger {
            parameters: None,
            payload: None,
            subject: None,
            tls: None,
            url: None,
        }
    }
}


