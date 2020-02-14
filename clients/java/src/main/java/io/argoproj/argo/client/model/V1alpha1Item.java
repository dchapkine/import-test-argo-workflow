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
import io.argoproj.argo.client.model.V1alpha1ItemValue;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * +protobuf&#x3D;true +protobuf.options.(gogoproto.goproto_stringer)&#x3D;false +k8s:openapi-gen&#x3D;true
 */
@ApiModel(description = "+protobuf=true +protobuf.options.(gogoproto.goproto_stringer)=false +k8s:openapi-gen=true")

public class V1alpha1Item {
  public static final String SERIALIZED_NAME_BOOL_VAL = "boolVal";
  @SerializedName(SERIALIZED_NAME_BOOL_VAL)
  private Boolean boolVal;

  public static final String SERIALIZED_NAME_LIST_VAL = "listVal";
  @SerializedName(SERIALIZED_NAME_LIST_VAL)
  private List<V1alpha1ItemValue> listVal = null;

  public static final String SERIALIZED_NAME_MAP_VAL = "mapVal";
  @SerializedName(SERIALIZED_NAME_MAP_VAL)
  private Map<String, V1alpha1ItemValue> mapVal = null;

  public static final String SERIALIZED_NAME_NUM_VAL = "numVal";
  @SerializedName(SERIALIZED_NAME_NUM_VAL)
  private String numVal;

  public static final String SERIALIZED_NAME_STR_VAL = "strVal";
  @SerializedName(SERIALIZED_NAME_STR_VAL)
  private String strVal;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;


  public V1alpha1Item boolVal(Boolean boolVal) {
    
    this.boolVal = boolVal;
    return this;
  }

   /**
   * Get boolVal
   * @return boolVal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getBoolVal() {
    return boolVal;
  }


  public void setBoolVal(Boolean boolVal) {
    this.boolVal = boolVal;
  }


  public V1alpha1Item listVal(List<V1alpha1ItemValue> listVal) {
    
    this.listVal = listVal;
    return this;
  }

  public V1alpha1Item addListValItem(V1alpha1ItemValue listValItem) {
    if (this.listVal == null) {
      this.listVal = new ArrayList<V1alpha1ItemValue>();
    }
    this.listVal.add(listValItem);
    return this;
  }

   /**
   * Get listVal
   * @return listVal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<V1alpha1ItemValue> getListVal() {
    return listVal;
  }


  public void setListVal(List<V1alpha1ItemValue> listVal) {
    this.listVal = listVal;
  }


  public V1alpha1Item mapVal(Map<String, V1alpha1ItemValue> mapVal) {
    
    this.mapVal = mapVal;
    return this;
  }

  public V1alpha1Item putMapValItem(String key, V1alpha1ItemValue mapValItem) {
    if (this.mapVal == null) {
      this.mapVal = new HashMap<String, V1alpha1ItemValue>();
    }
    this.mapVal.put(key, mapValItem);
    return this;
  }

   /**
   * Get mapVal
   * @return mapVal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Map<String, V1alpha1ItemValue> getMapVal() {
    return mapVal;
  }


  public void setMapVal(Map<String, V1alpha1ItemValue> mapVal) {
    this.mapVal = mapVal;
  }


  public V1alpha1Item numVal(String numVal) {
    
    this.numVal = numVal;
    return this;
  }

   /**
   * Get numVal
   * @return numVal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getNumVal() {
    return numVal;
  }


  public void setNumVal(String numVal) {
    this.numVal = numVal;
  }


  public V1alpha1Item strVal(String strVal) {
    
    this.strVal = strVal;
    return this;
  }

   /**
   * Get strVal
   * @return strVal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getStrVal() {
    return strVal;
  }


  public void setStrVal(String strVal) {
    this.strVal = strVal;
  }


  public V1alpha1Item type(String type) {
    
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getType() {
    return type;
  }


  public void setType(String type) {
    this.type = type;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1alpha1Item v1alpha1Item = (V1alpha1Item) o;
    return Objects.equals(this.boolVal, v1alpha1Item.boolVal) &&
        Objects.equals(this.listVal, v1alpha1Item.listVal) &&
        Objects.equals(this.mapVal, v1alpha1Item.mapVal) &&
        Objects.equals(this.numVal, v1alpha1Item.numVal) &&
        Objects.equals(this.strVal, v1alpha1Item.strVal) &&
        Objects.equals(this.type, v1alpha1Item.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(boolVal, listVal, mapVal, numVal, strVal, type);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1alpha1Item {\n");
    sb.append("    boolVal: ").append(toIndentedString(boolVal)).append("\n");
    sb.append("    listVal: ").append(toIndentedString(listVal)).append("\n");
    sb.append("    mapVal: ").append(toIndentedString(mapVal)).append("\n");
    sb.append("    numVal: ").append(toIndentedString(numVal)).append("\n");
    sb.append("    strVal: ").append(toIndentedString(strVal)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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

