/*
 * Argo Server API
 * The Argo Server based API for Argo
 *
 * The version of the OpenAPI document: latest
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package io.argoproj.argo.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.argoproj.argo.client.model.V1LocalObjectReference;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * V1ScaleIOVolumeSource
 */

public class V1ScaleIOVolumeSource {
  public static final String SERIALIZED_NAME_FS_TYPE = "fsType";
  @SerializedName(SERIALIZED_NAME_FS_TYPE)
  private String fsType;

  public static final String SERIALIZED_NAME_GATEWAY = "gateway";
  @SerializedName(SERIALIZED_NAME_GATEWAY)
  private String gateway;

  public static final String SERIALIZED_NAME_PROTECTION_DOMAIN = "protectionDomain";
  @SerializedName(SERIALIZED_NAME_PROTECTION_DOMAIN)
  private String protectionDomain;

  public static final String SERIALIZED_NAME_READ_ONLY = "readOnly";
  @SerializedName(SERIALIZED_NAME_READ_ONLY)
  private Boolean readOnly;

  public static final String SERIALIZED_NAME_SECRET_REF = "secretRef";
  @SerializedName(SERIALIZED_NAME_SECRET_REF)
  private V1LocalObjectReference secretRef;

  public static final String SERIALIZED_NAME_SSL_ENABLED = "sslEnabled";
  @SerializedName(SERIALIZED_NAME_SSL_ENABLED)
  private Boolean sslEnabled;

  public static final String SERIALIZED_NAME_STORAGE_MODE = "storageMode";
  @SerializedName(SERIALIZED_NAME_STORAGE_MODE)
  private String storageMode;

  public static final String SERIALIZED_NAME_STORAGE_POOL = "storagePool";
  @SerializedName(SERIALIZED_NAME_STORAGE_POOL)
  private String storagePool;

  public static final String SERIALIZED_NAME_SYSTEM = "system";
  @SerializedName(SERIALIZED_NAME_SYSTEM)
  private String system;

  public static final String SERIALIZED_NAME_VOLUME_NAME = "volumeName";
  @SerializedName(SERIALIZED_NAME_VOLUME_NAME)
  private String volumeName;


  public V1ScaleIOVolumeSource fsType(String fsType) {
    
    this.fsType = fsType;
    return this;
  }

