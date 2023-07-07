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
pub struct IoArgoprojEventsV1alpha1EventContext {
    /// DataContentType - A MIME (RFC2046) string describing the media type of `data`.
    #[serde(rename = "datacontenttype", skip_serializing_if = "Option::is_none")]
    pub datacontenttype: Option<String>,
    /// ID of the event; must be non-empty and unique within the scope of the producer.
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    /// Source - A URI describing the event producer.
    #[serde(rename = "source", skip_serializing_if = "Option::is_none")]
    pub source: Option<String>,
    /// SpecVersion - The version of the CloudEvents specification used by the io.argoproj.workflow.v1alpha1.
    #[serde(rename = "specversion", skip_serializing_if = "Option::is_none")]
    pub specversion: Option<String>,
    #[serde(rename = "subject", skip_serializing_if = "Option::is_none")]
    pub subject: Option<String>,
    /// Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.
    #[serde(rename = "time", skip_serializing_if = "Option::is_none")]
    pub time: Option<String>,
    /// Type - The type of the occurrence which has happened.
    #[serde(rename = "type", skip_serializing_if = "Option::is_none")]
    pub _type: Option<String>,
}

impl IoArgoprojEventsV1alpha1EventContext {
    pub fn new() -> IoArgoprojEventsV1alpha1EventContext {
        IoArgoprojEventsV1alpha1EventContext {
            datacontenttype: None,
            id: None,
            source: None,
            specversion: None,
            subject: None,
            time: None,
            _type: None,
        }
    }
}


