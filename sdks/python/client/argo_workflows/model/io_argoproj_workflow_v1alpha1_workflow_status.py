"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.model_utils import (  # noqa: F401
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
    OpenApiModel
)
from argo_workflows.exceptions import ApiAttributeError


def lazy_import():
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_art_gc_status import IoArgoprojWorkflowV1alpha1ArtGCStatus
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_artifact_repository_ref_status import IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_condition import IoArgoprojWorkflowV1alpha1Condition
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_node_status import IoArgoprojWorkflowV1alpha1NodeStatus
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_outputs import IoArgoprojWorkflowV1alpha1Outputs
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_synchronization_status import IoArgoprojWorkflowV1alpha1SynchronizationStatus
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_template import IoArgoprojWorkflowV1alpha1Template
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_spec import IoArgoprojWorkflowV1alpha1WorkflowSpec
    from argo_workflows.model.volume import Volume
    globals()['IoArgoprojWorkflowV1alpha1ArtGCStatus'] = IoArgoprojWorkflowV1alpha1ArtGCStatus
    globals()['IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus'] = IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus
    globals()['IoArgoprojWorkflowV1alpha1Condition'] = IoArgoprojWorkflowV1alpha1Condition
    globals()['IoArgoprojWorkflowV1alpha1NodeStatus'] = IoArgoprojWorkflowV1alpha1NodeStatus
    globals()['IoArgoprojWorkflowV1alpha1Outputs'] = IoArgoprojWorkflowV1alpha1Outputs
    globals()['IoArgoprojWorkflowV1alpha1SynchronizationStatus'] = IoArgoprojWorkflowV1alpha1SynchronizationStatus
    globals()['IoArgoprojWorkflowV1alpha1Template'] = IoArgoprojWorkflowV1alpha1Template
    globals()['IoArgoprojWorkflowV1alpha1WorkflowSpec'] = IoArgoprojWorkflowV1alpha1WorkflowSpec
    globals()['Volume'] = Volume


