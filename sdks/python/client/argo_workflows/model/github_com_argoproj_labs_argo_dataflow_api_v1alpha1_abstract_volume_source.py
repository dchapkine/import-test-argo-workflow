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
    from argo_workflows.model.aws_elastic_block_store_volume_source import AWSElasticBlockStoreVolumeSource
    from argo_workflows.model.azure_disk_volume_source import AzureDiskVolumeSource
    from argo_workflows.model.azure_file_volume_source import AzureFileVolumeSource
    from argo_workflows.model.ceph_fs_volume_source import CephFSVolumeSource
    from argo_workflows.model.cinder_volume_source import CinderVolumeSource
    from argo_workflows.model.config_map_volume_source import ConfigMapVolumeSource
    from argo_workflows.model.csi_volume_source import CSIVolumeSource
    from argo_workflows.model.downward_api_volume_source import DownwardAPIVolumeSource
    from argo_workflows.model.empty_dir_volume_source import EmptyDirVolumeSource
    from argo_workflows.model.ephemeral_volume_source import EphemeralVolumeSource
    from argo_workflows.model.fc_volume_source import FCVolumeSource
    from argo_workflows.model.flex_volume_source import FlexVolumeSource
    from argo_workflows.model.flocker_volume_source import FlockerVolumeSource
    from argo_workflows.model.gce_persistent_disk_volume_source import GCEPersistentDiskVolumeSource
    from argo_workflows.model.git_repo_volume_source import GitRepoVolumeSource
    from argo_workflows.model.glusterfs_volume_source import GlusterfsVolumeSource
    from argo_workflows.model.host_path_volume_source import HostPathVolumeSource
    from argo_workflows.model.iscsi_volume_source import ISCSIVolumeSource
    from argo_workflows.model.nfs_volume_source import NFSVolumeSource
    from argo_workflows.model.persistent_volume_claim_volume_source import PersistentVolumeClaimVolumeSource
    from argo_workflows.model.photon_persistent_disk_volume_source import PhotonPersistentDiskVolumeSource
    from argo_workflows.model.portworx_volume_source import PortworxVolumeSource
    from argo_workflows.model.projected_volume_source import ProjectedVolumeSource
    from argo_workflows.model.quobyte_volume_source import QuobyteVolumeSource
    from argo_workflows.model.rbd_volume_source import RBDVolumeSource
    from argo_workflows.model.scale_io_volume_source import ScaleIOVolumeSource
    from argo_workflows.model.secret_volume_source import SecretVolumeSource
    from argo_workflows.model.storage_os_volume_source import StorageOSVolumeSource
    from argo_workflows.model.vsphere_virtual_disk_volume_source import VsphereVirtualDiskVolumeSource
    globals()['AWSElasticBlockStoreVolumeSource'] = AWSElasticBlockStoreVolumeSource
    globals()['AzureDiskVolumeSource'] = AzureDiskVolumeSource
    globals()['AzureFileVolumeSource'] = AzureFileVolumeSource
    globals()['CSIVolumeSource'] = CSIVolumeSource
    globals()['CephFSVolumeSource'] = CephFSVolumeSource
    globals()['CinderVolumeSource'] = CinderVolumeSource
    globals()['ConfigMapVolumeSource'] = ConfigMapVolumeSource
    globals()['DownwardAPIVolumeSource'] = DownwardAPIVolumeSource
    globals()['EmptyDirVolumeSource'] = EmptyDirVolumeSource
    globals()['EphemeralVolumeSource'] = EphemeralVolumeSource
    globals()['FCVolumeSource'] = FCVolumeSource
    globals()['FlexVolumeSource'] = FlexVolumeSource
    globals()['FlockerVolumeSource'] = FlockerVolumeSource
    globals()['GCEPersistentDiskVolumeSource'] = GCEPersistentDiskVolumeSource
    globals()['GitRepoVolumeSource'] = GitRepoVolumeSource
    globals()['GlusterfsVolumeSource'] = GlusterfsVolumeSource
    globals()['HostPathVolumeSource'] = HostPathVolumeSource
    globals()['ISCSIVolumeSource'] = ISCSIVolumeSource
    globals()['NFSVolumeSource'] = NFSVolumeSource
    globals()['PersistentVolumeClaimVolumeSource'] = PersistentVolumeClaimVolumeSource
    globals()['PhotonPersistentDiskVolumeSource'] = PhotonPersistentDiskVolumeSource
    globals()['PortworxVolumeSource'] = PortworxVolumeSource
    globals()['ProjectedVolumeSource'] = ProjectedVolumeSource
    globals()['QuobyteVolumeSource'] = QuobyteVolumeSource
    globals()['RBDVolumeSource'] = RBDVolumeSource
    globals()['ScaleIOVolumeSource'] = ScaleIOVolumeSource
    globals()['SecretVolumeSource'] = SecretVolumeSource
    globals()['StorageOSVolumeSource'] = StorageOSVolumeSource
    globals()['VsphereVirtualDiskVolumeSource'] = VsphereVirtualDiskVolumeSource


