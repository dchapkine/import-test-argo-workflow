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
import io.argoproj.argo.client.model.V1ManagedFieldsEntry;
import io.argoproj.argo.client.model.V1OwnerReference;
import io.argoproj.argo.client.model.V1Time;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
 */
@ApiModel(description = "ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.")

public class V1ObjectMeta {
  public static final String SERIALIZED_NAME_ANNOTATIONS = "annotations";
  @SerializedName(SERIALIZED_NAME_ANNOTATIONS)
  private Map<String, String> annotations = null;

  public static final String SERIALIZED_NAME_CLUSTER_NAME = "clusterName";
  @SerializedName(SERIALIZED_NAME_CLUSTER_NAME)
  private String clusterName;

  public static final String SERIALIZED_NAME_CREATION_TIMESTAMP = "creationTimestamp";
  @SerializedName(SERIALIZED_NAME_CREATION_TIMESTAMP)
  private V1Time creationTimestamp;

  public static final String SERIALIZED_NAME_DELETION_GRACE_PERIOD_SECONDS = "deletionGracePeriodSeconds";
  @SerializedName(SERIALIZED_NAME_DELETION_GRACE_PERIOD_SECONDS)
  private String deletionGracePeriodSeconds;

  public static final String SERIALIZED_NAME_DELETION_TIMESTAMP = "deletionTimestamp";
  @SerializedName(SERIALIZED_NAME_DELETION_TIMESTAMP)
  private V1Time deletionTimestamp;

  public static final String SERIALIZED_NAME_FINALIZERS = "finalizers";
  @SerializedName(SERIALIZED_NAME_FINALIZERS)
  private List<String> finalizers = null;

  public static final String SERIALIZED_NAME_GENERATE_NAME = "generateName";
  @SerializedName(SERIALIZED_NAME_GENERATE_NAME)
  private String generateName;

  public static final String SERIALIZED_NAME_GENERATION = "generation";
  @SerializedName(SERIALIZED_NAME_GENERATION)
  private String generation;

  public static final String SERIALIZED_NAME_LABELS = "labels";
  @SerializedName(SERIALIZED_NAME_LABELS)
  private Map<String, String> labels = null;

  public static final String SERIALIZED_NAME_MANAGED_FIELDS = "managedFields";
  @SerializedName(SERIALIZED_NAME_MANAGED_FIELDS)
  private List<V1ManagedFieldsEntry> managedFields = null;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NAMESPACE = "namespace";
  @SerializedName(SERIALIZED_NAME_NAMESPACE)
  private String namespace;

  public static final String SERIALIZED_NAME_OWNER_REFERENCES = "ownerReferences";
  @SerializedName(SERIALIZED_NAME_OWNER_REFERENCES)
  private List<V1OwnerReference> ownerReferences = null;

  public static final String SERIALIZED_NAME_RESOURCE_VERSION = "resourceVersion";
  @SerializedName(SERIALIZED_NAME_RESOURCE_VERSION)
  private String resourceVersion;

  public static final String SERIALIZED_NAME_SELF_LINK = "selfLink";
  @SerializedName(SERIALIZED_NAME_SELF_LINK)
  private String selfLink;

  public static final String SERIALIZED_NAME_UID = "uid";
  @SerializedName(SERIALIZED_NAME_UID)
  private String uid;


  public V1ObjectMeta annotations(Map<String, String> annotations) {
    
    this.annotations = annotations;
    return this;
  }

  public V1ObjectMeta putAnnotationsItem(String key, String annotationsItem) {
    if (this.annotations == null) {
      this.annotations = new HashMap<String, String>();
    }
    this.annotations.put(key, annotationsItem);
    return this;
  }

