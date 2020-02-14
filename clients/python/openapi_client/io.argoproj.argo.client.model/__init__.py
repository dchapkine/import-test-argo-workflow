# coding: utf-8

# flake8: noqa
"""
    Argo Server API

    The Argo Server based API for Argo  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.io.argoproj.argo.client.model.apismetav1_preconditions import Apismetav1Preconditions
from openapi_client.io.argoproj.argo.client.model.cronworkflow_create_cron_workflow_request import CronworkflowCreateCronWorkflowRequest
from openapi_client.io.argoproj.argo.client.model.cronworkflow_update_cron_workflow_request import CronworkflowUpdateCronWorkflowRequest
from openapi_client.io.argoproj.argo.client.model.info_info_response import InfoInfoResponse
from openapi_client.io.argoproj.argo.client.model.intstr_int_or_string import IntstrIntOrString
from openapi_client.io.argoproj.argo.client.model.protobuf_any import ProtobufAny
from openapi_client.io.argoproj.argo.client.model.resource_quantity import ResourceQuantity
from openapi_client.io.argoproj.argo.client.model.runtime_stream_error import RuntimeStreamError
from openapi_client.io.argoproj.argo.client.model.v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_affinity import V1Affinity
from openapi_client.io.argoproj.argo.client.model.v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_azure_file_volume_source import V1AzureFileVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_csi_volume_source import V1CSIVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_capabilities import V1Capabilities
from openapi_client.io.argoproj.argo.client.model.v1_ceph_fs_volume_source import V1CephFSVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_cinder_volume_source import V1CinderVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_config_map_env_source import V1ConfigMapEnvSource
from openapi_client.io.argoproj.argo.client.model.v1_config_map_key_selector import V1ConfigMapKeySelector
from openapi_client.io.argoproj.argo.client.model.v1_config_map_projection import V1ConfigMapProjection
from openapi_client.io.argoproj.argo.client.model.v1_config_map_volume_source import V1ConfigMapVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_container import V1Container
from openapi_client.io.argoproj.argo.client.model.v1_container_port import V1ContainerPort
from openapi_client.io.argoproj.argo.client.model.v1_create_options import V1CreateOptions
from openapi_client.io.argoproj.argo.client.model.v1_delete_options import V1DeleteOptions
from openapi_client.io.argoproj.argo.client.model.v1_downward_api_projection import V1DownwardAPIProjection
from openapi_client.io.argoproj.argo.client.model.v1_downward_api_volume_file import V1DownwardAPIVolumeFile
from openapi_client.io.argoproj.argo.client.model.v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_empty_dir_volume_source import V1EmptyDirVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_env_from_source import V1EnvFromSource
from openapi_client.io.argoproj.argo.client.model.v1_env_var import V1EnvVar
from openapi_client.io.argoproj.argo.client.model.v1_env_var_source import V1EnvVarSource
from openapi_client.io.argoproj.argo.client.model.v1_exec_action import V1ExecAction
from openapi_client.io.argoproj.argo.client.model.v1_fc_volume_source import V1FCVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_fields_v1 import V1FieldsV1
from openapi_client.io.argoproj.argo.client.model.v1_flex_volume_source import V1FlexVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_flocker_volume_source import V1FlockerVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_get_options import V1GetOptions
from openapi_client.io.argoproj.argo.client.model.v1_git_repo_volume_source import V1GitRepoVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_glusterfs_volume_source import V1GlusterfsVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_http_get_action import V1HTTPGetAction
from openapi_client.io.argoproj.argo.client.model.v1_http_header import V1HTTPHeader
from openapi_client.io.argoproj.argo.client.model.v1_handler import V1Handler
from openapi_client.io.argoproj.argo.client.model.v1_host_alias import V1HostAlias
from openapi_client.io.argoproj.argo.client.model.v1_host_path_volume_source import V1HostPathVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_iscsi_volume_source import V1ISCSIVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_key_to_path import V1KeyToPath
from openapi_client.io.argoproj.argo.client.model.v1_label_selector import V1LabelSelector
from openapi_client.io.argoproj.argo.client.model.v1_label_selector_requirement import V1LabelSelectorRequirement
from openapi_client.io.argoproj.argo.client.model.v1_lifecycle import V1Lifecycle
from openapi_client.io.argoproj.argo.client.model.v1_list_meta import V1ListMeta
from openapi_client.io.argoproj.argo.client.model.v1_list_options import V1ListOptions
from openapi_client.io.argoproj.argo.client.model.v1_local_object_reference import V1LocalObjectReference
from openapi_client.io.argoproj.argo.client.model.v1_managed_fields_entry import V1ManagedFieldsEntry
from openapi_client.io.argoproj.argo.client.model.v1_nfs_volume_source import V1NFSVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_node_affinity import V1NodeAffinity
from openapi_client.io.argoproj.argo.client.model.v1_node_selector import V1NodeSelector
from openapi_client.io.argoproj.argo.client.model.v1_node_selector_requirement import V1NodeSelectorRequirement
from openapi_client.io.argoproj.argo.client.model.v1_node_selector_term import V1NodeSelectorTerm
from openapi_client.io.argoproj.argo.client.model.v1_object_field_selector import V1ObjectFieldSelector
from openapi_client.io.argoproj.argo.client.model.v1_object_meta import V1ObjectMeta
from openapi_client.io.argoproj.argo.client.model.v1_object_reference import V1ObjectReference
from openapi_client.io.argoproj.argo.client.model.v1_owner_reference import V1OwnerReference
from openapi_client.io.argoproj.argo.client.model.v1_persistent_volume_claim import V1PersistentVolumeClaim
from openapi_client.io.argoproj.argo.client.model.v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition
from openapi_client.io.argoproj.argo.client.model.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from openapi_client.io.argoproj.argo.client.model.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus
from openapi_client.io.argoproj.argo.client.model.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_pod_affinity import V1PodAffinity
from openapi_client.io.argoproj.argo.client.model.v1_pod_affinity_term import V1PodAffinityTerm
from openapi_client.io.argoproj.argo.client.model.v1_pod_anti_affinity import V1PodAntiAffinity
from openapi_client.io.argoproj.argo.client.model.v1_pod_dns_config import V1PodDNSConfig
from openapi_client.io.argoproj.argo.client.model.v1_pod_dns_config_option import V1PodDNSConfigOption
from openapi_client.io.argoproj.argo.client.model.v1_pod_log_options import V1PodLogOptions
from openapi_client.io.argoproj.argo.client.model.v1_pod_security_context import V1PodSecurityContext
from openapi_client.io.argoproj.argo.client.model.v1_portworx_volume_source import V1PortworxVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from openapi_client.io.argoproj.argo.client.model.v1_probe import V1Probe
from openapi_client.io.argoproj.argo.client.model.v1_projected_volume_source import V1ProjectedVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_quobyte_volume_source import V1QuobyteVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_rbd_volume_source import V1RBDVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_resource_field_selector import V1ResourceFieldSelector
from openapi_client.io.argoproj.argo.client.model.v1_resource_requirements import V1ResourceRequirements
from openapi_client.io.argoproj.argo.client.model.v1_se_linux_options import V1SELinuxOptions
from openapi_client.io.argoproj.argo.client.model.v1_scale_io_volume_source import V1ScaleIOVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_secret_env_source import V1SecretEnvSource
from openapi_client.io.argoproj.argo.client.model.v1_secret_key_selector import V1SecretKeySelector
from openapi_client.io.argoproj.argo.client.model.v1_secret_projection import V1SecretProjection
from openapi_client.io.argoproj.argo.client.model.v1_secret_volume_source import V1SecretVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_security_context import V1SecurityContext
from openapi_client.io.argoproj.argo.client.model.v1_service_account_token_projection import V1ServiceAccountTokenProjection
from openapi_client.io.argoproj.argo.client.model.v1_storage_os_volume_source import V1StorageOSVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_sysctl import V1Sysctl
from openapi_client.io.argoproj.argo.client.model.v1_tcp_socket_action import V1TCPSocketAction
from openapi_client.io.argoproj.argo.client.model.v1_time import V1Time
from openapi_client.io.argoproj.argo.client.model.v1_toleration import V1Toleration
from openapi_client.io.argoproj.argo.client.model.v1_typed_local_object_reference import V1TypedLocalObjectReference
from openapi_client.io.argoproj.argo.client.model.v1_volume import V1Volume
from openapi_client.io.argoproj.argo.client.model.v1_volume_device import V1VolumeDevice
from openapi_client.io.argoproj.argo.client.model.v1_volume_mount import V1VolumeMount
from openapi_client.io.argoproj.argo.client.model.v1_volume_projection import V1VolumeProjection
from openapi_client.io.argoproj.argo.client.model.v1_volume_source import V1VolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource
from openapi_client.io.argoproj.argo.client.model.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
from openapi_client.io.argoproj.argo.client.model.v1_windows_security_context_options import V1WindowsSecurityContextOptions
from openapi_client.io.argoproj.argo.client.model.v1alpha1_archive_strategy import V1alpha1ArchiveStrategy
from openapi_client.io.argoproj.argo.client.model.v1alpha1_arguments import V1alpha1Arguments
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifact import V1alpha1Artifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifact_location import V1alpha1ArtifactLocation
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifact_repository_ref import V1alpha1ArtifactRepositoryRef
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifactory_artifact import V1alpha1ArtifactoryArtifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifactory_auth import V1alpha1ArtifactoryAuth
from openapi_client.io.argoproj.argo.client.model.v1alpha1_backoff import V1alpha1Backoff
from openapi_client.io.argoproj.argo.client.model.v1alpha1_continue_on import V1alpha1ContinueOn
from openapi_client.io.argoproj.argo.client.model.v1alpha1_cron_workflow import V1alpha1CronWorkflow
from openapi_client.io.argoproj.argo.client.model.v1alpha1_cron_workflow_list import V1alpha1CronWorkflowList
from openapi_client.io.argoproj.argo.client.model.v1alpha1_cron_workflow_spec import V1alpha1CronWorkflowSpec
from openapi_client.io.argoproj.argo.client.model.v1alpha1_cron_workflow_status import V1alpha1CronWorkflowStatus
from openapi_client.io.argoproj.argo.client.model.v1alpha1_dag_task import V1alpha1DAGTask
from openapi_client.io.argoproj.argo.client.model.v1alpha1_dag_template import V1alpha1DAGTemplate
from openapi_client.io.argoproj.argo.client.model.v1alpha1_executor_config import V1alpha1ExecutorConfig
from openapi_client.io.argoproj.argo.client.model.v1alpha1_git_artifact import V1alpha1GitArtifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_hdfs_artifact import V1alpha1HDFSArtifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_hdfs_config import V1alpha1HDFSConfig
from openapi_client.io.argoproj.argo.client.model.v1alpha1_hdfs_krb_config import V1alpha1HDFSKrbConfig
from openapi_client.io.argoproj.argo.client.model.v1alpha1_http_artifact import V1alpha1HTTPArtifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_inputs import V1alpha1Inputs
from openapi_client.io.argoproj.argo.client.model.v1alpha1_item import V1alpha1Item
from openapi_client.io.argoproj.argo.client.model.v1alpha1_item_value import V1alpha1ItemValue
from openapi_client.io.argoproj.argo.client.model.v1alpha1_metadata import V1alpha1Metadata
from openapi_client.io.argoproj.argo.client.model.v1alpha1_outputs import V1alpha1Outputs
from openapi_client.io.argoproj.argo.client.model.v1alpha1_parallel_steps import V1alpha1ParallelSteps
from openapi_client.io.argoproj.argo.client.model.v1alpha1_parameter import V1alpha1Parameter
from openapi_client.io.argoproj.argo.client.model.v1alpha1_pod_gc import V1alpha1PodGC
from openapi_client.io.argoproj.argo.client.model.v1alpha1_raw_artifact import V1alpha1RawArtifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_resource_template import V1alpha1ResourceTemplate
from openapi_client.io.argoproj.argo.client.model.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from openapi_client.io.argoproj.argo.client.model.v1alpha1_s3_artifact import V1alpha1S3Artifact
from openapi_client.io.argoproj.argo.client.model.v1alpha1_s3_bucket import V1alpha1S3Bucket
from openapi_client.io.argoproj.argo.client.model.v1alpha1_script_template import V1alpha1ScriptTemplate
from openapi_client.io.argoproj.argo.client.model.v1alpha1_sequence import V1alpha1Sequence
from openapi_client.io.argoproj.argo.client.model.v1alpha1_suspend_template import V1alpha1SuspendTemplate
from openapi_client.io.argoproj.argo.client.model.v1alpha1_ttl_strategy import V1alpha1TTLStrategy
from openapi_client.io.argoproj.argo.client.model.v1alpha1_template import V1alpha1Template
from openapi_client.io.argoproj.argo.client.model.v1alpha1_template_ref import V1alpha1TemplateRef
from openapi_client.io.argoproj.argo.client.model.v1alpha1_user_container import V1alpha1UserContainer
from openapi_client.io.argoproj.argo.client.model.v1alpha1_value_from import V1alpha1ValueFrom
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow import V1alpha1Workflow
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_list import V1alpha1WorkflowList
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_status import V1alpha1WorkflowStatus
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_step import V1alpha1WorkflowStep
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_template import V1alpha1WorkflowTemplate
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_template_list import V1alpha1WorkflowTemplateList
from openapi_client.io.argoproj.argo.client.model.v1alpha1_workflow_template_spec import V1alpha1WorkflowTemplateSpec
from openapi_client.io.argoproj.argo.client.model.workflow_log_entry import WorkflowLogEntry
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_create_request import WorkflowWorkflowCreateRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_lint_request import WorkflowWorkflowLintRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_resubmit_request import WorkflowWorkflowResubmitRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_resume_request import WorkflowWorkflowResumeRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_retry_request import WorkflowWorkflowRetryRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_suspend_request import WorkflowWorkflowSuspendRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_terminate_request import WorkflowWorkflowTerminateRequest
from openapi_client.io.argoproj.argo.client.model.workflow_workflow_watch_event import WorkflowWorkflowWatchEvent
from openapi_client.io.argoproj.argo.client.model.workflowtemplate_workflow_template_create_request import WorkflowtemplateWorkflowTemplateCreateRequest
from openapi_client.io.argoproj.argo.client.model.workflowtemplate_workflow_template_lint_request import WorkflowtemplateWorkflowTemplateLintRequest
from openapi_client.io.argoproj.argo.client.model.workflowtemplate_workflow_template_update_request import WorkflowtemplateWorkflowTemplateUpdateRequest
from openapi_client.io.argoproj.argo.client.model.workflowv1alpha1_node_status import Workflowv1alpha1NodeStatus
