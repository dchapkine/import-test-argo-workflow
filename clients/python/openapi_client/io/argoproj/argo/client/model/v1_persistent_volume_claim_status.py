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


class V1PersistentVolumeClaimStatus(object):
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
        'access_modes': 'list[str]',
        'capacity': 'dict(str, ResourceQuantity)',
        'conditions': 'list[V1PersistentVolumeClaimCondition]',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, capacity=None, conditions=None, phase=None, local_vars_configuration=None):  # noqa: E501
        """V1PersistentVolumeClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_modes = None
        self._capacity = None
        self._conditions = None
        self._phase = None
        self.discriminator = None

        if access_modes is not None:
            self.access_modes = access_modes
        if capacity is not None:
            self.capacity = capacity
        if conditions is not None:
            self.conditions = conditions
        if phase is not None:
            self.phase = phase

    @property
    def access_modes(self):
        """Gets the access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501


        :return: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this V1PersistentVolumeClaimStatus.


        :param access_modes: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """Gets the capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501


        :return: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, ResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1PersistentVolumeClaimStatus.


        :param capacity: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: dict(str, ResourceQuantity)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """Gets the conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501


        :return: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[V1PersistentVolumeClaimCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1PersistentVolumeClaimStatus.


        :param conditions: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[V1PersistentVolumeClaimCondition]
        """

        self._conditions = conditions

    @property
    def phase(self):
        """Gets the phase of this V1PersistentVolumeClaimStatus.  # noqa: E501


        :return: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1PersistentVolumeClaimStatus.


        :param phase: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

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
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return True

        return self.to_dict() != other.to_dict()
