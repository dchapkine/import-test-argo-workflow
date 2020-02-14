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


package io.argoproj.argo.client.api;

import io.argoproj.argo.client.ApiException;
import io.argoproj.argo.client.model.V1alpha1WorkflowTemplate;
import io.argoproj.argo.client.model.V1alpha1WorkflowTemplateList;
import io.argoproj.argo.client.model.WorkflowtemplateWorkflowTemplateCreateRequest;
import io.argoproj.argo.client.model.WorkflowtemplateWorkflowTemplateLintRequest;
import io.argoproj.argo.client.model.WorkflowtemplateWorkflowTemplateUpdateRequest;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for WorkflowTemplateServiceApi
 */
@Ignore
public class WorkflowTemplateServiceApiTest {

    private final WorkflowTemplateServiceApi api = new WorkflowTemplateServiceApi();

    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createWorkflowTemplateTest() throws ApiException {
        String namespace = null;
        WorkflowtemplateWorkflowTemplateCreateRequest body = null;
        V1alpha1WorkflowTemplate response = api.createWorkflowTemplate(namespace, body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteWorkflowTemplateTest() throws ApiException {
        String namespace = null;
        String name = null;
        String deleteOptionsGracePeriodSeconds = null;
        String deleteOptionsPreconditionsUid = null;
        String deleteOptionsPreconditionsResourceVersion = null;
        Boolean deleteOptionsOrphanDependents = null;
        String deleteOptionsPropagationPolicy = null;
        List<String> deleteOptionsDryRun = null;
        Object response = api.deleteWorkflowTemplate(namespace, name, deleteOptionsGracePeriodSeconds, deleteOptionsPreconditionsUid, deleteOptionsPreconditionsResourceVersion, deleteOptionsOrphanDependents, deleteOptionsPropagationPolicy, deleteOptionsDryRun);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getWorkflowTemplateTest() throws ApiException {
        String namespace = null;
        String name = null;
        String getOptionsResourceVersion = null;
        V1alpha1WorkflowTemplate response = api.getWorkflowTemplate(namespace, name, getOptionsResourceVersion);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void lintWorkflowTemplateTest() throws ApiException {
        String namespace = null;
        WorkflowtemplateWorkflowTemplateLintRequest body = null;
        V1alpha1WorkflowTemplate response = api.lintWorkflowTemplate(namespace, body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listWorkflowTemplatesTest() throws ApiException {
        String namespace = null;
        String listOptionsLabelSelector = null;
        String listOptionsFieldSelector = null;
        Boolean listOptionsWatch = null;
        Boolean listOptionsAllowWatchBookmarks = null;
        String listOptionsResourceVersion = null;
        String listOptionsTimeoutSeconds = null;
        String listOptionsLimit = null;
        String listOptionsContinue = null;
        V1alpha1WorkflowTemplateList response = api.listWorkflowTemplates(namespace, listOptionsLabelSelector, listOptionsFieldSelector, listOptionsWatch, listOptionsAllowWatchBookmarks, listOptionsResourceVersion, listOptionsTimeoutSeconds, listOptionsLimit, listOptionsContinue);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateWorkflowTemplateTest() throws ApiException {
        String namespace = null;
        String name = null;
        WorkflowtemplateWorkflowTemplateUpdateRequest body = null;
        V1alpha1WorkflowTemplate response = api.updateWorkflowTemplate(namespace, name, body);

        // TODO: test validations
    }
    
}
