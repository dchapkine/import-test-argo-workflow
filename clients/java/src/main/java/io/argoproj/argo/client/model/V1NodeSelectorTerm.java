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
import io.argoproj.argo.client.model.V1NodeSelectorRequirement;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
 */
@ApiModel(description = "A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.")

public class V1NodeSelectorTerm {
  public static final String SERIALIZED_NAME_MATCH_EXPRESSIONS = "matchExpressions";
  @SerializedName(SERIALIZED_NAME_MATCH_EXPRESSIONS)
  private List<V1NodeSelectorRequirement> matchExpressions = null;

  public static final String SERIALIZED_NAME_MATCH_FIELDS = "matchFields";
  @SerializedName(SERIALIZED_NAME_MATCH_FIELDS)
  private List<V1NodeSelectorRequirement> matchFields = null;


  public V1NodeSelectorTerm matchExpressions(List<V1NodeSelectorRequirement> matchExpressions) {
    
    this.matchExpressions = matchExpressions;
    return this;
  }

  public V1NodeSelectorTerm addMatchExpressionsItem(V1NodeSelectorRequirement matchExpressionsItem) {
    if (this.matchExpressions == null) {
      this.matchExpressions = new ArrayList<V1NodeSelectorRequirement>();
    }
    this.matchExpressions.add(matchExpressionsItem);
    return this;
  }

   /**
   * Get matchExpressions
   * @return matchExpressions
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<V1NodeSelectorRequirement> getMatchExpressions() {
    return matchExpressions;
  }


  public void setMatchExpressions(List<V1NodeSelectorRequirement> matchExpressions) {
    this.matchExpressions = matchExpressions;
  }


  public V1NodeSelectorTerm matchFields(List<V1NodeSelectorRequirement> matchFields) {
    
    this.matchFields = matchFields;
    return this;
  }

  public V1NodeSelectorTerm addMatchFieldsItem(V1NodeSelectorRequirement matchFieldsItem) {
    if (this.matchFields == null) {
      this.matchFields = new ArrayList<V1NodeSelectorRequirement>();
    }
    this.matchFields.add(matchFieldsItem);
    return this;
  }

   /**
   * Get matchFields
   * @return matchFields
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<V1NodeSelectorRequirement> getMatchFields() {
    return matchFields;
  }


  public void setMatchFields(List<V1NodeSelectorRequirement> matchFields) {
    this.matchFields = matchFields;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1NodeSelectorTerm v1NodeSelectorTerm = (V1NodeSelectorTerm) o;
    return Objects.equals(this.matchExpressions, v1NodeSelectorTerm.matchExpressions) &&
        Objects.equals(this.matchFields, v1NodeSelectorTerm.matchFields);
  }

  @Override
  public int hashCode() {
    return Objects.hash(matchExpressions, matchFields);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1NodeSelectorTerm {\n");
    sb.append("    matchExpressions: ").append(toIndentedString(matchExpressions)).append("\n");
    sb.append("    matchFields: ").append(toIndentedString(matchFields)).append("\n");
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

