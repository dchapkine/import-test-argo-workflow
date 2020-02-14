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
from openapi_client.io.argoproj.argo.client.model.v1alpha1_sequence import V1alpha1Sequence  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1Sequence(unittest.TestCase):
    """V1alpha1Sequence unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Sequence
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_sequence.V1alpha1Sequence()  # noqa: E501
        if include_optional :
            return V1alpha1Sequence(
                count = '0', 
                end = '0', 
                format = '0', 
                start = '0'
            )
        else :
            return V1alpha1Sequence(
        )

    def testV1alpha1Sequence(self):
        """Test V1alpha1Sequence"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
