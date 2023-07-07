/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// IoArgoprojWorkflowV1alpha1Prometheus : Prometheus is a prometheus metric to be emitted



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct IoArgoprojWorkflowV1alpha1Prometheus {
    #[serde(rename = "counter", skip_serializing_if = "Option::is_none")]
    pub counter: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1Counter>>,
    #[serde(rename = "gauge", skip_serializing_if = "Option::is_none")]
    pub gauge: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1Gauge>>,
    /// Help is a string that describes the metric
    #[serde(rename = "help")]
    pub help: String,
    #[serde(rename = "histogram", skip_serializing_if = "Option::is_none")]
    pub histogram: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1Histogram>>,
    /// Labels is a list of metric labels
    #[serde(rename = "labels", skip_serializing_if = "Option::is_none")]
    pub labels: Option<Vec<crate::models::IoArgoprojWorkflowV1alpha1MetricLabel>>,
    /// Name is the name of the metric
    #[serde(rename = "name")]
    pub name: String,
    /// When is a conditional statement that decides when to emit the metric
    #[serde(rename = "when", skip_serializing_if = "Option::is_none")]
    pub when: Option<String>,
}

impl IoArgoprojWorkflowV1alpha1Prometheus {
    /// Prometheus is a prometheus metric to be emitted
    pub fn new(help: String, name: String) -> IoArgoprojWorkflowV1alpha1Prometheus {
        IoArgoprojWorkflowV1alpha1Prometheus {
            counter: None,
            gauge: None,
            help,
            histogram: None,
            labels: None,
            name,
            when: None,
        }
    }
}


