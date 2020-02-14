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
from openapi_client.io.argoproj.argo.client.model.v1alpha1_cron_workflow_status import V1alpha1CronWorkflowStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1CronWorkflowStatus(unittest.TestCase):
    """V1alpha1CronWorkflowStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1CronWorkflowStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_cron_workflow_status.V1alpha1CronWorkflowStatus()  # noqa: E501
        if include_optional :
            return V1alpha1CronWorkflowStatus(
                active = [
                    openapi_client.models.object_reference_contains_enough_information_to_let_you_inspect_or_modify_the_referred_object/
+k8s:deepcopy_gen:interfaces=k8s/io/apimachinery/pkg/runtime/object.ObjectReference contains enough information to let you inspect or modify the referred object.
+k8s:deepcopy-gen:interfaces=k8s.io/apimachinery/pkg/runtime.Object(
                        api_version = '0', 
                        field_path = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', )
                    ], 
                last_scheduled_time = openapi_client.models.v1_time.v1Time(
                    nanos = 56, 
                    seconds = '0', )
            )
        else :
            return V1alpha1CronWorkflowStatus(
        )

    def testV1alpha1CronWorkflowStatus(self):
        """Test V1alpha1CronWorkflowStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
