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
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * V1alpha1ArchiveStrategy
 */

public class V1alpha1ArchiveStrategy {
  public static final String SERIALIZED_NAME_NONE = "none";
  @SerializedName(SERIALIZED_NAME_NONE)
  private Object none;

  public static final String SERIALIZED_NAME_TAR = "tar";
  @SerializedName(SERIALIZED_NAME_TAR)
  private Object tar;


  public V1alpha1ArchiveStrategy none(Object none) {
    
    this.none = none;
    return this;
  }

   /**
   * NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately.
   * @return none
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately.")

  public Object getNone() {
    return none;
  }


  public void setNone(Object none) {
    this.none = none;
  }


  public V1alpha1ArchiveStrategy tar(Object tar) {
    
    this.tar = tar;
    return this;
  }

   /**
   * Get tar
   * @return tar
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getTar() {
    return tar;
  }


  public void setTar(Object tar) {
    this.tar = tar;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1alpha1ArchiveStrategy v1alpha1ArchiveStrategy = (V1alpha1ArchiveStrategy) o;
    return Objects.equals(this.none, v1alpha1ArchiveStrategy.none) &&
        Objects.equals(this.tar, v1alpha1ArchiveStrategy.tar);
  }

  @Override
  public int hashCode() {
    return Objects.hash(none, tar);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1alpha1ArchiveStrategy {\n");
    sb.append("    none: ").append(toIndentedString(none)).append("\n");
    sb.append("    tar: ").append(toIndentedString(tar)).append("\n");
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

