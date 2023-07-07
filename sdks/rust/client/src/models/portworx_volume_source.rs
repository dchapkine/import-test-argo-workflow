/*
 * Argo Workflows API
 *
 * Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/
 *
 * The version of the OpenAPI document: VERSION
 * 
 * Generated by: https://openapi-generator.tech
 */

/// PortworxVolumeSource : PortworxVolumeSource represents a Portworx volume resource.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PortworxVolumeSource {
    /// FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\". Implicitly inferred to be \"ext4\" if unspecified.
    #[serde(rename = "fsType", skip_serializing_if = "Option::is_none")]
    pub fs_type: Option<String>,
    /// Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    #[serde(rename = "readOnly", skip_serializing_if = "Option::is_none")]
    pub read_only: Option<bool>,
    /// VolumeID uniquely identifies a Portworx volume
    #[serde(rename = "volumeID")]
    pub volume_id: String,
}

impl PortworxVolumeSource {
    /// PortworxVolumeSource represents a Portworx volume resource.
    pub fn new(volume_id: String) -> PortworxVolumeSource {
        PortworxVolumeSource {
            fs_type: None,
            read_only: None,
            volume_id,
        }
    }
}


