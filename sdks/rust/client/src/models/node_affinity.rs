/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// NodeAffinity : Node affinity is a group of node affinity scheduling rules.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct NodeAffinity {
    /// The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    #[serde(rename = "preferredDuringSchedulingIgnoredDuringExecution", skip_serializing_if = "Option::is_none")]
    pub preferred_during_scheduling_ignored_during_execution: Option<Vec<crate::models::PreferredSchedulingTerm>>,
    #[serde(rename = "requiredDuringSchedulingIgnoredDuringExecution", skip_serializing_if = "Option::is_none")]
    pub required_during_scheduling_ignored_during_execution: Option<Box<crate::models::NodeSelector>>,
}

impl NodeAffinity {
    /// Node affinity is a group of node affinity scheduling rules.
    pub fn new() -> NodeAffinity {
        NodeAffinity {
            preferred_during_scheduling_ignored_during_execution: None,
            required_during_scheduling_ignored_during_execution: None,
        }
    }
}


