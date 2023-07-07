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
pub struct IoArgoprojWorkflowV1alpha1LintCronWorkflowRequest {
    #[serde(rename = "cronWorkflow", skip_serializing_if = "Option::is_none")]
    pub cron_workflow: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1CronWorkflow>>,
    #[serde(rename = "namespace", skip_serializing_if = "Option::is_none")]
    pub namespace: Option<String>,
}

impl IoArgoprojWorkflowV1alpha1LintCronWorkflowRequest {
    pub fn new() -> IoArgoprojWorkflowV1alpha1LintCronWorkflowRequest {
        IoArgoprojWorkflowV1alpha1LintCronWorkflowRequest {
            cron_workflow: None,
            namespace: None,
        }
    }
}


