# coding: utf-8

"""
    Argo Server API

    The Argo Server based API for Argo  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1ConfigMapEnvSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'local_object_reference': 'V1LocalObjectReference',
        'optional': 'bool'
    }

    attribute_map = {
        'local_object_reference': 'localObjectReference',
        'optional': 'optional'
    }

    def __init__(self, local_object_reference=None, optional=None, local_vars_configuration=None):  # noqa: E501
        """V1ConfigMapEnvSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._local_object_reference = None
        self._optional = None
        self.discriminator = None

        if local_object_reference is not None:
            self.local_object_reference = local_object_reference
        if optional is not None:
            self.optional = optional

    @property
    def local_object_reference(self):
        """Gets the local_object_reference of this V1ConfigMapEnvSource.  # noqa: E501


        :return: The local_object_reference of this V1ConfigMapEnvSource.  # noqa: E501
        :rtype: V1LocalObjectReference
        """
        return self._local_object_reference

    @local_object_reference.setter
    def local_object_reference(self, local_object_reference):
        """Sets the local_object_reference of this V1ConfigMapEnvSource.


        :param local_object_reference: The local_object_reference of this V1ConfigMapEnvSource.  # noqa: E501
        :type: V1LocalObjectReference
        """

        self._local_object_reference = local_object_reference

    @property
    def optional(self):
        """Gets the optional of this V1ConfigMapEnvSource.  # noqa: E501


        :return: The optional of this V1ConfigMapEnvSource.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this V1ConfigMapEnvSource.


        :param optional: The optional of this V1ConfigMapEnvSource.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ConfigMapEnvSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ConfigMapEnvSource):
            return True

        return self.to_dict() != other.to_dict()
