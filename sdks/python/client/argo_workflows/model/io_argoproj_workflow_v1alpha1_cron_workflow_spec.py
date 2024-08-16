"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/latest/  # noqa: E501

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
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_stop_strategy import IoArgoprojWorkflowV1alpha1StopStrategy
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_spec import IoArgoprojWorkflowV1alpha1WorkflowSpec
    from argo_workflows.model.object_meta import ObjectMeta
    globals()['IoArgoprojWorkflowV1alpha1StopStrategy'] = IoArgoprojWorkflowV1alpha1StopStrategy
    globals()['IoArgoprojWorkflowV1alpha1WorkflowSpec'] = IoArgoprojWorkflowV1alpha1WorkflowSpec
    globals()['ObjectMeta'] = ObjectMeta


class IoArgoprojWorkflowV1alpha1CronWorkflowSpec(ModelNormal):
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
            'schedule': (str,),  # noqa: E501
            'workflow_spec': (IoArgoprojWorkflowV1alpha1WorkflowSpec,),  # noqa: E501
            'concurrency_policy': (str,),  # noqa: E501
            'failed_jobs_history_limit': (int,),  # noqa: E501
            'schedules': ([str],),  # noqa: E501
            'starting_deadline_seconds': (int,),  # noqa: E501
            'stop_strategy': (IoArgoprojWorkflowV1alpha1StopStrategy,),  # noqa: E501
            'successful_jobs_history_limit': (int,),  # noqa: E501
            'suspend': (bool,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'when': (str,),  # noqa: E501
            'workflow_metadata': (ObjectMeta,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'schedule': 'schedule',  # noqa: E501
        'workflow_spec': 'workflowSpec',  # noqa: E501
        'concurrency_policy': 'concurrencyPolicy',  # noqa: E501
        'failed_jobs_history_limit': 'failedJobsHistoryLimit',  # noqa: E501
        'schedules': 'schedules',  # noqa: E501
        'starting_deadline_seconds': 'startingDeadlineSeconds',  # noqa: E501
        'stop_strategy': 'stopStrategy',  # noqa: E501
        'successful_jobs_history_limit': 'successfulJobsHistoryLimit',  # noqa: E501
        'suspend': 'suspend',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'when': 'when',  # noqa: E501
        'workflow_metadata': 'workflowMetadata',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, schedule, workflow_spec, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1CronWorkflowSpec - a model defined in OpenAPI

        Args:
            schedule (str): Schedule is a schedule to run the Workflow in Cron format
            workflow_spec (IoArgoprojWorkflowV1alpha1WorkflowSpec):

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
            concurrency_policy (str): ConcurrencyPolicy is the K8s-style concurrency policy that will be used. [optional]  # noqa: E501
            failed_jobs_history_limit (int): FailedJobsHistoryLimit is the number of failed jobs to be kept at a time. [optional]  # noqa: E501
            schedules ([str]): Schedules is a list of schedules to run the Workflow in Cron format. [optional]  # noqa: E501
            starting_deadline_seconds (int): StartingDeadlineSeconds is the K8s-style deadline that will limit the time a CronWorkflow will be run after its original scheduled time if it is missed.. [optional]  # noqa: E501
            stop_strategy (IoArgoprojWorkflowV1alpha1StopStrategy): [optional]  # noqa: E501
            successful_jobs_history_limit (int): SuccessfulJobsHistoryLimit is the number of successful jobs to be kept at a time. [optional]  # noqa: E501
            suspend (bool): Suspend is a flag that will stop new CronWorkflows from running if set to true. [optional]  # noqa: E501
            timezone (str): Timezone is the timezone against which the cron schedule will be calculated, e.g. \"Asia/Tokyo\". Default is machine's local time.. [optional]  # noqa: E501
            when (str): v3.6 and after: When clause can be used to determine a run should or shouldn't be scheduled. This new When clause allows for the full expressivity of expr-lang.. [optional]  # noqa: E501
            workflow_metadata (ObjectMeta): [optional]  # noqa: E501
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

        self.schedule = schedule
        self.workflow_spec = workflow_spec
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
    def __init__(self, schedule, workflow_spec, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1CronWorkflowSpec - a model defined in OpenAPI

        Args:
            schedule (str): Schedule is a schedule to run the Workflow in Cron format
            workflow_spec (IoArgoprojWorkflowV1alpha1WorkflowSpec):

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
            concurrency_policy (str): ConcurrencyPolicy is the K8s-style concurrency policy that will be used. [optional]  # noqa: E501
            failed_jobs_history_limit (int): FailedJobsHistoryLimit is the number of failed jobs to be kept at a time. [optional]  # noqa: E501
            schedules ([str]): Schedules is a list of schedules to run the Workflow in Cron format. [optional]  # noqa: E501
            starting_deadline_seconds (int): StartingDeadlineSeconds is the K8s-style deadline that will limit the time a CronWorkflow will be run after its original scheduled time if it is missed.. [optional]  # noqa: E501
            stop_strategy (IoArgoprojWorkflowV1alpha1StopStrategy): [optional]  # noqa: E501
            successful_jobs_history_limit (int): SuccessfulJobsHistoryLimit is the number of successful jobs to be kept at a time. [optional]  # noqa: E501
            suspend (bool): Suspend is a flag that will stop new CronWorkflows from running if set to true. [optional]  # noqa: E501
            timezone (str): Timezone is the timezone against which the cron schedule will be calculated, e.g. \"Asia/Tokyo\". Default is machine's local time.. [optional]  # noqa: E501
            when (str): v3.6 and after: When clause can be used to determine a run should or shouldn't be scheduled. This new When clause allows for the full expressivity of expr-lang.. [optional]  # noqa: E501
            workflow_metadata (ObjectMeta): [optional]  # noqa: E501
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

        self.schedule = schedule
        self.workflow_spec = workflow_spec
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
