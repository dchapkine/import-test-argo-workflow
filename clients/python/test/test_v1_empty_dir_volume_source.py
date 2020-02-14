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
from openapi_client.io.argoproj.argo.client.model.v1_empty_dir_volume_source import V1EmptyDirVolumeSource  # noqa: E501
from openapi_client.rest import ApiException

class TestV1EmptyDirVolumeSource(unittest.TestCase):
    """V1EmptyDirVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EmptyDirVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_empty_dir_volume_source.V1EmptyDirVolumeSource()  # noqa: E501
        if include_optional :
            return V1EmptyDirVolumeSource(
                medium = '0', 
                size_limit = openapi_client.models.resource_quantity.resourceQuantity(
                    string = '0', )
            )
        else :
            return V1EmptyDirVolumeSource(
        )

    def testV1EmptyDirVolumeSource(self):
        """Test V1EmptyDirVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
