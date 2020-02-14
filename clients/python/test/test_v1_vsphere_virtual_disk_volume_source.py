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
from openapi_client.io.argoproj.argo.client.model.v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource  # noqa: E501
from openapi_client.rest import ApiException

class TestV1VsphereVirtualDiskVolumeSource(unittest.TestCase):
    """V1VsphereVirtualDiskVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VsphereVirtualDiskVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_vsphere_virtual_disk_volume_source.V1VsphereVirtualDiskVolumeSource()  # noqa: E501
        if include_optional :
            return V1VsphereVirtualDiskVolumeSource(
                fs_type = '0', 
                storage_policy_id = '0', 
                storage_policy_name = '0', 
                volume_path = '0'
            )
        else :
            return V1VsphereVirtualDiskVolumeSource(
        )

    def testV1VsphereVirtualDiskVolumeSource(self):
        """Test V1VsphereVirtualDiskVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
