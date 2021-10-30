"""
    Argo Server API

    You can get examples of requests and responses by using the CLI with `--gloglevel=9`, e.g. `argo list --gloglevel=9`  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.affinity import Affinity
    from openapi_client.model.host_alias import HostAlias
    from openapi_client.model.io_argoproj_workflow_v1alpha1_arguments import IoArgoprojWorkflowV1alpha1Arguments
    from openapi_client.model.io_argoproj_workflow_v1alpha1_artifact_repository_ref import IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef
    from openapi_client.model.io_argoproj_workflow_v1alpha1_executor_config import IoArgoprojWorkflowV1alpha1ExecutorConfig
    from openapi_client.model.io_argoproj_workflow_v1alpha1_metadata import IoArgoprojWorkflowV1alpha1Metadata
    from openapi_client.model.io_argoproj_workflow_v1alpha1_metrics import IoArgoprojWorkflowV1alpha1Metrics
    from openapi_client.model.io_argoproj_workflow_v1alpha1_pod_gc import IoArgoprojWorkflowV1alpha1PodGC
    from openapi_client.model.io_argoproj_workflow_v1alpha1_retry_strategy import IoArgoprojWorkflowV1alpha1RetryStrategy
    from openapi_client.model.io_argoproj_workflow_v1alpha1_synchronization import IoArgoprojWorkflowV1alpha1Synchronization
    from openapi_client.model.io_argoproj_workflow_v1alpha1_template import IoArgoprojWorkflowV1alpha1Template
    from openapi_client.model.io_argoproj_workflow_v1alpha1_ttl_strategy import IoArgoprojWorkflowV1alpha1TTLStrategy
    from openapi_client.model.io_argoproj_workflow_v1alpha1_volume_claim_gc import IoArgoprojWorkflowV1alpha1VolumeClaimGC
    from openapi_client.model.io_argoproj_workflow_v1alpha1_workflow_template_ref import IoArgoprojWorkflowV1alpha1WorkflowTemplateRef
    from openapi_client.model.io_k8s_api_policy_v1beta1_pod_disruption_budget_spec import IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec
    from openapi_client.model.local_object_reference import LocalObjectReference
    from openapi_client.model.object_meta import ObjectMeta
    from openapi_client.model.persistent_volume_claim import PersistentVolumeClaim
    from openapi_client.model.pod_dns_config import PodDNSConfig
    from openapi_client.model.pod_security_context import PodSecurityContext
    from openapi_client.model.toleration import Toleration
    from openapi_client.model.volume import Volume
    globals()['Affinity'] = Affinity
    globals()['HostAlias'] = HostAlias
    globals()['IoArgoprojWorkflowV1alpha1Arguments'] = IoArgoprojWorkflowV1alpha1Arguments
    globals()['IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef'] = IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef
    globals()['IoArgoprojWorkflowV1alpha1ExecutorConfig'] = IoArgoprojWorkflowV1alpha1ExecutorConfig
    globals()['IoArgoprojWorkflowV1alpha1Metadata'] = IoArgoprojWorkflowV1alpha1Metadata
    globals()['IoArgoprojWorkflowV1alpha1Metrics'] = IoArgoprojWorkflowV1alpha1Metrics
    globals()['IoArgoprojWorkflowV1alpha1PodGC'] = IoArgoprojWorkflowV1alpha1PodGC
    globals()['IoArgoprojWorkflowV1alpha1RetryStrategy'] = IoArgoprojWorkflowV1alpha1RetryStrategy
    globals()['IoArgoprojWorkflowV1alpha1Synchronization'] = IoArgoprojWorkflowV1alpha1Synchronization
    globals()['IoArgoprojWorkflowV1alpha1TTLStrategy'] = IoArgoprojWorkflowV1alpha1TTLStrategy
    globals()['IoArgoprojWorkflowV1alpha1Template'] = IoArgoprojWorkflowV1alpha1Template
    globals()['IoArgoprojWorkflowV1alpha1VolumeClaimGC'] = IoArgoprojWorkflowV1alpha1VolumeClaimGC
    globals()['IoArgoprojWorkflowV1alpha1WorkflowTemplateRef'] = IoArgoprojWorkflowV1alpha1WorkflowTemplateRef
    globals()['IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec'] = IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec
    globals()['LocalObjectReference'] = LocalObjectReference
    globals()['ObjectMeta'] = ObjectMeta
    globals()['PersistentVolumeClaim'] = PersistentVolumeClaim
    globals()['PodDNSConfig'] = PodDNSConfig
    globals()['PodSecurityContext'] = PodSecurityContext
    globals()['Toleration'] = Toleration
    globals()['Volume'] = Volume


class IoArgoprojWorkflowV1alpha1WorkflowTemplateSpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'active_deadline_seconds': (int,),  # noqa: E501
            'affinity': (Affinity,),  # noqa: E501
            'archive_logs': (bool,),  # noqa: E501
            'arguments': (IoArgoprojWorkflowV1alpha1Arguments,),  # noqa: E501
            'artifact_repository_ref': (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef,),  # noqa: E501
            'automount_service_account_token': (bool,),  # noqa: E501
            'dns_config': (PodDNSConfig,),  # noqa: E501
            'dns_policy': (str,),  # noqa: E501
            'entrypoint': (str,),  # noqa: E501
            'executor': (IoArgoprojWorkflowV1alpha1ExecutorConfig,),  # noqa: E501
            'host_aliases': ([HostAlias],),  # noqa: E501
            'host_network': (bool,),  # noqa: E501
            'image_pull_secrets': ([LocalObjectReference],),  # noqa: E501
            'metrics': (IoArgoprojWorkflowV1alpha1Metrics,),  # noqa: E501
            'node_selector': ({str: (str,)},),  # noqa: E501
            'on_exit': (str,),  # noqa: E501
            'parallelism': (int,),  # noqa: E501
            'pod_disruption_budget': (IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec,),  # noqa: E501
            'pod_gc': (IoArgoprojWorkflowV1alpha1PodGC,),  # noqa: E501
            'pod_metadata': (IoArgoprojWorkflowV1alpha1Metadata,),  # noqa: E501
            'pod_priority': (int,),  # noqa: E501
            'pod_priority_class_name': (str,),  # noqa: E501
            'pod_spec_patch': (str,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'retry_strategy': (IoArgoprojWorkflowV1alpha1RetryStrategy,),  # noqa: E501
            'scheduler_name': (str,),  # noqa: E501
            'security_context': (PodSecurityContext,),  # noqa: E501
            'service_account_name': (str,),  # noqa: E501
            'shutdown': (str,),  # noqa: E501
            'suspend': (bool,),  # noqa: E501
            'synchronization': (IoArgoprojWorkflowV1alpha1Synchronization,),  # noqa: E501
            'template_defaults': (IoArgoprojWorkflowV1alpha1Template,),  # noqa: E501
            'templates': ([IoArgoprojWorkflowV1alpha1Template],),  # noqa: E501
            'tolerations': ([Toleration],),  # noqa: E501
            'ttl_strategy': (IoArgoprojWorkflowV1alpha1TTLStrategy,),  # noqa: E501
            'volume_claim_gc': (IoArgoprojWorkflowV1alpha1VolumeClaimGC,),  # noqa: E501
            'volume_claim_templates': ([PersistentVolumeClaim],),  # noqa: E501
            'volumes': ([Volume],),  # noqa: E501
            'workflow_metadata': (ObjectMeta,),  # noqa: E501
            'workflow_template_ref': (IoArgoprojWorkflowV1alpha1WorkflowTemplateRef,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',  # noqa: E501
        'affinity': 'affinity',  # noqa: E501
        'archive_logs': 'archiveLogs',  # noqa: E501
        'arguments': 'arguments',  # noqa: E501
        'artifact_repository_ref': 'artifactRepositoryRef',  # noqa: E501
        'automount_service_account_token': 'automountServiceAccountToken',  # noqa: E501
        'dns_config': 'dnsConfig',  # noqa: E501
        'dns_policy': 'dnsPolicy',  # noqa: E501
        'entrypoint': 'entrypoint',  # noqa: E501
        'executor': 'executor',  # noqa: E501
        'host_aliases': 'hostAliases',  # noqa: E501
        'host_network': 'hostNetwork',  # noqa: E501
        'image_pull_secrets': 'imagePullSecrets',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'node_selector': 'nodeSelector',  # noqa: E501
        'on_exit': 'onExit',  # noqa: E501
        'parallelism': 'parallelism',  # noqa: E501
        'pod_disruption_budget': 'podDisruptionBudget',  # noqa: E501
        'pod_gc': 'podGC',  # noqa: E501
        'pod_metadata': 'podMetadata',  # noqa: E501
        'pod_priority': 'podPriority',  # noqa: E501
        'pod_priority_class_name': 'podPriorityClassName',  # noqa: E501
        'pod_spec_patch': 'podSpecPatch',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'retry_strategy': 'retryStrategy',  # noqa: E501
        'scheduler_name': 'schedulerName',  # noqa: E501
        'security_context': 'securityContext',  # noqa: E501
        'service_account_name': 'serviceAccountName',  # noqa: E501
        'shutdown': 'shutdown',  # noqa: E501
        'suspend': 'suspend',  # noqa: E501
        'synchronization': 'synchronization',  # noqa: E501
        'template_defaults': 'templateDefaults',  # noqa: E501
        'templates': 'templates',  # noqa: E501
        'tolerations': 'tolerations',  # noqa: E501
        'ttl_strategy': 'ttlStrategy',  # noqa: E501
        'volume_claim_gc': 'volumeClaimGC',  # noqa: E501
        'volume_claim_templates': 'volumeClaimTemplates',  # noqa: E501
        'volumes': 'volumes',  # noqa: E501
        'workflow_metadata': 'workflowMetadata',  # noqa: E501
        'workflow_template_ref': 'workflowTemplateRef',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowTemplateSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_deadline_seconds (int): Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the io.argoproj.workflow.v1alpha1. A value of zero is used to terminate a Running workflow. [optional]  # noqa: E501
            affinity (Affinity): [optional]  # noqa: E501
            archive_logs (bool): ArchiveLogs indicates if the container logs should be archived. [optional]  # noqa: E501
            arguments (IoArgoprojWorkflowV1alpha1Arguments): [optional]  # noqa: E501
            artifact_repository_ref (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef): [optional]  # noqa: E501
            automount_service_account_token (bool): AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.. [optional]  # noqa: E501
            dns_config (PodDNSConfig): [optional]  # noqa: E501
            dns_policy (str): Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.. [optional]  # noqa: E501
            entrypoint (str): Entrypoint is a template reference to the starting point of the io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            executor (IoArgoprojWorkflowV1alpha1ExecutorConfig): [optional]  # noqa: E501
            host_aliases ([HostAlias]): [optional]  # noqa: E501
            host_network (bool): Host networking requested for this workflow pod. Default to false.. [optional]  # noqa: E501
            image_pull_secrets ([LocalObjectReference]): ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod. [optional]  # noqa: E501
            metrics (IoArgoprojWorkflowV1alpha1Metrics): [optional]  # noqa: E501
            node_selector ({str: (str,)}): NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.. [optional]  # noqa: E501
            on_exit (str): OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            parallelism (int): Parallelism limits the max total parallel pods that can execute at the same time in a workflow. [optional]  # noqa: E501
            pod_disruption_budget (IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec): [optional]  # noqa: E501
            pod_gc (IoArgoprojWorkflowV1alpha1PodGC): [optional]  # noqa: E501
            pod_metadata (IoArgoprojWorkflowV1alpha1Metadata): [optional]  # noqa: E501
            pod_priority (int): Priority to apply to workflow pods.. [optional]  # noqa: E501
            pod_priority_class_name (str): PriorityClassName to apply to workflow pods.. [optional]  # noqa: E501
            pod_spec_patch (str): PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).. [optional]  # noqa: E501
            priority (int): Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.. [optional]  # noqa: E501
            retry_strategy (IoArgoprojWorkflowV1alpha1RetryStrategy): [optional]  # noqa: E501
            scheduler_name (str): Set scheduler name for all pods. Will be overridden if container/script template's scheduler name is set. Default scheduler will be used if neither specified.. [optional]  # noqa: E501
            security_context (PodSecurityContext): [optional]  # noqa: E501
            service_account_name (str): ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.. [optional]  # noqa: E501
            shutdown (str): Shutdown will shutdown the workflow according to its ShutdownStrategy. [optional]  # noqa: E501
            suspend (bool): Suspend will suspend the workflow and prevent execution of any future steps in the workflow. [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1Synchronization): [optional]  # noqa: E501
            template_defaults (IoArgoprojWorkflowV1alpha1Template): [optional]  # noqa: E501
            templates ([IoArgoprojWorkflowV1alpha1Template]): Templates is a list of workflow templates used in a workflow. [optional]  # noqa: E501
            tolerations ([Toleration]): Tolerations to apply to workflow pods.. [optional]  # noqa: E501
            ttl_strategy (IoArgoprojWorkflowV1alpha1TTLStrategy): [optional]  # noqa: E501
            volume_claim_gc (IoArgoprojWorkflowV1alpha1VolumeClaimGC): [optional]  # noqa: E501
            volume_claim_templates ([PersistentVolumeClaim]): VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow. [optional]  # noqa: E501
            volumes ([Volume]): Volumes is a list of volumes that can be mounted by containers in a io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            workflow_metadata (ObjectMeta): [optional]  # noqa: E501
            workflow_template_ref (IoArgoprojWorkflowV1alpha1WorkflowTemplateRef): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowTemplateSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_deadline_seconds (int): Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the io.argoproj.workflow.v1alpha1. A value of zero is used to terminate a Running workflow. [optional]  # noqa: E501
            affinity (Affinity): [optional]  # noqa: E501
            archive_logs (bool): ArchiveLogs indicates if the container logs should be archived. [optional]  # noqa: E501
            arguments (IoArgoprojWorkflowV1alpha1Arguments): [optional]  # noqa: E501
            artifact_repository_ref (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef): [optional]  # noqa: E501
            automount_service_account_token (bool): AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.. [optional]  # noqa: E501
            dns_config (PodDNSConfig): [optional]  # noqa: E501
            dns_policy (str): Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.. [optional]  # noqa: E501
            entrypoint (str): Entrypoint is a template reference to the starting point of the io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            executor (IoArgoprojWorkflowV1alpha1ExecutorConfig): [optional]  # noqa: E501
            host_aliases ([HostAlias]): [optional]  # noqa: E501
            host_network (bool): Host networking requested for this workflow pod. Default to false.. [optional]  # noqa: E501
            image_pull_secrets ([LocalObjectReference]): ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod. [optional]  # noqa: E501
            metrics (IoArgoprojWorkflowV1alpha1Metrics): [optional]  # noqa: E501
            node_selector ({str: (str,)}): NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.. [optional]  # noqa: E501
            on_exit (str): OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            parallelism (int): Parallelism limits the max total parallel pods that can execute at the same time in a workflow. [optional]  # noqa: E501
            pod_disruption_budget (IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec): [optional]  # noqa: E501
            pod_gc (IoArgoprojWorkflowV1alpha1PodGC): [optional]  # noqa: E501
            pod_metadata (IoArgoprojWorkflowV1alpha1Metadata): [optional]  # noqa: E501
            pod_priority (int): Priority to apply to workflow pods.. [optional]  # noqa: E501
            pod_priority_class_name (str): PriorityClassName to apply to workflow pods.. [optional]  # noqa: E501
            pod_spec_patch (str): PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).. [optional]  # noqa: E501
            priority (int): Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.. [optional]  # noqa: E501
            retry_strategy (IoArgoprojWorkflowV1alpha1RetryStrategy): [optional]  # noqa: E501
            scheduler_name (str): Set scheduler name for all pods. Will be overridden if container/script template's scheduler name is set. Default scheduler will be used if neither specified.. [optional]  # noqa: E501
            security_context (PodSecurityContext): [optional]  # noqa: E501
            service_account_name (str): ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.. [optional]  # noqa: E501
            shutdown (str): Shutdown will shutdown the workflow according to its ShutdownStrategy. [optional]  # noqa: E501
            suspend (bool): Suspend will suspend the workflow and prevent execution of any future steps in the workflow. [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1Synchronization): [optional]  # noqa: E501
            template_defaults (IoArgoprojWorkflowV1alpha1Template): [optional]  # noqa: E501
            templates ([IoArgoprojWorkflowV1alpha1Template]): Templates is a list of workflow templates used in a workflow. [optional]  # noqa: E501
            tolerations ([Toleration]): Tolerations to apply to workflow pods.. [optional]  # noqa: E501
            ttl_strategy (IoArgoprojWorkflowV1alpha1TTLStrategy): [optional]  # noqa: E501
            volume_claim_gc (IoArgoprojWorkflowV1alpha1VolumeClaimGC): [optional]  # noqa: E501
            volume_claim_templates ([PersistentVolumeClaim]): VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow. [optional]  # noqa: E501
            volumes ([Volume]): Volumes is a list of volumes that can be mounted by containers in a io.argoproj.workflow.v1alpha1.. [optional]  # noqa: E501
            workflow_metadata (ObjectMeta): [optional]  # noqa: E501
            workflow_template_ref (IoArgoprojWorkflowV1alpha1WorkflowTemplateRef): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
