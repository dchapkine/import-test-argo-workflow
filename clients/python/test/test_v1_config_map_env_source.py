# coding: utf-8

"""
    Argo Server API

    The Argo Server based API for Argo  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.io.argoproj.argo.client.model.v1_config_map_env_source import V1ConfigMapEnvSource  # noqa: E501
from openapi_client.rest import ApiException

class TestV1ConfigMapEnvSource(unittest.TestCase):
    """V1ConfigMapEnvSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ConfigMapEnvSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_config_map_env_source.V1ConfigMapEnvSource()  # noqa: E501
        if include_optional :
            return V1ConfigMapEnvSource(
                local_object_reference = openapi_client.models.v1_local_object_reference.v1LocalObjectReference(
                    name = '0', ), 
                optional = True
            )
        else :
            return V1ConfigMapEnvSource(
        )

    def testV1ConfigMapEnvSource(self):
        """Test V1ConfigMapEnvSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
