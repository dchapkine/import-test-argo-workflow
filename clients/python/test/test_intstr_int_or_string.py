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
from openapi_client.io.argoproj.argo.client.model.intstr_int_or_string import IntstrIntOrString  # noqa: E501
from openapi_client.rest import ApiException

class TestIntstrIntOrString(unittest.TestCase):
    """IntstrIntOrString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IntstrIntOrString
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.intstr_int_or_string.IntstrIntOrString()  # noqa: E501
        if include_optional :
            return IntstrIntOrString(
                int_val = 56, 
                str_val = '0', 
                type = '0'
            )
        else :
            return IntstrIntOrString(
        )

    def testIntstrIntOrString(self):
        """Test IntstrIntOrString"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
