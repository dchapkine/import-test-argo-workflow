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
from openapi_client.io.argoproj.argo.client.model.v1alpha1_dag_template import V1alpha1DAGTemplate  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1DAGTemplate(unittest.TestCase):
    """V1alpha1DAGTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1DAGTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_dag_template.V1alpha1DAGTemplate()  # noqa: E501
        if include_optional :
            return V1alpha1DAGTemplate(
                fail_fast = True, 
                target = '0', 
                tasks = [
                    openapi_client.models.dag_task_represents_a_node_in_the_graph_during_dag_execution.DAGTask represents a node in the graph during DAG execution(
                        arguments = openapi_client.models.arguments_to_a_template.Arguments to a template(
                            artifacts = [
                                openapi_client.models.artifact_indicates_an_artifact_to_place_at_a_specified_path.Artifact indicates an artifact to place at a specified path(
                                    archive = openapi_client.models.archive_strategy_describes_how_to_archive_files/directory_when_saving_artifacts.ArchiveStrategy describes how to archive files/directory when saving artifacts(
                                        none = openapi_client.models.v1alpha1_none_strategy.v1alpha1NoneStrategy(), 
                                        tar = openapi_client.models.tar_strategy_will_tar_and_gzip_the_file_or_directory_when_saving.TarStrategy will tar and gzip the file or directory when saving(), ), 
                                    artifact_location = openapi_client.models.v1alpha1_artifact_location.v1alpha1ArtifactLocation(
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
                                            repo = '0', 
                                            revision = '0', 
                                            ssh_private_key_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
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
                                                    optional = True, ), 
                                                bucket = '0', 
                                                endpoint = '0', 
                                                insecure = True, 
                                                region = '0', 
                                                role_arn = '0', 
                                                secret_key_secret = openapi_client.models.v1_secret_key_selector.v1SecretKeySelector(
                                                    key = '0', 
                                                    optional = True, ), ), ), ), 
                                    from = '0', 
                                    global_name = '0', 
                                    mode = 56, 
                                    name = '0', 
                                    optional = True, 
                                    path = '0', )
                                ], 
                            parameters = [
                                openapi_client.models.parameter_indicate_a_passed_string_parameter_to_a_service_template_with_an_optional_default_value.Parameter indicate a passed string parameter to a service template with an optional default value(
                                    default = '0', 
                                    global_name = '0', 
                                    name = '0', 
                                    value = '0', 
                                    value_from = openapi_client.models.value_from_describes_a_location_in_which_to_obtain_the_value_to_a_parameter.ValueFrom describes a location in which to obtain the value to a parameter(
                                        jq_filter = '0', 
                                        json_path = '0', 
                                        parameter = '0', 
                                        path = '0', ), )
                                ], ), 
                        continue_on = openapi_client.models.v1alpha1_continue_on.v1alpha1ContinueOn(
                            error = True, 
                            failed = True, ), 
                        dependencies = [
                            '0'
                            ], 
                        name = '0', 
                        on_exit = '0', 
                        template = '0', 
                        template_ref = openapi_client.models.v1alpha1_template_ref.v1alpha1TemplateRef(
                            name = '0', 
                            runtime_resolution = True, 
                            template = '0', ), 
                        when = '0', 
                        with_items = [
                            openapi_client.models.item_expands_a_single_workflow_step_into_multiple_parallel_steps
the_value_of_item_can_be_a_map,_string,_bool,_or_number.Item expands a single workflow step into multiple parallel steps
The value of Item can be a map, string, bool, or number(
                                bool_val = True, 
                                list_val = [
                                    openapi_client.models.+protobuf=true
+protobuf/options/(gogoproto/goproto_stringer)=false
+k8s:openapi_gen=true.+protobuf=true
+protobuf.options.(gogoproto.goproto_stringer)=false
+k8s:openapi-gen=true(
                                        bool_val = True, 
                                        map_val = {
                                            'key' : '0'
                                            }, 
                                        num_val = '0', 
                                        str_val = '0', 
                                        type = '0', )
                                    ], 
                                map_val = {
                                    'key' : openapi_client.models.+protobuf=true
+protobuf/options/(gogoproto/goproto_stringer)=false
+k8s:openapi_gen=true.+protobuf=true
+protobuf.options.(gogoproto.goproto_stringer)=false
+k8s:openapi-gen=true(
                                        bool_val = True, 
                                        num_val = '0', 
                                        str_val = '0', 
                                        type = '0', )
                                    }, 
                                num_val = '0', 
                                str_val = '0', 
                                type = '0', )
                            ], 
                        with_param = '0', 
                        with_sequence = openapi_client.models.sequence_expands_a_workflow_step_into_numeric_range.Sequence expands a workflow step into numeric range(
                            count = '0', 
                            end = '0', 
                            format = '0', 
                            start = '0', ), )
                    ]
            )
        else :
            return V1alpha1DAGTemplate(
        )

    def testV1alpha1DAGTemplate(self):
        """Test V1alpha1DAGTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
