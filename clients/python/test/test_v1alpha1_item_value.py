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
from openapi_client.io.argoproj.argo.client.model.v1alpha1_item_value import V1alpha1ItemValue  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1ItemValue(unittest.TestCase):
    """V1alpha1ItemValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ItemValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_item_value.V1alpha1ItemValue()  # noqa: E501
        if include_optional :
            return V1alpha1ItemValue(
                bool_val = True, 
                list_val = [
                    'YQ=='
                    ], 
                map_val = {
                    'key' : '0'
                    }, 
                num_val = '0', 
                str_val = '0', 
                type = '0'
            )
        else :
            return V1alpha1ItemValue(
        )

    def testV1alpha1ItemValue(self):
        """Test V1alpha1ItemValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