   /**
   * Get fsType
   * @return fsType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getFsType() {
    return fsType;
  }


  public void setFsType(String fsType) {
    this.fsType = fsType;
  }


  public V1ScaleIOVolumeSource gateway(String gateway) {
    
    this.gateway = gateway;
    return this;
  }

   /**
   * The host address of the ScaleIO API Gateway.
   * @return gateway
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The host address of the ScaleIO API Gateway.")

  public String getGateway() {
    return gateway;
  }


  public void setGateway(String gateway) {
    this.gateway = gateway;
  }


  public V1ScaleIOVolumeSource protectionDomain(String protectionDomain) {
    
    this.protectionDomain = protectionDomain;
    return this;
  }

   /**
   * Get protectionDomain
   * @return protectionDomain
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getProtectionDomain() {
    return protectionDomain;
  }


  public void setProtectionDomain(String protectionDomain) {
    this.protectionDomain = protectionDomain;
  }


  public V1ScaleIOVolumeSource readOnly(Boolean readOnly) {
    
    this.readOnly = readOnly;
    return this;
  }

   /**
   * Get readOnly
   * @return readOnly
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getReadOnly() {
    return readOnly;
  }


  public void setReadOnly(Boolean readOnly) {
    this.readOnly = readOnly;
  }


  public V1ScaleIOVolumeSource secretRef(V1LocalObjectReference secretRef) {
    
    this.secretRef = secretRef;
    return this;
  }

   /**
   * Get secretRef
   * @return secretRef
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1LocalObjectReference getSecretRef() {
    return secretRef;
  }


  public void setSecretRef(V1LocalObjectReference secretRef) {
    this.secretRef = secretRef;
  }


  public V1ScaleIOVolumeSource sslEnabled(Boolean sslEnabled) {
    
    this.sslEnabled = sslEnabled;
    return this;
  }

   /**
   * Get sslEnabled
   * @return sslEnabled
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getSslEnabled() {
    return sslEnabled;
  }


  public void setSslEnabled(Boolean sslEnabled) {
    this.sslEnabled = sslEnabled;
  }


  public V1ScaleIOVolumeSource storageMode(String storageMode) {
    
    this.storageMode = storageMode;
    return this;
  }

   /**
   * Get storageMode
   * @return storageMode
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getStorageMode() {
    return storageMode;
  }


  public void setStorageMode(String storageMode) {
    this.storageMode = storageMode;
  }


  public V1ScaleIOVolumeSource storagePool(String storagePool) {
    
    this.storagePool = storagePool;
    return this;
  }

   /**
   * Get storagePool
   * @return storagePool
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getStoragePool() {
    return storagePool;
  }


  public void setStoragePool(String storagePool) {
    this.storagePool = storagePool;
  }


  public V1ScaleIOVolumeSource system(String system) {
    
    this.system = system;
    return this;
  }

   /**
   * The name of the storage system as configured in ScaleIO.
   * @return system
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The name of the storage system as configured in ScaleIO.")

  public String getSystem() {
    return system;
  }


  public void setSystem(String system) {
    this.system = system;
  }


  public V1ScaleIOVolumeSource volumeName(String volumeName) {
    
    this.volumeName = volumeName;
    return this;
  }

   /**
   * The name of a volume already created in the ScaleIO system that is associated with this volume source.
   * @return volumeName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The name of a volume already created in the ScaleIO system that is associated with this volume source.")

  public String getVolumeName() {
    return volumeName;
  }


  public void setVolumeName(String volumeName) {
    this.volumeName = volumeName;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1ScaleIOVolumeSource v1ScaleIOVolumeSource = (V1ScaleIOVolumeSource) o;
    return Objects.equals(this.fsType, v1ScaleIOVolumeSource.fsType) &&
        Objects.equals(this.gateway, v1ScaleIOVolumeSource.gateway) &&
        Objects.equals(this.protectionDomain, v1ScaleIOVolumeSource.protectionDomain) &&
        Objects.equals(this.readOnly, v1ScaleIOVolumeSource.readOnly) &&
        Objects.equals(this.secretRef, v1ScaleIOVolumeSource.secretRef) &&
        Objects.equals(this.sslEnabled, v1ScaleIOVolumeSource.sslEnabled) &&
        Objects.equals(this.storageMode, v1ScaleIOVolumeSource.storageMode) &&
        Objects.equals(this.storagePool, v1ScaleIOVolumeSource.storagePool) &&
        Objects.equals(this.system, v1ScaleIOVolumeSource.system) &&
        Objects.equals(this.volumeName, v1ScaleIOVolumeSource.volumeName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fsType, gateway, protectionDomain, readOnly, secretRef, sslEnabled, storageMode, storagePool, system, volumeName);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1ScaleIOVolumeSource {\n");
    sb.append("    fsType: ").append(toIndentedString(fsType)).append("\n");
    sb.append("    gateway: ").append(toIndentedString(gateway)).append("\n");
    sb.append("    protectionDomain: ").append(toIndentedString(protectionDomain)).append("\n");
    sb.append("    readOnly: ").append(toIndentedString(readOnly)).append("\n");
    sb.append("    secretRef: ").append(toIndentedString(secretRef)).append("\n");
    sb.append("    sslEnabled: ").append(toIndentedString(sslEnabled)).append("\n");
    sb.append("    storageMode: ").append(toIndentedString(storageMode)).append("\n");
    sb.append("    storagePool: ").append(toIndentedString(storagePool)).append("\n");
    sb.append("    system: ").append(toIndentedString(system)).append("\n");
    sb.append("    volumeName: ").append(toIndentedString(volumeName)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

