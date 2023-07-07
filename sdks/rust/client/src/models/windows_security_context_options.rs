/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// WindowsSecurityContextOptions : WindowsSecurityContextOptions contain Windows-specific options and credentials.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WindowsSecurityContextOptions {
    /// GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.
    #[serde(rename = "gmsaCredentialSpec", skip_serializing_if = "Option::is_none")]
    pub gmsa_credential_spec: Option<String>,
    /// GMSACredentialSpecName is the name of the GMSA credential spec to use.
    #[serde(rename = "gmsaCredentialSpecName", skip_serializing_if = "Option::is_none")]
    pub gmsa_credential_spec_name: Option<String>,
    /// HostProcess determines if a container should be run as a 'Host Process' container. This field is alpha-level and will only be honored by components that enable the WindowsHostProcessContainers feature flag. Setting this field without the feature flag will result in errors when validating the Pod. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers).  In addition, if HostProcess is true then HostNetwork must also be set to true.
    #[serde(rename = "hostProcess", skip_serializing_if = "Option::is_none")]
    pub host_process: Option<bool>,
    /// The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    #[serde(rename = "runAsUserName", skip_serializing_if = "Option::is_none")]
    pub run_as_user_name: Option<String>,
}

impl WindowsSecurityContextOptions {
    /// WindowsSecurityContextOptions contain Windows-specific options and credentials.
    pub fn new() -> WindowsSecurityContextOptions {
        WindowsSecurityContextOptions {
            gmsa_credential_spec: None,
            gmsa_credential_spec_name: None,
            host_process: None,
            run_as_user_name: None,
        }
    }
}