class IoArgoprojWorkflowV1alpha1WorkflowStatus(ModelNormal):
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
            'artifact_gc_status': (IoArgoprojWorkflowV1alpha1ArtGCStatus,),  # noqa: E501
            'artifact_repository_ref': (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus,),  # noqa: E501
            'compressed_nodes': (str,),  # noqa: E501
            'conditions': ([IoArgoprojWorkflowV1alpha1Condition],),  # noqa: E501
            'estimated_duration': (int,),  # noqa: E501
            'finished_at': (datetime,),  # noqa: E501
            'message': (str,),  # noqa: E501
            'nodes': ({str: (IoArgoprojWorkflowV1alpha1NodeStatus,)},),  # noqa: E501
            'offload_node_status_version': (str,),  # noqa: E501
            'outputs': (IoArgoprojWorkflowV1alpha1Outputs,),  # noqa: E501
            'persistent_volume_claims': ([Volume],),  # noqa: E501
            'phase': (str,),  # noqa: E501
            'progress': (str,),  # noqa: E501
            'resources_duration': ({str: (int,)},),  # noqa: E501
            'started_at': (datetime,),  # noqa: E501
            'stored_templates': ({str: (IoArgoprojWorkflowV1alpha1Template,)},),  # noqa: E501
            'stored_workflow_template_spec': (IoArgoprojWorkflowV1alpha1WorkflowSpec,),  # noqa: E501
            'synchronization': (IoArgoprojWorkflowV1alpha1SynchronizationStatus,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'artifact_gc_status': 'artifactGCStatus',  # noqa: E501
        'artifact_repository_ref': 'artifactRepositoryRef',  # noqa: E501
        'compressed_nodes': 'compressedNodes',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'estimated_duration': 'estimatedDuration',  # noqa: E501
        'finished_at': 'finishedAt',  # noqa: E501
        'message': 'message',  # noqa: E501
        'nodes': 'nodes',  # noqa: E501
        'offload_node_status_version': 'offloadNodeStatusVersion',  # noqa: E501
        'outputs': 'outputs',  # noqa: E501
        'persistent_volume_claims': 'persistentVolumeClaims',  # noqa: E501
        'phase': 'phase',  # noqa: E501
        'progress': 'progress',  # noqa: E501
        'resources_duration': 'resourcesDuration',  # noqa: E501
        'started_at': 'startedAt',  # noqa: E501
        'stored_templates': 'storedTemplates',  # noqa: E501
        'stored_workflow_template_spec': 'storedWorkflowTemplateSpec',  # noqa: E501
        'synchronization': 'synchronization',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowStatus - a model defined in OpenAPI

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
            artifact_gc_status (IoArgoprojWorkflowV1alpha1ArtGCStatus): [optional]  # noqa: E501
            artifact_repository_ref (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus): [optional]  # noqa: E501
            compressed_nodes (str): Compressed and base64 decoded Nodes map. [optional]  # noqa: E501
            conditions ([IoArgoprojWorkflowV1alpha1Condition]): Conditions is a list of conditions the Workflow may have. [optional]  # noqa: E501
            estimated_duration (int): EstimatedDuration in seconds.. [optional]  # noqa: E501
            finished_at (datetime): Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.. [optional]  # noqa: E501
            message (str): A human readable message indicating details about why the workflow is in this condition.. [optional]  # noqa: E501
            nodes ({str: (IoArgoprojWorkflowV1alpha1NodeStatus,)}): Nodes is a mapping between a node ID and the node's status.. [optional]  # noqa: E501
            offload_node_status_version (str): Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.. [optional]  # noqa: E501
            outputs (IoArgoprojWorkflowV1alpha1Outputs): [optional]  # noqa: E501
            persistent_volume_claims ([Volume]): PersistentVolumeClaims tracks all PVCs that were created as part of the io.argoproj.workflow.v1alpha1. The contents of this list are drained at the end of the workflow.. [optional]  # noqa: E501
            phase (str): Phase a simple, high-level summary of where the workflow is in its lifecycle.. [optional]  # noqa: E501
            progress (str): Progress to completion. [optional]  # noqa: E501
            resources_duration ({str: (int,)}): ResourcesDuration is the total for the workflow. [optional]  # noqa: E501
            started_at (datetime): Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.. [optional]  # noqa: E501
            stored_templates ({str: (IoArgoprojWorkflowV1alpha1Template,)}): StoredTemplates is a mapping between a template ref and the node's status.. [optional]  # noqa: E501
            stored_workflow_template_spec (IoArgoprojWorkflowV1alpha1WorkflowSpec): [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1SynchronizationStatus): [optional]  # noqa: E501
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
        """IoArgoprojWorkflowV1alpha1WorkflowStatus - a model defined in OpenAPI

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
            artifact_gc_status (IoArgoprojWorkflowV1alpha1ArtGCStatus): [optional]  # noqa: E501
            artifact_repository_ref (IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus): [optional]  # noqa: E501
            compressed_nodes (str): Compressed and base64 decoded Nodes map. [optional]  # noqa: E501
            conditions ([IoArgoprojWorkflowV1alpha1Condition]): Conditions is a list of conditions the Workflow may have. [optional]  # noqa: E501
            estimated_duration (int): EstimatedDuration in seconds.. [optional]  # noqa: E501
            finished_at (datetime): Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.. [optional]  # noqa: E501
            message (str): A human readable message indicating details about why the workflow is in this condition.. [optional]  # noqa: E501
            nodes ({str: (IoArgoprojWorkflowV1alpha1NodeStatus,)}): Nodes is a mapping between a node ID and the node's status.. [optional]  # noqa: E501
            offload_node_status_version (str): Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.. [optional]  # noqa: E501
            outputs (IoArgoprojWorkflowV1alpha1Outputs): [optional]  # noqa: E501
            persistent_volume_claims ([Volume]): PersistentVolumeClaims tracks all PVCs that were created as part of the io.argoproj.workflow.v1alpha1. The contents of this list are drained at the end of the workflow.. [optional]  # noqa: E501
            phase (str): Phase a simple, high-level summary of where the workflow is in its lifecycle.. [optional]  # noqa: E501
            progress (str): Progress to completion. [optional]  # noqa: E501
            resources_duration ({str: (int,)}): ResourcesDuration is the total for the workflow. [optional]  # noqa: E501
            started_at (datetime): Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.. [optional]  # noqa: E501
            stored_templates ({str: (IoArgoprojWorkflowV1alpha1Template,)}): StoredTemplates is a mapping between a template ref and the node's status.. [optional]  # noqa: E501
            stored_workflow_template_spec (IoArgoprojWorkflowV1alpha1WorkflowSpec): [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1SynchronizationStatus): [optional]  # noqa: E501
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
