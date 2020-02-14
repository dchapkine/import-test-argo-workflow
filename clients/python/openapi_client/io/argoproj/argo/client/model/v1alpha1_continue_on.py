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


class V1alpha1ContinueOn(object):
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
        'error': 'bool',
        'failed': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'failed': 'failed'
    }

    def __init__(self, error=None, failed=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ContinueOn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._failed = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if failed is not None:
            self.failed = failed

    @property
    def error(self):
        """Gets the error of this V1alpha1ContinueOn.  # noqa: E501


        :return: The error of this V1alpha1ContinueOn.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1alpha1ContinueOn.


        :param error: The error of this V1alpha1ContinueOn.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def failed(self):
        """Gets the failed of this V1alpha1ContinueOn.  # noqa: E501


        :return: The failed of this V1alpha1ContinueOn.  # noqa: E501
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this V1alpha1ContinueOn.


        :param failed: The failed of this V1alpha1ContinueOn.  # noqa: E501
        :type: bool
        """

        self._failed = failed

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
        if not isinstance(other, V1alpha1ContinueOn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ContinueOn):
            return True

        return self.to_dict() != other.to_dict()
