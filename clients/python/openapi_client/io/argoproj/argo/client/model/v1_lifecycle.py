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


class V1Lifecycle(object):
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
        'post_start': 'V1Handler',
        'pre_stop': 'V1Handler'
    }

    attribute_map = {
        'post_start': 'postStart',
        'pre_stop': 'preStop'
    }

    def __init__(self, post_start=None, pre_stop=None, local_vars_configuration=None):  # noqa: E501
        """V1Lifecycle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._post_start = None
        self._pre_stop = None
        self.discriminator = None

        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop

    @property
    def post_start(self):
        """Gets the post_start of this V1Lifecycle.  # noqa: E501


        :return: The post_start of this V1Lifecycle.  # noqa: E501
        :rtype: V1Handler
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this V1Lifecycle.


        :param post_start: The post_start of this V1Lifecycle.  # noqa: E501
        :type: V1Handler
        """

        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this V1Lifecycle.  # noqa: E501


        :return: The pre_stop of this V1Lifecycle.  # noqa: E501
        :rtype: V1Handler
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this V1Lifecycle.


        :param pre_stop: The pre_stop of this V1Lifecycle.  # noqa: E501
        :type: V1Handler
        """

        self._pre_stop = pre_stop

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
        if not isinstance(other, V1Lifecycle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Lifecycle):
            return True

        return self.to_dict() != other.to_dict()
