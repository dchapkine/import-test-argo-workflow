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
pub struct IoArgoprojWorkflowV1alpha1Submit {
    #[serde(rename = "arguments", skip_serializing_if = "Option::is_none")]
    pub arguments: Option<Box<crate::models::IoArgoprojWorkflowV1alpha1Arguments>>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<Box<crate::models::ObjectMeta>>,
    #[serde(rename = "workflowTemplateRef")]
    pub workflow_template_ref: Box<crate::models::IoArgoprojWorkflowV1alpha1WorkflowTemplateRef>,
}

impl IoArgoprojWorkflowV1alpha1Submit {
    pub fn new(workflow_template_ref: crate::models::IoArgoprojWorkflowV1alpha1WorkflowTemplateRef) -> IoArgoprojWorkflowV1alpha1Submit {
        IoArgoprojWorkflowV1alpha1Submit {
            arguments: None,
            metadata: None,
            workflow_template_ref: Box::new(workflow_template_ref),
        }
    }
}


