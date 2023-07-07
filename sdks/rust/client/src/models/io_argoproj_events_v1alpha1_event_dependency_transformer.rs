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
pub struct IoArgoprojEventsV1alpha1EventDependencyTransformer {
    #[serde(rename = "jq", skip_serializing_if = "Option::is_none")]
    pub jq: Option<String>,
    #[serde(rename = "script", skip_serializing_if = "Option::is_none")]
    pub script: Option<String>,
}

impl IoArgoprojEventsV1alpha1EventDependencyTransformer {
    pub fn new() -> IoArgoprojEventsV1alpha1EventDependencyTransformer {
        IoArgoprojEventsV1alpha1EventDependencyTransformer {
            jq: None,
            script: None,
        }
    }
}


