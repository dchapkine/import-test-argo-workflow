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
from openapi_client.io.argoproj.argo.client.model.v1_delete_options import V1DeleteOptions  # noqa: E501
from openapi_client.rest import ApiException

class TestV1DeleteOptions(unittest.TestCase):
    """V1DeleteOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DeleteOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_delete_options.V1DeleteOptions()  # noqa: E501
        if include_optional :
            return V1DeleteOptions(
                dry_run = [
                    '0'
                    ], 
                grace_period_seconds = '0', 
                orphan_dependents = True, 
                preconditions = openapi_client.models.apismetav1_preconditions.apismetav1Preconditions(
                    resource_version = '0', 
                    uid = '0', ), 
                propagation_policy = '0'
            )
        else :
            return V1DeleteOptions(
        )

    def testV1DeleteOptions(self):
        """Test V1DeleteOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