   /**
   * Get annotations
   * @return annotations
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Map<String, String> getAnnotations() {
    return annotations;
  }


  public void setAnnotations(Map<String, String> annotations) {
    this.annotations = annotations;
  }


  public V1ObjectMeta clusterName(String clusterName) {
    
    this.clusterName = clusterName;
    return this;
  }

   /**
   * Get clusterName
   * @return clusterName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getClusterName() {
    return clusterName;
  }


  public void setClusterName(String clusterName) {
    this.clusterName = clusterName;
  }


  public V1ObjectMeta creationTimestamp(V1Time creationTimestamp) {
    
    this.creationTimestamp = creationTimestamp;
    return this;
  }

   /**
   * Get creationTimestamp
   * @return creationTimestamp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1Time getCreationTimestamp() {
    return creationTimestamp;
  }


  public void setCreationTimestamp(V1Time creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
  }


  public V1ObjectMeta deletionGracePeriodSeconds(String deletionGracePeriodSeconds) {
    
    this.deletionGracePeriodSeconds = deletionGracePeriodSeconds;
    return this;
  }

   /**
   * Get deletionGracePeriodSeconds
   * @return deletionGracePeriodSeconds
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDeletionGracePeriodSeconds() {
    return deletionGracePeriodSeconds;
  }


  public void setDeletionGracePeriodSeconds(String deletionGracePeriodSeconds) {
    this.deletionGracePeriodSeconds = deletionGracePeriodSeconds;
  }


  public V1ObjectMeta deletionTimestamp(V1Time deletionTimestamp) {
    
    this.deletionTimestamp = deletionTimestamp;
    return this;
  }

   /**
   * Get deletionTimestamp
   * @return deletionTimestamp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1Time getDeletionTimestamp() {
    return deletionTimestamp;
  }


  public void setDeletionTimestamp(V1Time deletionTimestamp) {
    this.deletionTimestamp = deletionTimestamp;
  }


  public V1ObjectMeta finalizers(List<String> finalizers) {
    
    this.finalizers = finalizers;
    return this;
  }

  public V1ObjectMeta addFinalizersItem(String finalizersItem) {
    if (this.finalizers == null) {
      this.finalizers = new ArrayList<String>();
    }
    this.finalizers.add(finalizersItem);
    return this;
  }

   /**
   * Get finalizers
   * @return finalizers
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getFinalizers() {
    return finalizers;
  }


  public void setFinalizers(List<String> finalizers) {
    this.finalizers = finalizers;
  }


  public V1ObjectMeta generateName(String generateName) {
    
    this.generateName = generateName;
    return this;
  }

   /**
   * GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency +optional
   * @return generateName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency +optional")

  public String getGenerateName() {
    return generateName;
  }


  public void setGenerateName(String generateName) {
    this.generateName = generateName;
  }


  public V1ObjectMeta generation(String generation) {
    
    this.generation = generation;
    return this;
  }

   /**
   * Get generation
   * @return generation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getGeneration() {
    return generation;
  }


  public void setGeneration(String generation) {
    this.generation = generation;
  }


  public V1ObjectMeta labels(Map<String, String> labels) {
    
    this.labels = labels;
    return this;
  }

  public V1ObjectMeta putLabelsItem(String key, String labelsItem) {
    if (this.labels == null) {
      this.labels = new HashMap<String, String>();
    }
    this.labels.put(key, labelsItem);
    return this;
  }

   /**
   * Get labels
   * @return labels
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Map<String, String> getLabels() {
    return labels;
  }


  public void setLabels(Map<String, String> labels) {
    this.labels = labels;
  }


  public V1ObjectMeta managedFields(List<V1ManagedFieldsEntry> managedFields) {
    
    this.managedFields = managedFields;
    return this;
  }

  public V1ObjectMeta addManagedFieldsItem(V1ManagedFieldsEntry managedFieldsItem) {
    if (this.managedFields == null) {
      this.managedFields = new ArrayList<V1ManagedFieldsEntry>();
    }
    this.managedFields.add(managedFieldsItem);
    return this;
  }

   /**
   * ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn&#39;t need to set or understand this field. A workflow can be the user&#39;s name, a controller&#39;s name, or the name of a specific apply path like \&quot;ci-cd\&quot;. The set of fields is always in the version that the workflow used when modifying the object.  +optional
   * @return managedFields
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.  +optional")

  public List<V1ManagedFieldsEntry> getManagedFields() {
    return managedFields;
  }


  public void setManagedFields(List<V1ManagedFieldsEntry> managedFields) {
    this.managedFields = managedFields;
  }


  public V1ObjectMeta name(String name) {
    
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public V1ObjectMeta namespace(String namespace) {
    
    this.namespace = namespace;
    return this;
  }

   /**
   * Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \&quot;default\&quot; namespace, but \&quot;default\&quot; is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces +optional
   * @return namespace
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces +optional")

  public String getNamespace() {
    return namespace;
  }


  public void setNamespace(String namespace) {
    this.namespace = namespace;
  }


  public V1ObjectMeta ownerReferences(List<V1OwnerReference> ownerReferences) {
    
    this.ownerReferences = ownerReferences;
    return this;
  }

  public V1ObjectMeta addOwnerReferencesItem(V1OwnerReference ownerReferencesItem) {
    if (this.ownerReferences == null) {
      this.ownerReferences = new ArrayList<V1OwnerReference>();
    }
    this.ownerReferences.add(ownerReferencesItem);
    return this;
  }

   /**
   * Get ownerReferences
   * @return ownerReferences
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<V1OwnerReference> getOwnerReferences() {
    return ownerReferences;
  }


  public void setOwnerReferences(List<V1OwnerReference> ownerReferences) {
    this.ownerReferences = ownerReferences;
  }


  public V1ObjectMeta resourceVersion(String resourceVersion) {
    
    this.resourceVersion = resourceVersion;
    return this;
  }

   /**
   * An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional
   * @return resourceVersion
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional")

  public String getResourceVersion() {
    return resourceVersion;
  }


  public void setResourceVersion(String resourceVersion) {
    this.resourceVersion = resourceVersion;
  }


  public V1ObjectMeta selfLink(String selfLink) {
    
    this.selfLink = selfLink;
    return this;
  }

   /**
   * SelfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional
   * @return selfLink
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "SelfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional")

  public String getSelfLink() {
    return selfLink;
  }


  public void setSelfLink(String selfLink) {
    this.selfLink = selfLink;
  }


  public V1ObjectMeta uid(String uid) {
    
    this.uid = uid;
    return this;
  }

   /**
   * UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids +optional
   * @return uid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids +optional")

  public String getUid() {
    return uid;
  }


  public void setUid(String uid) {
    this.uid = uid;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1ObjectMeta v1ObjectMeta = (V1ObjectMeta) o;
    return Objects.equals(this.annotations, v1ObjectMeta.annotations) &&
        Objects.equals(this.clusterName, v1ObjectMeta.clusterName) &&
        Objects.equals(this.creationTimestamp, v1ObjectMeta.creationTimestamp) &&
        Objects.equals(this.deletionGracePeriodSeconds, v1ObjectMeta.deletionGracePeriodSeconds) &&
        Objects.equals(this.deletionTimestamp, v1ObjectMeta.deletionTimestamp) &&
        Objects.equals(this.finalizers, v1ObjectMeta.finalizers) &&
        Objects.equals(this.generateName, v1ObjectMeta.generateName) &&
        Objects.equals(this.generation, v1ObjectMeta.generation) &&
        Objects.equals(this.labels, v1ObjectMeta.labels) &&
        Objects.equals(this.managedFields, v1ObjectMeta.managedFields) &&
        Objects.equals(this.name, v1ObjectMeta.name) &&
        Objects.equals(this.namespace, v1ObjectMeta.namespace) &&
        Objects.equals(this.ownerReferences, v1ObjectMeta.ownerReferences) &&
        Objects.equals(this.resourceVersion, v1ObjectMeta.resourceVersion) &&
        Objects.equals(this.selfLink, v1ObjectMeta.selfLink) &&
        Objects.equals(this.uid, v1ObjectMeta.uid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annotations, clusterName, creationTimestamp, deletionGracePeriodSeconds, deletionTimestamp, finalizers, generateName, generation, labels, managedFields, name, namespace, ownerReferences, resourceVersion, selfLink, uid);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1ObjectMeta {\n");
    sb.append("    annotations: ").append(toIndentedString(annotations)).append("\n");
    sb.append("    clusterName: ").append(toIndentedString(clusterName)).append("\n");
    sb.append("    creationTimestamp: ").append(toIndentedString(creationTimestamp)).append("\n");
    sb.append("    deletionGracePeriodSeconds: ").append(toIndentedString(deletionGracePeriodSeconds)).append("\n");
    sb.append("    deletionTimestamp: ").append(toIndentedString(deletionTimestamp)).append("\n");
    sb.append("    finalizers: ").append(toIndentedString(finalizers)).append("\n");
    sb.append("    generateName: ").append(toIndentedString(generateName)).append("\n");
    sb.append("    generation: ").append(toIndentedString(generation)).append("\n");
    sb.append("    labels: ").append(toIndentedString(labels)).append("\n");
    sb.append("    managedFields: ").append(toIndentedString(managedFields)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    namespace: ").append(toIndentedString(namespace)).append("\n");
    sb.append("    ownerReferences: ").append(toIndentedString(ownerReferences)).append("\n");
    sb.append("    resourceVersion: ").append(toIndentedString(resourceVersion)).append("\n");
    sb.append("    selfLink: ").append(toIndentedString(selfLink)).append("\n");
    sb.append("    uid: ").append(toIndentedString(uid)).append("\n");
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