class GithubComArgoprojLabsArgoDataflowApiV1alpha1AbstractVolumeSource(ModelNormal):
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
            'aws_elastic_block_store': (AWSElasticBlockStoreVolumeSource,),  # noqa: E501
            'azure_disk': (AzureDiskVolumeSource,),  # noqa: E501
            'azure_file': (AzureFileVolumeSource,),  # noqa: E501
            'cephfs': (CephFSVolumeSource,),  # noqa: E501
            'cinder': (CinderVolumeSource,),  # noqa: E501
            'config_map': (ConfigMapVolumeSource,),  # noqa: E501
            'csi': (CSIVolumeSource,),  # noqa: E501
            'downward_api': (DownwardAPIVolumeSource,),  # noqa: E501
            'empty_dir': (EmptyDirVolumeSource,),  # noqa: E501
            'ephemeral': (EphemeralVolumeSource,),  # noqa: E501
            'fc': (FCVolumeSource,),  # noqa: E501
            'flex_volume': (FlexVolumeSource,),  # noqa: E501
            'flocker': (FlockerVolumeSource,),  # noqa: E501
            'gce_persistent_disk': (GCEPersistentDiskVolumeSource,),  # noqa: E501
            'git_repo': (GitRepoVolumeSource,),  # noqa: E501
            'glusterfs': (GlusterfsVolumeSource,),  # noqa: E501
            'host_path': (HostPathVolumeSource,),  # noqa: E501
            'iscsi': (ISCSIVolumeSource,),  # noqa: E501
            'nfs': (NFSVolumeSource,),  # noqa: E501
            'persistent_volume_claim': (PersistentVolumeClaimVolumeSource,),  # noqa: E501
            'photon_persistent_disk': (PhotonPersistentDiskVolumeSource,),  # noqa: E501
            'portworx_volume': (PortworxVolumeSource,),  # noqa: E501
            'projected': (ProjectedVolumeSource,),  # noqa: E501
            'quobyte': (QuobyteVolumeSource,),  # noqa: E501
            'rbd': (RBDVolumeSource,),  # noqa: E501
            'scale_io': (ScaleIOVolumeSource,),  # noqa: E501
            'secret': (SecretVolumeSource,),  # noqa: E501
            'storageos': (StorageOSVolumeSource,),  # noqa: E501
            'vsphere_volume': (VsphereVirtualDiskVolumeSource,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'aws_elastic_block_store': 'awsElasticBlockStore',  # noqa: E501
        'azure_disk': 'azureDisk',  # noqa: E501
        'azure_file': 'azureFile',  # noqa: E501
        'cephfs': 'cephfs',  # noqa: E501
        'cinder': 'cinder',  # noqa: E501
        'config_map': 'configMap',  # noqa: E501
        'csi': 'csi',  # noqa: E501
        'downward_api': 'downwardAPI',  # noqa: E501
        'empty_dir': 'emptyDir',  # noqa: E501
        'ephemeral': 'ephemeral',  # noqa: E501
        'fc': 'fc',  # noqa: E501
        'flex_volume': 'flexVolume',  # noqa: E501
        'flocker': 'flocker',  # noqa: E501
        'gce_persistent_disk': 'gcePersistentDisk',  # noqa: E501
        'git_repo': 'gitRepo',  # noqa: E501
        'glusterfs': 'glusterfs',  # noqa: E501
        'host_path': 'hostPath',  # noqa: E501
        'iscsi': 'iscsi',  # noqa: E501
        'nfs': 'nfs',  # noqa: E501
        'persistent_volume_claim': 'persistentVolumeClaim',  # noqa: E501
        'photon_persistent_disk': 'photonPersistentDisk',  # noqa: E501
        'portworx_volume': 'portworxVolume',  # noqa: E501
        'projected': 'projected',  # noqa: E501
        'quobyte': 'quobyte',  # noqa: E501
        'rbd': 'rbd',  # noqa: E501
        'scale_io': 'scaleIO',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'storageos': 'storageos',  # noqa: E501
        'vsphere_volume': 'vsphereVolume',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """GithubComArgoprojLabsArgoDataflowApiV1alpha1AbstractVolumeSource - a model defined in OpenAPI

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
            aws_elastic_block_store (AWSElasticBlockStoreVolumeSource): [optional]  # noqa: E501
            azure_disk (AzureDiskVolumeSource): [optional]  # noqa: E501
            azure_file (AzureFileVolumeSource): [optional]  # noqa: E501
            cephfs (CephFSVolumeSource): [optional]  # noqa: E501
            cinder (CinderVolumeSource): [optional]  # noqa: E501
            config_map (ConfigMapVolumeSource): [optional]  # noqa: E501
            csi (CSIVolumeSource): [optional]  # noqa: E501
            downward_api (DownwardAPIVolumeSource): [optional]  # noqa: E501
            empty_dir (EmptyDirVolumeSource): [optional]  # noqa: E501
            ephemeral (EphemeralVolumeSource): [optional]  # noqa: E501
            fc (FCVolumeSource): [optional]  # noqa: E501
            flex_volume (FlexVolumeSource): [optional]  # noqa: E501
            flocker (FlockerVolumeSource): [optional]  # noqa: E501
            gce_persistent_disk (GCEPersistentDiskVolumeSource): [optional]  # noqa: E501
            git_repo (GitRepoVolumeSource): [optional]  # noqa: E501
            glusterfs (GlusterfsVolumeSource): [optional]  # noqa: E501
            host_path (HostPathVolumeSource): [optional]  # noqa: E501
            iscsi (ISCSIVolumeSource): [optional]  # noqa: E501
            nfs (NFSVolumeSource): [optional]  # noqa: E501
            persistent_volume_claim (PersistentVolumeClaimVolumeSource): [optional]  # noqa: E501
            photon_persistent_disk (PhotonPersistentDiskVolumeSource): [optional]  # noqa: E501
            portworx_volume (PortworxVolumeSource): [optional]  # noqa: E501
            projected (ProjectedVolumeSource): [optional]  # noqa: E501
            quobyte (QuobyteVolumeSource): [optional]  # noqa: E501
            rbd (RBDVolumeSource): [optional]  # noqa: E501
            scale_io (ScaleIOVolumeSource): [optional]  # noqa: E501
            secret (SecretVolumeSource): [optional]  # noqa: E501
            storageos (StorageOSVolumeSource): [optional]  # noqa: E501
            vsphere_volume (VsphereVirtualDiskVolumeSource): [optional]  # noqa: E501
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
        """GithubComArgoprojLabsArgoDataflowApiV1alpha1AbstractVolumeSource - a model defined in OpenAPI

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
            aws_elastic_block_store (AWSElasticBlockStoreVolumeSource): [optional]  # noqa: E501
            azure_disk (AzureDiskVolumeSource): [optional]  # noqa: E501
            azure_file (AzureFileVolumeSource): [optional]  # noqa: E501
            cephfs (CephFSVolumeSource): [optional]  # noqa: E501
            cinder (CinderVolumeSource): [optional]  # noqa: E501
            config_map (ConfigMapVolumeSource): [optional]  # noqa: E501
            csi (CSIVolumeSource): [optional]  # noqa: E501
            downward_api (DownwardAPIVolumeSource): [optional]  # noqa: E501
            empty_dir (EmptyDirVolumeSource): [optional]  # noqa: E501
            ephemeral (EphemeralVolumeSource): [optional]  # noqa: E501
            fc (FCVolumeSource): [optional]  # noqa: E501
            flex_volume (FlexVolumeSource): [optional]  # noqa: E501
            flocker (FlockerVolumeSource): [optional]  # noqa: E501
            gce_persistent_disk (GCEPersistentDiskVolumeSource): [optional]  # noqa: E501
            git_repo (GitRepoVolumeSource): [optional]  # noqa: E501
            glusterfs (GlusterfsVolumeSource): [optional]  # noqa: E501
            host_path (HostPathVolumeSource): [optional]  # noqa: E501
            iscsi (ISCSIVolumeSource): [optional]  # noqa: E501
            nfs (NFSVolumeSource): [optional]  # noqa: E501
            persistent_volume_claim (PersistentVolumeClaimVolumeSource): [optional]  # noqa: E501
            photon_persistent_disk (PhotonPersistentDiskVolumeSource): [optional]  # noqa: E501
            portworx_volume (PortworxVolumeSource): [optional]  # noqa: E501
            projected (ProjectedVolumeSource): [optional]  # noqa: E501
            quobyte (QuobyteVolumeSource): [optional]  # noqa: E501
            rbd (RBDVolumeSource): [optional]  # noqa: E501
            scale_io (ScaleIOVolumeSource): [optional]  # noqa: E501
            secret (SecretVolumeSource): [optional]  # noqa: E501
            storageos (StorageOSVolumeSource): [optional]  # noqa: E501
            vsphere_volume (VsphereVirtualDiskVolumeSource): [optional]  # noqa: E501
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
