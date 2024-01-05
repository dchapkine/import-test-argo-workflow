"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/release-3.4/  # noqa: E501

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
    from argo_workflows.model.container_port import ContainerPort
    from argo_workflows.model.env_from_source import EnvFromSource
    from argo_workflows.model.env_var import EnvVar
    from argo_workflows.model.lifecycle import Lifecycle
    from argo_workflows.model.probe import Probe
    from argo_workflows.model.resource_requirements import ResourceRequirements
    from argo_workflows.model.security_context import SecurityContext
    from argo_workflows.model.volume_device import VolumeDevice
    from argo_workflows.model.volume_mount import VolumeMount
    globals()['ContainerPort'] = ContainerPort
    globals()['EnvFromSource'] = EnvFromSource
    globals()['EnvVar'] = EnvVar
    globals()['Lifecycle'] = Lifecycle
    globals()['Probe'] = Probe
    globals()['ResourceRequirements'] = ResourceRequirements
    globals()['SecurityContext'] = SecurityContext
    globals()['VolumeDevice'] = VolumeDevice
    globals()['VolumeMount'] = VolumeMount


class IoArgoprojWorkflowV1alpha1ScriptTemplate(ModelNormal):
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
            'image': (str,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'args': ([str],),  # noqa: E501
            'command': ([str],),  # noqa: E501
            'env': ([EnvVar],),  # noqa: E501
            'env_from': ([EnvFromSource],),  # noqa: E501
            'image_pull_policy': (str,),  # noqa: E501
            'lifecycle': (Lifecycle,),  # noqa: E501
            'liveness_probe': (Probe,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'ports': ([ContainerPort],),  # noqa: E501
            'readiness_probe': (Probe,),  # noqa: E501
            'resources': (ResourceRequirements,),  # noqa: E501
            'security_context': (SecurityContext,),  # noqa: E501
            'startup_probe': (Probe,),  # noqa: E501
            'stdin': (bool,),  # noqa: E501
            'stdin_once': (bool,),  # noqa: E501
            'termination_message_path': (str,),  # noqa: E501
            'termination_message_policy': (str,),  # noqa: E501
            'tty': (bool,),  # noqa: E501
            'volume_devices': ([VolumeDevice],),  # noqa: E501
            'volume_mounts': ([VolumeMount],),  # noqa: E501
            'working_dir': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'image': 'image',  # noqa: E501
        'source': 'source',  # noqa: E501
        'args': 'args',  # noqa: E501
        'command': 'command',  # noqa: E501
        'env': 'env',  # noqa: E501
        'env_from': 'envFrom',  # noqa: E501
        'image_pull_policy': 'imagePullPolicy',  # noqa: E501
        'lifecycle': 'lifecycle',  # noqa: E501
        'liveness_probe': 'livenessProbe',  # noqa: E501
        'name': 'name',  # noqa: E501
        'ports': 'ports',  # noqa: E501
        'readiness_probe': 'readinessProbe',  # noqa: E501
        'resources': 'resources',  # noqa: E501
        'security_context': 'securityContext',  # noqa: E501
        'startup_probe': 'startupProbe',  # noqa: E501
        'stdin': 'stdin',  # noqa: E501
        'stdin_once': 'stdinOnce',  # noqa: E501
        'termination_message_path': 'terminationMessagePath',  # noqa: E501
        'termination_message_policy': 'terminationMessagePolicy',  # noqa: E501
        'tty': 'tty',  # noqa: E501
        'volume_devices': 'volumeDevices',  # noqa: E501
        'volume_mounts': 'volumeMounts',  # noqa: E501
        'working_dir': 'workingDir',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, image, source, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ScriptTemplate - a model defined in OpenAPI

        Args:
            image (str): Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.
            source (str): Source contains the source code of the script to execute

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
            args ([str]): Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell. [optional]  # noqa: E501
            command ([str]): Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell. [optional]  # noqa: E501
            env ([EnvVar]): List of environment variables to set in the container. Cannot be updated.. [optional]  # noqa: E501
            env_from ([EnvFromSource]): List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.. [optional]  # noqa: E501
            image_pull_policy (str): Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images. [optional]  # noqa: E501
            lifecycle (Lifecycle): [optional]  # noqa: E501
            liveness_probe (Probe): [optional]  # noqa: E501
            name (str): Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.. [optional]  # noqa: E501
            ports ([ContainerPort]): List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.. [optional]  # noqa: E501
            readiness_probe (Probe): [optional]  # noqa: E501
            resources (ResourceRequirements): [optional]  # noqa: E501
            security_context (SecurityContext): [optional]  # noqa: E501
            startup_probe (Probe): [optional]  # noqa: E501
            stdin (bool): Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.. [optional]  # noqa: E501
            stdin_once (bool): Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false. [optional]  # noqa: E501
            termination_message_path (str): Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.. [optional]  # noqa: E501
            termination_message_policy (str): Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.. [optional]  # noqa: E501
            tty (bool): Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.. [optional]  # noqa: E501
            volume_devices ([VolumeDevice]): volumeDevices is the list of block devices to be used by the container.. [optional]  # noqa: E501
            volume_mounts ([VolumeMount]): Pod volumes to mount into the container's filesystem. Cannot be updated.. [optional]  # noqa: E501
            working_dir (str): Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.. [optional]  # noqa: E501
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

        self.image = image
        self.source = source
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
    def __init__(self, image, source, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ScriptTemplate - a model defined in OpenAPI

        Args:
            image (str): Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.
            source (str): Source contains the source code of the script to execute

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
            args ([str]): Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell. [optional]  # noqa: E501
            command ([str]): Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell. [optional]  # noqa: E501
            env ([EnvVar]): List of environment variables to set in the container. Cannot be updated.. [optional]  # noqa: E501
            env_from ([EnvFromSource]): List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.. [optional]  # noqa: E501
            image_pull_policy (str): Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images. [optional]  # noqa: E501
            lifecycle (Lifecycle): [optional]  # noqa: E501
            liveness_probe (Probe): [optional]  # noqa: E501
            name (str): Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.. [optional]  # noqa: E501
            ports ([ContainerPort]): List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.. [optional]  # noqa: E501
            readiness_probe (Probe): [optional]  # noqa: E501
            resources (ResourceRequirements): [optional]  # noqa: E501
            security_context (SecurityContext): [optional]  # noqa: E501
            startup_probe (Probe): [optional]  # noqa: E501
            stdin (bool): Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.. [optional]  # noqa: E501
            stdin_once (bool): Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false. [optional]  # noqa: E501
            termination_message_path (str): Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.. [optional]  # noqa: E501
            termination_message_policy (str): Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.. [optional]  # noqa: E501
            tty (bool): Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.. [optional]  # noqa: E501
            volume_devices ([VolumeDevice]): volumeDevices is the list of block devices to be used by the container.. [optional]  # noqa: E501
            volume_mounts ([VolumeMount]): Pod volumes to mount into the container's filesystem. Cannot be updated.. [optional]  # noqa: E501
            working_dir (str): Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.. [optional]  # noqa: E501
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

        self.image = image
        self.source = source
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
