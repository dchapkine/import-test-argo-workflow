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
from openapi_client.io.argoproj.argo.client.model.v1alpha1_artifact_location import V1alpha1ArtifactLocation  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1ArtifactLocation(unittest.TestCase):
    """V1alpha1ArtifactLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ArtifactLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_artifact_location.V1alpha1ArtifactLocation()  # noqa: E501
        if include_optional :
            return V1alpha1ArtifactLocation(
                archive_logs = True, 
                artifactory = openapi_client.models.artifactory_artifact_is_the_location_of_an_artifactory_artifact.ArtifactoryArtifact is the location of an artifactory artifact(
                    artifactory_auth = openapi_client.models.artifactory_auth_describes_the_secret_selectors_required_for_authenticating_to_artifactory.ArtifactoryAuth describes the secret selectors required for authenticating to artifactory(
                        password_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                            key = '0', 
                            local_object_reference = openapi_client.models.v1_local_object_reference.v1LocalObjectReference(
                                name = '0', ), 
                            optional = True, ), 
                        username_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                            key = '0', 
                            optional = True, ), ), 
                    url = '0', ), 
                git = openapi_client.models.git_artifact_is_the_location_of_an_git_artifact.GitArtifact is the location of an git artifact(
                    depth = '0', 
                    fetch = [
                        '0'
                        ], 
                    insecure_ignore_host_key = True, 
                    password_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                        key = '0', 
                        local_object_reference = openapi_client.models.v1_local_object_reference.v1LocalObjectReference(
                            name = '0', ), 
                        optional = True, ), 
                    repo = '0', 
                    revision = '0', 
                    ssh_private_key_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                        key = '0', 
                        optional = True, ), 
                    username_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                        key = '0', 
                        optional = True, ), ), 
                hdfs = openapi_client.models.hdfs_artifact_is_the_location_of_an_hdfs_artifact.HDFSArtifact is the location of an HDFS artifact(
                    force = True, 
                    h_dfs_config = openapi_client.models.hdfs_config_is_configurations_for_hdfs.HDFSConfig is configurations for HDFS(
                        addresses = [
                            '0'
                            ], 
                        h_dfs_krb_config = openapi_client.models.hdfs_krb_config_is_auth_configurations_for_kerberos.HDFSKrbConfig is auth configurations for Kerberos(
                            krb_c_cache_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                                key = '0', 
                                local_object_reference = openapi_client.models.v1_local_object_reference.v1LocalObjectReference(
                                    name = '0', ), 
                                optional = True, ), 
                            krb_config_config_map = openapi_client.models.v1_config_map_key_selector.v1ConfigMapKeySelector(
                                key = '0', 
                                optional = True, ), 
                            krb_keytab_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                                key = '0', 
                                optional = True, ), 
                            krb_realm = '0', 
                            krb_service_principal_name = '0', 
                            krb_username = '0', ), 
                        hdfs_user = '0', ), 
                    path = '0', ), 
                http = openapi_client.models.http_artifact_allows_an_file_served_on_http_to_be_placed_as_an_input_artifact_in_a_container.HTTPArtifact allows an file served on HTTP to be placed as an input artifact in a container(
                    url = '0', ), 
                raw = openapi_client.models.raw_artifact_allows_raw_string_content_to_be_placed_as_an_artifact_in_a_container.RawArtifact allows raw string content to be placed as an artifact in a container(
                    data = '0', ), 
                s3 = openapi_client.models.s3_artifact_is_the_location_of_an_s3_artifact.S3Artifact is the location of an S3 artifact(
                    key = '0', 
                    s3_bucket = openapi_client.models.s3_bucket_contains_the_access_information_required_for_interfacing_with_an_s3_bucket.S3Bucket contains the access information required for interfacing with an S3 bucket(
                        access_key_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                            key = '0', 
                            local_object_reference = openapi_client.models.v1_local_object_reference.v1LocalObjectReference(
                                name = '0', ), 
                            optional = True, ), 
                        bucket = '0', 
                        endpoint = '0', 
                        insecure = True, 
                        region = '0', 
                        role_arn = '0', 
                        secret_key_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                            key = '0', 
                            optional = True, ), ), )
            )
        else :
            return V1alpha1ArtifactLocation(
        )

    def testV1alpha1ArtifactLocation(self):
        """Test V1alpha1ArtifactLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
