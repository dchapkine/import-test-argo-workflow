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
)
from ..model_utils import OpenApiModel
from argo_workflows.exceptions import ApiAttributeError


def lazy_import():
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_arguments import IoArgoprojWorkflowV1alpha1Arguments
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_continue_on import IoArgoprojWorkflowV1alpha1ContinueOn
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_lifecycle_hook import IoArgoprojWorkflowV1alpha1LifecycleHook
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_sequence import IoArgoprojWorkflowV1alpha1Sequence
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_template import IoArgoprojWorkflowV1alpha1Template
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_template_ref import IoArgoprojWorkflowV1alpha1TemplateRef
    globals()['IoArgoprojWorkflowV1alpha1Arguments'] = IoArgoprojWorkflowV1alpha1Arguments
    globals()['IoArgoprojWorkflowV1alpha1ContinueOn'] = IoArgoprojWorkflowV1alpha1ContinueOn
    globals()['IoArgoprojWorkflowV1alpha1LifecycleHook'] = IoArgoprojWorkflowV1alpha1LifecycleHook
    globals()['IoArgoprojWorkflowV1alpha1Sequence'] = IoArgoprojWorkflowV1alpha1Sequence
    globals()['IoArgoprojWorkflowV1alpha1Template'] = IoArgoprojWorkflowV1alpha1Template
    globals()['IoArgoprojWorkflowV1alpha1TemplateRef'] = IoArgoprojWorkflowV1alpha1TemplateRef


class IoArgoprojWorkflowV1alpha1DAGTask(ModelNormal):
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
            'name': (str,),  # noqa: E501
            'arguments': (IoArgoprojWorkflowV1alpha1Arguments,),  # noqa: E501
            'continue_on': (IoArgoprojWorkflowV1alpha1ContinueOn,),  # noqa: E501
            'dependencies': ([str],),  # noqa: E501
            'depends': (str,),  # noqa: E501
            'hooks': ({str: (IoArgoprojWorkflowV1alpha1LifecycleHook,)},),  # noqa: E501
            'inline': (IoArgoprojWorkflowV1alpha1Template,),  # noqa: E501
            'on_exit': (str,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'template': (str,),  # noqa: E501
            'template_ref': (IoArgoprojWorkflowV1alpha1TemplateRef,),  # noqa: E501
            'when': (str,),  # noqa: E501
            'with_items': ([dict],),  # noqa: E501
            'with_param': (str,),  # noqa: E501
            'with_sequence': (IoArgoprojWorkflowV1alpha1Sequence,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'arguments': 'arguments',  # noqa: E501
        'continue_on': 'continueOn',  # noqa: E501
        'dependencies': 'dependencies',  # noqa: E501
        'depends': 'depends',  # noqa: E501
        'hooks': 'hooks',  # noqa: E501
        'inline': 'inline',  # noqa: E501
        'on_exit': 'onExit',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'template': 'template',  # noqa: E501
        'template_ref': 'templateRef',  # noqa: E501
        'when': 'when',  # noqa: E501
        'with_items': 'withItems',  # noqa: E501
        'with_param': 'withParam',  # noqa: E501
        'with_sequence': 'withSequence',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1DAGTask - a model defined in OpenAPI

        Args:
            name (str): Name is the name of the target

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
            arguments (IoArgoprojWorkflowV1alpha1Arguments): [optional]  # noqa: E501
            continue_on (IoArgoprojWorkflowV1alpha1ContinueOn): [optional]  # noqa: E501
            dependencies ([str]): Dependencies are name of other targets which this depends on. [optional]  # noqa: E501
            depends (str): Depends are name of other targets which this depends on. [optional]  # noqa: E501
            hooks ({str: (IoArgoprojWorkflowV1alpha1LifecycleHook,)}): Hooks hold the lifecycle hook which is invoked at lifecycle of task, irrespective of the success, failure, or error status of the primary task. [optional]  # noqa: E501
            inline (IoArgoprojWorkflowV1alpha1Template): [optional]  # noqa: E501
            on_exit (str): OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. DEPRECATED: Use Hooks[exit].Template instead.. [optional]  # noqa: E501
            priority (int): Priority controls which task is scheduled first. Higher values will be processed first.. [optional]  # noqa: E501
            template (str): Name of template to execute. [optional]  # noqa: E501
            template_ref (IoArgoprojWorkflowV1alpha1TemplateRef): [optional]  # noqa: E501
            when (str): When is an expression in which the task should conditionally execute. [optional]  # noqa: E501
            with_items ([dict]): WithItems expands a task into multiple parallel tasks from the items in the list. [optional]  # noqa: E501
            with_param (str): WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list.. [optional]  # noqa: E501
            with_sequence (IoArgoprojWorkflowV1alpha1Sequence): [optional]  # noqa: E501
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

        self.name = name
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
    def __init__(self, name, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1DAGTask - a model defined in OpenAPI

        Args:
            name (str): Name is the name of the target

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
            arguments (IoArgoprojWorkflowV1alpha1Arguments): [optional]  # noqa: E501
            continue_on (IoArgoprojWorkflowV1alpha1ContinueOn): [optional]  # noqa: E501
            dependencies ([str]): Dependencies are name of other targets which this depends on. [optional]  # noqa: E501
            depends (str): Depends are name of other targets which this depends on. [optional]  # noqa: E501
            hooks ({str: (IoArgoprojWorkflowV1alpha1LifecycleHook,)}): Hooks hold the lifecycle hook which is invoked at lifecycle of task, irrespective of the success, failure, or error status of the primary task. [optional]  # noqa: E501
            inline (IoArgoprojWorkflowV1alpha1Template): [optional]  # noqa: E501
            on_exit (str): OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. DEPRECATED: Use Hooks[exit].Template instead.. [optional]  # noqa: E501
            priority (int): Priority controls which task is scheduled first. Higher values will be processed first.. [optional]  # noqa: E501
            template (str): Name of template to execute. [optional]  # noqa: E501
            template_ref (IoArgoprojWorkflowV1alpha1TemplateRef): [optional]  # noqa: E501
            when (str): When is an expression in which the task should conditionally execute. [optional]  # noqa: E501
            with_items ([dict]): WithItems expands a task into multiple parallel tasks from the items in the list. [optional]  # noqa: E501
            with_param (str): WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list.. [optional]  # noqa: E501
            with_sequence (IoArgoprojWorkflowV1alpha1Sequence): [optional]  # noqa: E501
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

        self.name = name
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
