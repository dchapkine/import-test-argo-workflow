# coding: utf-8

"""
    Argo Server API

    The Argo Server based API for Argo  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from io.argoproj.argo.client.api.workflow_service_api import WorkflowServiceApi  # noqa: E501
from openapi_client.rest import ApiException


class TestWorkflowServiceApi(unittest.TestCase):
    """WorkflowServiceApi unit test stubs"""

    def setUp(self):
        self.api = io.argoproj.argo.client.api.workflow_service_api.WorkflowServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workflow(self):
        """Test case for create_workflow

        """
        pass

    def test_delete_workflow(self):
        """Test case for delete_workflow

        """
        pass

    def test_get_workflow(self):
        """Test case for get_workflow

        """
        pass

    def test_lint_workflow(self):
        """Test case for lint_workflow

        """
        pass

    def test_list_workflows(self):
        """Test case for list_workflows

        """
        pass

    def test_pod_logs(self):
        """Test case for pod_logs

        """
        pass

    def test_resubmit_workflow(self):
        """Test case for resubmit_workflow

        """
        pass

    def test_resume_workflow(self):
        """Test case for resume_workflow

        """
        pass

    def test_retry_workflow(self):
        """Test case for retry_workflow

        """
        pass

    def test_suspend_workflow(self):
        """Test case for suspend_workflow

        """
        pass

    def test_terminate_workflow(self):
        """Test case for terminate_workflow

        """
        pass

    def test_watch_workflows(self):
        """Test case for watch_workflows

        """
        pass


if __name__ == '__main__':
    unittest.main()
