"""Types generated from the semantic model. Do not edit."""

# ruff: noqa: E501, UP013
from __future__ import annotations

from typing import (
    Any,
    Literal,
    NotRequired,
    TypedDict,
)

__all__ = ['ActorInputBean', 'ActorsMap', 'AddAtlassianTeamRequest', 'AddAtlassianTeamRequestPlanningStyle', 'AddFieldBean', 'AddGroupBean', 'AddIssueTypesToContext', 'AddNotificationsDetails', 'AddSecuritySchemeLevelsRequestBean', 'AddWorklogAdjustEstimate', 'AnalyseExpressionCheck', 'AnnouncementBannerConfiguration', 'AnnouncementBannerConfigurationUpdate', 'AnnouncementBannerConfigurationVisibility', 'AppWorkflowTransitionRule', 'Application', 'ApplicationProperty', 'ApplicationRole', 'ApprovalConfiguration', 'ApprovalConfigurationActive', 'ApprovalConfigurationConditionType', 'ApprovalConfigurationExcludeItem', 'ApprovalConfigurationPreview', 'ArchiveIssueAsyncRequest', 'ArchivedIssuesFilterRequest', 'AssociateFieldConfigurationsWithIssueTypesRequest', 'AssociateSecuritySchemeWithProjectDetails', 'AssociatedItemBean', 'AssociationContextObject', 'Attachment', 'AttachmentArchiveEntry', 'AttachmentArchiveImpl', 'AttachmentArchiveItemReadable', 'AttachmentArchiveMetadataReadable', 'AttachmentMetadata', 'AttachmentSettings', 'AuditEntry', 'AuditPage', 'AuditRecordBean', 'AuditRecords', 'AuditUser', 'AuditUserAvatarUrls', 'AutoCompleteSuggestion', 'AutoCompleteSuggestions', 'AvailableDashboardGadget', 'AvailableDashboardGadgetsResponse', 'AvailableWorkflowConnectRule', 'AvailableWorkflowConnectRuleRuleType', 'AvailableWorkflowForgeRule', 'AvailableWorkflowForgeRuleRuleType', 'AvailableWorkflowSystemRule', 'AvailableWorkflowSystemRuleRuleType', 'AvailableWorkflowTriggerTypes', 'AvailableWorkflowTriggers', 'Avatar', 'AvatarUrlsBean', 'Avatars', 'BoardColumnPayload', 'BoardFeaturePayload', 'BoardFeaturePayloadFeatureKey', 'BoardFeaturesPayload', 'BoardPayload', 'BoardPayloadCardColorStrategy', 'BoardsPayload', 'BulkAgentSessionInvocation', 'BulkAgentSessionItemError', 'BulkAgentSessionItemErrorType', 'BulkAgentSessionOutcome', 'BulkAgentSessionOutcomeResult', 'BulkAgentSessionsResponse', 'BulkChangeOwnerDetails', 'BulkChangelogRequestBean', 'BulkChangelogResponseBean', 'BulkContextualConfiguration', 'BulkCustomFieldOptionCreateRequest', 'BulkCustomFieldOptionUpdateRequest', 'BulkDeleteWorklogsAdjustEstimate', 'BulkEditActionError', 'BulkEditGetFields', 'BulkEditShareableEntityRequest', 'BulkEditShareableEntityRequestAction', 'BulkEditShareableEntityResponse', 'BulkEditShareableEntityResponseAction', 'BulkFetchIssueRequestBean', 'BulkIssueIsWatching', 'BulkIssuePropertyUpdateRequest', 'BulkIssueResults', 'BulkMoveWorklogsAdjustEstimate', 'BulkOperationErrorResponse', 'BulkOperationErrorResult', 'BulkOperationProgress', 'BulkOperationProgressStatus', 'BulkPermissionGrants', 'BulkPermissionsRequestBean', 'BulkPolicyOperationResponse', 'BulkProjectPermissionGrants', 'BulkProjectPermissions', 'BulkProjectPolicyRequest', 'BulkRedactionRequest', 'BulkRedactionResponse', 'BulkStartAgentSessionsBatchRequest', 'BulkStartUniformAgentSessionsRequest', 'BulkTransitionGetAvailableTransitions', 'BulkTransitionSubmitInput', 'BulkWorklogKeyRequestBean', 'BulkWorklogKeyResponseBean', 'CardLayout', 'CardLayoutField', 'CardLayoutFieldMode', 'ChangeDetails', 'ChangeFilterOwner', 'ChangedValueBean', 'ChangedWorklog', 'ChangedWorklogs', 'Changelog', 'ColumnItem', 'ColumnRequestBody', 'Comment', 'ComponentIssuesCount', 'ComponentJsonBean', 'ComponentWithIssueCount', 'ComponentWithIssueCountAssigneeType', 'ComponentWithIssueCountRealAssigneeType', 'CompoundClause', 'CompoundClauseOperator', 'ConditionGroupConfiguration', 'ConditionGroupConfigurationOperation', 'ConditionGroupPayload', 'ConditionGroupPayloadOperation', 'ConditionGroupUpdate', 'ConditionGroupUpdateOperation', 'Configuration', 'ConfigurationsListParameters', 'ConnectCustomFieldValue', 'ConnectCustomFieldValueType', 'ConnectCustomFieldValues', 'ConnectModule', 'ConnectModules', 'ContainerForProjectFeatures', 'ContainerForRegisteredWebhooks', 'ContainerForWebhookIDs', 'ContainerOfWorkflowSchemeAssociations', 'ContentItem', 'ContentItemEntityType', 'Context', 'ContextDefaultValues', 'ContextForProjectAndIssueType', 'ContextualConfiguration', 'ConvertedJqlQueries', 'CreateCrossProjectReleaseRequest', 'CreateCustomFieldContext', 'CreateCustomFieldRequest', 'CreateDateFieldRequest', 'CreateDateFieldRequestType', 'CreateExclusionRulesRequest', 'CreateFieldAssociationSchemeLinksBean', 'CreateFieldAssociationSchemeRequest', 'CreateFieldAssociationSchemeResponse', 'CreateIssueSecuritySchemeDetails', 'CreateIssueSourceRequest', 'CreateIssueSourceRequestType', 'CreateNotificationSchemeDetails', 'CreatePermissionHolderRequest', 'CreatePermissionHolderRequestType', 'CreatePermissionRequest', 'CreatePermissionRequestType', 'CreatePlanOnlyTeamRequest', 'CreatePlanOnlyTeamRequestPlanningStyle', 'CreatePlanRequest', 'CreatePriorityDetails', 'CreatePriorityDetailsIconUrl', 'CreatePrioritySchemeDetails', 'CreateProjectDetails', 'CreateProjectDetailsAssigneeType', 'CreateProjectDetailsProjectTemplateKey', 'CreateProjectDetailsProjectTypeKey', 'CreateResolutionDetails', 'CreateSchedulingRequest', 'CreateSchedulingRequestDependencies', 'CreateSchedulingRequestEstimation', 'CreateSchedulingRequestInferredDates', 'CreateUiModificationDetails', 'CreateUpdateRoleRequestBean', 'CreatedIssue', 'CreatedIssues', 'CustomContextVariable', 'CustomFieldConfigurations', 'CustomFieldContext', 'CustomFieldContextDefaultValue', 'CustomFieldContextDefaultValueCascadingOption', 'CustomFieldContextDefaultValueDate', 'CustomFieldContextDefaultValueDateTime', 'CustomFieldContextDefaultValueFloat', 'CustomFieldContextDefaultValueForgeDateTimeField', 'CustomFieldContextDefaultValueForgeGroupField', 'CustomFieldContextDefaultValueForgeMultiGroupField', 'CustomFieldContextDefaultValueForgeMultiStringField', 'CustomFieldContextDefaultValueForgeMultiUserField', 'CustomFieldContextDefaultValueForgeNumberField', 'CustomFieldContextDefaultValueForgeObjectField', 'CustomFieldContextDefaultValueForgeStringField', 'CustomFieldContextDefaultValueForgeUserField', 'CustomFieldContextDefaultValueLabels', 'CustomFieldContextDefaultValueLongText', 'CustomFieldContextDefaultValueMultiUserPicker', 'CustomFieldContextDefaultValueMultipleGroupPicker', 'CustomFieldContextDefaultValueMultipleOption', 'CustomFieldContextDefaultValueMultipleVersionPicker', 'CustomFieldContextDefaultValueProject', 'CustomFieldContextDefaultValueReadOnly', 'CustomFieldContextDefaultValueSingleGroupPicker', 'CustomFieldContextDefaultValueSingleOption', 'CustomFieldContextDefaultValueSingleVersionPicker', 'CustomFieldContextDefaultValueTextArea', 'CustomFieldContextDefaultValueTextField', 'CustomFieldContextDefaultValueUpdate', 'CustomFieldContextDefaultValueUrl', 'CustomFieldContextDefaultValuesUpdate', 'CustomFieldContextOption', 'CustomFieldContextProjectMapping', 'CustomFieldContextSingleUserPickerDefaults', 'CustomFieldContextUpdateDetails', 'CustomFieldCreatedContextOptionsList', 'CustomFieldDefinitionJsonBean', 'CustomFieldDefinitionJsonBeanSearcherKey', 'CustomFieldOption', 'CustomFieldOptionCreate', 'CustomFieldOptionUpdate', 'CustomFieldPayload', 'CustomFieldPayloadOnConflict', 'CustomFieldPayloadScope', 'CustomFieldReplacement', 'CustomFieldUpdatedContextOptionsList', 'CustomFieldValueUpdate', 'CustomFieldValueUpdateDetails', 'CustomTemplateOptions', 'CustomTemplateRequestDto', 'CustomTemplatesProjectDetails', 'CustomTemplatesProjectDetailsAccessLevel', 'CustomTemplatesProjectDetailsAssigneeType', 'Dashboard', 'DashboardDetails', 'DashboardGadget', 'DashboardGadgetColor', 'DashboardGadgetPosition', 'DashboardGadgetResponse', 'DashboardGadgetSettings', 'DashboardGadgetUpdateRequest', 'DataClassificationLevelsBean', 'DataClassificationTagBean', 'DateRangeFilterRequest', 'DefaultLevelValue', 'DefaultShareScope', 'DefaultShareScopeScope', 'DefaultWorkflow', 'DefaultWorkflowEditorResponse', 'DefaultWorkflowEditorResponseValue', 'DeleteAndReplaceVersionBean', 'DeleteAvatarType', 'DeleteFieldAssociationSchemeResponse', 'DeleteIssueDeleteSubtasks', 'DeleteWorklogAdjustEstimate', 'DetailedErrorCollection', 'DocumentVersion', 'DuplicatePlanRequest', 'EditTemplateRequest', 'EntityProperty', 'EntityPropertyDetails', 'Error', 'ErrorCollection', 'ErrorCollections', 'ErrorMessage', 'ErrorResponse', 'Errors', 'EventNotification', 'EventNotificationNotificationType', 'ExpandPrioritySchemePage', 'ExportArchivedIssuesTaskProgressResponse', 'FailedWebhook', 'FailedWebhooks', 'Field', 'FieldAssociationItemPayload', 'FieldAssociationParameters', 'FieldAssociationSchemeFieldSearchResult', 'FieldAssociationSchemeLinks', 'FieldAssociationSchemeLinksBean', 'FieldAssociationSchemeMatchedFilters', 'FieldAssociationSchemeProjectSearchResult', 'FieldAssociationsRequest', 'FieldCapabilityPayload', 'FieldChangedClause', 'FieldChangedClauseOperator', 'FieldConfiguration', 'FieldConfigurationDetails', 'FieldConfigurationIssueTypeItem', 'FieldConfigurationItem', 'FieldConfigurationItemsDetails', 'FieldConfigurationScheme', 'FieldConfigurationSchemeProjectAssociation', 'FieldConfigurationSchemeProjects', 'FieldConfigurationToIssueTypeMapping', 'FieldCreateMetadata', 'FieldDetails', 'FieldIdentifierObject', 'FieldLastUsed', 'FieldLastUsedType', 'FieldLayoutConfiguration', 'FieldLayoutPayload', 'FieldLayoutSchemePayload', 'FieldMetadata', 'FieldProjectAssociation', 'FieldReferenceData', 'FieldReferenceDataAuto', 'FieldReferenceDataDeprecated', 'FieldReferenceDataOrderable', 'FieldReferenceDataSearchable', 'FieldSchemePayload', 'FieldSchemePayloadOnConflict', 'FieldSchemeToFieldsPartialFailure', 'FieldSchemeToFieldsResponse', 'FieldSchemeToProjectsPartialFailure', 'FieldSchemeToProjectsRequest', 'FieldSchemeToProjectsResponse', 'FieldUpdateOperation', 'FieldValueClause', 'FieldValueClauseOperator', 'FieldWasClause', 'FieldWasClauseOperator', 'Fields', 'FieldsSchemeItemParameter', 'FieldsSchemeItemParameterRendererType', 'FieldsSchemeItemWorkTypeParameter', 'FieldsSchemeItemWorkTypeParameterRendererType', 'Filter', 'FilterDetails', 'FilterSubscription', 'FilterSubscriptionsList', 'FindComponentsForProjectsOrderBy', 'FindUsersAndGroupsAvatarSize', 'ForgePanelProjectPinAsyncResponse', 'ForgePanelProjectPinRequest', 'ForgePanelProjectPinStatus', 'ForgePanelProjectPinStatusRequest', 'ForgePanelProjectPinStatusResponse', 'FoundGroup', 'FoundGroupManagedBy', 'FoundGroupUsageType', 'FoundGroups', 'FoundUsers', 'FoundUsersAndGroups', 'FromLayoutPayload', 'FunctionOperand', 'FunctionReferenceData', 'FunctionReferenceDataIsList', 'FunctionReferenceDataSupportsListAndSingleValueOperators', 'GetAccessibleProjectTypeByKeyProjectTypeKey', 'GetAllDashboardsFilter', 'GetAllIssueTypeSchemesOrderBy', 'GetAllSystemAvatarsType', 'GetAllUserDataClassificationLevelsOrderBy', 'GetAllUserDataClassificationLevelsStatusItem', 'GetApproximateApplicationLicenseCountApplicationKey', 'GetAtlassianTeamResponse', 'GetAtlassianTeamResponsePlanningStyle', 'GetAvatarImageByIdFormat', 'GetAvatarImageByIdSize', 'GetAvatarImageByIdType', 'GetAvatarImageByOwnerFormat', 'GetAvatarImageByOwnerSize', 'GetAvatarImageByOwnerType', 'GetAvatarImageByTypeFormat', 'GetAvatarImageByTypeSize', 'GetAvatarImageByTypeType', 'GetAvatarsType', 'GetCommentsOrderBy', 'GetCrossProjectReleaseResponse', 'GetCustomFieldResponse', 'GetDashboardsPaginatedOrderBy', 'GetDashboardsPaginatedStatus', 'GetDateFieldResponse', 'GetDateFieldResponseType', 'GetExclusionRulesResponse', 'GetFieldAssociationParametersResponse', 'GetFieldAssociationSchemeByIdResponse', 'GetFieldAssociationSchemeResponse', 'GetFieldsPaginatedOrderBy', 'GetFieldsPaginatedTypeItem', 'GetFiltersPaginatedOrderBy', 'GetForgeAppPropertyKeysResponse', 'GetForgeAppPropertyKeysResponseKeysItem', 'GetForgeAppPropertyResponse', 'GetIssueSourceResponse', 'GetIssueSourceResponseType', 'GetIssueTypeScreenSchemesOrderBy', 'GetPermissionHolderResponse', 'GetPermissionHolderResponseType', 'GetPermissionResponse', 'GetPermissionResponseType', 'GetPlanOnlyTeamResponse', 'GetPlanOnlyTeamResponsePlanningStyle', 'GetPlanResponse', 'GetPlanResponseForPage', 'GetPlanResponseForPageStatus', 'GetPlanResponseStatus', 'GetPrioritySchemesOrderBy', 'GetProjectComponentsComponentSource', 'GetProjectComponentsPaginatedComponentSource', 'GetProjectComponentsPaginatedOrderBy', 'GetProjectTypeByKeyProjectTypeKey', 'GetProjectVersionsPaginatedOrderBy', 'GetProjectsWithFieldSchemesResponse', 'GetRemoteIssueLinksResponse', 'GetSchedulingResponse', 'GetSchedulingResponseDependencies', 'GetSchedulingResponseEstimation', 'GetSchedulingResponseInferredDates', 'GetScreenSchemesOrderBy', 'GetScreensOrderBy', 'GetScreensScopeItem', 'GetTeamResponseForPage', 'GetTeamResponseForPageType', 'GetTrashedFieldsPaginatedExpand', 'GetWorkflowTransitionRuleConfigurationsTypesItem', 'GetWorkflowsPaginatedOrderBy', 'GlobalScopeBean', 'GlobalScopeBeanAttributesItem', 'Group', 'GroupDetails', 'GroupLabel', 'GroupLabelType', 'GroupName', 'HealthCheckResult', 'Hierarchy', 'HistoryMetadata', 'HistoryMetadataParticipant', 'Icon', 'IdBean', 'IdOrKeyBean', 'IncludedFields', 'IssueArchivalSyncRequest', 'IssueArchivalSyncResponse', 'IssueBean', 'IssueBulkDeletePayload', 'IssueBulkEditField', 'IssueBulkEditFieldMultiSelectFieldOptionsItem', 'IssueBulkEditPayload', 'IssueBulkMovePayload', 'IssueBulkOperationsFieldOption', 'IssueBulkTransitionForWorkflow', 'IssueBulkTransitionPayload', 'IssueBulkWatchOrUnwatchPayload', 'IssueChangeLog', 'IssueChangelogIds', 'IssueCommentListRequestBean', 'IssueContextVariable', 'IssueCreateMetadata', 'IssueEntityProperties', 'IssueEntityPropertiesForMultiUpdate', 'IssueError', 'IssueEvent', 'IssueFieldOption', 'IssueFieldOptionConfiguration', 'IssueFieldOptionConfigurationAttributesItem', 'IssueFieldOptionCreateBean', 'IssueFieldOptionScopeBean', 'IssueFilterForBulkPropertyDelete', 'IssueFilterForBulkPropertySet', 'IssueLayoutItemPayload', 'IssueLayoutItemPayloadSectionType', 'IssueLayoutItemPayloadType', 'IssueLayoutPayload', 'IssueLayoutPayloadIssueLayoutType', 'IssueLimitReportResponseBean', 'IssueLink', 'IssueLinkType', 'IssueLinkTypes', 'IssueList', 'IssueMatches', 'IssueMatchesForJql', 'IssuePickerSuggestions', 'IssuePickerSuggestionsIssueType', 'IssueSecurityLevelMember', 'IssueSecuritySchemeToProjectMapping', 'IssueTransition', 'IssueTransitionStatus', 'IssueTypeCreateBean', 'IssueTypeCreateBeanType', 'IssueTypeDefaultValue', 'IssueTypeDefaultValueUpdate', 'IssueTypeDetails', 'IssueTypeHierarchyPayload', 'IssueTypeHierarchyPayloadOnConflict', 'IssueTypeIds', 'IssueTypeIdsToRemove', 'IssueTypeInfo', 'IssueTypeIssueCreateMetadata', 'IssueTypePayload', 'IssueTypePayloadOnConflict', 'IssueTypeProjectCreatePayload', 'IssueTypeScheme', 'IssueTypeSchemeDetails', 'IssueTypeSchemeId', 'IssueTypeSchemeMapping', 'IssueTypeSchemePayload', 'IssueTypeSchemeProjectAssociation', 'IssueTypeSchemeProjects', 'IssueTypeSchemeUpdateDetails', 'IssueTypeScreenScheme', 'IssueTypeScreenSchemeDetails', 'IssueTypeScreenSchemeId', 'IssueTypeScreenSchemeItem', 'IssueTypeScreenSchemeMapping', 'IssueTypeScreenSchemeMappingDetails', 'IssueTypeScreenSchemePayload', 'IssueTypeScreenSchemeProjectAssociation', 'IssueTypeScreenSchemeUpdateDetails', 'IssueTypeScreenSchemesProjects', 'IssueTypeToContextMapping', 'IssueTypeUpdateBean', 'IssueTypeWithStatus', 'IssueTypeWorkflowMapping', 'IssueTypesWorkflowMapping', 'IssueUpdateDetails', 'IssueUpdateMetadata', 'IssuesAndJqlQueries', 'IssuesJqlMetaDataBean', 'IssuesMetaBean', 'IssuesUpdateBean', 'JExpEvaluateIssuesJqlMetaDataBean', 'JExpEvaluateIssuesMetaBean', 'JExpEvaluateJiraExpressionResultBean', 'JExpEvaluateMetaDataBean', 'JexpEvaluateCtxIssues', 'JexpEvaluateCtxJqlIssues', 'JexpIssues', 'JexpJqlIssues', 'JexpJqlIssuesValidation', 'JiraCascadingSelectField', 'JiraColorField', 'JiraColorInput', 'JiraComponentField', 'JiraDateField', 'JiraDateInput', 'JiraDateTimeField', 'JiraDateTimeInput', 'JiraDurationField', 'JiraExpressionAnalysis', 'JiraExpressionComplexity', 'JiraExpressionEvalContextBean', 'JiraExpressionEvalRequestBean', 'JiraExpressionEvaluateContextBean', 'JiraExpressionEvaluateRequestBean', 'JiraExpressionEvaluationMetaDataBean', 'JiraExpressionForAnalysis', 'JiraExpressionResult', 'JiraExpressionValidationError', 'JiraExpressionValidationErrorType', 'JiraExpressionsAnalysis', 'JiraExpressionsComplexityBean', 'JiraExpressionsComplexityValueBean', 'JiraGroupInput', 'JiraIssueFields', 'JiraIssueTypeField', 'JiraLabelPropertiesInputJackson1', 'JiraLabelPropertiesInputJackson1Color', 'JiraLabelsField', 'JiraLabelsFieldBulkEditMultiSelectFieldOption', 'JiraLabelsInput', 'JiraMultiSelectComponentField', 'JiraMultiSelectComponentFieldBulkEditMultiSelectFieldOption', 'JiraMultipleGroupPickerField', 'JiraMultipleSelectField', 'JiraMultipleSelectUserPickerField', 'JiraMultipleVersionPickerField', 'JiraMultipleVersionPickerFieldBulkEditMultiSelectFieldOption', 'JiraNumberField', 'JiraPriorityField', 'JiraRichTextField', 'JiraRichTextInput', 'JiraSelectedOptionField', 'JiraSingleGroupPickerField', 'JiraSingleLineTextField', 'JiraSingleSelectField', 'JiraSingleSelectUserPickerField', 'JiraSingleVersionPickerField', 'JiraStatus', 'JiraStatusInput', 'JiraStatusStatusCategory', 'JiraTimeTrackingField', 'JiraUrlField', 'JiraUserField', 'JiraVersionField', 'JiraWorkflow', 'JiraWorkflowPreviewStatus', 'JiraWorkflowPreviewStatusStatusCategory', 'JiraWorkflowStatus', 'JiraWorkflowStatusStatusCategory', 'JqlCountRequestBean', 'JqlCountResultsBean', 'JqlFunctionPrecomputationBean', 'JqlFunctionPrecomputationGetByIdRequest', 'JqlFunctionPrecomputationGetByIdResponse', 'JqlFunctionPrecomputationUpdateBean', 'JqlFunctionPrecomputationUpdateErrorResponse', 'JqlFunctionPrecomputationUpdateRequestBean', 'JqlFunctionPrecomputationUpdateResponse', 'JqlPersonalDataMigrationRequest', 'JqlQueriesToParse', 'JqlQueriesToSanitize', 'JqlQuery', 'JqlQueryClause', 'JqlQueryClauseOperand', 'JqlQueryClauseTimePredicate', 'JqlQueryClauseTimePredicateOperator', 'JqlQueryField', 'JqlQueryFieldEntityProperty', 'JqlQueryFieldEntityPropertyType', 'JqlQueryOrderByClause', 'JqlQueryOrderByClauseElement', 'JqlQueryOrderByClauseElementDirection', 'JqlQueryToSanitize', 'JqlQueryUnitaryOperand', 'JqlQueryWithUnknownUsers', 'JqlReferenceData', 'JsonContextVariable', 'JsonNode', 'JsonNodeNumberType', 'JsonTypeBean', 'KeywordOperand', 'KeywordOperandKeyword', 'License', 'LicenseMetric', 'LicensedApplication', 'LicensedApplicationPlan', 'LimitExceededResponseBean', 'LinkGroup', 'LinkIssueRequestJsonBean', 'LinkedIssue', 'ListOperand', 'ListWrapperCallbackApplicationRole', 'ListWrapperCallbackGroupName', 'Locale', 'MappingsByIssueTypeOverride', 'MappingsByWorkflow', 'MigrationResourceUpdateEntityPropertiesValuePutEntityType', 'MinimalFieldSchemeToFieldsPartialFailure', 'MinimalFieldSchemeToFieldsResponse', 'MoveFieldBean', 'MoveFieldBeanPosition', 'MultiIssueEntityProperties', 'MultipleCustomFieldValuesUpdate', 'MultipleCustomFieldValuesUpdateDetails', 'NestedResponse', 'NewUserDetails', 'NonWorkingDay', 'Notification', 'NotificationEvent', 'NotificationRecipients', 'NotificationRecipientsRestrictions', 'NotificationScheme', 'NotificationSchemeAndProjectMappingJsonBean', 'NotificationSchemeEvent', 'NotificationSchemeEventDetails', 'NotificationSchemeEventIdPayload', 'NotificationSchemeEventPayload', 'NotificationSchemeEventTypeId', 'NotificationSchemeId', 'NotificationSchemeNotificationDetails', 'NotificationSchemeNotificationDetailsPayload', 'NotificationSchemePayload', 'NotificationSchemePayloadOnConflict', 'OldToNewSecurityLevelMappingsBean', 'OperationMessage', 'Operations', 'OrderOfCustomFieldOptions', 'OrderOfCustomFieldOptionsPosition', 'OrderOfIssueTypes', 'OrderOfIssueTypesPosition', 'PageBean2ComponentJsonBean', 'PageBean2FieldAssociationSchemeFieldSearchResult', 'PageBean2FieldAssociationSchemeProjectSearchResult', 'PageBean2GetFieldAssociationSchemeResponse', 'PageBean2GetProjectsWithFieldSchemesResponse', 'PageBean2JqlFunctionPrecomputationBean', 'PageBean2ProjectFieldBean', 'PageBeanBulkContextualConfiguration', 'PageBeanChangelog', 'PageBeanComment', 'PageBeanComponentWithIssueCount', 'PageBeanContext', 'PageBeanContextDefaultValues', 'PageBeanContextForProjectAndIssueType', 'PageBeanContextualConfiguration', 'PageBeanCustomFieldContext', 'PageBeanCustomFieldContextDefaultValue', 'PageBeanCustomFieldContextOption', 'PageBeanCustomFieldContextProjectMapping', 'PageBeanDashboard', 'PageBeanField', 'PageBeanFieldConfigurationDetails', 'PageBeanFieldConfigurationIssueTypeItem', 'PageBeanFieldConfigurationItem', 'PageBeanFieldConfigurationScheme', 'PageBeanFieldConfigurationSchemeProjects', 'PageBeanFieldProjectAssociation', 'PageBeanFilterDetails', 'PageBeanGroupDetails', 'PageBeanIssueFieldOption', 'PageBeanIssueSecurityLevelMember', 'PageBeanIssueSecuritySchemeToProjectMapping', 'PageBeanIssueTypeScheme', 'PageBeanIssueTypeSchemeMapping', 'PageBeanIssueTypeSchemeProjects', 'PageBeanIssueTypeScreenScheme', 'PageBeanIssueTypeScreenSchemeItem', 'PageBeanIssueTypeScreenSchemesProjects', 'PageBeanIssueTypeToContextMapping', 'PageBeanNotificationScheme', 'PageBeanNotificationSchemeAndProjectMappingJsonBean', 'PageBeanPriority', 'PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects', 'PageBeanPriorityWithSequence', 'PageBeanProject', 'PageBeanProjectDetails', 'PageBeanResolutionJsonBean', 'PageBeanScreen', 'PageBeanScreenScheme', 'PageBeanScreenWithTab', 'PageBeanSecurityLevel', 'PageBeanSecurityLevelMember', 'PageBeanSecuritySchemeWithProjects', 'PageBeanString', 'PageBeanUiModificationDetails', 'PageBeanUser', 'PageBeanUserDetails', 'PageBeanUserKey', 'PageBeanVersion', 'PageBeanWebhook', 'PageBeanWorkflow', 'PageBeanWorkflowScheme', 'PageBeanWorkflowTransitionRules', 'PageOfChangelogs', 'PageOfComments', 'PageOfCreateMetaIssueTypeWithField', 'PageOfCreateMetaIssueTypes', 'PageOfDashboards', 'PageOfStatuses', 'PageOfWorklogs', 'PageWithCursorGetPlanResponseForPage', 'PageWithCursorGetTeamResponseForPage', 'PagedListUserDetailsApplicationUser', 'ParameterRemovalDetails', 'ParseJqlQueriesValidation', 'ParsedJqlQueries', 'ParsedJqlQuery', 'PermissionDetails', 'PermissionGrant', 'PermissionGrantDto', 'PermissionGrants', 'PermissionHolder', 'PermissionPayloadDto', 'PermissionPayloadDtoOnConflict', 'PermissionScheme', 'PermissionSchemes', 'Permissions', 'PermissionsKeysBean', 'PermittedProjects', 'PolicyApplicationViolation', 'PolicySummary', 'PolicySummaryResponse', 'PreviewConditionGroupConfiguration', 'PreviewConditionGroupConfigurationOperation', 'PreviewRuleConfiguration', 'PreviewTrigger', 'Priority', 'PriorityId', 'PriorityMapping', 'PrioritySchemeChangesWithoutMappings', 'PrioritySchemeId', 'PrioritySchemeWithPaginatedPrioritiesAndProjects', 'PriorityWithSequence', 'Project', 'ProjectAndIssueTypePair', 'ProjectArchetype', 'ProjectArchetypeRealType', 'ProjectArchetypeStyle', 'ProjectArchetypeType', 'ProjectAssigneeType', 'ProjectAvatars', 'ProjectCategory', 'ProjectComponent', 'ProjectComponentAssigneeType', 'ProjectComponentRealAssigneeType', 'ProjectCreateResourceIdentifier', 'ProjectCreateResourceIdentifierType', 'ProjectCustomTemplateCreateRequestDto', 'ProjectDataPolicies', 'ProjectDataPolicy', 'ProjectDetails', 'ProjectDetailsProjectTypeKey', 'ProjectEmailAddress', 'ProjectFeature', 'ProjectFeatureState', 'ProjectFieldBean', 'ProjectId', 'ProjectIdentifierBean', 'ProjectIdentifiers', 'ProjectIds', 'ProjectInsight', 'ProjectIssueCreateMetadata', 'ProjectIssueSecurityLevels', 'ProjectIssueTypeHierarchy', 'ProjectIssueTypeMapping', 'ProjectIssueTypeMappings', 'ProjectIssueTypeQueryContext', 'ProjectIssueTypesHierarchyLevel', 'ProjectLandingPageInfo', 'ProjectPayload', 'ProjectPayloadProjectTypeKey', 'ProjectPermissions', 'ProjectPinAction', 'ProjectPinActionAction', 'ProjectProjectTypeKey', 'ProjectResult', 'ProjectRole', 'ProjectRoleActorsUpdateBean', 'ProjectRoleDetails', 'ProjectRoleDetailsType', 'ProjectRoleGroup', 'ProjectRoleUser', 'ProjectScopeBean', 'ProjectScopeBeanAttributesItem', 'ProjectStyle', 'ProjectTemplateKey', 'ProjectTemplateModel', 'ProjectTemplateModelType', 'ProjectType', 'ProjectUsage', 'ProjectUsagePage', 'ProjectWithDataPolicy', 'PropertyKey', 'PropertyKeys', 'PublishDraftWorkflowScheme', 'PublishedWorkflowId', 'QuickFilterPayload', 'RedactionJobStatusResponse', 'RedactionJobStatusResponseJobStatus', 'RedactionPosition', 'RegisteredWebhook', 'RemoteIssueLink', 'RemoteIssueLinkIdentifies', 'RemoteIssueLinkRequest', 'RemoteObject', 'RemoveFieldAssociationsRequestItem', 'RemoveOptionFromIssuesResult', 'ReorderIssuePriorities', 'ReorderIssueResolutionsRequest', 'RequiredMappingByIssueType', 'RequiredMappingByWorkflows', 'Resolution', 'ResolutionId', 'ResolutionJsonBean', 'RestrictedPermission', 'RoleActor', 'RoleActorType', 'RolePayload', 'RolePayloadOnConflict', 'RolePayloadType', 'RolesCapabilityPayload', 'RuleConfiguration', 'RulePayload', 'SanitizedJqlQueries', 'SanitizedJqlQuery', 'SaveProjectTemplateRequest', 'SaveProjectTemplateRequestTemplateType', 'SaveTemplateRequest', 'SaveTemplateResponse', 'Scope', 'ScopePayload', 'ScopePayloadType', 'ScopeType', 'Screen', 'ScreenDetails', 'ScreenPayload', 'ScreenScheme', 'ScreenSchemeDetails', 'ScreenSchemeId', 'ScreenSchemePayload', 'ScreenTypes', 'ScreenWithTab', 'ScreenableField', 'ScreenableTab', 'SearchAndReconcileRequestBean', 'SearchAndReconcileResults', 'SearchAutoCompleteFilter', 'SearchProjectsAction', 'SearchProjectsOrderBy', 'SearchProjectsStatusItem', 'SearchResultFieldParameters', 'SearchResultWorkTypeParameters', 'SearchWarning', 'SearchWarningLimitDetails', 'SecurityLevel', 'SecurityLevelMember', 'SecurityLevelMemberPayload', 'SecurityLevelMemberPayloadType', 'SecurityLevelPayload', 'SecurityScheme', 'SecuritySchemeId', 'SecuritySchemeLevelBean', 'SecuritySchemeLevelMemberBean', 'SecuritySchemeMembersRequest', 'SecuritySchemePayload', 'SecuritySchemeWithProjects', 'SecuritySchemes', 'ServerInformation', 'ServiceRegistry', 'ServiceRegistryTier', 'SetDefaultLevelsRequest', 'SetDefaultPriorityRequest', 'SetDefaultResolutionRequest', 'SetProjectPoliciesRequest', 'SharePermission', 'SharePermissionInputBean', 'SharePermissionInputBeanType', 'SharePermissionType', 'SimpleApplicationPropertyBean', 'SimpleErrorCollection', 'SimpleLink', 'SimpleListWrapperApplicationRole', 'SimpleListWrapperGroupName', 'SimplifiedHierarchyLevel', 'SimplifiedIssueTransition', 'SingleRedactionRequest', 'SingleRedactionResponse', 'StatePolicyDocument', 'StatePolicyRule', 'Status', 'StatusCategory', 'StatusCreate', 'StatusCreateRequest', 'StatusCreateStatusCategory', 'StatusDetails', 'StatusLayoutUpdate', 'StatusMapping', 'StatusMappingDto', 'StatusMetadata', 'StatusMetadataCategory', 'StatusMigration', 'StatusPayload', 'StatusPayloadOnConflict', 'StatusPayloadScope', 'StatusPayloadStatusCategory', 'StatusProjectIssueTypeUsage', 'StatusProjectIssueTypeUsageDto', 'StatusProjectIssueTypeUsagePage', 'StatusProjectUsage', 'StatusProjectUsageDto', 'StatusProjectUsagePage', 'StatusScope', 'StatusScopeType', 'StatusUpdate', 'StatusUpdateRequest', 'StatusUpdateStatusCategory', 'StatusWorkflowUsageDto', 'StatusWorkflowUsagePage', 'StatusWorkflowUsageWorkflow', 'StatusesPerWorkflow', 'StoreAvatarType', 'StreamingResponseBody', 'StringList', 'SubmittedBulkOperation', 'SuggestedIssue', 'SuggestedMappingsForPrioritiesRequestBean', 'SuggestedMappingsForProjectsRequestBean', 'SuggestedMappingsRequestBean', 'SwimlanePayload', 'SwimlanesPayload', 'SwimlanesPayloadSwimlaneStrategy', 'SystemAvatars', 'TabPayload', 'TargetClassification', 'TargetMandatoryFields', 'TargetStatus', 'TargetToSourcesMapping', 'TaskProgress', 'TaskProgressBeanJsonNode', 'TaskProgressBeanJsonNodeStatus', 'TaskProgressBeanObject', 'TaskProgressBeanObjectStatus', 'TaskProgressBeanRemoveOptionFromIssuesResult', 'TaskProgressBeanRemoveOptionFromIssuesResultStatus', 'TaskProgressStatus', 'TimeTrackingConfiguration', 'TimeTrackingConfigurationDefaultUnit', 'TimeTrackingConfigurationTimeFormat', 'TimeTrackingDetails', 'TimeTrackingProvider', 'ToLayoutPayload', 'Transition', 'TransitionLink', 'TransitionPayload', 'TransitionPayloadType', 'TransitionPreview', 'TransitionPreviewType', 'TransitionScreenDetails', 'TransitionType', 'TransitionUpdateDto', 'TransitionUpdateDtoType', 'Transitions', 'UiModificationContextDetails', 'UiModificationContextDetailsViewType', 'UiModificationDetails', 'UiModificationIdentifiers', 'UnrestrictedUserEmail', 'UpdateCustomFieldDetails', 'UpdateCustomFieldDetailsSearcherKey', 'UpdateDefaultProjectClassificationBean', 'UpdateDefaultScreenScheme', 'UpdateFieldAssociationSchemeLinksBean', 'UpdateFieldAssociationSchemeRequest', 'UpdateFieldAssociationSchemeResponse', 'UpdateFieldAssociationsRequestItem', 'UpdateFieldConfigurationSchemeDetails', 'UpdateFieldSchemeParametersPartialFailure', 'UpdateFieldSchemeParametersRequest', 'UpdateFieldSchemeParametersResponse', 'UpdateIssueSecurityLevelDetails', 'UpdateIssueSecuritySchemeRequestBean', 'UpdateNotificationSchemeDetails', 'UpdatePrioritiesInSchemeRequestBean', 'UpdatePriorityDetails', 'UpdatePriorityDetailsIconUrl', 'UpdatePrioritySchemeRequestBean', 'UpdatePrioritySchemeResponseBean', 'UpdateProjectDetails', 'UpdateProjectDetailsAssigneeType', 'UpdateProjectsInSchemeRequestBean', 'UpdateResolutionDetails', 'UpdateScreenDetails', 'UpdateScreenSchemeDetails', 'UpdateScreenTypes', 'UpdateUiModificationDetails', 'UpdateUserToGroupBean', 'UpdateWorklogAdjustEstimate', 'UpdatedProjectCategory', 'User', 'UserAccountType', 'UserBean', 'UserBeanAvatarUrls', 'UserColumnRequestBody', 'UserContextVariable', 'UserDetails', 'UserFilter', 'UserKey', 'UserList', 'UserMigrationBean', 'UserPermission', 'UserPermissionType', 'UserPickerUser', 'UserPickerUserAccountType', 'ValidatePolicyRequest', 'ValidationOptionsForCreate', 'ValidationOptionsForCreateLevelsItem', 'ValidationOptionsForUpdate', 'ValidationOptionsForUpdateLevelsItem', 'ValueOperand', 'Version', 'VersionApprover', 'VersionIssueCounts', 'VersionIssuesStatus', 'VersionMoveBean', 'VersionMoveBeanPosition', 'VersionRelatedWork', 'VersionUnresolvedIssuesCount', 'VersionUsageInCustomField', 'Visibility', 'VisibilityType', 'Votes', 'WarningCollection', 'Watchers', 'Webhook', 'WebhookDetails', 'WebhookDetailsEventsItem', 'WebhookEventsItem', 'WebhookRegistrationDetails', 'WebhooksExpirationDate', 'WorkTypeParameters', 'Workflow', 'WorkflowAssociationStatusMapping', 'WorkflowCapabilities', 'WorkflowCapabilitiesEditorScope', 'WorkflowCapabilitiesProjectTypesItem', 'WorkflowCapabilityPayload', 'WorkflowCompoundCondition', 'WorkflowCompoundConditionOperator', 'WorkflowCondition', 'WorkflowCopyRequest', 'WorkflowCreate', 'WorkflowCreateRequest', 'WorkflowCreateResponse', 'WorkflowCreateValidateRequest', 'WorkflowDocumentDto', 'WorkflowDocumentStatusDto', 'WorkflowDocumentVersionBean', 'WorkflowElementReference', 'WorkflowHistoryItemDto', 'WorkflowHistoryListRequest', 'WorkflowHistoryListResponseDto', 'WorkflowHistoryReadRequest', 'WorkflowHistoryReadResponseDto', 'WorkflowId', 'WorkflowLayout', 'WorkflowMetadataAndIssueTypeRestModel', 'WorkflowMetadataRestModel', 'WorkflowOperations', 'WorkflowPayload', 'WorkflowPayloadOnConflict', 'WorkflowPreview', 'WorkflowPreviewLayout', 'WorkflowPreviewRequest', 'WorkflowPreviewResponse', 'WorkflowPreviewScope', 'WorkflowPreviewScopeType', 'WorkflowPreviewStatus', 'WorkflowProjectIdScope', 'WorkflowProjectIssueTypeUsage', 'WorkflowProjectIssueTypeUsageDto', 'WorkflowProjectIssueTypeUsagePage', 'WorkflowProjectUsageDto', 'WorkflowReadRequest', 'WorkflowReadResponse', 'WorkflowReferenceStatus', 'WorkflowRuleConfiguration', 'WorkflowRules', 'WorkflowRulesSearch', 'WorkflowRulesSearchDetails', 'WorkflowScheme', 'WorkflowSchemeAssociation', 'WorkflowSchemeAssociations', 'WorkflowSchemeIdName', 'WorkflowSchemePayload', 'WorkflowSchemePayloadOnConflict', 'WorkflowSchemeProjectAssociation', 'WorkflowSchemeProjectSwitchBean', 'WorkflowSchemeProjectUsageDto', 'WorkflowSchemeReadRequest', 'WorkflowSchemeReadResponse', 'WorkflowSchemeUpdateRequest', 'WorkflowSchemeUpdateRequiredMappingsRequest', 'WorkflowSchemeUpdateRequiredMappingsResponse', 'WorkflowSchemeUsage', 'WorkflowSchemeUsageDto', 'WorkflowSchemeUsagePage', 'WorkflowScope', 'WorkflowScopeType', 'WorkflowSearchResponse', 'WorkflowSimpleCondition', 'WorkflowStatus', 'WorkflowStatusLayout', 'WorkflowStatusLayoutPayload', 'WorkflowStatusPayload', 'WorkflowStatusUpdate', 'WorkflowStatusUpdateStatusCategory', 'WorkflowTransition', 'WorkflowTransitionLinks', 'WorkflowTransitionRule', 'WorkflowTransitionRules', 'WorkflowTransitionRulesDetails', 'WorkflowTransitionRulesUpdate', 'WorkflowTransitionRulesUpdateErrorDetails', 'WorkflowTransitionRulesUpdateErrors', 'WorkflowTransitions', 'WorkflowTransitionsType', 'WorkflowTrigger', 'WorkflowUpdate', 'WorkflowUpdateRequest', 'WorkflowUpdateResponse', 'WorkflowUpdateValidateRequestBean', 'WorkflowValidationError', 'WorkflowValidationErrorLevel', 'WorkflowValidationErrorList', 'WorkflowValidationErrorType', 'WorkflowsWithTransitionRulesDetails', 'WorkingDaysConfig', 'Worklog', 'WorklogCompositeKey', 'WorklogIdsRequestBean', 'WorklogKeyResult', 'WorklogsMoveRequestBean', 'WorkspaceDataPolicy']

ActorInputBean = TypedDict(
    'ActorInputBean',
    {
    'group': NotRequired["list[str]"],
    'group_id': NotRequired["list[str]"],
    'user': NotRequired["list[str]"],
    },
)

ActorsMap = TypedDict(
    'ActorsMap',
    {
    'group': NotRequired["list[str]"],
    'group_id': NotRequired["list[str]"],
    'user': NotRequired["list[str]"],
    },
)

AddAtlassianTeamRequest = TypedDict(
    'AddAtlassianTeamRequest',
    {
    'capacity': NotRequired["float"],
    'id': "str",
    'issue_source_id': NotRequired["int"],
    'planning_style': "AddAtlassianTeamRequestPlanningStyle",
    'sprint_length': NotRequired["int"],
    },
)

type AddAtlassianTeamRequestPlanningStyle = Literal['Scrum', 'Kanban']
"""The planning style for the Atlassian team. This must be "Scrum" or "Kanban"."""

AddFieldBean = TypedDict(
    'AddFieldBean',
    {
    'field_id': "str",
    },
)

AddGroupBean = TypedDict(
    'AddGroupBean',
    {
    'name': "str",
    },
)

AddIssueTypesToContext = TypedDict(
    'AddIssueTypesToContext',
    {
    'default_value': NotRequired["CustomFieldContextDefaultValue"],
    'is_any_issue_type': NotRequired["bool"],
    'issue_type_ids': NotRequired["list[str | None] | None"],
    },
)

AddNotificationsDetails = TypedDict(
    'AddNotificationsDetails',
    {
    'notification_scheme_events': "list[NotificationSchemeEventDetails]",
    },
)
"""Details of notifications which should be added to the notification scheme."""

AddSecuritySchemeLevelsRequestBean = TypedDict(
    'AddSecuritySchemeLevelsRequestBean',
    {
    'levels': NotRequired["list[SecuritySchemeLevelBean]"],
    },
)

type AddWorklogAdjustEstimate = Literal['new', 'leave', 'manual', 'auto']

type AnalyseExpressionCheck = Literal['syntax', 'type', 'complexity']

AnnouncementBannerConfiguration = TypedDict(
    'AnnouncementBannerConfiguration',
    {
    'hash_id': NotRequired["str"],
    'is_dismissible': NotRequired["bool"],
    'is_enabled': NotRequired["bool"],
    'message': NotRequired["str"],
    'visibility': NotRequired["AnnouncementBannerConfigurationVisibility"],
    },
)
"""Announcement banner configuration."""

AnnouncementBannerConfigurationUpdate = TypedDict(
    'AnnouncementBannerConfigurationUpdate',
    {
    'is_dismissible': NotRequired["bool"],
    'is_enabled': NotRequired["bool"],
    'message': NotRequired["str"],
    'visibility': NotRequired["str"],
    },
)
"""Configuration of the announcement banner."""

type AnnouncementBannerConfigurationVisibility = Literal['public', 'private']
"""Visibility of the announcement banner."""

AppWorkflowTransitionRule = TypedDict(
    'AppWorkflowTransitionRule',
    {
    'configuration': "RuleConfiguration",
    'id': "str",
    'key': "str",
    'transition': NotRequired["WorkflowTransition"],
    },
)
"""A workflow transition rule."""

Application = TypedDict(
    'Application',
    {
    'name': NotRequired["str"],
    'type': NotRequired["str"],
    },
)
"""The application the linked item is in."""

ApplicationProperty = TypedDict(
    'ApplicationProperty',
    {
    'allowed_values': NotRequired["list[str]"],
    'default_value': NotRequired["str"],
    'desc': NotRequired["str"],
    'example': NotRequired["str"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""Details of an application property."""

ApplicationRole = TypedDict(
    'ApplicationRole',
    {
    'default_groups': NotRequired["list[str]"],
    'default_groups_details': NotRequired["list[GroupName]"],
    'defined': NotRequired["bool"],
    'group_details': NotRequired["list[GroupName]"],
    'groups': NotRequired["list[str]"],
    'has_unlimited_seats': NotRequired["bool"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'number_of_seats': NotRequired["int"],
    'platform': NotRequired["bool"],
    'remaining_seats': NotRequired["int"],
    'selected_by_default': NotRequired["bool"],
    'user_count': NotRequired["int"],
    'user_count_description': NotRequired["str"],
    },
)
"""Details of an application role."""

ApprovalConfiguration = TypedDict(
    'ApprovalConfiguration',
    {
    'active': "ApprovalConfigurationActive",
    'condition_type': "ApprovalConfigurationConditionType",
    'condition_value': "str",
    'exclude': NotRequired["list[ApprovalConfigurationExcludeItem | None] | None"],
    'field_id': "str",
    'pre_populated_field_id': NotRequired["str | None"],
    'transition_approved': "str",
    'transition_rejected': "str",
    },
)
"""The approval configuration of a status within a workflow. Applies only to Jira Service Management approvals."""

type ApprovalConfigurationActive = Literal['true', 'false']
"""Whether the approval configuration is active."""

type ApprovalConfigurationConditionType = Literal['number', 'percent', 'numberPerPrincipal']
"""How the required approval count is calculated. It may be configured to require a specific number of approvals, or approval by a percentage of approvers. If the approvers source field is Approver groups, you can configure how many approvals per group are required for the request to be approved. The number will be the same across all groups."""

type ApprovalConfigurationExcludeItem = Literal['assignee', 'reporter']
"""A list of roles that should be excluded as possible approvers."""

ApprovalConfigurationPreview = TypedDict(
    'ApprovalConfigurationPreview',
    {
    'active': NotRequired["str"],
    'transition_approved': NotRequired["str"],
    'transition_rejected': NotRequired["str"],
    },
)
"""Approval configuration."""

ArchiveIssueAsyncRequest = TypedDict(
    'ArchiveIssueAsyncRequest',
    {
    'jql': NotRequired["str"],
    },
)

ArchivedIssuesFilterRequest = TypedDict(
    'ArchivedIssuesFilterRequest',
    {
    'archived_by': NotRequired["list[str]"],
    'archived_date_range': NotRequired["DateRangeFilterRequest"],
    'issue_types': NotRequired["list[str]"],
    'projects': NotRequired["list[str]"],
    'reporters': NotRequired["list[str]"],
    },
)
"""Details of a filter for exporting archived issues."""

AssociateFieldConfigurationsWithIssueTypesRequest = TypedDict(
    'AssociateFieldConfigurationsWithIssueTypesRequest',
    {
    'mappings': "list[FieldConfigurationToIssueTypeMapping]",
    },
)
"""Details of a field configuration to issue type mappings."""

AssociateSecuritySchemeWithProjectDetails = TypedDict(
    'AssociateSecuritySchemeWithProjectDetails',
    {
    'old_to_new_security_level_mappings': NotRequired["list[OldToNewSecurityLevelMappingsBean]"],
    'project_id': "str",
    'scheme_id': "str",
    },
)
"""Issue security scheme, project, and remapping details."""

AssociatedItemBean = TypedDict(
    'AssociatedItemBean',
    {
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_name': NotRequired["str"],
    'type_name': NotRequired["str"],
    },
)
"""Details of an item associated with the changed record."""

AssociationContextObject = TypedDict(
    'AssociationContextObject',
    {
    'identifier': NotRequired["dict[str, Any]"],
    'type': "str",
    },
)
"""Field association for example PROJECT\\_ID."""

Attachment = TypedDict(
    'Attachment',
    {
    'author': NotRequired["UserDetails"],
    'content': NotRequired["str"],
    'created': NotRequired["str"],
    'filename': NotRequired["str"],
    'id': NotRequired["str"],
    'mime_type': NotRequired["str"],
    'self': NotRequired["str"],
    'size': NotRequired["int"],
    'thumbnail': NotRequired["str"],
    },
)
"""Details about an attachment."""

AttachmentArchiveEntry = TypedDict(
    'AttachmentArchiveEntry',
    {
    'abbreviated_name': NotRequired["str"],
    'entry_index': NotRequired["int"],
    'media_type': NotRequired["str"],
    'name': NotRequired["str"],
    'size': NotRequired["int"],
    },
)

AttachmentArchiveImpl = TypedDict(
    'AttachmentArchiveImpl',
    {
    'entries': NotRequired["list[AttachmentArchiveEntry]"],
    'total_entry_count': NotRequired["int"],
    },
)

AttachmentArchiveItemReadable = TypedDict(
    'AttachmentArchiveItemReadable',
    {
    'index': NotRequired["int"],
    'label': NotRequired["str"],
    'media_type': NotRequired["str"],
    'path': NotRequired["str"],
    'size': NotRequired["str"],
    },
)
"""Metadata for an item in an attachment archive."""

AttachmentArchiveMetadataReadable = TypedDict(
    'AttachmentArchiveMetadataReadable',
    {
    'entries': NotRequired["list[AttachmentArchiveItemReadable]"],
    'id': NotRequired["int"],
    'media_type': NotRequired["str"],
    'name': NotRequired["str"],
    'total_entry_count': NotRequired["int"],
    },
)
"""Metadata for an archive (for example a zip) and its contents."""

AttachmentMetadata = TypedDict(
    'AttachmentMetadata',
    {
    'author': NotRequired["User"],
    'content': NotRequired["str"],
    'created': NotRequired["str"],
    'filename': NotRequired["str"],
    'id': NotRequired["int"],
    'mime_type': NotRequired["str"],
    'properties': NotRequired["dict[str, Any]"],
    'self': NotRequired["str"],
    'size': NotRequired["int"],
    'thumbnail': NotRequired["str"],
    },
)
"""Metadata for an issue attachment."""

AttachmentSettings = TypedDict(
    'AttachmentSettings',
    {
    'enabled': NotRequired["bool"],
    'upload_limit': NotRequired["int"],
    },
)
"""Details of the instance's attachment settings."""

AuditEntry = TypedDict(
    'AuditEntry',
    {
    'caller': NotRequired["str"],
    'created_at': NotRequired["str"],
    'filter_id': NotRequired["str"],
    'jql': NotRequired["str"],
    'request_url': NotRequired["str"],
    'user': NotRequired["AuditUser"],
    'user_agent': NotRequired["str"],
    'validation_message': NotRequired["str"],
    },
)

AuditPage = TypedDict(
    'AuditPage',
    {
    'entries': NotRequired["list[AuditEntry]"],
    'is_last': NotRequired["bool"],
    'next_page_token': NotRequired["str"],
    'next_page_url': NotRequired["str"],
    },
)

AuditRecordBean = TypedDict(
    'AuditRecordBean',
    {
    'associated_items': NotRequired["list[AssociatedItemBean]"],
    'author_key': NotRequired["str"],
    'category': NotRequired["str"],
    'changed_values': NotRequired["list[ChangedValueBean]"],
    'created': NotRequired["str"],
    'description': NotRequired["str"],
    'event_source': NotRequired["str"],
    'id': NotRequired["int"],
    'object_item': NotRequired["AssociatedItemBean"],
    'remote_address': NotRequired["str"],
    'summary': NotRequired["str"],
    },
)
"""An audit record."""

AuditRecords = TypedDict(
    'AuditRecords',
    {
    'limit': NotRequired["int"],
    'offset': NotRequired["int"],
    'records': NotRequired["list[AuditRecordBean]"],
    'total': NotRequired["int"],
    },
)
"""Container for a list of audit records."""

AuditUser = TypedDict(
    'AuditUser',
    {
    'account_id': NotRequired["str"],
    'active': NotRequired["bool"],
    'avatar_urls': NotRequired["AuditUserAvatarUrls"],
    'display_name': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)

AuditUserAvatarUrls = TypedDict(
    'AuditUserAvatarUrls',
    {
    'n16_x_16': NotRequired["str"],
    'n24_x_24': NotRequired["str"],
    'n32_x_32': NotRequired["str"],
    'n48_x_48': NotRequired["str"],
    },
)

AutoCompleteSuggestion = TypedDict(
    'AutoCompleteSuggestion',
    {
    'display_name': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""A field auto-complete suggestion."""

AutoCompleteSuggestions = TypedDict(
    'AutoCompleteSuggestions',
    {
    'results': NotRequired["list[AutoCompleteSuggestion]"],
    },
)
"""The results from a JQL query."""

AvailableDashboardGadget = TypedDict(
    'AvailableDashboardGadget',
    {
    'module_key': NotRequired["str"],
    'title': "str",
    'uri': NotRequired["str"],
    },
)
"""The details of the available dashboard gadget."""

AvailableDashboardGadgetsResponse = TypedDict(
    'AvailableDashboardGadgetsResponse',
    {
    'gadgets': "list[AvailableDashboardGadget]",
    },
)
"""The list of available gadgets."""

AvailableWorkflowConnectRule = TypedDict(
    'AvailableWorkflowConnectRule',
    {
    'addon_key': NotRequired["str"],
    'create_url': NotRequired["str"],
    'description': NotRequired["str"],
    'edit_url': NotRequired["str"],
    'module_key': NotRequired["str"],
    'name': NotRequired["str"],
    'rule_key': NotRequired["str"],
    'rule_type': NotRequired["AvailableWorkflowConnectRuleRuleType"],
    'view_url': NotRequired["str"],
    },
)
"""The Connect provided ecosystem rules available."""

type AvailableWorkflowConnectRuleRuleType = Literal['Condition', 'Validator', 'Function', 'Screen']
"""The rule type."""

AvailableWorkflowForgeRule = TypedDict(
    'AvailableWorkflowForgeRule',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'rule_key': NotRequired["str"],
    'rule_type': NotRequired["AvailableWorkflowForgeRuleRuleType"],
    },
)
"""The Forge provided ecosystem rules available."""

type AvailableWorkflowForgeRuleRuleType = Literal['Condition', 'Validator', 'Function', 'Screen']
"""The rule type."""

AvailableWorkflowSystemRule = TypedDict(
    'AvailableWorkflowSystemRule',
    {
    'description': "str",
    'incompatible_rule_keys': "list[str]",
    'is_available_for_initial_transition': "bool",
    'is_visible': "bool",
    'name': "str",
    'rule_key': "str",
    'rule_type': "AvailableWorkflowSystemRuleRuleType",
    },
)
"""The Atlassian provided system rules available."""

type AvailableWorkflowSystemRuleRuleType = Literal['Condition', 'Validator', 'Function', 'Screen']
"""The rule type."""

AvailableWorkflowTriggerTypes = TypedDict(
    'AvailableWorkflowTriggerTypes',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["str"],
    },
)
"""The list of available trigger types."""

AvailableWorkflowTriggers = TypedDict(
    'AvailableWorkflowTriggers',
    {
    'available_types': "list[AvailableWorkflowTriggerTypes]",
    'rule_key': "str",
    },
)
"""The trigger rules available."""

Avatar = TypedDict(
    'Avatar',
    {
    'file_name': NotRequired["str"],
    'id': "str",
    'is_deletable': NotRequired["bool"],
    'is_selected': NotRequired["bool"],
    'is_system_avatar': NotRequired["bool"],
    'owner': NotRequired["str"],
    'urls': NotRequired["dict[str, str]"],
    },
)
"""Details of an avatar."""

AvatarUrlsBean = TypedDict(
    'AvatarUrlsBean',
    {
    'n16_x_16': NotRequired["str"],
    'n24_x_24': NotRequired["str"],
    'n32_x_32': NotRequired["str"],
    'n48_x_48': NotRequired["str"],
    },
)

Avatars = TypedDict(
    'Avatars',
    {
    'custom': NotRequired["list[Avatar]"],
    'system': NotRequired["list[Avatar]"],
    },
)
"""Details about system and custom avatars."""

BoardColumnPayload = TypedDict(
    'BoardColumnPayload',
    {
    'maximum_issue_constraint': NotRequired["int"],
    'minimum_issue_constraint': NotRequired["int"],
    'name': NotRequired["str"],
    'status_ids': NotRequired["list[ProjectCreateResourceIdentifier]"],
    },
)
"""The payload for creating a board column"""

BoardFeaturePayload = TypedDict(
    'BoardFeaturePayload',
    {
    'feature_key': NotRequired["BoardFeaturePayloadFeatureKey"],
    'state': NotRequired["bool"],
    },
)
"""The payload for setting a board feature"""

type BoardFeaturePayloadFeatureKey = Literal['ESTIMATION', 'SPRINTS']
"""The key of the feature"""

BoardFeaturesPayload = TypedDict(
    'BoardFeaturesPayload',
    {
    'board_features': NotRequired["dict[str, list[BoardFeaturePayload]]"],
    },
)
"""Configuration of features for one or more boards. Replaces the deprecated features field on BoardPayload"""

BoardPayload = TypedDict(
    'BoardPayload',
    {
    'board_filter_jql': NotRequired["str"],
    'card_color_strategy': NotRequired["BoardPayloadCardColorStrategy"],
    'card_layout': NotRequired["CardLayout"],
    'card_layouts': NotRequired["list[CardLayoutField]"],
    'columns': NotRequired["list[BoardColumnPayload]"],
    'enable_card_cover': NotRequired["bool"],
    'features': NotRequired["list[BoardFeaturePayload]"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'quick_filters': NotRequired["list[QuickFilterPayload]"],
    'supports_sprint': NotRequired["bool"],
    'swimlanes': NotRequired["SwimlanesPayload"],
    'working_days_config': NotRequired["WorkingDaysConfig"],
    },
)
"""The payload for creating a board"""

type BoardPayloadCardColorStrategy = Literal['ISSUE_TYPE', 'REQUEST_TYPE', 'ASSIGNEE', 'PRIORITY', 'NONE', 'CUSTOM']
"""Card color settings of the board"""

BoardsPayload = TypedDict(
    'BoardsPayload',
    {
    'boards': NotRequired["list[BoardPayload]"],
    },
)

BulkAgentSessionInvocation = TypedDict(
    'BulkAgentSessionInvocation',
    {
    'agent_id': "str",
    'issue_id': "str",
    'request_id': "str",
    'user_prompt': NotRequired["str | None"],
    },
)
"""One agent-session invocation for an issue."""

BulkAgentSessionItemError = TypedDict(
    'BulkAgentSessionItemError',
    {
    'message': NotRequired["str"],
    'status_code': NotRequired["int"],
    'type': NotRequired["BulkAgentSessionItemErrorType"],
    },
)
"""An item-level error inside an HTTP 200 response."""

type BulkAgentSessionItemErrorType = Literal['AGENT_NOT_ASSIGNABLE', 'AGENT_NOT_FOUND', 'INVALID_REQUEST_ID', 'ISSUE_NOT_FOUND', 'IDEMPOTENCY_CONFLICT', 'ISSUE_VERSION_MISSING', 'ISSUE_ACCESS_DENIED', 'RATE_LIMITED', 'CONCURRENCY_SATURATED', 'AGENT_TRIGGER_FAILED', 'IDEMPOTENCY_ERROR', 'PRIOR_ATTEMPT_FAILED', 'SESSION_NOT_STARTED', 'IN_DOUBT', 'UNEXPECTED_ERROR']
"""Error type."""

BulkAgentSessionOutcome = TypedDict(
    'BulkAgentSessionOutcome',
    {
    'agent_id': NotRequired["str"],
    'conversation_id': NotRequired["str | None"],
    'error': NotRequired["BulkAgentSessionItemError | None"],
    'issue_id': NotRequired["str"],
    'request_id': NotRequired["str"],
    'result': NotRequired["BulkAgentSessionOutcomeResult"],
    },
)
"""The start outcome for one invocation."""

type BulkAgentSessionOutcomeResult = Literal['STARTED', 'ALREADY_STARTED', 'FAILED', 'RATE_LIMITED', 'IN_DOUBT']
"""STARTED: session started; ALREADY\\_STARTED: recorded successful retry; FAILED: invocation failed; RATE\\_LIMITED: admission denied; IN\\_DOUBT: start could not be confirmed."""

BulkAgentSessionsResponse = TypedDict(
    'BulkAgentSessionsResponse',
    {
    'already_started_count': NotRequired["int"],
    'failed_count': NotRequired["int"],
    'rate_limited_count': NotRequired["int"],
    'results': NotRequired["list[BulkAgentSessionOutcome]"],
    'started_count': NotRequired["int"],
    'success': NotRequired["bool"],
    },
)
"""Session-start outcomes, not completion of the agent's work."""

BulkChangeOwnerDetails = TypedDict(
    'BulkChangeOwnerDetails',
    {
    'autofix_name': "bool",
    'new_owner': "str",
    },
)
"""Details for changing owners of shareable entities"""

BulkChangelogRequestBean = TypedDict(
    'BulkChangelogRequestBean',
    {
    'field_ids': NotRequired["list[str]"],
    'issue_ids_or_keys': "list[str]",
    'max_results': NotRequired["int"],
    'next_page_token': NotRequired["str"],
    },
)
"""Request bean for bulk changelog retrieval"""

BulkChangelogResponseBean = TypedDict(
    'BulkChangelogResponseBean',
    {
    'issue_change_logs': NotRequired["list[IssueChangeLog]"],
    'next_page_token': NotRequired["str"],
    },
)
"""A page of changelogs which is designed to handle multiple issues"""

BulkContextualConfiguration = TypedDict(
    'BulkContextualConfiguration',
    {
    'configuration': NotRequired["Any"],
    'custom_field_id': "str",
    'field_context_id': "str",
    'id': "str",
    'schema': NotRequired["Any"],
    },
)
"""Details of the contextual configuration for a custom field."""

BulkCustomFieldOptionCreateRequest = TypedDict(
    'BulkCustomFieldOptionCreateRequest',
    {
    'options': NotRequired["list[CustomFieldOptionCreate]"],
    },
)
"""Details of the options to create for a custom field."""

BulkCustomFieldOptionUpdateRequest = TypedDict(
    'BulkCustomFieldOptionUpdateRequest',
    {
    'options': NotRequired["list[CustomFieldOptionUpdate]"],
    },
)
"""Details of the options to update for a custom field."""

type BulkDeleteWorklogsAdjustEstimate = Literal['leave', 'auto']

BulkEditActionError = TypedDict(
    'BulkEditActionError',
    {
    'error_messages': "list[str]",
    'errors': "dict[str, str]",
    },
)
"""Errors of bulk edit action."""

BulkEditGetFields = TypedDict(
    'BulkEditGetFields',
    {
    'ending_before': NotRequired["str"],
    'fields': NotRequired["list[IssueBulkEditField]"],
    'starting_after': NotRequired["str"],
    },
)
"""Bulk Edit Get Fields Response."""

BulkEditShareableEntityRequest = TypedDict(
    'BulkEditShareableEntityRequest',
    {
    'action': "BulkEditShareableEntityRequestAction",
    'change_owner_details': NotRequired["BulkChangeOwnerDetails"],
    'entity_ids': "list[int]",
    'extend_admin_permissions': NotRequired["bool"],
    'permission_details': NotRequired["PermissionDetails"],
    },
)
"""Details of a request to bulk edit shareable entity."""

type BulkEditShareableEntityRequestAction = Literal['changeOwner', 'changePermission', 'addPermission', 'removePermission']
"""Allowed action for bulk edit shareable entity"""

BulkEditShareableEntityResponse = TypedDict(
    'BulkEditShareableEntityResponse',
    {
    'action': "BulkEditShareableEntityResponseAction",
    'entity_errors': NotRequired["dict[str, BulkEditActionError]"],
    },
)
"""Details of a request to bulk edit shareable entity."""

type BulkEditShareableEntityResponseAction = Literal['changeOwner', 'changePermission', 'addPermission', 'removePermission']
"""Allowed action for bulk edit shareable entity"""

BulkFetchIssueRequestBean = TypedDict(
    'BulkFetchIssueRequestBean',
    {
    'expand': NotRequired["list[str]"],
    'fields': NotRequired["list[str]"],
    'fields_by_keys': NotRequired["bool"],
    'issue_ids_or_keys': "list[str]",
    'properties': NotRequired["list[str]"],
    },
)

BulkIssueIsWatching = TypedDict(
    'BulkIssueIsWatching',
    {
    'issues_is_watching': NotRequired["dict[str, bool]"],
    },
)
"""A container for the watch status of a list of issues."""

BulkIssuePropertyUpdateRequest = TypedDict(
    'BulkIssuePropertyUpdateRequest',
    {
    'expression': NotRequired["str"],
    'filter': NotRequired["IssueFilterForBulkPropertySet"],
    'value': NotRequired["Any"],
    },
)
"""Bulk issue property update request details."""

BulkIssueResults = TypedDict(
    'BulkIssueResults',
    {
    'issue_errors': NotRequired["list[IssueError]"],
    'issues': NotRequired["list[IssueBean]"],
    },
)
"""The list of requested issues & fields."""

type BulkMoveWorklogsAdjustEstimate = Literal['leave', 'auto']

BulkOperationErrorResponse = TypedDict(
    'BulkOperationErrorResponse',
    {
    'errors': NotRequired["list[ErrorMessage]"],
    },
)

BulkOperationErrorResult = TypedDict(
    'BulkOperationErrorResult',
    {
    'element_errors': NotRequired["ErrorCollection"],
    'failed_element_number': NotRequired["int"],
    'status': NotRequired["int"],
    },
)

BulkOperationProgress = TypedDict(
    'BulkOperationProgress',
    {
    'created': NotRequired["str"],
    'failed_accessible_issues': NotRequired["dict[str, list[str]]"],
    'invalid_or_inaccessible_issue_count': NotRequired["int"],
    'processed_accessible_issues': NotRequired["list[int]"],
    'progress_percent': NotRequired["int"],
    'started': NotRequired["str"],
    'status': NotRequired["BulkOperationProgressStatus"],
    'submitted_by': NotRequired["User"],
    'task_id': NotRequired["str"],
    'total_issue_count': NotRequired["int"],
    'updated': NotRequired["str"],
    },
)

type BulkOperationProgressStatus = Literal['ENQUEUED', 'RUNNING', 'COMPLETE', 'FAILED', 'CANCEL_REQUESTED', 'CANCELLED', 'DEAD']
"""The status of the task."""

BulkPermissionGrants = TypedDict(
    'BulkPermissionGrants',
    {
    'global_permissions': "list[str]",
    'project_permissions': "list[BulkProjectPermissionGrants]",
    },
)
"""Details of global and project permissions granted to the user."""

BulkPermissionsRequestBean = TypedDict(
    'BulkPermissionsRequestBean',
    {
    'account_id': NotRequired["str"],
    'global_permissions': NotRequired["list[str]"],
    'project_permissions': NotRequired["list[BulkProjectPermissions]"],
    },
)
"""Details of global permissions to look up and project permissions with associated projects and issues to look up."""

BulkPolicyOperationResponse = TypedDict(
    'BulkPolicyOperationResponse',
    {
    'failed': NotRequired["list[ProjectResult]"],
    'successful': NotRequired["list[ProjectResult]"],
    },
)

BulkProjectPermissionGrants = TypedDict(
    'BulkProjectPermissionGrants',
    {
    'issues': "list[int]",
    'permission': "str",
    'projects': "list[int]",
    },
)
"""List of project permissions and the projects and issues those permissions grant access to."""

BulkProjectPermissions = TypedDict(
    'BulkProjectPermissions',
    {
    'issues': NotRequired["list[int]"],
    'permissions': "list[str]",
    'projects': NotRequired["list[int]"],
    },
)
"""Details of project permissions and associated issues and projects to look up."""

BulkProjectPolicyRequest = TypedDict(
    'BulkProjectPolicyRequest',
    {
    'project_ids': NotRequired["list[int]"],
    },
)

BulkRedactionRequest = TypedDict(
    'BulkRedactionRequest',
    {
    'redactions': NotRequired["list[SingleRedactionRequest]"],
    },
)

BulkRedactionResponse = TypedDict(
    'BulkRedactionResponse',
    {
    'results': "list[SingleRedactionResponse]",
    },
)

BulkStartAgentSessionsBatchRequest = TypedDict(
    'BulkStartAgentSessionsBatchRequest',
    {
    'client_mutation_id': "str",
    'invocations': "list[BulkAgentSessionInvocation]",
    },
)
"""A batch of agent-session invocations."""

BulkStartUniformAgentSessionsRequest = TypedDict(
    'BulkStartUniformAgentSessionsRequest',
    {
    'agent_id': "str",
    'client_mutation_id': "str",
    'issue_ids': "list[str]",
    'user_prompt': NotRequired["str | None"],
    },
)
"""Start one agent across multiple issues with a shared optional prompt."""

BulkTransitionGetAvailableTransitions = TypedDict(
    'BulkTransitionGetAvailableTransitions',
    {
    'available_transitions': NotRequired["list[IssueBulkTransitionForWorkflow]"],
    'ending_before': NotRequired["str"],
    'starting_after': NotRequired["str"],
    },
)
"""Bulk Transition Get Available Transitions Response."""

BulkTransitionSubmitInput = TypedDict(
    'BulkTransitionSubmitInput',
    {
    'selected_issue_ids_or_keys': "list[str]",
    'transition_id': "str",
    },
)

BulkWorklogKeyRequestBean = TypedDict(
    'BulkWorklogKeyRequestBean',
    {
    'requests': NotRequired["list[WorklogCompositeKey]"],
    },
)

BulkWorklogKeyResponseBean = TypedDict(
    'BulkWorklogKeyResponseBean',
    {
    'worklogs': NotRequired["list[WorklogKeyResult]"],
    },
)

CardLayout = TypedDict(
    'CardLayout',
    {
    'show_days_in_column': NotRequired["bool"],
    },
)
"""Card layout configuration."""

CardLayoutField = TypedDict(
    'CardLayoutField',
    {
    'field_id': NotRequired["str"],
    'id': NotRequired["int"],
    'mode': NotRequired["CardLayoutFieldMode"],
    'position': NotRequired["int"],
    },
)
"""Card layout settings of the board"""

type CardLayoutFieldMode = Literal['PLAN', 'WORK']

ChangeDetails = TypedDict(
    'ChangeDetails',
    {
    'field': NotRequired["str"],
    'field_id': NotRequired["str"],
    'fieldtype': NotRequired["str"],
    'from': NotRequired["str"],
    'from_string': NotRequired["str"],
    'to': NotRequired["str"],
    'to_string': NotRequired["str"],
    },
)
"""A change item."""

ChangeFilterOwner = TypedDict(
    'ChangeFilterOwner',
    {
    'account_id': "str",
    },
)
"""The account ID of the new owner."""

ChangedValueBean = TypedDict(
    'ChangedValueBean',
    {
    'changed_from': NotRequired["str"],
    'changed_to': NotRequired["str"],
    'field_name': NotRequired["str"],
    },
)
"""Details of names changed in the record event."""

ChangedWorklog = TypedDict(
    'ChangedWorklog',
    {
    'properties': NotRequired["list[EntityProperty]"],
    'updated_time': NotRequired["int"],
    'worklog_id': NotRequired["int"],
    },
)
"""Details of a changed worklog."""

ChangedWorklogs = TypedDict(
    'ChangedWorklogs',
    {
    'last_page': NotRequired["bool"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'since': NotRequired["int"],
    'until': NotRequired["int"],
    'values': NotRequired["list[ChangedWorklog]"],
    },
)
"""List of changed worklogs."""

Changelog = TypedDict(
    'Changelog',
    {
    'author': NotRequired["UserDetails"],
    'created': NotRequired["str"],
    'history_metadata': NotRequired["HistoryMetadata"],
    'id': NotRequired["str"],
    'items': NotRequired["list[ChangeDetails]"],
    },
)
"""A log of changes made to issue fields. Changelogs related to workflow associations are currently being deprecated."""

ColumnItem = TypedDict(
    'ColumnItem',
    {
    'label': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""Details of an issue navigator column item."""

ColumnRequestBody = TypedDict(
    'ColumnRequestBody',
    {
    'columns': NotRequired["list[str]"],
    },
)

Comment = TypedDict(
    'Comment',
    {
    'author': NotRequired["UserDetails"],
    'body': NotRequired["Any"],
    'created': NotRequired["str"],
    'id': NotRequired["str"],
    'jsd_author_can_see_request': NotRequired["bool"],
    'jsd_public': NotRequired["bool"],
    'properties': NotRequired["list[EntityProperty]"],
    'rendered_body': NotRequired["str"],
    'self': NotRequired["str"],
    'update_author': NotRequired["UserDetails"],
    'updated': NotRequired["str"],
    'visibility': NotRequired["Visibility"],
    },
)
"""A comment."""

ComponentIssuesCount = TypedDict(
    'ComponentIssuesCount',
    {
    'issue_count': NotRequired["int"],
    'self': NotRequired["str"],
    },
)
"""Count of issues assigned to a component."""

ComponentJsonBean = TypedDict(
    'ComponentJsonBean',
    {
    'ari': NotRequired["str"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'metadata': NotRequired["dict[str, str]"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)

ComponentWithIssueCount = TypedDict(
    'ComponentWithIssueCount',
    {
    'assignee': NotRequired["User"],
    'assignee_type': NotRequired["ComponentWithIssueCountAssigneeType"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'is_assignee_type_valid': NotRequired["bool"],
    'issue_count': NotRequired["int"],
    'lead': NotRequired["User"],
    'name': NotRequired["str"],
    'project': NotRequired["str"],
    'project_id': NotRequired["int"],
    'real_assignee': NotRequired["User"],
    'real_assignee_type': NotRequired["ComponentWithIssueCountRealAssigneeType"],
    'self': NotRequired["str"],
    },
)
"""Details about a component with a count of the issues it contains."""

type ComponentWithIssueCountAssigneeType = Literal['PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED']
"""
The nominal user type used to determine the assignee for issues created with this component. See `realAssigneeType` for details on how the type of the user, and hence the user, assigned to issues is determined. Takes the following values:

 *  `PROJECT_LEAD` the assignee to any issues created with this component is nominally the lead for the project the component is in.
 *  `COMPONENT_LEAD` the assignee to any issues created with this component is nominally the lead for the component.
 *  `UNASSIGNED` an assignee is not set for issues created with this component.
 *  `PROJECT_DEFAULT` the assignee to any issues created with this component is nominally the default assignee for the project that the component is in.
"""

type ComponentWithIssueCountRealAssigneeType = Literal['PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED']
"""
The type of the assignee that is assigned to issues created with this component, when an assignee cannot be set from the `assigneeType`. For example, `assigneeType` is set to `COMPONENT_LEAD` but no component lead is set. This property is set to one of the following values:

 *  `PROJECT_LEAD` when `assigneeType` is `PROJECT_LEAD` and the project lead has permission to be assigned issues in the project that the component is in.
 *  `COMPONENT_LEAD` when `assignee`Type is `COMPONENT_LEAD` and the component lead has permission to be assigned issues in the project that the component is in.
 *  `UNASSIGNED` when `assigneeType` is `UNASSIGNED` and Jira is configured to allow unassigned issues.
 *  `PROJECT_DEFAULT` when none of the preceding cases are true.
"""

CompoundClause = TypedDict(
    'CompoundClause',
    {
    'clauses': "list[JqlQueryClause]",
    'operator': "CompoundClauseOperator",
    },
)
"""A JQL query clause that consists of nested clauses. For example, `(labels in (urgent, blocker) OR lastCommentedBy = currentUser()). Note that, where nesting is not defined, the parser nests JQL clauses based on the operator precedence. For example, "A OR B AND C" is parsed as "(A OR B) AND C". See Setting the precedence of operators for more information about precedence in JQL queries.`"""

type CompoundClauseOperator = Literal['and', 'or', 'not']
"""The operator between the clauses."""

ConditionGroupConfiguration = TypedDict(
    'ConditionGroupConfiguration',
    {
    'condition_groups': NotRequired["list[ConditionGroupConfiguration | None]"],
    'conditions': NotRequired["list[WorkflowRuleConfiguration | None]"],
    'operation': NotRequired["ConditionGroupConfigurationOperation"],
    },
)
"""The conditions group associated with the transition."""

type ConditionGroupConfigurationOperation = Literal['ANY', 'ALL']
"""Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."""

ConditionGroupPayload = TypedDict(
    'ConditionGroupPayload',
    {
    'condition_group': NotRequired["list[ConditionGroupPayload]"],
    'conditions': NotRequired["list[RulePayload]"],
    'operation': NotRequired["ConditionGroupPayloadOperation"],
    },
)
"""The payload for creating a condition group in a workflow"""

type ConditionGroupPayloadOperation = Literal['ANY', 'ALL']
"""Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."""

ConditionGroupUpdate = TypedDict(
    'ConditionGroupUpdate',
    {
    'condition_groups': NotRequired["list[ConditionGroupUpdate | None]"],
    'conditions': NotRequired["list[WorkflowRuleConfiguration | None]"],
    'operation': "ConditionGroupUpdateOperation",
    },
)
"""The conditions group associated with the transition."""

type ConditionGroupUpdateOperation = Literal['ANY', 'ALL']
"""Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."""

Configuration = TypedDict(
    'Configuration',
    {
    'attachments_enabled': NotRequired["bool"],
    'issue_linking_enabled': NotRequired["bool"],
    'sub_tasks_enabled': NotRequired["bool"],
    'time_tracking_configuration': NotRequired["TimeTrackingConfiguration"],
    'time_tracking_enabled': NotRequired["bool"],
    'unassigned_issues_allowed': NotRequired["bool"],
    'voting_enabled': NotRequired["bool"],
    'watching_enabled': NotRequired["bool"],
    },
)
"""Details about the configuration of Jira."""

ConfigurationsListParameters = TypedDict(
    'ConfigurationsListParameters',
    {
    'field_ids_or_keys': "list[str]",
    },
)
"""List of custom fields identifiers which will be used to filter configurations"""

ConnectCustomFieldValue = TypedDict(
    'ConnectCustomFieldValue',
    {
    'type': "ConnectCustomFieldValueType",
    'field_id': "int",
    'issue_id': "int",
    'number': NotRequired["float"],
    'option_id': NotRequired["str"],
    'rich_text': NotRequired["str"],
    'string': NotRequired["str"],
    'text': NotRequired["str"],
    },
)
"""A list of custom field details."""

type ConnectCustomFieldValueType = Literal['StringIssueField', 'NumberIssueField', 'RichTextIssueField', 'SingleSelectIssueField', 'MultiSelectIssueField', 'TextIssueField']
"""The type of custom field."""

ConnectCustomFieldValues = TypedDict(
    'ConnectCustomFieldValues',
    {
    'update_value_list': NotRequired["list[ConnectCustomFieldValue]"],
    },
)
"""Details of updates for a custom field."""

type ConnectModule = dict[str, Any]
"""
A [Connect module](https://developer.atlassian.com/cloud/jira/platform/about-jira-modules/) in the same format as in the
[app descriptor](https://developer.atlassian.com/cloud/jira/platform/app-descriptor/).
"""

ConnectModules = TypedDict(
    'ConnectModules',
    {
    'modules': "list[ConnectModule]",
    },
)

ContainerForProjectFeatures = TypedDict(
    'ContainerForProjectFeatures',
    {
    'features': NotRequired["list[ProjectFeature]"],
    },
)
"""The list of features on a project."""

ContainerForRegisteredWebhooks = TypedDict(
    'ContainerForRegisteredWebhooks',
    {
    'webhook_registration_result': NotRequired["list[RegisteredWebhook]"],
    },
)
"""Container for a list of registered webhooks. Webhook details are returned in the same order as the request."""

ContainerForWebhookIDs = TypedDict(
    'ContainerForWebhookIDs',
    {
    'webhook_ids': "list[int]",
    },
)
"""Container for a list of webhook IDs."""

ContainerOfWorkflowSchemeAssociations = TypedDict(
    'ContainerOfWorkflowSchemeAssociations',
    {
    'values': "list[WorkflowSchemeAssociations]",
    },
)
"""A container for a list of workflow schemes together with the projects they are associated with."""

ContentItem = TypedDict(
    'ContentItem',
    {
    'entity_id': "str",
    'entity_type': "ContentItemEntityType",
    'id': "str",
    },
)
"""Represents the content to redact"""

type ContentItemEntityType = Literal['issuefieldvalue', 'issue-comment', 'issue-worklog']
"""
The type of the entity to redact; It will be one of the following:

 *  **issuefieldvalue** \\- To redact in issue fields
 *  **issue-comment** \\- To redact in issue comments.
 *  **issue-worklog** \\- To redact in issue worklogs
"""

Context = TypedDict(
    'Context',
    {
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    },
)
"""A context."""

ContextDefaultValues = TypedDict(
    'ContextDefaultValues',
    {
    'context_id': "int",
    'default_values': NotRequired["list[IssueTypeDefaultValue]"],
    },
)
"""Default values grouped by custom field context."""

ContextForProjectAndIssueType = TypedDict(
    'ContextForProjectAndIssueType',
    {
    'context_id': "str",
    'issue_type_id': "str",
    'project_id': "str",
    },
)
"""The project and issue type mapping with a matching custom field context."""

ContextualConfiguration = TypedDict(
    'ContextualConfiguration',
    {
    'configuration': NotRequired["Any"],
    'field_context_id': "str",
    'id': "str",
    'schema': NotRequired["Any"],
    },
)
"""Details of the contextual configuration for a custom field."""

ConvertedJqlQueries = TypedDict(
    'ConvertedJqlQueries',
    {
    'queries_with_unknown_users': NotRequired["list[JqlQueryWithUnknownUsers]"],
    'query_strings': NotRequired["list[str]"],
    },
)
"""The converted JQL queries."""

CreateCrossProjectReleaseRequest = TypedDict(
    'CreateCrossProjectReleaseRequest',
    {
    'name': "str",
    'release_ids': NotRequired["list[int]"],
    },
)

CreateCustomFieldContext = TypedDict(
    'CreateCustomFieldContext',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'issue_type_ids': NotRequired["list[str]"],
    'name': "str",
    'project_ids': NotRequired["list[str]"],
    },
)
"""The details of a created custom field context."""

CreateCustomFieldRequest = TypedDict(
    'CreateCustomFieldRequest',
    {
    'custom_field_id': "int",
    'filter': NotRequired["bool"],
    },
)

CreateDateFieldRequest = TypedDict(
    'CreateDateFieldRequest',
    {
    'date_custom_field_id': NotRequired["int"],
    'type': "CreateDateFieldRequestType",
    },
)

type CreateDateFieldRequestType = Literal['DueDate', 'TargetStartDate', 'TargetEndDate', 'DateCustomField']
"""The date field type. This must be "DueDate", "TargetStartDate", "TargetEndDate" or "DateCustomField"."""

CreateExclusionRulesRequest = TypedDict(
    'CreateExclusionRulesRequest',
    {
    'issue_ids': NotRequired["list[int]"],
    'issue_type_ids': NotRequired["list[int]"],
    'number_of_days_to_show_completed_issues': NotRequired["int"],
    'release_ids': NotRequired["list[int]"],
    'work_status_category_ids': NotRequired["list[int]"],
    'work_status_ids': NotRequired["list[int]"],
    },
)

CreateFieldAssociationSchemeLinksBean = TypedDict(
    'CreateFieldAssociationSchemeLinksBean',
    {
    'associations': NotRequired["str"],
    'projects': NotRequired["str"],
    },
)

CreateFieldAssociationSchemeRequest = TypedDict(
    'CreateFieldAssociationSchemeRequest',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""Request object for creating a new field association scheme."""

CreateFieldAssociationSchemeResponse = TypedDict(
    'CreateFieldAssociationSchemeResponse',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'links': NotRequired["CreateFieldAssociationSchemeLinksBean"],
    'name': NotRequired["str"],
    },
)
"""Response object after successfully creating a new field association scheme."""

CreateIssueSecuritySchemeDetails = TypedDict(
    'CreateIssueSecuritySchemeDetails',
    {
    'description': NotRequired["str"],
    'levels': NotRequired["list[SecuritySchemeLevelBean]"],
    'name': "str",
    },
)
"""Issue security scheme and it's details"""

CreateIssueSourceRequest = TypedDict(
    'CreateIssueSourceRequest',
    {
    'type': "CreateIssueSourceRequestType",
    'value': "int",
    },
)

type CreateIssueSourceRequestType = Literal['Board', 'Project', 'Filter']
"""The issue source type. This must be "Board", "Project" or "Filter"."""

CreateNotificationSchemeDetails = TypedDict(
    'CreateNotificationSchemeDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    'notification_scheme_events': NotRequired["list[NotificationSchemeEventDetails]"],
    },
)
"""Details of an notification scheme."""

CreatePermissionHolderRequest = TypedDict(
    'CreatePermissionHolderRequest',
    {
    'type': "CreatePermissionHolderRequestType",
    'value': "str",
    },
)

type CreatePermissionHolderRequestType = Literal['Group', 'AccountId']
"""The permission holder type. This must be "Group" or "AccountId"."""

CreatePermissionRequest = TypedDict(
    'CreatePermissionRequest',
    {
    'holder': "CreatePermissionHolderRequest",
    'type': "CreatePermissionRequestType",
    },
)

type CreatePermissionRequestType = Literal['View', 'Edit']
"""The permission type. This must be "View" or "Edit"."""

CreatePlanOnlyTeamRequest = TypedDict(
    'CreatePlanOnlyTeamRequest',
    {
    'capacity': NotRequired["float"],
    'issue_source_id': NotRequired["int"],
    'member_account_ids': NotRequired["list[str]"],
    'name': "str",
    'planning_style': "CreatePlanOnlyTeamRequestPlanningStyle",
    'sprint_length': NotRequired["int"],
    },
)

type CreatePlanOnlyTeamRequestPlanningStyle = Literal['Scrum', 'Kanban']
"""The planning style for the plan-only team. This must be "Scrum" or "Kanban"."""

CreatePlanRequest = TypedDict(
    'CreatePlanRequest',
    {
    'cross_project_releases': NotRequired["list[CreateCrossProjectReleaseRequest]"],
    'custom_fields': NotRequired["list[CreateCustomFieldRequest]"],
    'exclusion_rules': NotRequired["CreateExclusionRulesRequest"],
    'issue_sources': "list[CreateIssueSourceRequest]",
    'lead_account_id': NotRequired["str"],
    'name': "str",
    'permissions': NotRequired["list[CreatePermissionRequest]"],
    'scheduling': "CreateSchedulingRequest",
    },
)

CreatePriorityDetails = TypedDict(
    'CreatePriorityDetails',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str | None"],
    'icon_url': NotRequired["CreatePriorityDetailsIconUrl | None"],
    'name': "str",
    'status_color': "str",
    },
)
"""Details of an issue priority."""

type CreatePriorityDetailsIconUrl = Literal['/images/icons/priorities/blocker.png', '/images/icons/priorities/critical.png', '/images/icons/priorities/high.png', '/images/icons/priorities/highest.png', '/images/icons/priorities/low.png', '/images/icons/priorities/lowest.png', '/images/icons/priorities/major.png', '/images/icons/priorities/medium.png', '/images/icons/priorities/minor.png', '/images/icons/priorities/trivial.png', '/images/icons/priorities/blocker_new.png', '/images/icons/priorities/critical_new.png', '/images/icons/priorities/high_new.png', '/images/icons/priorities/highest_new.png', '/images/icons/priorities/low_new.png', '/images/icons/priorities/lowest_new.png', '/images/icons/priorities/major_new.png', '/images/icons/priorities/medium_new.png', '/images/icons/priorities/minor_new.png', '/images/icons/priorities/trivial_new.png']
"""The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Either the iconUrl or avatarId must be defined, but not both."""

CreatePrioritySchemeDetails = TypedDict(
    'CreatePrioritySchemeDetails',
    {
    'default_priority_id': "int",
    'description': NotRequired["str"],
    'mappings': NotRequired["PriorityMapping"],
    'name': "str",
    'priority_ids': "list[int]",
    'project_ids': NotRequired["list[int]"],
    },
)
"""Details of a new priority scheme"""

CreateProjectDetails = TypedDict(
    'CreateProjectDetails',
    {
    'assignee_type': NotRequired["CreateProjectDetailsAssigneeType"],
    'avatar_id': NotRequired["int"],
    'category_id': NotRequired["int"],
    'description': NotRequired["str"],
    'field_configuration_scheme': NotRequired["int"],
    'field_scheme': NotRequired["int"],
    'issue_security_scheme': NotRequired["int"],
    'issue_type_scheme': NotRequired["int"],
    'issue_type_screen_scheme': NotRequired["int"],
    'key': "str",
    'lead': NotRequired["str"],
    'lead_account_id': NotRequired["str"],
    'name': "str",
    'notification_scheme': NotRequired["int"],
    'permission_scheme': NotRequired["int"],
    'project_template_key': NotRequired["CreateProjectDetailsProjectTemplateKey"],
    'project_type_key': NotRequired["CreateProjectDetailsProjectTypeKey"],
    'url': NotRequired["str"],
    'workflow_scheme': NotRequired["int"],
    },
)
"""Details about the project."""

type CreateProjectDetailsAssigneeType = Literal['PROJECT_LEAD', 'UNASSIGNED']
"""The default assignee when creating issues for this project."""

type CreateProjectDetailsProjectTemplateKey = Literal['com.pyxis.greenhopper.jira:gh-simplified-agility-kanban', 'com.pyxis.greenhopper.jira:gh-simplified-agility-scrum', 'com.pyxis.greenhopper.jira:gh-simplified-basic', 'com.pyxis.greenhopper.jira:gh-simplified-kanban-classic', 'com.pyxis.greenhopper.jira:gh-simplified-scrum-classic', 'com.pyxis.greenhopper.jira:gh-cross-team-template', 'com.pyxis.greenhopper.jira:gh-cross-team-planning-template', 'com.atlassian.servicedesk:simplified-it-service-management', 'com.atlassian.servicedesk:simplified-it-service-management-basic', 'com.atlassian.servicedesk:simplified-it-service-management-operations', 'com.atlassian.servicedesk:simplified-internal-service-desk', 'com.atlassian.servicedesk:simplified-external-service-desk', 'com.atlassian.servicedesk:simplified-hr-service-desk', 'com.atlassian.servicedesk:simplified-facilities-service-desk', 'com.atlassian.servicedesk:simplified-legal-service-desk', 'com.atlassian.servicedesk:simplified-marketing-service-desk', 'com.atlassian.servicedesk:simplified-finance-service-desk', 'com.atlassian.servicedesk:simplified-analytics-service-desk', 'com.atlassian.servicedesk:simplified-design-service-desk', 'com.atlassian.servicedesk:simplified-sales-service-desk', 'com.atlassian.servicedesk:simplified-halp-service-desk', 'com.atlassian.servicedesk:next-gen-it-service-desk', 'com.atlassian.servicedesk:next-gen-hr-service-desk', 'com.atlassian.servicedesk:next-gen-legal-service-desk', 'com.atlassian.servicedesk:next-gen-marketing-service-desk', 'com.atlassian.servicedesk:next-gen-facilities-service-desk', 'com.atlassian.servicedesk:next-gen-analytics-service-desk', 'com.atlassian.servicedesk:next-gen-finance-service-desk', 'com.atlassian.servicedesk:next-gen-design-service-desk', 'com.atlassian.servicedesk:next-gen-sales-service-desk', 'com.atlassian.servicedesk:company-managed-blank-service-project', 'com.atlassian.servicedesk:company-managed-general-service-project', 'com.atlassian.servicedesk:team-managed-general-service-project', 'com.atlassian.jira-core-project-templates:jira-core-simplified-content-management', 'com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval', 'com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking', 'com.atlassian.jira-core-project-templates:jira-core-simplified-process-control', 'com.atlassian.jira-core-project-templates:jira-core-simplified-procurement', 'com.atlassian.jira-core-project-templates:jira-core-simplified-project-management', 'com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment', 'com.atlassian.jira-core-project-templates:jira-core-simplified-task-', 'com.atlassian.jcs:customer-service-management']
"""A predefined configuration for a project. The type of the `projectTemplateKey` must match with the type of the `projectTypeKey`."""

type CreateProjectDetailsProjectTypeKey = Literal['software', 'service_desk', 'business', 'customer_service']
"""The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type."""

CreateResolutionDetails = TypedDict(
    'CreateResolutionDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""Details of an issue resolution."""

CreateSchedulingRequest = TypedDict(
    'CreateSchedulingRequest',
    {
    'dependencies': NotRequired["CreateSchedulingRequestDependencies"],
    'end_date': NotRequired["CreateDateFieldRequest"],
    'estimation': "CreateSchedulingRequestEstimation",
    'inferred_dates': NotRequired["CreateSchedulingRequestInferredDates"],
    'start_date': NotRequired["CreateDateFieldRequest"],
    },
)

type CreateSchedulingRequestDependencies = Literal['Sequential', 'Concurrent']
"""The dependencies for the plan. This must be "Sequential" or "Concurrent"."""

type CreateSchedulingRequestEstimation = Literal['StoryPoints', 'Days', 'Hours']
"""The estimation unit for the plan. This must be "StoryPoints", "Days" or "Hours"."""

type CreateSchedulingRequestInferredDates = Literal['None', 'SprintDates', 'ReleaseDates', 'AnySprintDates']
"""The inferred dates for the plan. This must be "None", "SprintDates" or "ReleaseDates"."""

CreateUiModificationDetails = TypedDict(
    'CreateUiModificationDetails',
    {
    'contexts': NotRequired["list[UiModificationContextDetails]"],
    'data': NotRequired["str"],
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""The details of a UI modification."""

CreateUpdateRoleRequestBean = TypedDict(
    'CreateUpdateRoleRequestBean',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)

CreatedIssue = TypedDict(
    'CreatedIssue',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'self': NotRequired["str"],
    'transition': NotRequired["NestedResponse"],
    'watchers': NotRequired["NestedResponse"],
    },
)
"""Details about a created issue or subtask."""

CreatedIssues = TypedDict(
    'CreatedIssues',
    {
    'errors': NotRequired["list[BulkOperationErrorResult]"],
    'issues': NotRequired["list[CreatedIssue]"],
    },
)
"""Details about the issues created and the errors for requests that failed."""

type CustomContextVariable = UserContextVariable | IssueContextVariable | JsonContextVariable

CustomFieldConfigurations = TypedDict(
    'CustomFieldConfigurations',
    {
    'configurations': "list[ContextualConfiguration]",
    },
)
"""Details of configurations for a custom field."""

CustomFieldContext = TypedDict(
    'CustomFieldContext',
    {
    'description': "str",
    'id': "str",
    'is_any_issue_type': "bool",
    'is_global_context': "bool",
    'name': "str",
    },
)
"""The details of a custom field context."""

type CustomFieldContextDefaultValue = CustomFieldContextDefaultValueCascadingOption | CustomFieldContextDefaultValueMultipleOption | CustomFieldContextDefaultValueSingleOption | CustomFieldContextSingleUserPickerDefaults | CustomFieldContextDefaultValueMultiUserPicker | CustomFieldContextDefaultValueSingleGroupPicker | CustomFieldContextDefaultValueMultipleGroupPicker | CustomFieldContextDefaultValueDate | CustomFieldContextDefaultValueDateTime | CustomFieldContextDefaultValueUrl | CustomFieldContextDefaultValueProject | CustomFieldContextDefaultValueFloat | CustomFieldContextDefaultValueLabels | CustomFieldContextDefaultValueTextField | CustomFieldContextDefaultValueTextArea | CustomFieldContextDefaultValueLongText | CustomFieldContextDefaultValueReadOnly | CustomFieldContextDefaultValueSingleVersionPicker | CustomFieldContextDefaultValueMultipleVersionPicker | CustomFieldContextDefaultValueForgeStringField | CustomFieldContextDefaultValueForgeMultiStringField | CustomFieldContextDefaultValueForgeObjectField | CustomFieldContextDefaultValueForgeDateTimeField | CustomFieldContextDefaultValueForgeGroupField | CustomFieldContextDefaultValueForgeMultiGroupField | CustomFieldContextDefaultValueForgeNumberField | CustomFieldContextDefaultValueForgeUserField | CustomFieldContextDefaultValueForgeMultiUserField

CustomFieldContextDefaultValueCascadingOption = TypedDict(
    'CustomFieldContextDefaultValueCascadingOption',
    {
    'cascading_option_id': NotRequired["str"],
    'context_id': "str",
    'option_id': "str",
    'type': "str",
    },
)
"""The default value for a cascading select custom field."""

CustomFieldContextDefaultValueDate = TypedDict(
    'CustomFieldContextDefaultValueDate',
    {
    'context_id': "str",
    'date': NotRequired["str"],
    'type': "str",
    'use_current': NotRequired["bool"],
    },
)
"""The default value for a Date custom field."""

CustomFieldContextDefaultValueDateTime = TypedDict(
    'CustomFieldContextDefaultValueDateTime',
    {
    'context_id': "str",
    'date_time': NotRequired["str"],
    'type': "str",
    'use_current': NotRequired["bool"],
    },
)
"""The default value for a date time custom field."""

CustomFieldContextDefaultValueFloat = TypedDict(
    'CustomFieldContextDefaultValueFloat',
    {
    'context_id': "str",
    'number': "float",
    'type': "str",
    },
)
"""Default value for a float (number) custom field."""

CustomFieldContextDefaultValueForgeDateTimeField = TypedDict(
    'CustomFieldContextDefaultValueForgeDateTimeField',
    {
    'context_id': "str",
    'date_time': NotRequired["str"],
    'type': "str",
    'use_current': NotRequired["bool"],
    },
)
"""The default value for a Forge date time custom field."""

CustomFieldContextDefaultValueForgeGroupField = TypedDict(
    'CustomFieldContextDefaultValueForgeGroupField',
    {
    'context_id': "str",
    'group_id': "str",
    'type': "str",
    },
)
"""The default value for a Forge group custom field."""

CustomFieldContextDefaultValueForgeMultiGroupField = TypedDict(
    'CustomFieldContextDefaultValueForgeMultiGroupField',
    {
    'context_id': "str",
    'group_ids': "list[str]",
    'type': "str",
    },
)
"""The default value for a Forge collection of groups custom field."""

CustomFieldContextDefaultValueForgeMultiStringField = TypedDict(
    'CustomFieldContextDefaultValueForgeMultiStringField',
    {
    'context_id': "str",
    'type': "str",
    'values': NotRequired["list[str]"],
    },
)
"""The default text for a Forge collection of strings custom field."""

CustomFieldContextDefaultValueForgeMultiUserField = TypedDict(
    'CustomFieldContextDefaultValueForgeMultiUserField',
    {
    'account_ids': "list[str]",
    'context_id': "str",
    'type': "str",
    },
)
"""Defaults for a Forge collection of users custom field."""

CustomFieldContextDefaultValueForgeNumberField = TypedDict(
    'CustomFieldContextDefaultValueForgeNumberField',
    {
    'context_id': "str",
    'number': "float",
    'type': "str",
    },
)
"""Default value for a Forge number custom field."""

CustomFieldContextDefaultValueForgeObjectField = TypedDict(
    'CustomFieldContextDefaultValueForgeObjectField',
    {
    'context_id': "str",
    'object': NotRequired["dict[str, Any]"],
    'type': "str",
    },
)
"""The default value for a Forge object custom field."""

CustomFieldContextDefaultValueForgeStringField = TypedDict(
    'CustomFieldContextDefaultValueForgeStringField',
    {
    'context_id': "str",
    'text': NotRequired["str"],
    'type': "str",
    },
)
"""The default text for a Forge string custom field."""

CustomFieldContextDefaultValueForgeUserField = TypedDict(
    'CustomFieldContextDefaultValueForgeUserField',
    {
    'account_id': "str",
    'context_id': "str",
    'type': "str",
    'user_filter': "UserFilter",
    },
)
"""Defaults for a Forge user custom field."""

CustomFieldContextDefaultValueLabels = TypedDict(
    'CustomFieldContextDefaultValueLabels',
    {
    'context_id': "str",
    'labels': "list[str]",
    'type': "str",
    },
)
"""Default value for a labels custom field."""

CustomFieldContextDefaultValueLongText = TypedDict(
    'CustomFieldContextDefaultValueLongText',
    {
    'context_id': "str",
    'text': NotRequired["str"],
    'type': "str",
    },
)
"""The default text for a plain text paragraph custom field."""

CustomFieldContextDefaultValueMultiUserPicker = TypedDict(
    'CustomFieldContextDefaultValueMultiUserPicker',
    {
    'account_ids': "list[str]",
    'context_id': "str",
    'type': "str",
    },
)
"""The default value for a User Picker (multiple) custom field."""

CustomFieldContextDefaultValueMultipleGroupPicker = TypedDict(
    'CustomFieldContextDefaultValueMultipleGroupPicker',
    {
    'context_id': "str",
    'group_ids': "list[str]",
    'type': "str",
    },
)
"""The default value for a multiple group picker custom field."""

CustomFieldContextDefaultValueMultipleOption = TypedDict(
    'CustomFieldContextDefaultValueMultipleOption',
    {
    'context_id': "str",
    'option_ids': "list[str]",
    'type': "str",
    },
)
"""The default value for a multi-select custom field."""

CustomFieldContextDefaultValueMultipleVersionPicker = TypedDict(
    'CustomFieldContextDefaultValueMultipleVersionPicker',
    {
    'context_id': "str",
    'type': "str",
    'version_ids': "list[str]",
    'version_order': NotRequired["str"],
    },
)
"""The default value for a multiple version picker custom field."""

CustomFieldContextDefaultValueProject = TypedDict(
    'CustomFieldContextDefaultValueProject',
    {
    'context_id': "str",
    'project_id': "str",
    'type': "str",
    },
)
"""The default value for a project custom field."""

CustomFieldContextDefaultValueReadOnly = TypedDict(
    'CustomFieldContextDefaultValueReadOnly',
    {
    'context_id': "str",
    'text': NotRequired["str"],
    'type': "str",
    },
)
"""The default text for a read only custom field."""

CustomFieldContextDefaultValueSingleGroupPicker = TypedDict(
    'CustomFieldContextDefaultValueSingleGroupPicker',
    {
    'context_id': "str",
    'group_id': "str",
    'type': "str",
    },
)
"""The default value for a group picker custom field."""

CustomFieldContextDefaultValueSingleOption = TypedDict(
    'CustomFieldContextDefaultValueSingleOption',
    {
    'context_id': "str",
    'option_id': "str",
    'type': "str",
    },
)
"""The default value for a single select custom field."""

CustomFieldContextDefaultValueSingleVersionPicker = TypedDict(
    'CustomFieldContextDefaultValueSingleVersionPicker',
    {
    'context_id': "str",
    'type': "str",
    'version_id': "str",
    'version_order': NotRequired["str"],
    },
)
"""The default value for a version picker custom field."""

CustomFieldContextDefaultValueTextArea = TypedDict(
    'CustomFieldContextDefaultValueTextArea',
    {
    'context_id': "str",
    'text': NotRequired["str"],
    'type': "str",
    },
)
"""The default text for a text area custom field."""

CustomFieldContextDefaultValueTextField = TypedDict(
    'CustomFieldContextDefaultValueTextField',
    {
    'context_id': "str",
    'text': NotRequired["str"],
    'type': "str",
    },
)
"""The default text for a text custom field."""

CustomFieldContextDefaultValueUpdate = TypedDict(
    'CustomFieldContextDefaultValueUpdate',
    {
    'default_values': NotRequired["list[CustomFieldContextDefaultValue]"],
    },
)
"""Default values to update."""

CustomFieldContextDefaultValueUrl = TypedDict(
    'CustomFieldContextDefaultValueUrl',
    {
    'context_id': "str",
    'type': "str",
    'url': "str",
    },
)
"""The default value for a URL custom field."""

CustomFieldContextDefaultValuesUpdate = TypedDict(
    'CustomFieldContextDefaultValuesUpdate',
    {
    'default_values': NotRequired["list[IssueTypeDefaultValueUpdate]"],
    },
)
"""Default value updates grouped by context and issue type."""

CustomFieldContextOption = TypedDict(
    'CustomFieldContextOption',
    {
    'disabled': "bool",
    'id': "str",
    'option_id': NotRequired["str"],
    'value': "str",
    },
)
"""Details of the custom field options for a context."""

CustomFieldContextProjectMapping = TypedDict(
    'CustomFieldContextProjectMapping',
    {
    'context_id': "str",
    'is_global_context': NotRequired["bool"],
    'project_id': NotRequired["str"],
    },
)
"""Details of a context to project association."""

CustomFieldContextSingleUserPickerDefaults = TypedDict(
    'CustomFieldContextSingleUserPickerDefaults',
    {
    'account_id': "str",
    'context_id': "str",
    'type': "str",
    'user_filter': "UserFilter",
    },
)
"""Defaults for a User Picker (single) custom field."""

CustomFieldContextUpdateDetails = TypedDict(
    'CustomFieldContextUpdateDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of a custom field context."""

CustomFieldCreatedContextOptionsList = TypedDict(
    'CustomFieldCreatedContextOptionsList',
    {
    'options': NotRequired["list[CustomFieldContextOption]"],
    },
)
"""A list of custom field options for a context."""

CustomFieldDefinitionJsonBean = TypedDict(
    'CustomFieldDefinitionJsonBean',
    {
    'description': NotRequired["str"],
    'name': "str",
    'searcher_key': NotRequired["CustomFieldDefinitionJsonBeanSearcherKey"],
    'type': "str",
    },
)

type CustomFieldDefinitionJsonBeanSearcherKey = Literal['com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:daterange', 'com.atlassian.jira.plugin.system.customfieldtypes:datetimerange', 'com.atlassian.jira.plugin.system.customfieldtypes:exactnumber', 'com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:numberrange', 'com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:textsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher']
"""
The searcher defines the way the field is searched in Jira. For example, *com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher*.  
The search UI (basic search and JQL search) will display different operations and values for the field, based on the field searcher. You must specify a searcher that is valid for the field type, as listed below (abbreviated values shown):

 *  `cascadingselect`: `cascadingselectsearcher`
 *  `datepicker`: `daterange`
 *  `datetime`: `datetimerange`
 *  `float`: `exactnumber` or `numberrange`
 *  `grouppicker`: `grouppickersearcher`
 *  `importid`: `exactnumber` or `numberrange`
 *  `labels`: `labelsearcher`
 *  `multicheckboxes`: `multiselectsearcher`
 *  `multigrouppicker`: `multiselectsearcher`
 *  `multiselect`: `multiselectsearcher`
 *  `multiuserpicker`: `userpickergroupsearcher`
 *  `multiversion`: `versionsearcher`
 *  `project`: `projectsearcher`
 *  `radiobuttons`: `multiselectsearcher`
 *  `readonlyfield`: `textsearcher`
 *  `select`: `multiselectsearcher`
 *  `textarea`: `textsearcher`
 *  `textfield`: `textsearcher`
 *  `url`: `exacttextsearcher`
 *  `userpicker`: `userpickergroupsearcher`
 *  `version`: `versionsearcher`

If no searcher is provided, the field isn't searchable. However, [Forge custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/#jira-custom-field-type--beta-) have a searcher set automatically, so are always searchable.
"""

CustomFieldOption = TypedDict(
    'CustomFieldOption',
    {
    'self': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""Details of a custom option for a field."""

CustomFieldOptionCreate = TypedDict(
    'CustomFieldOptionCreate',
    {
    'disabled': NotRequired["bool"],
    'option_id': NotRequired["str"],
    'value': "str",
    },
)
"""Details of a custom field option to create."""

CustomFieldOptionUpdate = TypedDict(
    'CustomFieldOptionUpdate',
    {
    'disabled': NotRequired["bool"],
    'id': "str",
    'value': NotRequired["str"],
    },
)
"""Details of a custom field option for a context."""

CustomFieldPayload = TypedDict(
    'CustomFieldPayload',
    {
    'cf_type': NotRequired["str"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["CustomFieldPayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'scope': NotRequired["CustomFieldPayloadScope"],
    'searcher_key': NotRequired["str"],
    },
)
"""Defines the payload for the custom field definitions. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/\\#api-rest-api-3-field-post"""

type CustomFieldPayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use when there is a conflict with an existing custom field. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters"""

type CustomFieldPayloadScope = Literal['GLOBAL', 'TEMPLATE', 'PROJECT']
"""Allows an overwrite to declare the new Custom Field to be created as a GLOBAL-scoped field. Leave this as empty or null to use the project's default scope."""

CustomFieldReplacement = TypedDict(
    'CustomFieldReplacement',
    {
    'custom_field_id': NotRequired["int"],
    'move_to': NotRequired["int"],
    },
)
"""Details about the replacement for a deleted version."""

CustomFieldUpdatedContextOptionsList = TypedDict(
    'CustomFieldUpdatedContextOptionsList',
    {
    'options': NotRequired["list[CustomFieldOptionUpdate]"],
    },
)
"""A list of custom field options for a context."""

CustomFieldValueUpdate = TypedDict(
    'CustomFieldValueUpdate',
    {
    'issue_ids': "list[int]",
    'value': "Any",
    },
)
"""A list of issue IDs and the value to update a custom field to."""

CustomFieldValueUpdateDetails = TypedDict(
    'CustomFieldValueUpdateDetails',
    {
    'updates': NotRequired["list[CustomFieldValueUpdate]"],
    },
)
"""Details of updates for a custom field."""

CustomTemplateOptions = TypedDict(
    'CustomTemplateOptions',
    {
    'enable_screen_delegated_admin_support': NotRequired["bool"],
    'enable_workflow_delegated_admin_support': NotRequired["bool"],
    },
)

CustomTemplateRequestDto = TypedDict(
    'CustomTemplateRequestDto',
    {
    'board_features': NotRequired["BoardFeaturesPayload | None"],
    'boards': NotRequired["BoardsPayload | None"],
    'field': NotRequired["FieldCapabilityPayload | None"],
    'issue_type': NotRequired["IssueTypeProjectCreatePayload | None"],
    'notification': NotRequired["NotificationSchemePayload | None"],
    'permission_scheme': NotRequired["PermissionPayloadDto | None"],
    'project': NotRequired["ProjectPayload"],
    'role': NotRequired["RolesCapabilityPayload | None"],
    'scope': NotRequired["ScopePayload | None"],
    'security': NotRequired["SecuritySchemePayload | None"],
    'workflow': NotRequired["WorkflowCapabilityPayload | None"],
    },
)
"""The specific request object for creating a project with template."""

CustomTemplatesProjectDetails = TypedDict(
    'CustomTemplatesProjectDetails',
    {
    'access_level': NotRequired["CustomTemplatesProjectDetailsAccessLevel"],
    'additional_properties': NotRequired["dict[str, str]"],
    'assignee_type': NotRequired["CustomTemplatesProjectDetailsAssigneeType"],
    'avatar_id': NotRequired["int"],
    'category_id': NotRequired["int"],
    'description': NotRequired["str"],
    'enable_components': NotRequired["bool"],
    'key': NotRequired["str"],
    'language': NotRequired["str"],
    'lead_account_id': NotRequired["str"],
    'name': NotRequired["str"],
    'url': NotRequired["str"],
    },
)
"""Project Details"""

type CustomTemplatesProjectDetailsAccessLevel = Literal['open', 'limited', 'private', 'free']
"""The access level of the project. Only used by team-managed project"""

type CustomTemplatesProjectDetailsAssigneeType = Literal['PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED']
"""The default assignee when creating issues in the project"""

Dashboard = TypedDict(
    'Dashboard',
    {
    'automatic_refresh_ms': NotRequired["int"],
    'description': NotRequired["str"],
    'edit_permissions': NotRequired["list[SharePermission]"],
    'id': NotRequired["str"],
    'is_favourite': NotRequired["bool"],
    'is_writable': NotRequired["bool"],
    'name': NotRequired["str"],
    'owner': NotRequired["UserBean"],
    'popularity': NotRequired["int"],
    'rank': NotRequired["int"],
    'self': NotRequired["str"],
    'share_permissions': NotRequired["list[SharePermission]"],
    'system_dashboard': NotRequired["bool"],
    'view': NotRequired["str"],
    },
)
"""Details of a dashboard."""

DashboardDetails = TypedDict(
    'DashboardDetails',
    {
    'description': NotRequired["str"],
    'edit_permissions': "list[SharePermission]",
    'name': "str",
    'share_permissions': "list[SharePermission]",
    },
)
"""Details of a dashboard."""

DashboardGadget = TypedDict(
    'DashboardGadget',
    {
    'color': "DashboardGadgetColor",
    'id': "int",
    'module_key': NotRequired["str"],
    'position': "DashboardGadgetPosition",
    'title': "str",
    'uri': NotRequired["str"],
    },
)
"""Details of a gadget."""

type DashboardGadgetColor = Literal['blue', 'red', 'yellow', 'green', 'cyan', 'purple', 'gray', 'white']
"""The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`."""

DashboardGadgetPosition = TypedDict(
    'DashboardGadgetPosition',
    {
    'the_column_position_of_the_gadget': "int",
    'the_row_position_of_the_gadget': "int",
    },
)
"""Details of a gadget position."""

DashboardGadgetResponse = TypedDict(
    'DashboardGadgetResponse',
    {
    'gadgets': "list[DashboardGadget]",
    },
)
"""The list of gadgets on the dashboard."""

DashboardGadgetSettings = TypedDict(
    'DashboardGadgetSettings',
    {
    'color': NotRequired["str"],
    'ignore_uri_and_module_key_validation': NotRequired["bool"],
    'module_key': NotRequired["str"],
    'position': NotRequired["DashboardGadgetPosition"],
    'title': NotRequired["str"],
    'uri': NotRequired["str"],
    },
)
"""Details of the settings for a dashboard gadget."""

DashboardGadgetUpdateRequest = TypedDict(
    'DashboardGadgetUpdateRequest',
    {
    'color': NotRequired["str"],
    'position': NotRequired["DashboardGadgetPosition"],
    'title': NotRequired["str"],
    },
)
"""The details of the gadget to update."""

DataClassificationLevelsBean = TypedDict(
    'DataClassificationLevelsBean',
    {
    'classifications': NotRequired["list[DataClassificationTagBean]"],
    },
)
"""The data classification."""

DataClassificationTagBean = TypedDict(
    'DataClassificationTagBean',
    {
    'color': NotRequired["str"],
    'description': NotRequired["str"],
    'guideline': NotRequired["str"],
    'guideline_adf': NotRequired["str"],
    'id': "str",
    'name': NotRequired["str"],
    'rank': NotRequired["int"],
    'status': "str",
    },
)
"""The data classification."""

DateRangeFilterRequest = TypedDict(
    'DateRangeFilterRequest',
    {
    'date_after': "str",
    'date_before': "str",
    },
)
"""List issues archived within a specified date range."""

DefaultLevelValue = TypedDict(
    'DefaultLevelValue',
    {
    'default_level_id': "str",
    'issue_security_scheme_id': "str",
    },
)
"""Details of scheme and new default level."""

DefaultShareScope = TypedDict(
    'DefaultShareScope',
    {
    'scope': "DefaultShareScopeScope",
    },
)
"""Details of the scope of the default sharing for new filters and dashboards."""

type DefaultShareScopeScope = Literal['GLOBAL', 'AUTHENTICATED', 'PRIVATE']
"""
The scope of the default sharing for new filters and dashboards:

 *  `AUTHENTICATED` Shared with all logged-in users.
 *  `GLOBAL` Shared with all logged-in users. This shows as `AUTHENTICATED` in the response.
 *  `PRIVATE` Not shared with any users.
"""

DefaultWorkflow = TypedDict(
    'DefaultWorkflow',
    {
    'update_draft_if_needed': NotRequired["bool"],
    'workflow': "str",
    },
)
"""Details about the default workflow."""

DefaultWorkflowEditorResponse = TypedDict(
    'DefaultWorkflowEditorResponse',
    {
    'value': NotRequired["DefaultWorkflowEditorResponseValue"],
    },
)

type DefaultWorkflowEditorResponseValue = Literal['NEW', 'LEGACY']

DeleteAndReplaceVersionBean = TypedDict(
    'DeleteAndReplaceVersionBean',
    {
    'custom_field_replacement_list': NotRequired["list[CustomFieldReplacement]"],
    'move_affected_issues_to': NotRequired["int"],
    'move_fix_issues_to': NotRequired["int"],
    },
)

type DeleteAvatarType = Literal['project', 'issuetype', 'priority']

DeleteFieldAssociationSchemeResponse = TypedDict(
    'DeleteFieldAssociationSchemeResponse',
    {
    'deleted': NotRequired["bool"],
    'id': NotRequired["str"],
    },
)
"""Response object after successfully deleting a field association scheme."""

type DeleteIssueDeleteSubtasks = Literal['true', 'false']

type DeleteWorklogAdjustEstimate = Literal['new', 'leave', 'manual', 'auto']

DetailedErrorCollection = TypedDict(
    'DetailedErrorCollection',
    {
    'details': NotRequired["dict[str, Any]"],
    'error_messages': NotRequired["list[str]"],
    'errors': NotRequired["dict[str, str]"],
    },
)

DocumentVersion = TypedDict(
    'DocumentVersion',
    {
    'id': NotRequired["str"],
    'version_number': NotRequired["int"],
    },
)
"""The current version details of this workflow scheme."""

DuplicatePlanRequest = TypedDict(
    'DuplicatePlanRequest',
    {
    'name': "str",
    },
)

EditTemplateRequest = TypedDict(
    'EditTemplateRequest',
    {
    'template_description': NotRequired["str"],
    'template_generation_options': NotRequired["CustomTemplateOptions"],
    'template_key': NotRequired["str"],
    'template_name': NotRequired["str"],
    },
)
"""Request to edit a custom template"""

EntityProperty = TypedDict(
    'EntityProperty',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    },
)
"""An entity property, for more information see [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/)."""

EntityPropertyDetails = TypedDict(
    'EntityPropertyDetails',
    {
    'entity_id': "float",
    'key': "str",
    'value': "str",
    },
)

Error = TypedDict(
    'Error',
    {
    'count': NotRequired["int"],
    'issue_ids_or_keys': NotRequired["list[str]"],
    'message': NotRequired["str"],
    },
)

ErrorCollection = TypedDict(
    'ErrorCollection',
    {
    'error_messages': NotRequired["list[str]"],
    'errors': NotRequired["dict[str, str]"],
    'status': NotRequired["int"],
    },
)
"""Error messages from an operation."""

type ErrorCollections = dict[str, Any]

ErrorMessage = TypedDict(
    'ErrorMessage',
    {
    'message': NotRequired["str"],
    },
)

ErrorResponse = TypedDict(
    'ErrorResponse',
    {
    'error_messages': NotRequired["list[str]"],
    'errors': NotRequired["dict[str, str]"],
    },
)

Errors = TypedDict(
    'Errors',
    {
    'issue_is_subtask': NotRequired["Error"],
    'issues_in_archived_projects': NotRequired["Error"],
    'issues_in_unlicensed_projects': NotRequired["Error"],
    'issues_not_found': NotRequired["Error"],
    'user_does_not_have_permission': NotRequired["Error"],
    },
)

EventNotification = TypedDict(
    'EventNotification',
    {
    'email_address': NotRequired["str"],
    'expand': NotRequired["str"],
    'field': NotRequired["FieldDetails"],
    'group': NotRequired["GroupName"],
    'id': NotRequired["int"],
    'notification_type': NotRequired["EventNotificationNotificationType"],
    'parameter': NotRequired["str"],
    'project_role': NotRequired["ProjectRole"],
    'recipient': NotRequired["str"],
    'user': NotRequired["UserDetails"],
    },
)
"""Details about a notification associated with an event."""

type EventNotificationNotificationType = Literal['CurrentAssignee', 'Reporter', 'CurrentUser', 'ProjectLead', 'ComponentLead', 'User', 'Group', 'ProjectRole', 'EmailAddress', 'AllWatchers', 'UserCustomField', 'GroupCustomField']
"""Identifies the recipients of the notification."""

ExpandPrioritySchemePage = TypedDict(
    'ExpandPrioritySchemePage',
    {
    'max_results': NotRequired["int"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)

ExportArchivedIssuesTaskProgressResponse = TypedDict(
    'ExportArchivedIssuesTaskProgressResponse',
    {
    'file_url': NotRequired["str"],
    'payload': NotRequired["str"],
    'progress': NotRequired["int"],
    'status': NotRequired["str"],
    'submitted_time': NotRequired["str"],
    'task_id': NotRequired["str"],
    },
)
"""The response for status request for a running/completed export task."""

FailedWebhook = TypedDict(
    'FailedWebhook',
    {
    'body': NotRequired["str"],
    'failure_time': "int",
    'id': "str",
    'url': "str",
    },
)
"""Details about a failed webhook."""

FailedWebhooks = TypedDict(
    'FailedWebhooks',
    {
    'max_results': "int",
    'next': NotRequired["str"],
    'values': "list[FailedWebhook]",
    },
)
"""A page of failed webhooks."""

Field = TypedDict(
    'Field',
    {
    'contexts_count': NotRequired["int"],
    'description': NotRequired["str"],
    'id': "str",
    'is_locked': NotRequired["bool"],
    'is_unscreenable': NotRequired["bool"],
    'key': NotRequired["str"],
    'last_used': NotRequired["FieldLastUsed"],
    'name': "str",
    'projects_count': NotRequired["int"],
    'schema': "JsonTypeBean",
    'screens_count': NotRequired["int"],
    'searcher_key': NotRequired["str"],
    'stable_id': NotRequired["str"],
    'translated_description': NotRequired["str"],
    'translated_name': NotRequired["str"],
    'type_display_name': NotRequired["str"],
    },
)
"""Details of a field."""

FieldAssociationItemPayload = TypedDict(
    'FieldAssociationItemPayload',
    {
    'description': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'qualifier_id': NotRequired["ProjectCreateResourceIdentifier"],
    'qualifier_type': NotRequired["ProjectCreateResourceIdentifier"],
    'renderer_type': NotRequired["str"],
    'required': NotRequired["bool"],
    },
)
"""Defines the payload for the field association scheme."""

FieldAssociationParameters = TypedDict(
    'FieldAssociationParameters',
    {
    'description': NotRequired["str"],
    'is_required': "bool",
    'renderer_type': NotRequired["str"],
    },
)

FieldAssociationSchemeFieldSearchResult = TypedDict(
    'FieldAssociationSchemeFieldSearchResult',
    {
    'allowed_operations': NotRequired["list[str]"],
    'field_id': NotRequired["str"],
    'parameters': NotRequired["SearchResultFieldParameters"],
    'restricted_to_work_types': NotRequired["list[str]"],
    'work_type_parameters': NotRequired["list[SearchResultWorkTypeParameters]"],
    },
)
"""Field association scheme field search results."""

FieldAssociationSchemeLinks = TypedDict(
    'FieldAssociationSchemeLinks',
    {
    'associations': NotRequired["str"],
    'projects': NotRequired["str"],
    },
)

FieldAssociationSchemeLinksBean = TypedDict(
    'FieldAssociationSchemeLinksBean',
    {
    'associations': NotRequired["str"],
    'projects': NotRequired["str"],
    },
)

FieldAssociationSchemeMatchedFilters = TypedDict(
    'FieldAssociationSchemeMatchedFilters',
    {
    'project_ids': NotRequired["list[int]"],
    'query': NotRequired["str"],
    },
)
"""Matched filters for field association scheme search."""

FieldAssociationSchemeProjectSearchResult = TypedDict(
    'FieldAssociationSchemeProjectSearchResult',
    {
    'avatar_urls': NotRequired["dict[str, str]"],
    'deleted': NotRequired["bool"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Project search results for field association scheme."""

FieldAssociationsRequest = TypedDict(
    'FieldAssociationsRequest',
    {
    'association_contexts': "list[AssociationContextObject]",
    'fields': "list[FieldIdentifierObject]",
    },
)
"""Details of field associations with projects."""

FieldCapabilityPayload = TypedDict(
    'FieldCapabilityPayload',
    {
    'custom_field_definitions': NotRequired["list[CustomFieldPayload | None] | None"],
    'field_layout_scheme': NotRequired["FieldLayoutSchemePayload | None"],
    'field_layouts': NotRequired["list[FieldLayoutPayload | None] | None"],
    'field_scheme': NotRequired["FieldSchemePayload | None"],
    'issue_layouts': NotRequired["list[IssueLayoutPayload | None] | None"],
    'issue_type_screen_scheme': NotRequired["IssueTypeScreenSchemePayload | None"],
    'screen_scheme': NotRequired["list[ScreenSchemePayload | None] | None"],
    'screens': NotRequired["list[ScreenPayload | None] | None"],
    },
)
"""Defines the payload for the fields, screens, screen schemes, issue type screen schemes, field layouts, and field layout schemes"""

FieldChangedClause = TypedDict(
    'FieldChangedClause',
    {
    'field': "JqlQueryField",
    'operator': "FieldChangedClauseOperator",
    'predicates': "list[JqlQueryClauseTimePredicate]",
    },
)
"""A clause that asserts whether a field was changed. For example, `status CHANGED AFTER startOfMonth(-1M)`.See [CHANGED](https://confluence.atlassian.com/x/dgiiLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for more information about the CHANGED operator."""

type FieldChangedClauseOperator = Literal['changed']
"""The operator applied to the field."""

FieldConfiguration = TypedDict(
    'FieldConfiguration',
    {
    'description': "str",
    'id': "int",
    'is_default': NotRequired["bool"],
    'name': "str",
    },
)
"""Details of a field configuration."""

FieldConfigurationDetails = TypedDict(
    'FieldConfigurationDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""Details of a field configuration."""

FieldConfigurationIssueTypeItem = TypedDict(
    'FieldConfigurationIssueTypeItem',
    {
    'field_configuration_id': "str",
    'field_configuration_scheme_id': "str",
    'issue_type_id': "str",
    },
)
"""The field configuration for an issue type."""

FieldConfigurationItem = TypedDict(
    'FieldConfigurationItem',
    {
    'description': NotRequired["str"],
    'id': "str",
    'is_hidden': NotRequired["bool"],
    'is_required': NotRequired["bool"],
    'renderer': NotRequired["str"],
    },
)
"""A field within a field configuration."""

FieldConfigurationItemsDetails = TypedDict(
    'FieldConfigurationItemsDetails',
    {
    'field_configuration_items': "list[FieldConfigurationItem]",
    },
)
"""Details of field configuration items."""

FieldConfigurationScheme = TypedDict(
    'FieldConfigurationScheme',
    {
    'description': NotRequired["str"],
    'id': "str",
    'name': "str",
    },
)
"""Details of a field configuration scheme."""

FieldConfigurationSchemeProjectAssociation = TypedDict(
    'FieldConfigurationSchemeProjectAssociation',
    {
    'field_configuration_scheme_id': NotRequired["str"],
    'project_id': "str",
    },
)
"""Associated field configuration scheme and project."""

FieldConfigurationSchemeProjects = TypedDict(
    'FieldConfigurationSchemeProjects',
    {
    'field_configuration_scheme': NotRequired["FieldConfigurationScheme"],
    'project_ids': "list[str]",
    },
)
"""Project list with assigned field configuration schema."""

FieldConfigurationToIssueTypeMapping = TypedDict(
    'FieldConfigurationToIssueTypeMapping',
    {
    'field_configuration_id': "str",
    'issue_type_id': "str",
    },
)
"""The field configuration to issue type mapping."""

FieldCreateMetadata = TypedDict(
    'FieldCreateMetadata',
    {
    'allowed_values': NotRequired["list[Any]"],
    'auto_complete_url': NotRequired["str"],
    'configuration': NotRequired["dict[str, Any]"],
    'default_value': NotRequired["Any"],
    'field_id': "str",
    'has_default_value': NotRequired["bool"],
    'key': "str",
    'name': "str",
    'operations': "list[str]",
    'required': "bool",
    'schema': "JsonTypeBean",
    },
)
"""The metadata describing an issue field for createmeta."""

FieldDetails = TypedDict(
    'FieldDetails',
    {
    'clause_names': NotRequired["list[str]"],
    'custom': NotRequired["bool"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'navigable': NotRequired["bool"],
    'orderable': NotRequired["bool"],
    'schema': NotRequired["JsonTypeBean"],
    'scope': NotRequired["Scope"],
    'searchable': NotRequired["bool"],
    },
)
"""Details about a field."""

FieldIdentifierObject = TypedDict(
    'FieldIdentifierObject',
    {
    'identifier': NotRequired["dict[str, Any]"],
    'type': "str",
    },
)
"""Identifier for a field for example FIELD\\_ID."""

FieldLastUsed = TypedDict(
    'FieldLastUsed',
    {
    'type': NotRequired["FieldLastUsedType"],
    'value': NotRequired["str"],
    },
)
"""Information about the most recent use of a field."""

type FieldLastUsedType = Literal['TRACKED', 'NOT_TRACKED', 'NO_INFORMATION']
"""
Last used value type:

 *  *TRACKED*: field is tracked and a last used date is available.
 *  *NOT\\_TRACKED*: field is not tracked, last used date is not available.
 *  *NO\\_INFORMATION*: field is tracked, but no last used date is available.
"""

FieldLayoutConfiguration = TypedDict(
    'FieldLayoutConfiguration',
    {
    'field': NotRequired["bool"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'required': NotRequired["bool"],
    },
)
"""Defines the payload for the field layout configuration. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/\\#api-rest-api-3-fieldconfiguration-post"""

FieldLayoutPayload = TypedDict(
    'FieldLayoutPayload',
    {
    'configuration': NotRequired["list[FieldLayoutConfiguration]"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""Defines the payload for the field layouts. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/\\#api-group-issue-field-configurations" + fieldlayout is what users would see as "Field Configuration" in Jira's UI - https://support.atlassian.com/jira-cloud-administration/docs/manage-issue-field-configurations/"""

FieldLayoutSchemePayload = TypedDict(
    'FieldLayoutSchemePayload',
    {
    'default_field_layout': NotRequired["ProjectCreateResourceIdentifier"],
    'description': NotRequired["str"],
    'explicit_mappings': NotRequired["dict[str, ProjectCreateResourceIdentifier]"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""
Deprecated use [fieldAssociationScheme](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) instead Defines the payload for the field layout schemes. See [ Field configuration scheme](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-rest-api-3-fieldconfigurationscheme-post).

[ How to configure a field configuration scheme](https://support.atlassian.com/jira-cloud-administration/docs/configure-a-field-configuration-scheme/).
"""

FieldMetadata = TypedDict(
    'FieldMetadata',
    {
    'allowed_values': NotRequired["list[Any]"],
    'auto_complete_url': NotRequired["str"],
    'configuration': NotRequired["dict[str, Any]"],
    'default_value': NotRequired["Any"],
    'has_default_value': NotRequired["bool"],
    'key': "str",
    'name': "str",
    'operations': "list[str]",
    'required': "bool",
    'schema': "JsonTypeBean",
    },
)
"""The metadata describing an issue field."""

FieldProjectAssociation = TypedDict(
    'FieldProjectAssociation',
    {
    'project_id': NotRequired["str"],
    },
)
"""List of project associations."""

FieldReferenceData = TypedDict(
    'FieldReferenceData',
    {
    'auto': NotRequired["FieldReferenceDataAuto"],
    'cfid': NotRequired["str"],
    'deprecated': NotRequired["FieldReferenceDataDeprecated"],
    'deprecated_searcher_key': NotRequired["str"],
    'display_name': NotRequired["str"],
    'operators': NotRequired["list[str]"],
    'orderable': NotRequired["FieldReferenceDataOrderable"],
    'searchable': NotRequired["FieldReferenceDataSearchable"],
    'types': NotRequired["list[str]"],
    'value': NotRequired["str"],
    },
)
"""Details of a field that can be used in advanced searches."""

type FieldReferenceDataAuto = Literal['true', 'false']
"""Whether the field provide auto-complete suggestions."""

type FieldReferenceDataDeprecated = Literal['true', 'false']
"""Whether this field has been deprecated."""

type FieldReferenceDataOrderable = Literal['true', 'false']
"""Whether the field can be used in a query's `ORDER BY` clause."""

type FieldReferenceDataSearchable = Literal['true', 'false']
"""Whether the content of this field can be searched."""

FieldSchemePayload = TypedDict(
    'FieldSchemePayload',
    {
    'description': NotRequired["str"],
    'items': NotRequired["list[FieldAssociationItemPayload]"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["FieldSchemePayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""Defines the payload to configure the field scheme for a project. See [Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes)."""

type FieldSchemePayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use when there is a conflict with an existing field scheme. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters"""

FieldSchemeToFieldsPartialFailure = TypedDict(
    'FieldSchemeToFieldsPartialFailure',
    {
    'error': NotRequired["str"],
    'field_id': "str",
    'scheme_id': "int",
    'success': "bool",
    'work_type_ids': "list[int]",
    },
)
"""Partial failure result when updating field scheme to fields associations."""

FieldSchemeToFieldsResponse = TypedDict(
    'FieldSchemeToFieldsResponse',
    {
    'results': "list[FieldSchemeToFieldsPartialFailure]",
    },
)
"""Response for updating field associations."""

FieldSchemeToProjectsPartialFailure = TypedDict(
    'FieldSchemeToProjectsPartialFailure',
    {
    'error': NotRequired["str"],
    'project_id': "int",
    'scheme_id': "int",
    'success': "bool",
    },
)
"""Partial failure result when updating field scheme to projects associations."""

FieldSchemeToProjectsRequest = TypedDict(
    'FieldSchemeToProjectsRequest',
    {
    'project_ids': "list[int]",
    },
)
"""Request for associating field schemes to projects."""

FieldSchemeToProjectsResponse = TypedDict(
    'FieldSchemeToProjectsResponse',
    {
    'results': "list[FieldSchemeToProjectsPartialFailure]",
    },
)
"""Response for updating field scheme to projects associations."""

FieldUpdateOperation = TypedDict(
    'FieldUpdateOperation',
    {
    'add': NotRequired["Any"],
    'copy': NotRequired["Any"],
    'edit': NotRequired["Any"],
    'remove': NotRequired["Any"],
    'set': NotRequired["Any"],
    },
)
"""Details of an operation to perform on a field."""

FieldValueClause = TypedDict(
    'FieldValueClause',
    {
    'field': "JqlQueryField",
    'operand': "JqlQueryClauseOperand",
    'operator': "FieldValueClauseOperator",
    },
)
"""A clause that asserts the current value of a field. For example, `summary ~ test`."""

type FieldValueClauseOperator = Literal['=', '!=', '>', '<', '>=', '<=', 'in', 'not in', '~', '~=', 'is', 'is not']
"""The operator between the field and operand."""

FieldWasClause = TypedDict(
    'FieldWasClause',
    {
    'field': "JqlQueryField",
    'operand': "JqlQueryClauseOperand",
    'operator': "FieldWasClauseOperator",
    'predicates': "list[JqlQueryClauseTimePredicate]",
    },
)
"""A clause that asserts a previous value of a field. For example, `status WAS "Resolved" BY currentUser() BEFORE "2019/02/02"`. See [WAS](https://confluence.atlassian.com/x/dgiiLQ#Advancedsearching-operatorsreference-WASWAS) for more information about the WAS operator."""

type FieldWasClauseOperator = Literal['was', 'was in', 'was not in', 'was not']
"""The operator between the field and operand."""

Fields = TypedDict(
    'Fields',
    {
    'assignee': NotRequired["UserDetails"],
    'issue_type': NotRequired["IssueTypeDetails"],
    'issuetype': NotRequired["IssueTypeDetails"],
    'priority': NotRequired["Priority"],
    'status': NotRequired["StatusDetails"],
    'summary': NotRequired["str"],
    'timetracking': NotRequired["TimeTrackingDetails"],
    },
)
"""Key fields from the linked issue."""

FieldsSchemeItemParameter = TypedDict(
    'FieldsSchemeItemParameter',
    {
    'description': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'renderer_type': NotRequired["FieldsSchemeItemParameterRendererType"],
    },
)
"""The default parameters to apply to the field across all work types in the specified schemes, may be null if only work type-specific updates are needed"""

type FieldsSchemeItemParameterRendererType = Literal['jira-text-renderer', 'atlassian-wiki-renderer']
"""The renderer type for the field, null to preserve current renderer type"""

FieldsSchemeItemWorkTypeParameter = TypedDict(
    'FieldsSchemeItemWorkTypeParameter',
    {
    'description': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'renderer_type': NotRequired["FieldsSchemeItemWorkTypeParameterRendererType"],
    'work_type_id': NotRequired["int"],
    },
)
"""The list of work type-specific parameter overrides, may be empty if only default parameters are being updated"""

type FieldsSchemeItemWorkTypeParameterRendererType = Literal['jira-text-renderer', 'atlassian-wiki-renderer']
"""The renderer type for the field for this work type, null to use default or preserve current"""

Filter = TypedDict(
    'Filter',
    {
    'approximate_last_used': NotRequired["str"],
    'description': NotRequired["str"],
    'edit_permissions': NotRequired["list[SharePermission]"],
    'favourite': NotRequired["bool"],
    'favourited_count': NotRequired["int"],
    'id': NotRequired["str"],
    'jql': NotRequired["str"],
    'name': "str",
    'owner': NotRequired["User"],
    'search_url': NotRequired["str"],
    'self': NotRequired["str"],
    'share_permissions': NotRequired["list[SharePermission]"],
    'shared_users': NotRequired["UserList"],
    'subscriptions': NotRequired["FilterSubscriptionsList"],
    'view_url': NotRequired["str"],
    },
)
"""Details about a filter."""

FilterDetails = TypedDict(
    'FilterDetails',
    {
    'approximate_last_used': NotRequired["str"],
    'description': NotRequired["str"],
    'edit_permissions': NotRequired["list[SharePermission]"],
    'expand': NotRequired["str"],
    'favourite': NotRequired["bool"],
    'favourited_count': NotRequired["int"],
    'id': NotRequired["str"],
    'jql': NotRequired["str"],
    'name': "str",
    'owner': NotRequired["User"],
    'search_url': NotRequired["str"],
    'self': NotRequired["str"],
    'share_permissions': NotRequired["list[SharePermission]"],
    'subscriptions': NotRequired["list[FilterSubscription]"],
    'view_url': NotRequired["str"],
    },
)
"""Details of a filter."""

FilterSubscription = TypedDict(
    'FilterSubscription',
    {
    'group': NotRequired["GroupName"],
    'id': NotRequired["int"],
    'user': NotRequired["User"],
    },
)
"""Details of a user or group subscribing to a filter."""

FilterSubscriptionsList = TypedDict(
    'FilterSubscriptionsList',
    {
    'end_index': NotRequired["int"],
    'items': NotRequired["list[FilterSubscription]"],
    'max_results': NotRequired["int"],
    'size': NotRequired["int"],
    'start_index': NotRequired["int"],
    },
)
"""A paginated list of subscriptions to a filter."""

type FindComponentsForProjectsOrderBy = Literal['description', '-description', '+description', 'name', '-name', '+name']

type FindUsersAndGroupsAvatarSize = Literal['xsmall', 'xsmall@2x', 'xsmall@3x', 'small', 'small@2x', 'small@3x', 'medium', 'medium@2x', 'medium@3x', 'large', 'large@2x', 'large@3x', 'xlarge', 'xlarge@2x', 'xlarge@3x', 'xxlarge', 'xxlarge@2x', 'xxlarge@3x', 'xxxlarge', 'xxxlarge@2x', 'xxxlarge@3x']

ForgePanelProjectPinAsyncResponse = TypedDict(
    'ForgePanelProjectPinAsyncResponse',
    {
    'task_id': NotRequired["str"],
    },
)

ForgePanelProjectPinRequest = TypedDict(
    'ForgePanelProjectPinRequest',
    {
    'module_id': "str",
    'project_list': "list[ProjectPinAction]",
    },
)

ForgePanelProjectPinStatus = TypedDict(
    'ForgePanelProjectPinStatus',
    {
    'error': NotRequired["str"],
    'pinned': NotRequired["bool"],
    'pinned_at': NotRequired["int"],
    'project_id_or_key': NotRequired["str"],
    },
)
"""The pin status of an issue panel (added by a Forge app) for a single project."""

ForgePanelProjectPinStatusRequest = TypedDict(
    'ForgePanelProjectPinStatusRequest',
    {
    'module_id': "str",
    'project_list': "list[str]",
    },
)

ForgePanelProjectPinStatusResponse = TypedDict(
    'ForgePanelProjectPinStatusResponse',
    {
    'module_id': NotRequired["str"],
    'statuses': NotRequired["list[ForgePanelProjectPinStatus]"],
    },
)

FoundGroup = TypedDict(
    'FoundGroup',
    {
    'avatar_url': NotRequired["str"],
    'group_id': NotRequired["str"],
    'html': NotRequired["str"],
    'labels': NotRequired["list[GroupLabel]"],
    'managed_by': NotRequired["FoundGroupManagedBy"],
    'name': NotRequired["str"],
    'usage_type': NotRequired["FoundGroupUsageType"],
    },
)
"""A group found in a search."""

type FoundGroupManagedBy = Literal['EXTERNAL', 'ADMINS', 'TEAM_MEMBERS', 'OPEN']
"""
Describes who/how the team is managed. The possible values are  
\\* external - when team is synced from an external directory like SCIM or HRIS, and team members cannot be modified.  
\\* admins - when a team is managed by an admin (team members can only be modified by admins).  
\\* team-members - managed by existing team members, new members need to be invited to join.  
\\* open - anyone can join or modify this team.
"""

type FoundGroupUsageType = Literal['USERBASE_GROUP', 'TEAM_COLLABORATION', 'ADMIN_OVERSIGHT']
"""
Describes the type of group. The possible values are  
\\* team-collaboration - A platform team managed in people directory.  
\\* userbase-group - a group of users created in adminhub.  
\\* admin-oversight - currently unused.
"""

FoundGroups = TypedDict(
    'FoundGroups',
    {
    'groups': NotRequired["list[FoundGroup]"],
    'header': NotRequired["str"],
    'total': NotRequired["int"],
    },
)
"""The list of groups found in a search, including header text (Showing X of Y matching groups) and total of matched groups."""

FoundUsers = TypedDict(
    'FoundUsers',
    {
    'header': NotRequired["str"],
    'total': NotRequired["int"],
    'users': NotRequired["list[UserPickerUser]"],
    },
)
"""The list of users found in a search, including header text (Showing X of Y matching users) and total of matched users."""

FoundUsersAndGroups = TypedDict(
    'FoundUsersAndGroups',
    {
    'groups': NotRequired["FoundGroups"],
    'users': NotRequired["FoundUsers"],
    },
)
"""List of users and groups found in a search."""

FromLayoutPayload = TypedDict(
    'FromLayoutPayload',
    {
    'from_port': NotRequired["int"],
    'status': NotRequired["ProjectCreateResourceIdentifier"],
    'to_port_override': NotRequired["int"],
    },
)
"""The payload for the layout details for the start end of a transition"""

FunctionOperand = TypedDict(
    'FunctionOperand',
    {
    'arguments': "list[str]",
    'encoded_operand': NotRequired["str"],
    'function': "str",
    },
)
"""An operand that is a function. See [Advanced searching - functions reference](https://confluence.atlassian.com/x/dwiiLQ) for more information about JQL functions."""

FunctionReferenceData = TypedDict(
    'FunctionReferenceData',
    {
    'display_name': NotRequired["str"],
    'is_list': NotRequired["FunctionReferenceDataIsList"],
    'supports_list_and_single_value_operators': NotRequired["FunctionReferenceDataSupportsListAndSingleValueOperators"],
    'types': NotRequired["list[str]"],
    'value': NotRequired["str"],
    },
)
"""Details of functions that can be used in advanced searches."""

type FunctionReferenceDataIsList = Literal['true', 'false']
"""Whether the function can take a list of arguments."""

type FunctionReferenceDataSupportsListAndSingleValueOperators = Literal['true', 'false']
"""Whether the function supports both single and list value operators."""

type GetAccessibleProjectTypeByKeyProjectTypeKey = Literal['software', 'service_desk', 'business', 'product_discovery']

type GetAllDashboardsFilter = Literal['my', 'favourite']

type GetAllIssueTypeSchemesOrderBy = Literal['name', '-name', '+name', 'id', '-id', '+id']

type GetAllSystemAvatarsType = Literal['issuetype', 'project', 'user', 'priority']

type GetAllUserDataClassificationLevelsOrderBy = Literal['rank', '-rank', '+rank']

type GetAllUserDataClassificationLevelsStatusItem = Literal['PUBLISHED', 'ARCHIVED', 'DRAFT']
"""The status of the project classification."""

type GetApproximateApplicationLicenseCountApplicationKey = Literal['jira-core', 'jira-product-discovery', 'jira-software', 'jira-servicedesk']

GetAtlassianTeamResponse = TypedDict(
    'GetAtlassianTeamResponse',
    {
    'capacity': NotRequired["float"],
    'id': "str",
    'issue_source_id': NotRequired["int"],
    'planning_style': "GetAtlassianTeamResponsePlanningStyle",
    'sprint_length': NotRequired["int"],
    },
)

type GetAtlassianTeamResponsePlanningStyle = Literal['Scrum', 'Kanban']
"""The planning style for the Atlassian team. This is "Scrum" or "Kanban"."""

type GetAvatarImageByIdFormat = Literal['png', 'svg']

type GetAvatarImageByIdSize = Literal['xsmall', 'small', 'medium', 'large', 'xlarge']

type GetAvatarImageByIdType = Literal['issuetype', 'project', 'priority']

type GetAvatarImageByOwnerFormat = Literal['png', 'svg']

type GetAvatarImageByOwnerSize = Literal['xsmall', 'small', 'medium', 'large', 'xlarge']

type GetAvatarImageByOwnerType = Literal['issuetype', 'project', 'priority']

type GetAvatarImageByTypeFormat = Literal['png', 'svg']

type GetAvatarImageByTypeSize = Literal['xsmall', 'small', 'medium', 'large', 'xlarge']

type GetAvatarImageByTypeType = Literal['issuetype', 'project', 'priority']

type GetAvatarsType = Literal['project', 'issuetype', 'priority']

type GetCommentsOrderBy = Literal['created', '-created', '+created']

GetCrossProjectReleaseResponse = TypedDict(
    'GetCrossProjectReleaseResponse',
    {
    'name': NotRequired["str"],
    'release_ids': NotRequired["list[int]"],
    },
)

GetCustomFieldResponse = TypedDict(
    'GetCustomFieldResponse',
    {
    'custom_field_id': "int",
    'filter': NotRequired["bool"],
    },
)

type GetDashboardsPaginatedOrderBy = Literal['description', '-description', '+description', 'favorite_count', '-favorite_count', '+favorite_count', 'id', '-id', '+id', 'is_favorite', '-is_favorite', '+is_favorite', 'name', '-name', '+name', 'owner', '-owner', '+owner']

type GetDashboardsPaginatedStatus = Literal['active', 'archived', 'deleted']

GetDateFieldResponse = TypedDict(
    'GetDateFieldResponse',
    {
    'date_custom_field_id': NotRequired["int"],
    'type': "GetDateFieldResponseType",
    },
)

type GetDateFieldResponseType = Literal['DueDate', 'TargetStartDate', 'TargetEndDate', 'DateCustomField']
"""The date field type. This is "DueDate", "TargetStartDate", "TargetEndDate" or "DateCustomField"."""

GetExclusionRulesResponse = TypedDict(
    'GetExclusionRulesResponse',
    {
    'issue_ids': NotRequired["list[int]"],
    'issue_type_ids': NotRequired["list[int]"],
    'number_of_days_to_show_completed_issues': "int",
    'release_ids': NotRequired["list[int]"],
    'work_status_category_ids': NotRequired["list[int]"],
    'work_status_ids': NotRequired["list[int]"],
    },
)

GetFieldAssociationParametersResponse = TypedDict(
    'GetFieldAssociationParametersResponse',
    {
    'field_id': "str",
    'parameters': NotRequired["FieldAssociationParameters"],
    'work_type_parameters': NotRequired["list[WorkTypeParameters]"],
    },
)
"""Response object for getting field association parameters."""

GetFieldAssociationSchemeByIdResponse = TypedDict(
    'GetFieldAssociationSchemeByIdResponse',
    {
    'description': NotRequired["str"],
    'fields_count': NotRequired["int"],
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'links': NotRequired["FieldAssociationSchemeLinks"],
    'name': NotRequired["str"],
    },
)
"""Response object for getting a field association scheme by ID."""

GetFieldAssociationSchemeResponse = TypedDict(
    'GetFieldAssociationSchemeResponse',
    {
    'description': NotRequired["str"],
    'fields_count': NotRequired["int"],
    'id': NotRequired["int"],
    'is_default': NotRequired["bool"],
    'links': NotRequired["FieldAssociationSchemeLinksBean"],
    'matched_filters': NotRequired["FieldAssociationSchemeMatchedFilters"],
    'name': NotRequired["str"],
    },
)
"""Response object for getting a field association scheme."""

type GetFieldsPaginatedOrderBy = Literal['contextsCount', '-contextsCount', '+contextsCount', 'lastUsed', '-lastUsed', '+lastUsed', 'name', '-name', '+name', 'screensCount', '-screensCount', '+screensCount', 'projectsCount', '-projectsCount', '+projectsCount']

type GetFieldsPaginatedTypeItem = Literal['custom', 'system']

type GetFiltersPaginatedOrderBy = Literal['description', '-description', '+description', 'favourite_count', '-favourite_count', '+favourite_count', 'id', '-id', '+id', 'is_favourite', '-is_favourite', '+is_favourite', 'name', '-name', '+name', 'owner', '-owner', '+owner', 'is_shared', '-is_shared', '+is_shared']

GetForgeAppPropertyKeysResponse = TypedDict(
    'GetForgeAppPropertyKeysResponse',
    {
    'keys': NotRequired["list[GetForgeAppPropertyKeysResponseKeysItem]"],
    },
)

GetForgeAppPropertyKeysResponseKeysItem = TypedDict(
    'GetForgeAppPropertyKeysResponseKeysItem',
    {
    'key': NotRequired["str"],
    'self': NotRequired["str"],
    },
)

GetForgeAppPropertyResponse = TypedDict(
    'GetForgeAppPropertyResponse',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    },
)

GetIssueSourceResponse = TypedDict(
    'GetIssueSourceResponse',
    {
    'type': "GetIssueSourceResponseType",
    'value': "int",
    },
)

type GetIssueSourceResponseType = Literal['Board', 'Project', 'Filter', 'Custom']
"""The issue source type. This is "Board", "Project" or "Filter"."""

type GetIssueTypeScreenSchemesOrderBy = Literal['name', '-name', '+name', 'id', '-id', '+id']

GetPermissionHolderResponse = TypedDict(
    'GetPermissionHolderResponse',
    {
    'type': "GetPermissionHolderResponseType",
    'value': "str",
    },
)

type GetPermissionHolderResponseType = Literal['Group', 'AccountId']
"""The permission holder type. This is "Group" or "AccountId"."""

GetPermissionResponse = TypedDict(
    'GetPermissionResponse',
    {
    'holder': "GetPermissionHolderResponse",
    'type': "GetPermissionResponseType",
    },
)

type GetPermissionResponseType = Literal['View', 'Edit']
"""The permission type. This is "View" or "Edit"."""

GetPlanOnlyTeamResponse = TypedDict(
    'GetPlanOnlyTeamResponse',
    {
    'capacity': NotRequired["float"],
    'id': "int",
    'issue_source_id': NotRequired["int"],
    'member_account_ids': NotRequired["list[str]"],
    'name': "str",
    'planning_style': "GetPlanOnlyTeamResponsePlanningStyle",
    'sprint_length': NotRequired["int"],
    },
)

type GetPlanOnlyTeamResponsePlanningStyle = Literal['Scrum', 'Kanban']
"""The planning style for the plan-only team. This is "Scrum" or "Kanban"."""

GetPlanResponse = TypedDict(
    'GetPlanResponse',
    {
    'cross_project_releases': NotRequired["list[GetCrossProjectReleaseResponse]"],
    'custom_fields': NotRequired["list[GetCustomFieldResponse]"],
    'exclusion_rules': NotRequired["GetExclusionRulesResponse"],
    'id': "int",
    'issue_sources': NotRequired["list[GetIssueSourceResponse]"],
    'last_saved': NotRequired["str"],
    'lead_account_id': NotRequired["str"],
    'name': NotRequired["str"],
    'permissions': NotRequired["list[GetPermissionResponse]"],
    'scheduling': "GetSchedulingResponse",
    'status': "GetPlanResponseStatus",
    },
)

GetPlanResponseForPage = TypedDict(
    'GetPlanResponseForPage',
    {
    'id': "str",
    'issue_sources': NotRequired["list[GetIssueSourceResponse]"],
    'name': "str",
    'scenario_id': "str",
    'status': "GetPlanResponseForPageStatus",
    },
)

type GetPlanResponseForPageStatus = Literal['Active', 'Trashed', 'Archived']
"""The plan status. This is "Active", "Trashed" or "Archived"."""

type GetPlanResponseStatus = Literal['Active', 'Trashed', 'Archived']
"""The plan status. This is "Active", "Trashed" or "Archived"."""

type GetPrioritySchemesOrderBy = Literal['name', '+name', '-name']

type GetProjectComponentsComponentSource = Literal['jira', 'compass', 'auto']

type GetProjectComponentsPaginatedComponentSource = Literal['jira', 'compass', 'auto']

type GetProjectComponentsPaginatedOrderBy = Literal['description', '-description', '+description', 'issueCount', '-issueCount', '+issueCount', 'lead', '-lead', '+lead', 'name', '-name', '+name']

type GetProjectTypeByKeyProjectTypeKey = Literal['software', 'service_desk', 'business', 'product_discovery']

type GetProjectVersionsPaginatedOrderBy = Literal['description', '-description', '+description', 'name', '-name', '+name', 'releaseDate', '-releaseDate', '+releaseDate', 'sequence', '-sequence', '+sequence', 'startDate', '-startDate', '+startDate']

GetProjectsWithFieldSchemesResponse = TypedDict(
    'GetProjectsWithFieldSchemesResponse',
    {
    'project_id': NotRequired["int"],
    'scheme_id': NotRequired["int"],
    },
)
"""Response item returned from get projects with field schemes."""

type GetRemoteIssueLinksResponse = list[RemoteIssueLink] | RemoteIssueLink

GetSchedulingResponse = TypedDict(
    'GetSchedulingResponse',
    {
    'dependencies': "GetSchedulingResponseDependencies",
    'end_date': "GetDateFieldResponse",
    'estimation': "GetSchedulingResponseEstimation",
    'inferred_dates': "GetSchedulingResponseInferredDates",
    'start_date': "GetDateFieldResponse",
    },
)

type GetSchedulingResponseDependencies = Literal['Sequential', 'Concurrent']
"""The dependencies for the plan. This is "Sequential" or "Concurrent"."""

type GetSchedulingResponseEstimation = Literal['StoryPoints', 'Days', 'Hours']
"""The estimation unit for the plan. This is "StoryPoints", "Days" or "Hours"."""

type GetSchedulingResponseInferredDates = Literal['None', 'SprintDates', 'ReleaseDates', 'AnySprintDates']
"""The inferred dates for the plan. This is "None", "SprintDates" or "ReleaseDates"."""

type GetScreenSchemesOrderBy = Literal['name', '-name', '+name', 'id', '-id', '+id']

type GetScreensOrderBy = Literal['name', '-name', '+name', 'id', '-id', '+id']

type GetScreensScopeItem = Literal['GLOBAL', 'TEMPLATE', 'PROJECT']

GetTeamResponseForPage = TypedDict(
    'GetTeamResponseForPage',
    {
    'id': "str",
    'name': NotRequired["str"],
    'type': "GetTeamResponseForPageType",
    },
)

type GetTeamResponseForPageType = Literal['PlanOnly', 'Atlassian']
"""The team type. This is "PlanOnly" or "Atlassian"."""

type GetTrashedFieldsPaginatedExpand = Literal['name', '-name', '+name', 'trashDate', '-trashDate', '+trashDate', 'plannedDeletionDate', '-plannedDeletionDate', '+plannedDeletionDate', 'projectsCount', '-projectsCount', '+projectsCount']

type GetWorkflowTransitionRuleConfigurationsTypesItem = Literal['postfunction', 'condition', 'validator']

type GetWorkflowsPaginatedOrderBy = Literal['name', '-name', '+name', 'created', '-created', '+created', 'updated', '+updated', '-updated']

GlobalScopeBean = TypedDict(
    'GlobalScopeBean',
    {
    'attributes': NotRequired["list[GlobalScopeBeanAttributesItem]"],
    },
)

type GlobalScopeBeanAttributesItem = Literal['notSelectable', 'defaultValue']

Group = TypedDict(
    'Group',
    {
    'expand': NotRequired["str"],
    'group_id': NotRequired["str | None"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    'users': NotRequired["PagedListUserDetailsApplicationUser"],
    },
)

GroupDetails = TypedDict(
    'GroupDetails',
    {
    'group_id': NotRequired["str | None"],
    'name': NotRequired["str"],
    },
)
"""Details about a group."""

GroupLabel = TypedDict(
    'GroupLabel',
    {
    'text': NotRequired["str"],
    'title': NotRequired["str"],
    'type': NotRequired["GroupLabelType"],
    },
)
"""A group label."""

type GroupLabelType = Literal['ADMIN', 'SINGLE', 'MULTIPLE']
"""The type of the group label."""

GroupName = TypedDict(
    'GroupName',
    {
    'group_id': NotRequired["str | None"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details about a group."""

HealthCheckResult = TypedDict(
    'HealthCheckResult',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'passed': NotRequired["bool"],
    },
)
"""Jira instance health check results. Deprecated and no longer returned."""

Hierarchy = TypedDict(
    'Hierarchy',
    {
    'base_level_id': NotRequired["int"],
    'levels': NotRequired["list[SimplifiedHierarchyLevel]"],
    },
)
"""The project issue type hierarchy."""

HistoryMetadata = TypedDict(
    'HistoryMetadata',
    {
    'activity_description': NotRequired["str"],
    'activity_description_key': NotRequired["str"],
    'actor': NotRequired["HistoryMetadataParticipant"],
    'cause': NotRequired["HistoryMetadataParticipant"],
    'description': NotRequired["str"],
    'description_key': NotRequired["str"],
    'email_description': NotRequired["str"],
    'email_description_key': NotRequired["str"],
    'extra_data': NotRequired["dict[str, str]"],
    'generator': NotRequired["HistoryMetadataParticipant"],
    'type': NotRequired["str"],
    },
)
"""Details of issue history metadata."""

HistoryMetadataParticipant = TypedDict(
    'HistoryMetadataParticipant',
    {
    'avatar_url': NotRequired["str"],
    'display_name': NotRequired["str"],
    'display_name_key': NotRequired["str"],
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'url': NotRequired["str"],
    },
)
"""Details of user or system associated with a issue history metadata item."""

Icon = TypedDict(
    'Icon',
    {
    'link': NotRequired["str"],
    'title': NotRequired["str"],
    'url_16_x_16': NotRequired["str"],
    },
)
"""
An icon. If no icon is defined:

 *  for a status icon, no status icon displays in Jira.
 *  for the remote object icon, the default link icon displays in Jira.
"""

IdBean = TypedDict(
    'IdBean',
    {
    'id': "int",
    },
)

IdOrKeyBean = TypedDict(
    'IdOrKeyBean',
    {
    'id': NotRequired["int"],
    'key': NotRequired["str"],
    },
)

IncludedFields = TypedDict(
    'IncludedFields',
    {
    'actually_included': NotRequired["list[str]"],
    'excluded': NotRequired["list[str]"],
    'included': NotRequired["list[str]"],
    },
)

IssueArchivalSyncRequest = TypedDict(
    'IssueArchivalSyncRequest',
    {
    'issue_ids_or_keys': NotRequired["list[str]"],
    },
)
"""List of Issue Ids Or Keys that are to be archived or unarchived"""

IssueArchivalSyncResponse = TypedDict(
    'IssueArchivalSyncResponse',
    {
    'errors': NotRequired["Errors"],
    'number_of_issues_updated': NotRequired["int"],
    },
)
"""Number of archived/unarchived issues and list of errors that occurred during the action, if any."""

IssueBean = TypedDict(
    'IssueBean',
    {
    'changelog': NotRequired["PageOfChangelogs"],
    'editmeta': NotRequired["IssueUpdateMetadata"],
    'expand': NotRequired["str"],
    'fields': NotRequired["dict[str, Any]"],
    'fields_to_include': NotRequired["IncludedFields"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'names': NotRequired["dict[str, str]"],
    'operations': NotRequired["Operations"],
    'properties': NotRequired["dict[str, Any]"],
    'rendered_fields': NotRequired["dict[str, Any]"],
    'schema': NotRequired["dict[str, JsonTypeBean]"],
    'self': NotRequired["str"],
    'transitions': NotRequired["list[IssueTransition]"],
    'versioned_representations': NotRequired["dict[str, dict[str, Any]]"],
    },
)
"""Details about an issue."""

IssueBulkDeletePayload = TypedDict(
    'IssueBulkDeletePayload',
    {
    'selected_issue_ids_or_keys': "list[str]",
    'send_bulk_notification': NotRequired["bool | None"],
    },
)
"""Issue Bulk Delete Payload"""

IssueBulkEditField = TypedDict(
    'IssueBulkEditField',
    {
    'description': NotRequired["str"],
    'field_options': NotRequired["list[IssueBulkOperationsFieldOption]"],
    'id': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'multi_select_field_options': NotRequired["list[IssueBulkEditFieldMultiSelectFieldOptionsItem]"],
    'name': NotRequired["str"],
    'search_url': NotRequired["str"],
    'type': NotRequired["str"],
    'unavailable_message': NotRequired["str"],
    },
)

type IssueBulkEditFieldMultiSelectFieldOptionsItem = Literal['ADD', 'REMOVE', 'REPLACE', 'REMOVE_ALL']

IssueBulkEditPayload = TypedDict(
    'IssueBulkEditPayload',
    {
    'edited_fields_input': "JiraIssueFields",
    'selected_actions': "list[str]",
    'selected_issue_ids_or_keys': "list[str]",
    'send_bulk_notification': NotRequired["bool | None"],
    },
)
"""Issue Bulk Edit Payload"""

IssueBulkMovePayload = TypedDict(
    'IssueBulkMovePayload',
    {
    'send_bulk_notification': NotRequired["bool | None"],
    'target_to_sources_mapping': NotRequired["dict[str, TargetToSourcesMapping]"],
    },
)
"""Issue Bulk Move Payload"""

type IssueBulkOperationsFieldOption = dict[str, Any]

IssueBulkTransitionForWorkflow = TypedDict(
    'IssueBulkTransitionForWorkflow',
    {
    'is_transitions_filtered': NotRequired["bool"],
    'issues': NotRequired["list[str]"],
    'transitions': NotRequired["list[SimplifiedIssueTransition]"],
    },
)

IssueBulkTransitionPayload = TypedDict(
    'IssueBulkTransitionPayload',
    {
    'bulk_transition_inputs': "list[BulkTransitionSubmitInput]",
    'send_bulk_notification': NotRequired["bool | None"],
    },
)
"""Issue Bulk Transition Payload"""

IssueBulkWatchOrUnwatchPayload = TypedDict(
    'IssueBulkWatchOrUnwatchPayload',
    {
    'selected_issue_ids_or_keys': "list[str]",
    },
)
"""Issue Bulk Watch Or Unwatch Payload"""

IssueChangeLog = TypedDict(
    'IssueChangeLog',
    {
    'change_histories': NotRequired["list[Changelog]"],
    'issue_id': NotRequired["str"],
    },
)
"""List of changelogs that belong to single issue"""

IssueChangelogIds = TypedDict(
    'IssueChangelogIds',
    {
    'changelog_ids': "list[int]",
    },
)
"""A list of changelog IDs."""

IssueCommentListRequestBean = TypedDict(
    'IssueCommentListRequestBean',
    {
    'ids': "list[int]",
    },
)

IssueContextVariable = TypedDict(
    'IssueContextVariable',
    {
    'id': NotRequired["int"],
    'key': NotRequired["str"],
    'type': "str",
    },
)
"""An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression."""

IssueCreateMetadata = TypedDict(
    'IssueCreateMetadata',
    {
    'expand': NotRequired["str"],
    'projects': NotRequired["list[ProjectIssueCreateMetadata]"],
    },
)
"""The wrapper for the issue creation metadata for a list of projects."""

IssueEntityProperties = TypedDict(
    'IssueEntityProperties',
    {
    'entities_ids': NotRequired["list[int]"],
    'properties': NotRequired["dict[str, JsonNode]"],
    },
)
"""Lists of issues and entity properties. See [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information."""

IssueEntityPropertiesForMultiUpdate = TypedDict(
    'IssueEntityPropertiesForMultiUpdate',
    {
    'issue_id': NotRequired["int"],
    'properties': NotRequired["dict[str, JsonNode]"],
    },
)
"""An issue ID with entity property values. See [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information."""

IssueError = TypedDict(
    'IssueError',
    {
    'error_message': NotRequired["str"],
    'id': NotRequired["str"],
    },
)
"""Describes the error that occurred when retrieving data for a particular issue."""

IssueEvent = TypedDict(
    'IssueEvent',
    {
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    },
)
"""Details about an issue event."""

IssueFieldOption = TypedDict(
    'IssueFieldOption',
    {
    'config': NotRequired["IssueFieldOptionConfiguration"],
    'id': "int",
    'properties': NotRequired["dict[str, Any]"],
    'value': "str",
    },
)
"""Details of the options for a select list issue field."""

IssueFieldOptionConfiguration = TypedDict(
    'IssueFieldOptionConfiguration',
    {
    'attributes': NotRequired["list[IssueFieldOptionConfigurationAttributesItem]"],
    'scope': NotRequired["IssueFieldOptionScopeBean"],
    },
)
"""Details of the projects the option is available in."""

type IssueFieldOptionConfigurationAttributesItem = Literal['notSelectable', 'defaultValue']

IssueFieldOptionCreateBean = TypedDict(
    'IssueFieldOptionCreateBean',
    {
    'config': NotRequired["IssueFieldOptionConfiguration"],
    'properties': NotRequired["dict[str, Any]"],
    'value': "str",
    },
)

IssueFieldOptionScopeBean = TypedDict(
    'IssueFieldOptionScopeBean',
    {
    'global': NotRequired["GlobalScopeBean"],
    'projects': NotRequired["list[int]"],
    'projects_2': NotRequired["list[ProjectScopeBean]"],
    },
)

IssueFilterForBulkPropertyDelete = TypedDict(
    'IssueFilterForBulkPropertyDelete',
    {
    'current_value': NotRequired["Any"],
    'entity_ids': NotRequired["list[int]"],
    },
)
"""Bulk operation filter details."""

IssueFilterForBulkPropertySet = TypedDict(
    'IssueFilterForBulkPropertySet',
    {
    'current_value': NotRequired["Any"],
    'entity_ids': NotRequired["list[int]"],
    'has_property': NotRequired["bool"],
    },
)
"""Bulk operation filter details."""

IssueLayoutItemPayload = TypedDict(
    'IssueLayoutItemPayload',
    {
    'item_key': NotRequired["ProjectCreateResourceIdentifier"],
    'properties': NotRequired["dict[str, Any]"],
    'section_type': NotRequired["IssueLayoutItemPayloadSectionType"],
    'type': NotRequired["IssueLayoutItemPayloadType"],
    },
)
"""Defines the payload to configure the issue layout item for a project."""

type IssueLayoutItemPayloadSectionType = Literal['content', 'primaryContext', 'secondaryContext']
"""The item section type"""

type IssueLayoutItemPayloadType = Literal['FIELD']
"""The item type. Currently only support FIELD"""

IssueLayoutPayload = TypedDict(
    'IssueLayoutPayload',
    {
    'container_id': NotRequired["ProjectCreateResourceIdentifier"],
    'issue_layout_type': NotRequired["IssueLayoutPayloadIssueLayoutType"],
    'items': NotRequired["list[IssueLayoutItemPayload]"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""Defines the payload to configure the issue layouts for a project."""

type IssueLayoutPayloadIssueLayoutType = Literal['ISSUE_VIEW', 'ISSUE_CREATE', 'REQUEST_FORM']
"""The issue layout type"""

IssueLimitReportResponseBean = TypedDict(
    'IssueLimitReportResponseBean',
    {
    'entities_breaching_limit': NotRequired["dict[str, dict[str, list[int]]]"],
    'issues_approaching_limit': NotRequired["dict[str, dict[str, int]]"],
    'issues_breaching_limit': NotRequired["dict[str, dict[str, int]]"],
    'limits': NotRequired["dict[str, int]"],
    },
)

IssueLink = TypedDict(
    'IssueLink',
    {
    'id': NotRequired["str"],
    'inward_issue': "LinkedIssue",
    'outward_issue': "LinkedIssue",
    'self': NotRequired["str"],
    'type': "IssueLinkType",
    },
)
"""Details of a link between issues."""

IssueLinkType = TypedDict(
    'IssueLinkType',
    {
    'id': NotRequired["str"],
    'inward': NotRequired["str"],
    'name': NotRequired["str"],
    'outward': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""
This object is used as follows:

 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on the type of link between the issues. Find a list of issue link types with [Get issue link types](#api-rest-api-3-issueLinkType-get).
 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and reports on issue link types.
"""

IssueLinkTypes = TypedDict(
    'IssueLinkTypes',
    {
    'issue_link_types': NotRequired["list[IssueLinkType]"],
    },
)
"""A list of issue link type beans."""

IssueList = TypedDict(
    'IssueList',
    {
    'issue_ids': "list[str]",
    },
)
"""A list of issue IDs."""

IssueMatches = TypedDict(
    'IssueMatches',
    {
    'matches': "list[IssueMatchesForJql]",
    },
)
"""A list of matched issues or errors for each JQL query, in the order the JQL queries were passed."""

IssueMatchesForJql = TypedDict(
    'IssueMatchesForJql',
    {
    'errors': "list[str]",
    'matched_issues': "list[int]",
    },
)
"""A list of the issues matched to a JQL query or details of errors encountered during matching."""

IssuePickerSuggestions = TypedDict(
    'IssuePickerSuggestions',
    {
    'sections': NotRequired["list[IssuePickerSuggestionsIssueType]"],
    },
)
"""A list of issues suggested for use in auto-completion."""

IssuePickerSuggestionsIssueType = TypedDict(
    'IssuePickerSuggestionsIssueType',
    {
    'id': NotRequired["str"],
    'issues': NotRequired["list[SuggestedIssue]"],
    'label': NotRequired["str"],
    'msg': NotRequired["str"],
    'sub': NotRequired["str"],
    },
)
"""A type of issue suggested for use in auto-completion."""

IssueSecurityLevelMember = TypedDict(
    'IssueSecurityLevelMember',
    {
    'holder': "PermissionHolder",
    'id': "int",
    'issue_security_level_id': "int",
    },
)
"""Issue security level member."""

IssueSecuritySchemeToProjectMapping = TypedDict(
    'IssueSecuritySchemeToProjectMapping',
    {
    'issue_security_scheme_id': NotRequired["str"],
    'project_id': NotRequired["str"],
    },
)
"""Details about an project using security scheme mapping."""

IssueTransition = TypedDict(
    'IssueTransition',
    {
    'expand': NotRequired["str"],
    'fields': NotRequired["dict[str, FieldMetadata]"],
    'has_screen': NotRequired["bool"],
    'id': NotRequired["str"],
    'is_available': NotRequired["bool"],
    'is_conditional': NotRequired["bool"],
    'is_global': NotRequired["bool"],
    'is_initial': NotRequired["bool"],
    'looped': NotRequired["bool"],
    'name': NotRequired["str"],
    'to': NotRequired["StatusDetails"],
    },
)
"""Details of an issue transition."""

IssueTransitionStatus = TypedDict(
    'IssueTransitionStatus',
    {
    'status_id': NotRequired["int"],
    'status_name': NotRequired["str"],
    },
)

IssueTypeCreateBean = TypedDict(
    'IssueTypeCreateBean',
    {
    'description': NotRequired["str"],
    'hierarchy_level': NotRequired["int"],
    'name': "str",
    'type': NotRequired["IssueTypeCreateBeanType"],
    },
)

type IssueTypeCreateBeanType = Literal['subtask', 'standard']
"""
Deprecated. Use `hierarchyLevel` instead. See the [deprecation notice](https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-fields-in-rest-apis-and-webhooks/54048) for details.

Whether the issue type is `subtype` or `standard`. Defaults to `standard`.
"""

IssueTypeDefaultValue = TypedDict(
    'IssueTypeDefaultValue',
    {
    'is_any_issue_type': NotRequired["bool | None"],
    'issue_type_id': NotRequired["str | None"],
    'value': NotRequired["CustomFieldContextDefaultValue"],
    },
)
"""A default value associated with an issue type within a context."""

IssueTypeDefaultValueUpdate = TypedDict(
    'IssueTypeDefaultValueUpdate',
    {
    'context_id': "int",
    'is_any_issue_type': NotRequired["bool | None"],
    'issue_type_id': NotRequired["str | None"],
    'value': NotRequired["CustomFieldContextDefaultValue"],
    },
)
"""A default value update for one issue-type scope in a context."""

IssueTypeDetails = TypedDict(
    'IssueTypeDetails',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str"],
    'entity_id': NotRequired["str"],
    'hierarchy_level': NotRequired["int"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    'subtask': NotRequired["bool"],
    },
)
"""Details about an issue type."""

IssueTypeHierarchyPayload = TypedDict(
    'IssueTypeHierarchyPayload',
    {
    'hierarchy_level': NotRequired["int"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["IssueTypeHierarchyPayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating an issue type hierarchy"""

type IssueTypeHierarchyPayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters"""

IssueTypeIds = TypedDict(
    'IssueTypeIds',
    {
    'issue_type_ids': "list[str]",
    },
)
"""The list of issue type IDs."""

IssueTypeIdsToRemove = TypedDict(
    'IssueTypeIdsToRemove',
    {
    'issue_type_ids': "list[str]",
    },
)
"""The list of issue type IDs to be removed from the field configuration scheme."""

IssueTypeInfo = TypedDict(
    'IssueTypeInfo',
    {
    'avatar_id': NotRequired["int"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    },
)
"""Details of an issue type."""

IssueTypeIssueCreateMetadata = TypedDict(
    'IssueTypeIssueCreateMetadata',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str"],
    'entity_id': NotRequired["str"],
    'expand': NotRequired["str"],
    'fields': NotRequired["dict[str, FieldMetadata]"],
    'hierarchy_level': NotRequired["int"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    'subtask': NotRequired["bool"],
    },
)
"""Details of the issue creation metadata for an issue type."""

IssueTypePayload = TypedDict(
    'IssueTypePayload',
    {
    'avatar_id': NotRequired["int | None"],
    'description': NotRequired["str | None"],
    'hierarchy_level': NotRequired["int"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["IssueTypePayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating an issue type"""

type IssueTypePayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters"""

IssueTypeProjectCreatePayload = TypedDict(
    'IssueTypeProjectCreatePayload',
    {
    'issue_type_hierarchy': NotRequired["list[IssueTypeHierarchyPayload | None] | None"],
    'issue_type_scheme': NotRequired["IssueTypeSchemePayload"],
    'issue_types': NotRequired["list[IssueTypePayload | None] | None"],
    },
)
"""The payload for creating issue types in a project"""

IssueTypeScheme = TypedDict(
    'IssueTypeScheme',
    {
    'default_issue_type_id': NotRequired["str"],
    'description': NotRequired["str"],
    'id': "str",
    'is_default': NotRequired["bool"],
    'name': "str",
    },
)
"""Details of an issue type scheme."""

IssueTypeSchemeDetails = TypedDict(
    'IssueTypeSchemeDetails',
    {
    'default_issue_type_id': NotRequired["str"],
    'description': NotRequired["str"],
    'issue_type_ids': "list[str]",
    'name': "str",
    },
)
"""Details of an issue type scheme and its associated issue types."""

IssueTypeSchemeId = TypedDict(
    'IssueTypeSchemeId',
    {
    'issue_type_scheme_id': "str",
    },
)
"""The ID of an issue type scheme."""

IssueTypeSchemeMapping = TypedDict(
    'IssueTypeSchemeMapping',
    {
    'issue_type_id': "str",
    'issue_type_scheme_id': "str",
    },
)
"""Issue type scheme item."""

IssueTypeSchemePayload = TypedDict(
    'IssueTypeSchemePayload',
    {
    'default_issue_type_id': NotRequired["ProjectCreateResourceIdentifier"],
    'description': NotRequired["str | None"],
    'issue_type_ids': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating issue type schemes"""

IssueTypeSchemeProjectAssociation = TypedDict(
    'IssueTypeSchemeProjectAssociation',
    {
    'issue_type_scheme_id': "str",
    'project_id': "str",
    },
)
"""Details of the association between an issue type scheme and project."""

IssueTypeSchemeProjects = TypedDict(
    'IssueTypeSchemeProjects',
    {
    'issue_type_scheme': "IssueTypeScheme",
    'project_ids': "list[str]",
    },
)
"""Issue type scheme with a list of the projects that use it."""

IssueTypeSchemeUpdateDetails = TypedDict(
    'IssueTypeSchemeUpdateDetails',
    {
    'default_issue_type_id': NotRequired["str"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of the name, description, and default issue type for an issue type scheme."""

IssueTypeScreenScheme = TypedDict(
    'IssueTypeScreenScheme',
    {
    'description': NotRequired["str"],
    'id': "str",
    'name': "str",
    },
)
"""Details of an issue type screen scheme."""

IssueTypeScreenSchemeDetails = TypedDict(
    'IssueTypeScreenSchemeDetails',
    {
    'description': NotRequired["str"],
    'issue_type_mappings': "list[IssueTypeScreenSchemeMapping]",
    'name': "str",
    },
)
"""The details of an issue type screen scheme."""

IssueTypeScreenSchemeId = TypedDict(
    'IssueTypeScreenSchemeId',
    {
    'id': "str",
    },
)
"""The ID of an issue type screen scheme."""

IssueTypeScreenSchemeItem = TypedDict(
    'IssueTypeScreenSchemeItem',
    {
    'issue_type_id': "str",
    'issue_type_screen_scheme_id': "str",
    'screen_scheme_id': "str",
    },
)
"""The screen scheme for an issue type."""

IssueTypeScreenSchemeMapping = TypedDict(
    'IssueTypeScreenSchemeMapping',
    {
    'issue_type_id': "str",
    'screen_scheme_id': "str",
    },
)
"""The IDs of the screen schemes for the issue type IDs."""

IssueTypeScreenSchemeMappingDetails = TypedDict(
    'IssueTypeScreenSchemeMappingDetails',
    {
    'issue_type_mappings': "list[IssueTypeScreenSchemeMapping]",
    },
)
"""A list of issue type screen scheme mappings."""

IssueTypeScreenSchemePayload = TypedDict(
    'IssueTypeScreenSchemePayload',
    {
    'default_screen_scheme': NotRequired["ProjectCreateResourceIdentifier"],
    'description': NotRequired["str"],
    'explicit_mappings': NotRequired["dict[str, ProjectCreateResourceIdentifier]"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""Defines the payload for the issue type screen schemes. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/\\#api-rest-api-3-issuetypescreenscheme-post"""

IssueTypeScreenSchemeProjectAssociation = TypedDict(
    'IssueTypeScreenSchemeProjectAssociation',
    {
    'issue_type_screen_scheme_id': NotRequired["str"],
    'project_id': NotRequired["str"],
    },
)
"""Associated issue type screen scheme and project."""

IssueTypeScreenSchemeUpdateDetails = TypedDict(
    'IssueTypeScreenSchemeUpdateDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of an issue type screen scheme."""

IssueTypeScreenSchemesProjects = TypedDict(
    'IssueTypeScreenSchemesProjects',
    {
    'issue_type_screen_scheme': "IssueTypeScreenScheme",
    'project_ids': "list[str]",
    },
)
"""Issue type screen scheme with a list of the projects that use it."""

IssueTypeToContextMapping = TypedDict(
    'IssueTypeToContextMapping',
    {
    'context_id': "str",
    'is_any_issue_type': NotRequired["bool"],
    'issue_type_id': NotRequired["str"],
    },
)
"""Mapping of an issue type to a context."""

IssueTypeUpdateBean = TypedDict(
    'IssueTypeUpdateBean',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)

IssueTypeWithStatus = TypedDict(
    'IssueTypeWithStatus',
    {
    'id': "str",
    'name': "str",
    'self': "str",
    'statuses': "list[StatusDetails]",
    'subtask': "bool",
    },
)
"""Status details for an issue type."""

IssueTypeWorkflowMapping = TypedDict(
    'IssueTypeWorkflowMapping',
    {
    'issue_type': NotRequired["str"],
    'update_draft_if_needed': NotRequired["bool"],
    'workflow': NotRequired["str"],
    },
)
"""Details about the mapping between an issue type and a workflow."""

IssueTypesWorkflowMapping = TypedDict(
    'IssueTypesWorkflowMapping',
    {
    'default_mapping': NotRequired["bool"],
    'issue_types': NotRequired["list[str]"],
    'update_draft_if_needed': NotRequired["bool"],
    'workflow': NotRequired["str"],
    },
)
"""Details about the mapping between issue types and a workflow."""

IssueUpdateDetails = TypedDict(
    'IssueUpdateDetails',
    {
    'fields': NotRequired["dict[str, Any]"],
    'history_metadata': NotRequired["HistoryMetadata"],
    'properties': NotRequired["list[EntityProperty]"],
    'transition': NotRequired["IssueTransition"],
    'update': NotRequired["dict[str, list[FieldUpdateOperation]]"],
    },
)
"""Details of an issue update request."""

IssueUpdateMetadata = TypedDict(
    'IssueUpdateMetadata',
    {
    'fields': NotRequired["dict[str, FieldMetadata]"],
    },
)
"""A list of editable field details."""

IssuesAndJqlQueries = TypedDict(
    'IssuesAndJqlQueries',
    {
    'issue_ids': "list[int]",
    'jqls': "list[str]",
    },
)
"""List of issues and JQL queries."""

IssuesJqlMetaDataBean = TypedDict(
    'IssuesJqlMetaDataBean',
    {
    'count': "int",
    'max_results': "int",
    'start_at': "int",
    'total_count': "int",
    'validation_warnings': NotRequired["list[str]"],
    },
)
"""The description of the page of issues loaded by the provided JQL query."""

IssuesMetaBean = TypedDict(
    'IssuesMetaBean',
    {
    'jql': NotRequired["IssuesJqlMetaDataBean"],
    },
)
"""Meta data describing the `issues` context variable."""

IssuesUpdateBean = TypedDict(
    'IssuesUpdateBean',
    {
    'issue_updates': NotRequired["list[IssueUpdateDetails]"],
    },
)

JExpEvaluateIssuesJqlMetaDataBean = TypedDict(
    'JExpEvaluateIssuesJqlMetaDataBean',
    {
    'is_last': NotRequired["bool"],
    'next_page_token': "str",
    },
)
"""The description of the page of issues loaded by the provided JQL query.This bean will be replacing IssuesJqlMetaDataBean bean as part of new `evaluate` endpoint"""

JExpEvaluateIssuesMetaBean = TypedDict(
    'JExpEvaluateIssuesMetaBean',
    {
    'jql': NotRequired["JExpEvaluateIssuesJqlMetaDataBean"],
    },
)
"""Meta data describing the `issues` context variable.This bean will be replacing IssuesMetaBean bean as part of new `evaluate` endpoint"""

JExpEvaluateJiraExpressionResultBean = TypedDict(
    'JExpEvaluateJiraExpressionResultBean',
    {
    'meta': NotRequired["JExpEvaluateMetaDataBean"],
    'value': "Any",
    },
)
"""The result of evaluating a Jira expression.This bean will be replacing `JiraExpressionResultBean` bean as part of new evaluate endpoint"""

JExpEvaluateMetaDataBean = TypedDict(
    'JExpEvaluateMetaDataBean',
    {
    'complexity': NotRequired["JiraExpressionsComplexityBean"],
    'issues': NotRequired["JExpEvaluateIssuesMetaBean"],
    },
)
"""Contains information about the expression evaluation. This bean will be replacing `JiraExpressionEvaluationMetaDataBean` bean as part of new `evaluate` endpoint"""

JexpEvaluateCtxIssues = TypedDict(
    'JexpEvaluateCtxIssues',
    {
    'jql': NotRequired["JexpEvaluateCtxJqlIssues"],
    },
)
"""The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. This bean will be replacing `JexpIssues` bean as part of new `evaluate` endpoint"""

JexpEvaluateCtxJqlIssues = TypedDict(
    'JexpEvaluateCtxJqlIssues',
    {
    'max_results': NotRequired["int"],
    'next_page_token': NotRequired["str"],
    'query': NotRequired["str"],
    },
)
"""The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. Not all issues returned by the JQL query are loaded, only those described by the `nextPageToken` and `maxResults` properties. This bean will be replacing JexpJqlIssues bean as part of new `evaluate` endpoint"""

JexpIssues = TypedDict(
    'JexpIssues',
    {
    'jql': NotRequired["JexpJqlIssues"],
    },
)
"""The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable."""

JexpJqlIssues = TypedDict(
    'JexpJqlIssues',
    {
    'max_results': NotRequired["int"],
    'query': NotRequired["str"],
    'start_at': NotRequired["int"],
    'validation': NotRequired["JexpJqlIssuesValidation"],
    },
)
"""The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. Not all issues returned by the JQL query are loaded, only those described by the `startAt` and `maxResults` properties. To determine whether it is necessary to iterate to ensure all the issues returned by the JQL query are evaluated, inspect `meta.issues.jql.count` in the response."""

type JexpJqlIssuesValidation = Literal['strict', 'warn', 'none']
"""Determines how to validate the JQL query and treat the validation results."""

JiraCascadingSelectField = TypedDict(
    'JiraCascadingSelectField',
    {
    'child_option_value': NotRequired["JiraSelectedOptionField"],
    'field_id': "str",
    'parent_option_value': "JiraSelectedOptionField",
    },
)

JiraColorField = TypedDict(
    'JiraColorField',
    {
    'color': "JiraColorInput",
    'field_id': "str",
    },
)

JiraColorInput = TypedDict(
    'JiraColorInput',
    {
    'name': "str",
    },
)

JiraComponentField = TypedDict(
    'JiraComponentField',
    {
    'component_id': "int",
    },
)

JiraDateField = TypedDict(
    'JiraDateField',
    {
    'date': NotRequired["JiraDateInput"],
    'field_id': "str",
    },
)

JiraDateInput = TypedDict(
    'JiraDateInput',
    {
    'formatted_date': "str",
    },
)

JiraDateTimeField = TypedDict(
    'JiraDateTimeField',
    {
    'date_time': "JiraDateTimeInput",
    'field_id': "str",
    },
)

JiraDateTimeInput = TypedDict(
    'JiraDateTimeInput',
    {
    'formatted_date_time': "str",
    },
)

JiraDurationField = TypedDict(
    'JiraDurationField',
    {
    'original_estimate_field': "str",
    },
)

JiraExpressionAnalysis = TypedDict(
    'JiraExpressionAnalysis',
    {
    'complexity': NotRequired["JiraExpressionComplexity"],
    'errors': NotRequired["list[JiraExpressionValidationError]"],
    'expression': "str",
    'type': NotRequired["str"],
    'valid': "bool",
    },
)
"""Details about the analysed Jira expression."""

JiraExpressionComplexity = TypedDict(
    'JiraExpressionComplexity',
    {
    'expensive_operations': "str",
    'variables': NotRequired["dict[str, str]"],
    },
)
"""Details about the complexity of the analysed Jira expression."""

JiraExpressionEvalContextBean = TypedDict(
    'JiraExpressionEvalContextBean',
    {
    'board': NotRequired["int"],
    'custom': NotRequired["list[CustomContextVariable]"],
    'customer_request': NotRequired["int"],
    'issue': NotRequired["IdOrKeyBean"],
    'issues': NotRequired["JexpIssues"],
    'project': NotRequired["IdOrKeyBean"],
    'service_desk': NotRequired["int"],
    'sprint': NotRequired["int"],
    },
)

JiraExpressionEvalRequestBean = TypedDict(
    'JiraExpressionEvalRequestBean',
    {
    'context': NotRequired["JiraExpressionEvalContextBean"],
    'expression': "str",
    },
)

JiraExpressionEvaluateContextBean = TypedDict(
    'JiraExpressionEvaluateContextBean',
    {
    'board': NotRequired["int"],
    'custom': NotRequired["list[CustomContextVariable]"],
    'customer_request': NotRequired["int"],
    'issue': NotRequired["IdOrKeyBean"],
    'issues': NotRequired["JexpEvaluateCtxIssues"],
    'project': NotRequired["IdOrKeyBean"],
    'service_desk': NotRequired["int"],
    'sprint': NotRequired["int"],
    },
)

JiraExpressionEvaluateRequestBean = TypedDict(
    'JiraExpressionEvaluateRequestBean',
    {
    'context': NotRequired["JiraExpressionEvaluateContextBean"],
    'expression': "str",
    },
)
"""The request to evaluate a Jira expression. This bean will be replacing `JiraExpressionEvaluateRequest` as part of new `evaluate` endpoint"""

JiraExpressionEvaluationMetaDataBean = TypedDict(
    'JiraExpressionEvaluationMetaDataBean',
    {
    'complexity': NotRequired["JiraExpressionsComplexityBean"],
    'issues': NotRequired["IssuesMetaBean"],
    },
)

JiraExpressionForAnalysis = TypedDict(
    'JiraExpressionForAnalysis',
    {
    'context_variables': NotRequired["dict[str, str]"],
    'expressions': "list[str]",
    },
)
"""Details of Jira expressions for analysis."""

JiraExpressionResult = TypedDict(
    'JiraExpressionResult',
    {
    'meta': NotRequired["JiraExpressionEvaluationMetaDataBean"],
    'value': "Any",
    },
)
"""The result of evaluating a Jira expression."""

JiraExpressionValidationError = TypedDict(
    'JiraExpressionValidationError',
    {
    'column': NotRequired["int"],
    'expression': NotRequired["str"],
    'line': NotRequired["int"],
    'message': "str",
    'type': "JiraExpressionValidationErrorType",
    },
)
"""
Details about syntax and type errors. The error details apply to the entire expression, unless the object includes:

 *  `line` and `column`
 *  `expression`
"""

type JiraExpressionValidationErrorType = Literal['syntax', 'type', 'other']
"""The error type."""

JiraExpressionsAnalysis = TypedDict(
    'JiraExpressionsAnalysis',
    {
    'results': "list[JiraExpressionAnalysis]",
    },
)
"""Details about the analysed Jira expression."""

JiraExpressionsComplexityBean = TypedDict(
    'JiraExpressionsComplexityBean',
    {
    'beans': "JiraExpressionsComplexityValueBean",
    'expensive_operations': "JiraExpressionsComplexityValueBean",
    'primitive_values': "JiraExpressionsComplexityValueBean",
    'steps': "JiraExpressionsComplexityValueBean",
    },
)

JiraExpressionsComplexityValueBean = TypedDict(
    'JiraExpressionsComplexityValueBean',
    {
    'limit': "int",
    'value': "int",
    },
)

JiraGroupInput = TypedDict(
    'JiraGroupInput',
    {
    'group_name': "str",
    },
)

JiraIssueFields = TypedDict(
    'JiraIssueFields',
    {
    'cascading_select_fields': NotRequired["list[JiraCascadingSelectField]"],
    'clearable_number_fields': NotRequired["list[JiraNumberField]"],
    'color_fields': NotRequired["list[JiraColorField]"],
    'date_picker_fields': NotRequired["list[JiraDateField]"],
    'date_time_picker_fields': NotRequired["list[JiraDateTimeField]"],
    'issue_type': NotRequired["JiraIssueTypeField"],
    'labels_fields': NotRequired["list[JiraLabelsField]"],
    'multiple_group_picker_fields': NotRequired["list[JiraMultipleGroupPickerField]"],
    'multiple_select_clearable_user_picker_fields': NotRequired["list[JiraMultipleSelectUserPickerField]"],
    'multiple_select_fields': NotRequired["list[JiraMultipleSelectField]"],
    'multiple_version_picker_fields': NotRequired["list[JiraMultipleVersionPickerField]"],
    'multiselect_components': NotRequired["JiraMultiSelectComponentField"],
    'original_estimate_field': NotRequired["JiraDurationField"],
    'priority': NotRequired["JiraPriorityField"],
    'rich_text_fields': NotRequired["list[JiraRichTextField]"],
    'single_group_picker_fields': NotRequired["list[JiraSingleGroupPickerField]"],
    'single_line_text_fields': NotRequired["list[JiraSingleLineTextField]"],
    'single_select_clearable_user_picker_fields': NotRequired["list[JiraSingleSelectUserPickerField]"],
    'single_select_fields': NotRequired["list[JiraSingleSelectField]"],
    'single_version_picker_fields': NotRequired["list[JiraSingleVersionPickerField]"],
    'status': NotRequired["JiraStatusInput"],
    'time_tracking_field': NotRequired["JiraTimeTrackingField"],
    'url_fields': NotRequired["list[JiraUrlField]"],
    },
)

JiraIssueTypeField = TypedDict(
    'JiraIssueTypeField',
    {
    'issue_type_id': "str",
    },
)

JiraLabelPropertiesInputJackson1 = TypedDict(
    'JiraLabelPropertiesInputJackson1',
    {
    'color': NotRequired["JiraLabelPropertiesInputJackson1Color"],
    'name': NotRequired["str"],
    },
)

type JiraLabelPropertiesInputJackson1Color = Literal['GREY_LIGHTEST', 'GREY_LIGHTER', 'GREY', 'GREY_DARKER', 'GREY_DARKEST', 'PURPLE_LIGHTEST', 'PURPLE_LIGHTER', 'PURPLE', 'PURPLE_DARKER', 'PURPLE_DARKEST', 'BLUE_LIGHTEST', 'BLUE_LIGHTER', 'BLUE', 'BLUE_DARKER', 'BLUE_DARKEST', 'TEAL_LIGHTEST', 'TEAL_LIGHTER', 'TEAL', 'TEAL_DARKER', 'TEAL_DARKEST', 'GREEN_LIGHTEST', 'GREEN_LIGHTER', 'GREEN', 'GREEN_DARKER', 'GREEN_DARKEST', 'LIME_LIGHTEST', 'LIME_LIGHTER', 'LIME', 'LIME_DARKER', 'LIME_DARKEST', 'YELLOW_LIGHTEST', 'YELLOW_LIGHTER', 'YELLOW', 'YELLOW_DARKER', 'YELLOW_DARKEST', 'ORANGE_LIGHTEST', 'ORANGE_LIGHTER', 'ORANGE', 'ORANGE_DARKER', 'ORANGE_DARKEST', 'RED_LIGHTEST', 'RED_LIGHTER', 'RED', 'RED_DARKER', 'RED_DARKEST', 'MAGENTA_LIGHTEST', 'MAGENTA_LIGHTER', 'MAGENTA', 'MAGENTA_DARKER', 'MAGENTA_DARKEST']

JiraLabelsField = TypedDict(
    'JiraLabelsField',
    {
    'bulk_edit_multi_select_field_option': "JiraLabelsFieldBulkEditMultiSelectFieldOption",
    'field_id': "str",
    'label_properties': NotRequired["list[JiraLabelPropertiesInputJackson1]"],
    'labels': "list[JiraLabelsInput]",
    },
)

type JiraLabelsFieldBulkEditMultiSelectFieldOption = Literal['ADD', 'REMOVE', 'REPLACE', 'REMOVE_ALL']

JiraLabelsInput = TypedDict(
    'JiraLabelsInput',
    {
    'name': "str",
    },
)

JiraMultiSelectComponentField = TypedDict(
    'JiraMultiSelectComponentField',
    {
    'bulk_edit_multi_select_field_option': "JiraMultiSelectComponentFieldBulkEditMultiSelectFieldOption",
    'components': "list[JiraComponentField]",
    'field_id': "str",
    },
)

type JiraMultiSelectComponentFieldBulkEditMultiSelectFieldOption = Literal['ADD', 'REMOVE', 'REPLACE', 'REMOVE_ALL']

JiraMultipleGroupPickerField = TypedDict(
    'JiraMultipleGroupPickerField',
    {
    'field_id': "str",
    'groups': "list[JiraGroupInput]",
    },
)

JiraMultipleSelectField = TypedDict(
    'JiraMultipleSelectField',
    {
    'field_id': "str",
    'options': "list[JiraSelectedOptionField]",
    },
)

JiraMultipleSelectUserPickerField = TypedDict(
    'JiraMultipleSelectUserPickerField',
    {
    'field_id': "str",
    'users': NotRequired["list[JiraUserField]"],
    },
)

JiraMultipleVersionPickerField = TypedDict(
    'JiraMultipleVersionPickerField',
    {
    'bulk_edit_multi_select_field_option': "JiraMultipleVersionPickerFieldBulkEditMultiSelectFieldOption",
    'field_id': "str",
    'versions': "list[JiraVersionField]",
    },
)

type JiraMultipleVersionPickerFieldBulkEditMultiSelectFieldOption = Literal['ADD', 'REMOVE', 'REPLACE', 'REMOVE_ALL']

JiraNumberField = TypedDict(
    'JiraNumberField',
    {
    'field_id': "str",
    'value': NotRequired["float"],
    },
)

JiraPriorityField = TypedDict(
    'JiraPriorityField',
    {
    'priority_id': "str",
    },
)

JiraRichTextField = TypedDict(
    'JiraRichTextField',
    {
    'field_id': "str",
    'rich_text': "JiraRichTextInput",
    },
)

JiraRichTextInput = TypedDict(
    'JiraRichTextInput',
    {
    'adf_value': NotRequired["dict[str, Any]"],
    },
)

JiraSelectedOptionField = TypedDict(
    'JiraSelectedOptionField',
    {
    'option_id': NotRequired["int"],
    },
)

JiraSingleGroupPickerField = TypedDict(
    'JiraSingleGroupPickerField',
    {
    'field_id': "str",
    'group': "JiraGroupInput",
    },
)

JiraSingleLineTextField = TypedDict(
    'JiraSingleLineTextField',
    {
    'field_id': "str",
    'text': "str",
    },
)

JiraSingleSelectField = TypedDict(
    'JiraSingleSelectField',
    {
    'field_id': "str",
    'option': "JiraSelectedOptionField",
    },
)
"""
Add or clear a single select field:

 *  To add, specify the option with an `optionId`.
 *  To clear, pass an option with `optionId` as `-1`.
"""

JiraSingleSelectUserPickerField = TypedDict(
    'JiraSingleSelectUserPickerField',
    {
    'field_id': "str",
    'user': NotRequired["JiraUserField"],
    },
)

JiraSingleVersionPickerField = TypedDict(
    'JiraSingleVersionPickerField',
    {
    'field_id': "str",
    'version': "JiraVersionField",
    },
)

JiraStatus = TypedDict(
    'JiraStatus',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["StatusScope"],
    'status_category': NotRequired["JiraStatusStatusCategory"],
    },
)
"""Details of a status."""

JiraStatusInput = TypedDict(
    'JiraStatusInput',
    {
    'status_id': "str",
    },
)

type JiraStatusStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

JiraTimeTrackingField = TypedDict(
    'JiraTimeTrackingField',
    {
    'time_remaining': "str",
    },
)

JiraUrlField = TypedDict(
    'JiraUrlField',
    {
    'field_id': "str",
    'url': "str",
    },
)

JiraUserField = TypedDict(
    'JiraUserField',
    {
    'account_id': "str",
    },
)

JiraVersionField = TypedDict(
    'JiraVersionField',
    {
    'version_id': NotRequired["str"],
    },
)

JiraWorkflow = TypedDict(
    'JiraWorkflow',
    {
    'created': NotRequired["str | None"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'is_editable': NotRequired["bool"],
    'looped_transition_container_layout': NotRequired["WorkflowLayout | None"],
    'name': NotRequired["str"],
    'scope': NotRequired["WorkflowScope"],
    'start_point_layout': NotRequired["WorkflowLayout | None"],
    'statuses': NotRequired["list[WorkflowReferenceStatus]"],
    'task_id': NotRequired["str | None"],
    'transitions': NotRequired["list[WorkflowTransitions]"],
    'updated': NotRequired["str | None"],
    'version': NotRequired["DocumentVersion"],
    },
)
"""Details of a workflow."""

JiraWorkflowPreviewStatus = TypedDict(
    'JiraWorkflowPreviewStatus',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'raw_name': NotRequired["str"],
    'scope': NotRequired["WorkflowPreviewScope"],
    'status_category': NotRequired["JiraWorkflowPreviewStatusStatusCategory"],
    'status_reference': NotRequired["str"],
    },
)
"""Details of a status."""

type JiraWorkflowPreviewStatusStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

JiraWorkflowStatus = TypedDict(
    'JiraWorkflowStatus',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["WorkflowScope"],
    'status_category': NotRequired["JiraWorkflowStatusStatusCategory"],
    'status_reference': NotRequired["str"],
    },
)
"""Details of a status."""

type JiraWorkflowStatusStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

JqlCountRequestBean = TypedDict(
    'JqlCountRequestBean',
    {
    'jql': NotRequired["str"],
    },
)

JqlCountResultsBean = TypedDict(
    'JqlCountResultsBean',
    {
    'count': NotRequired["int"],
    },
)

JqlFunctionPrecomputationBean = TypedDict(
    'JqlFunctionPrecomputationBean',
    {
    'arguments': NotRequired["list[str]"],
    'created': NotRequired["str"],
    'error': NotRequired["str"],
    'field': NotRequired["str"],
    'function_key': NotRequired["str"],
    'function_name': NotRequired["str"],
    'id': NotRequired["str"],
    'operator': NotRequired["str"],
    'updated': NotRequired["str"],
    'used': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""Jql function precomputation."""

JqlFunctionPrecomputationGetByIdRequest = TypedDict(
    'JqlFunctionPrecomputationGetByIdRequest',
    {
    'precomputation_i_ds': NotRequired["list[str]"],
    },
)
"""Request to fetch precomputations by ID."""

JqlFunctionPrecomputationGetByIdResponse = TypedDict(
    'JqlFunctionPrecomputationGetByIdResponse',
    {
    'not_found_precomputation_i_ds': NotRequired["list[str]"],
    'precomputations': NotRequired["list[JqlFunctionPrecomputationBean]"],
    },
)
"""Get precomputations by ID response."""

JqlFunctionPrecomputationUpdateBean = TypedDict(
    'JqlFunctionPrecomputationUpdateBean',
    {
    'error': NotRequired["str"],
    'id': "str",
    'value': NotRequired["str"],
    },
)
"""Precomputation id and its new value."""

JqlFunctionPrecomputationUpdateErrorResponse = TypedDict(
    'JqlFunctionPrecomputationUpdateErrorResponse',
    {
    'error_messages': NotRequired["list[str]"],
    'not_found_precomputation_i_ds': NotRequired["list[str]"],
    },
)
"""Error response returned updating JQL Function precomputations fails."""

JqlFunctionPrecomputationUpdateRequestBean = TypedDict(
    'JqlFunctionPrecomputationUpdateRequestBean',
    {
    'values': NotRequired["list[JqlFunctionPrecomputationUpdateBean]"],
    },
)
"""List of pairs (id and value) for precomputation updates."""

JqlFunctionPrecomputationUpdateResponse = TypedDict(
    'JqlFunctionPrecomputationUpdateResponse',
    {
    'not_found_precomputation_i_ds': NotRequired["list[str]"],
    },
)
"""Result of updating JQL Function precomputations."""

JqlPersonalDataMigrationRequest = TypedDict(
    'JqlPersonalDataMigrationRequest',
    {
    'query_strings': NotRequired["list[str]"],
    },
)
"""The JQL queries to be converted."""

JqlQueriesToParse = TypedDict(
    'JqlQueriesToParse',
    {
    'queries': "list[str]",
    },
)
"""A list of JQL queries to parse."""

JqlQueriesToSanitize = TypedDict(
    'JqlQueriesToSanitize',
    {
    'queries': "list[JqlQueryToSanitize]",
    },
)
"""The list of JQL queries to sanitize for the given account IDs."""

JqlQuery = TypedDict(
    'JqlQuery',
    {
    'order_by': NotRequired["JqlQueryOrderByClause"],
    'where': NotRequired["JqlQueryClause"],
    },
)
"""A parsed JQL query."""

type JqlQueryClause = CompoundClause | FieldValueClause | FieldWasClause | FieldChangedClause
"""A JQL query clause."""

type JqlQueryClauseOperand = ListOperand | ValueOperand | FunctionOperand | KeywordOperand
"""Details of an operand in a JQL clause."""

JqlQueryClauseTimePredicate = TypedDict(
    'JqlQueryClauseTimePredicate',
    {
    'operand': "JqlQueryClauseOperand",
    'operator': "JqlQueryClauseTimePredicateOperator",
    },
)
"""A time predicate for a temporal JQL clause."""

type JqlQueryClauseTimePredicateOperator = Literal['before', 'after', 'from', 'to', 'on', 'during', 'by']
"""The operator between the field and the operand."""

JqlQueryField = TypedDict(
    'JqlQueryField',
    {
    'encoded_name': NotRequired["str"],
    'name': "str",
    'property': NotRequired["list[JqlQueryFieldEntityProperty]"],
    },
)
"""A field used in a JQL query. See [Advanced searching - fields reference](https://confluence.atlassian.com/x/dAiiLQ) for more information about fields in JQL queries."""

JqlQueryFieldEntityProperty = TypedDict(
    'JqlQueryFieldEntityProperty',
    {
    'entity': "str",
    'key': "str",
    'path': "str",
    'type': NotRequired["JqlQueryFieldEntityPropertyType"],
    },
)
"""Details of an entity property."""

type JqlQueryFieldEntityPropertyType = Literal['number', 'string', 'text', 'date', 'user']
"""The type of the property value extraction. Not available if the extraction for the property is not registered on the instance with the [Entity property](https://developer.atlassian.com/cloud/jira/platform/modules/entity-property/) module."""

JqlQueryOrderByClause = TypedDict(
    'JqlQueryOrderByClause',
    {
    'fields': "list[JqlQueryOrderByClauseElement]",
    },
)
"""Details of the order-by JQL clause."""

JqlQueryOrderByClauseElement = TypedDict(
    'JqlQueryOrderByClauseElement',
    {
    'direction': NotRequired["JqlQueryOrderByClauseElementDirection"],
    'field': "JqlQueryField",
    },
)
"""An element of the order-by JQL clause."""

type JqlQueryOrderByClauseElementDirection = Literal['asc', 'desc']
"""The direction in which to order the results."""

JqlQueryToSanitize = TypedDict(
    'JqlQueryToSanitize',
    {
    'account_id': NotRequired["str | None"],
    'query': "str",
    },
)
"""The JQL query to sanitize for the account ID. If the account ID is null, sanitizing is performed for an anonymous user."""

type JqlQueryUnitaryOperand = ValueOperand | FunctionOperand | KeywordOperand
"""An operand that can be part of a list operand."""

JqlQueryWithUnknownUsers = TypedDict(
    'JqlQueryWithUnknownUsers',
    {
    'converted_query': NotRequired["str"],
    'original_query': NotRequired["str"],
    },
)
"""JQL queries that contained users that could not be found"""

JqlReferenceData = TypedDict(
    'JqlReferenceData',
    {
    'jql_reserved_words': NotRequired["list[str]"],
    'visible_field_names': NotRequired["list[FieldReferenceData]"],
    'visible_function_names': NotRequired["list[FunctionReferenceData]"],
    },
)
"""Lists of JQL reference data."""

JsonContextVariable = TypedDict(
    'JsonContextVariable',
    {
    'type': "str",
    'value': NotRequired["dict[str, Any]"],
    },
)
"""A JSON object with custom content."""

JsonNode = TypedDict(
    'JsonNode',
    {
    'array': NotRequired["bool"],
    'big_decimal': NotRequired["bool"],
    'big_integer': NotRequired["bool"],
    'big_integer_value': NotRequired["int"],
    'binary': NotRequired["bool"],
    'binary_value': NotRequired["list[str]"],
    'boolean': NotRequired["bool"],
    'boolean_value': NotRequired["bool"],
    'container_node': NotRequired["bool"],
    'decimal_value': NotRequired["float"],
    'double': NotRequired["bool"],
    'double_value': NotRequired["float"],
    'elements': NotRequired["dict[str, Any]"],
    'field_names': NotRequired["dict[str, Any]"],
    'fields': NotRequired["dict[str, Any]"],
    'floating_point_number': NotRequired["bool"],
    'int': NotRequired["bool"],
    'int_value': NotRequired["int"],
    'integral_number': NotRequired["bool"],
    'long': NotRequired["bool"],
    'long_value': NotRequired["int"],
    'missing_node': NotRequired["bool"],
    'null': NotRequired["bool"],
    'number': NotRequired["bool"],
    'number_type': NotRequired["JsonNodeNumberType"],
    'number_value': NotRequired["float"],
    'object': NotRequired["bool"],
    'pojo': NotRequired["bool"],
    'text_value': NotRequired["str"],
    'textual': NotRequired["bool"],
    'value_as_boolean': NotRequired["bool"],
    'value_as_double': NotRequired["float"],
    'value_as_int': NotRequired["int"],
    'value_as_long': NotRequired["int"],
    'value_as_text': NotRequired["str"],
    'value_node': NotRequired["bool"],
    },
)

type JsonNodeNumberType = Literal['INT', 'LONG', 'BIG_INTEGER', 'FLOAT', 'DOUBLE', 'BIG_DECIMAL']

JsonTypeBean = TypedDict(
    'JsonTypeBean',
    {
    'configuration': NotRequired["dict[str, Any]"],
    'custom': NotRequired["str"],
    'custom_id': NotRequired["int"],
    'items': NotRequired["str"],
    'system': NotRequired["str"],
    'type': "str",
    },
)
"""The schema of a field."""

KeywordOperand = TypedDict(
    'KeywordOperand',
    {
    'keyword': "KeywordOperandKeyword",
    },
)
"""An operand that is a JQL keyword. See [Advanced searching - keywords reference](https://confluence.atlassian.com/jiracorecloud/advanced-searching-keywords-reference-765593717.html#Advancedsearching-keywordsreference-EMPTYEMPTY) for more information about operand keywords."""

type KeywordOperandKeyword = Literal['empty']
"""The keyword that is the operand value."""

License = TypedDict(
    'License',
    {
    'applications': "list[LicensedApplication]",
    },
)
"""Details about a license for the Jira instance."""

LicenseMetric = TypedDict(
    'LicenseMetric',
    {
    'key': NotRequired["str"],
    'value': NotRequired["str"],
    },
)
"""A metric that provides insight into the active licence details"""

LicensedApplication = TypedDict(
    'LicensedApplication',
    {
    'id': "str",
    'plan': "LicensedApplicationPlan",
    },
)
"""Details about a licensed Jira application."""

type LicensedApplicationPlan = Literal['UNLICENSED', 'FREE', 'PAID']
"""The licensing plan."""

LimitExceededResponseBean = TypedDict(
    'LimitExceededResponseBean',
    {
    'current_count': NotRequired["int"],
    'entity_type': NotRequired["str"],
    'error_code': NotRequired["str"],
    'limit_type': NotRequired["str"],
    'max_allowed_limit': NotRequired["int"],
    'message': NotRequired["str"],
    'scope_id': NotRequired["str"],
    },
)

LinkGroup = TypedDict(
    'LinkGroup',
    {
    'groups': NotRequired["list[LinkGroup]"],
    'header': NotRequired["SimpleLink"],
    'id': NotRequired["str"],
    'links': NotRequired["list[SimpleLink]"],
    'style_class': NotRequired["str"],
    'weight': NotRequired["int"],
    },
)
"""Details a link group, which defines issue operations."""

LinkIssueRequestJsonBean = TypedDict(
    'LinkIssueRequestJsonBean',
    {
    'comment': NotRequired["Comment"],
    'inward_issue': "LinkedIssue",
    'outward_issue': "LinkedIssue",
    'type': "IssueLinkType",
    },
)

LinkedIssue = TypedDict(
    'LinkedIssue',
    {
    'fields': NotRequired["Fields"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""The ID or key of a linked issue."""

ListOperand = TypedDict(
    'ListOperand',
    {
    'encoded_operand': NotRequired["str"],
    'values': "list[JqlQueryUnitaryOperand]",
    },
)
"""An operand that is a list of values."""

type ListWrapperCallbackApplicationRole = dict[str, Any]

type ListWrapperCallbackGroupName = dict[str, Any]

Locale = TypedDict(
    'Locale',
    {
    'locale': NotRequired["str"],
    },
)
"""Details of a locale."""

MappingsByIssueTypeOverride = TypedDict(
    'MappingsByIssueTypeOverride',
    {
    'issue_type_id': NotRequired["str"],
    'status_mappings': NotRequired["list[WorkflowAssociationStatusMapping]"],
    },
)
"""The mappings for migrating issues from old statuses to new statuses when switching from one workflow scheme to another. This field is required if any statuses in the current project's workflows would no longer exist in the target workflow scheme. Each mapping defines how to update issues from an old status to the corresponding new status in the issue’s new workflow."""

MappingsByWorkflow = TypedDict(
    'MappingsByWorkflow',
    {
    'new_workflow_id': "str",
    'old_workflow_id': "str",
    'status_mappings': "list[WorkflowAssociationStatusMapping]",
    },
)
"""The status mappings by workflows. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`."""

type MigrationResourceUpdateEntityPropertiesValuePutEntityType = Literal['IssueProperty', 'CommentProperty', 'DashboardItemProperty', 'IssueTypeProperty', 'ProjectProperty', 'UserProperty', 'WorklogProperty', 'BoardProperty', 'SprintProperty']

MinimalFieldSchemeToFieldsPartialFailure = TypedDict(
    'MinimalFieldSchemeToFieldsPartialFailure',
    {
    'error': NotRequired["str"],
    'field_id': "str",
    'scheme_id': "int",
    'success': "bool",
    },
)
"""Minimal partial failure result when updating field scheme to fields associations."""

MinimalFieldSchemeToFieldsResponse = TypedDict(
    'MinimalFieldSchemeToFieldsResponse',
    {
    'results': "list[MinimalFieldSchemeToFieldsPartialFailure]",
    },
)
"""Minimal response for updating field scheme to fields associations."""

MoveFieldBean = TypedDict(
    'MoveFieldBean',
    {
    'after': NotRequired["str"],
    'position': NotRequired["MoveFieldBeanPosition"],
    },
)

type MoveFieldBeanPosition = Literal['Earlier', 'Later', 'First', 'Last']
"""The named position to which the screen tab field should be moved. Required if `after` isn't provided."""

MultiIssueEntityProperties = TypedDict(
    'MultiIssueEntityProperties',
    {
    'issues': NotRequired["list[IssueEntityPropertiesForMultiUpdate]"],
    },
)
"""A list of issues and their respective properties to set or update. See [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information."""

MultipleCustomFieldValuesUpdate = TypedDict(
    'MultipleCustomFieldValuesUpdate',
    {
    'custom_field': "str",
    'issue_ids': "list[int]",
    'value': "Any",
    },
)
"""A custom field and its new value with a list of issue to update."""

MultipleCustomFieldValuesUpdateDetails = TypedDict(
    'MultipleCustomFieldValuesUpdateDetails',
    {
    'updates': NotRequired["list[MultipleCustomFieldValuesUpdate]"],
    },
)
"""List of updates for a custom fields."""

NestedResponse = TypedDict(
    'NestedResponse',
    {
    'error_collection': NotRequired["ErrorCollection"],
    'status': NotRequired["int"],
    'warning_collection': NotRequired["WarningCollection"],
    },
)

NewUserDetails = TypedDict(
    'NewUserDetails',
    {
    'application_keys': NotRequired["list[str]"],
    'display_name': NotRequired["str"],
    'email_address': "str",
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'password': NotRequired["str"],
    'products': "list[str]",
    'self': NotRequired["str"],
    },
)
"""The user details."""

NonWorkingDay = TypedDict(
    'NonWorkingDay',
    {
    'id': NotRequired["int"],
    'iso_8601_date': NotRequired["str"],
    },
)

Notification = TypedDict(
    'Notification',
    {
    'html_body': NotRequired["str"],
    'restrict': NotRequired["NotificationRecipientsRestrictions"],
    'subject': NotRequired["str"],
    'text_body': NotRequired["str"],
    'to': NotRequired["NotificationRecipients"],
    },
)
"""Details about a notification."""

NotificationEvent = TypedDict(
    'NotificationEvent',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'template_event': NotRequired["NotificationEvent"],
    },
)
"""Details about a notification event."""

NotificationRecipients = TypedDict(
    'NotificationRecipients',
    {
    'assignee': NotRequired["bool"],
    'group_ids': NotRequired["list[str]"],
    'groups': NotRequired["list[GroupName]"],
    'reporter': NotRequired["bool"],
    'users': NotRequired["list[UserDetails]"],
    'voters': NotRequired["bool"],
    'watchers': NotRequired["bool"],
    },
)
"""Details of the users and groups to receive the notification."""

NotificationRecipientsRestrictions = TypedDict(
    'NotificationRecipientsRestrictions',
    {
    'group_ids': NotRequired["list[str]"],
    'groups': NotRequired["list[GroupName]"],
    'permissions': NotRequired["list[RestrictedPermission]"],
    },
)
"""Details of the group membership or permissions needed to receive the notification."""

NotificationScheme = TypedDict(
    'NotificationScheme',
    {
    'description': NotRequired["str"],
    'expand': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'notification_scheme_events': NotRequired["list[NotificationSchemeEvent]"],
    'projects': NotRequired["list[int]"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    },
)
"""Details about a notification scheme."""

NotificationSchemeAndProjectMappingJsonBean = TypedDict(
    'NotificationSchemeAndProjectMappingJsonBean',
    {
    'notification_scheme_id': NotRequired["str"],
    'project_id': NotRequired["str"],
    },
)

NotificationSchemeEvent = TypedDict(
    'NotificationSchemeEvent',
    {
    'event': NotRequired["NotificationEvent"],
    'notifications': NotRequired["list[EventNotification]"],
    },
)
"""Details about a notification scheme event."""

NotificationSchemeEventDetails = TypedDict(
    'NotificationSchemeEventDetails',
    {
    'event': "NotificationSchemeEventTypeId",
    'notifications': "list[NotificationSchemeNotificationDetails]",
    },
)
"""Details of a notification scheme event."""

NotificationSchemeEventIdPayload = TypedDict(
    'NotificationSchemeEventIdPayload',
    {
    'id': NotRequired["str"],
    },
)
"""The event ID to use for reference in the payload"""

NotificationSchemeEventPayload = TypedDict(
    'NotificationSchemeEventPayload',
    {
    'event': NotRequired["NotificationSchemeEventIdPayload"],
    'notifications': NotRequired["list[NotificationSchemeNotificationDetailsPayload]"],
    },
)
"""The payload for creating a notification scheme event. Defines which notifications should be sent for a specific event"""

NotificationSchemeEventTypeId = TypedDict(
    'NotificationSchemeEventTypeId',
    {
    'id': "str",
    },
)
"""The ID of an event that is being mapped to notifications."""

NotificationSchemeId = TypedDict(
    'NotificationSchemeId',
    {
    'id': "str",
    },
)
"""The ID of a notification scheme."""

NotificationSchemeNotificationDetails = TypedDict(
    'NotificationSchemeNotificationDetails',
    {
    'notification_type': "str",
    'parameter': NotRequired["str"],
    },
)
"""Details of a notification within a notification scheme."""

NotificationSchemeNotificationDetailsPayload = TypedDict(
    'NotificationSchemeNotificationDetailsPayload',
    {
    'notification_type': NotRequired["str"],
    'parameter': NotRequired["str"],
    },
)
"""The configuration for notification recipents"""

NotificationSchemePayload = TypedDict(
    'NotificationSchemePayload',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'notification_scheme_events': NotRequired["list[NotificationSchemeEventPayload]"],
    'on_conflict': NotRequired["NotificationSchemePayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating a notification scheme. The user has to supply the ID for the default notification scheme. For CMP this is provided in the project payload and should be left empty, for TMP it's provided using this payload"""

type NotificationSchemePayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use when there is a conflict with an existing entity"""

OldToNewSecurityLevelMappingsBean = TypedDict(
    'OldToNewSecurityLevelMappingsBean',
    {
    'new_level_id': "str",
    'old_level_id': "str",
    },
)

OperationMessage = TypedDict(
    'OperationMessage',
    {
    'message': "str",
    'status_code': "int",
    },
)

Operations = TypedDict(
    'Operations',
    {
    'link_groups': NotRequired["list[LinkGroup]"],
    },
)
"""Details of the operations that can be performed on the issue."""

OrderOfCustomFieldOptions = TypedDict(
    'OrderOfCustomFieldOptions',
    {
    'after': NotRequired["str"],
    'custom_field_option_ids': "list[str]",
    'position': NotRequired["OrderOfCustomFieldOptionsPosition"],
    },
)
"""An ordered list of custom field option IDs and information on where to move them."""

type OrderOfCustomFieldOptionsPosition = Literal['First', 'Last']
"""The position the custom field options should be moved to. Required if `after` isn't provided."""

OrderOfIssueTypes = TypedDict(
    'OrderOfIssueTypes',
    {
    'after': NotRequired["str"],
    'issue_type_ids': "list[str]",
    'position': NotRequired["OrderOfIssueTypesPosition"],
    },
)
"""An ordered list of issue type IDs and information about where to move them."""

type OrderOfIssueTypesPosition = Literal['First', 'Last']
"""The position the issue types should be moved to. Required if `after` isn't provided."""

PageBean2ComponentJsonBean = TypedDict(
    'PageBean2ComponentJsonBean',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ComponentJsonBean]"],
    },
)
"""A page of items."""

PageBean2FieldAssociationSchemeFieldSearchResult = TypedDict(
    'PageBean2FieldAssociationSchemeFieldSearchResult',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldAssociationSchemeFieldSearchResult]"],
    },
)
"""A page of items."""

PageBean2FieldAssociationSchemeProjectSearchResult = TypedDict(
    'PageBean2FieldAssociationSchemeProjectSearchResult',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldAssociationSchemeProjectSearchResult]"],
    },
)
"""A page of items."""

PageBean2GetFieldAssociationSchemeResponse = TypedDict(
    'PageBean2GetFieldAssociationSchemeResponse',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[GetFieldAssociationSchemeResponse]"],
    },
)
"""A page of items."""

PageBean2GetProjectsWithFieldSchemesResponse = TypedDict(
    'PageBean2GetProjectsWithFieldSchemesResponse',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[GetProjectsWithFieldSchemesResponse]"],
    },
)
"""A page of items."""

PageBean2JqlFunctionPrecomputationBean = TypedDict(
    'PageBean2JqlFunctionPrecomputationBean',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[JqlFunctionPrecomputationBean]"],
    },
)
"""A page of items."""

PageBean2ProjectFieldBean = TypedDict(
    'PageBean2ProjectFieldBean',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ProjectFieldBean]"],
    },
)
"""A page of items."""

PageBeanBulkContextualConfiguration = TypedDict(
    'PageBeanBulkContextualConfiguration',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[BulkContextualConfiguration]"],
    },
)
"""A page of items."""

PageBeanChangelog = TypedDict(
    'PageBeanChangelog',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Changelog]"],
    },
)
"""A page of items."""

PageBeanComment = TypedDict(
    'PageBeanComment',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Comment]"],
    },
)
"""A page of items."""

PageBeanComponentWithIssueCount = TypedDict(
    'PageBeanComponentWithIssueCount',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ComponentWithIssueCount]"],
    },
)
"""A page of items."""

PageBeanContext = TypedDict(
    'PageBeanContext',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Context]"],
    },
)
"""A page of items."""

PageBeanContextDefaultValues = TypedDict(
    'PageBeanContextDefaultValues',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ContextDefaultValues]"],
    },
)
"""A page of items."""

PageBeanContextForProjectAndIssueType = TypedDict(
    'PageBeanContextForProjectAndIssueType',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ContextForProjectAndIssueType]"],
    },
)
"""A page of items."""

PageBeanContextualConfiguration = TypedDict(
    'PageBeanContextualConfiguration',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ContextualConfiguration]"],
    },
)
"""A page of items."""

PageBeanCustomFieldContext = TypedDict(
    'PageBeanCustomFieldContext',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[CustomFieldContext]"],
    },
)
"""A page of items."""

PageBeanCustomFieldContextDefaultValue = TypedDict(
    'PageBeanCustomFieldContextDefaultValue',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[CustomFieldContextDefaultValue]"],
    },
)
"""A page of items."""

PageBeanCustomFieldContextOption = TypedDict(
    'PageBeanCustomFieldContextOption',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[CustomFieldContextOption]"],
    },
)
"""A page of items."""

PageBeanCustomFieldContextProjectMapping = TypedDict(
    'PageBeanCustomFieldContextProjectMapping',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[CustomFieldContextProjectMapping]"],
    },
)
"""A page of items."""

PageBeanDashboard = TypedDict(
    'PageBeanDashboard',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Dashboard]"],
    },
)
"""A page of items."""

PageBeanField = TypedDict(
    'PageBeanField',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Field]"],
    },
)
"""A page of items."""

PageBeanFieldConfigurationDetails = TypedDict(
    'PageBeanFieldConfigurationDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldConfigurationDetails]"],
    },
)
"""A page of items."""

PageBeanFieldConfigurationIssueTypeItem = TypedDict(
    'PageBeanFieldConfigurationIssueTypeItem',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldConfigurationIssueTypeItem]"],
    },
)
"""A page of items."""

PageBeanFieldConfigurationItem = TypedDict(
    'PageBeanFieldConfigurationItem',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldConfigurationItem]"],
    },
)
"""A page of items."""

PageBeanFieldConfigurationScheme = TypedDict(
    'PageBeanFieldConfigurationScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldConfigurationScheme]"],
    },
)
"""A page of items."""

PageBeanFieldConfigurationSchemeProjects = TypedDict(
    'PageBeanFieldConfigurationSchemeProjects',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldConfigurationSchemeProjects]"],
    },
)
"""A page of items."""

PageBeanFieldProjectAssociation = TypedDict(
    'PageBeanFieldProjectAssociation',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FieldProjectAssociation]"],
    },
)
"""A page of items."""

PageBeanFilterDetails = TypedDict(
    'PageBeanFilterDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[FilterDetails]"],
    },
)
"""A page of items."""

PageBeanGroupDetails = TypedDict(
    'PageBeanGroupDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[GroupDetails]"],
    },
)
"""A page of items."""

PageBeanIssueFieldOption = TypedDict(
    'PageBeanIssueFieldOption',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueFieldOption]"],
    },
)
"""A page of items."""

PageBeanIssueSecurityLevelMember = TypedDict(
    'PageBeanIssueSecurityLevelMember',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueSecurityLevelMember]"],
    },
)
"""A page of items."""

PageBeanIssueSecuritySchemeToProjectMapping = TypedDict(
    'PageBeanIssueSecuritySchemeToProjectMapping',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueSecuritySchemeToProjectMapping]"],
    },
)
"""A page of items."""

PageBeanIssueTypeScheme = TypedDict(
    'PageBeanIssueTypeScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeScheme]"],
    },
)
"""A page of items."""

PageBeanIssueTypeSchemeMapping = TypedDict(
    'PageBeanIssueTypeSchemeMapping',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeSchemeMapping]"],
    },
)
"""A page of items."""

PageBeanIssueTypeSchemeProjects = TypedDict(
    'PageBeanIssueTypeSchemeProjects',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeSchemeProjects]"],
    },
)
"""A page of items."""

PageBeanIssueTypeScreenScheme = TypedDict(
    'PageBeanIssueTypeScreenScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeScreenScheme]"],
    },
)
"""A page of items."""

PageBeanIssueTypeScreenSchemeItem = TypedDict(
    'PageBeanIssueTypeScreenSchemeItem',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeScreenSchemeItem]"],
    },
)
"""A page of items."""

PageBeanIssueTypeScreenSchemesProjects = TypedDict(
    'PageBeanIssueTypeScreenSchemesProjects',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeScreenSchemesProjects]"],
    },
)
"""A page of items."""

PageBeanIssueTypeToContextMapping = TypedDict(
    'PageBeanIssueTypeToContextMapping',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[IssueTypeToContextMapping]"],
    },
)
"""A page of items."""

PageBeanNotificationScheme = TypedDict(
    'PageBeanNotificationScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[NotificationScheme]"],
    },
)
"""A page of items."""

PageBeanNotificationSchemeAndProjectMappingJsonBean = TypedDict(
    'PageBeanNotificationSchemeAndProjectMappingJsonBean',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[NotificationSchemeAndProjectMappingJsonBean]"],
    },
)
"""A page of items."""

PageBeanPriority = TypedDict(
    'PageBeanPriority',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Priority]"],
    },
)
"""A page of items."""

PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects = TypedDict(
    'PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[PrioritySchemeWithPaginatedPrioritiesAndProjects]"],
    },
)
"""A page of items."""

PageBeanPriorityWithSequence = TypedDict(
    'PageBeanPriorityWithSequence',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[PriorityWithSequence]"],
    },
)
"""A page of items."""

PageBeanProject = TypedDict(
    'PageBeanProject',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Project]"],
    },
)
"""A page of items."""

PageBeanProjectDetails = TypedDict(
    'PageBeanProjectDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ProjectDetails]"],
    },
)
"""A page of items."""

PageBeanResolutionJsonBean = TypedDict(
    'PageBeanResolutionJsonBean',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ResolutionJsonBean]"],
    },
)
"""A page of items."""

PageBeanScreen = TypedDict(
    'PageBeanScreen',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Screen]"],
    },
)
"""A page of items."""

PageBeanScreenScheme = TypedDict(
    'PageBeanScreenScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ScreenScheme]"],
    },
)
"""A page of items."""

PageBeanScreenWithTab = TypedDict(
    'PageBeanScreenWithTab',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[ScreenWithTab]"],
    },
)
"""A page of items."""

PageBeanSecurityLevel = TypedDict(
    'PageBeanSecurityLevel',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[SecurityLevel]"],
    },
)
"""A page of items."""

PageBeanSecurityLevelMember = TypedDict(
    'PageBeanSecurityLevelMember',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[SecurityLevelMember]"],
    },
)
"""A page of items."""

PageBeanSecuritySchemeWithProjects = TypedDict(
    'PageBeanSecuritySchemeWithProjects',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[SecuritySchemeWithProjects]"],
    },
)
"""A page of items."""

PageBeanString = TypedDict(
    'PageBeanString',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[str]"],
    },
)
"""A page of items."""

PageBeanUiModificationDetails = TypedDict(
    'PageBeanUiModificationDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[UiModificationDetails]"],
    },
)
"""A page of items."""

PageBeanUser = TypedDict(
    'PageBeanUser',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[User]"],
    },
)
"""A page of items."""

PageBeanUserDetails = TypedDict(
    'PageBeanUserDetails',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[UserDetails]"],
    },
)
"""A page of items."""

PageBeanUserKey = TypedDict(
    'PageBeanUserKey',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[UserKey]"],
    },
)
"""A page of items."""

PageBeanVersion = TypedDict(
    'PageBeanVersion',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Version]"],
    },
)
"""A page of items."""

PageBeanWebhook = TypedDict(
    'PageBeanWebhook',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Webhook]"],
    },
)
"""A page of items."""

PageBeanWorkflow = TypedDict(
    'PageBeanWorkflow',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[Workflow]"],
    },
)
"""A page of items."""

PageBeanWorkflowScheme = TypedDict(
    'PageBeanWorkflowScheme',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[WorkflowScheme]"],
    },
)
"""A page of items."""

PageBeanWorkflowTransitionRules = TypedDict(
    'PageBeanWorkflowTransitionRules',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[WorkflowTransitionRules]"],
    },
)
"""A page of items."""

PageOfChangelogs = TypedDict(
    'PageOfChangelogs',
    {
    'histories': NotRequired["list[Changelog]"],
    'max_results': NotRequired["int"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)
"""A page of changelogs."""

PageOfComments = TypedDict(
    'PageOfComments',
    {
    'comments': NotRequired["list[Comment]"],
    'max_results': NotRequired["int"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)
"""A page of comments."""

PageOfCreateMetaIssueTypeWithField = TypedDict(
    'PageOfCreateMetaIssueTypeWithField',
    {
    'fields': NotRequired["list[FieldCreateMetadata]"],
    'max_results': NotRequired["int"],
    'results': NotRequired["list[FieldCreateMetadata]"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)
"""A page of CreateMetaIssueType with Field."""

PageOfCreateMetaIssueTypes = TypedDict(
    'PageOfCreateMetaIssueTypes',
    {
    'create_meta_issue_type': NotRequired["list[IssueTypeIssueCreateMetadata]"],
    'issue_types': NotRequired["list[IssueTypeIssueCreateMetadata]"],
    'max_results': NotRequired["int"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)
"""A page of CreateMetaIssueTypes."""

PageOfDashboards = TypedDict(
    'PageOfDashboards',
    {
    'dashboards': NotRequired["list[Dashboard]"],
    'max_results': NotRequired["int"],
    'next': NotRequired["str"],
    'prev': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    },
)
"""A page containing dashboard details."""

PageOfStatuses = TypedDict(
    'PageOfStatuses',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[JiraStatus]"],
    },
)

PageOfWorklogs = TypedDict(
    'PageOfWorklogs',
    {
    'max_results': NotRequired["int"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'worklogs': NotRequired["list[Worklog]"],
    },
)
"""Paginated list of worklog details"""

PageWithCursorGetPlanResponseForPage = TypedDict(
    'PageWithCursorGetPlanResponseForPage',
    {
    'cursor': NotRequired["str"],
    'last': NotRequired["bool"],
    'next_page_cursor': NotRequired["str"],
    'size': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[GetPlanResponseForPage]"],
    },
)

PageWithCursorGetTeamResponseForPage = TypedDict(
    'PageWithCursorGetTeamResponseForPage',
    {
    'cursor': NotRequired["str"],
    'last': NotRequired["bool"],
    'next_page_cursor': NotRequired["str"],
    'size': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[GetTeamResponseForPage]"],
    },
)

PagedListUserDetailsApplicationUser = TypedDict(
    'PagedListUserDetailsApplicationUser',
    {
    'end_index': NotRequired["int"],
    'items': NotRequired["list[UserDetails]"],
    'max_results': NotRequired["int"],
    'size': NotRequired["int"],
    'start_index': NotRequired["int"],
    },
)
"""A paged list. To access additional details append `[start-index:end-index]` to the expand request. For example, `?expand=sharedUsers[10:40]` returns a list starting at item 10 and finishing at item 40."""

ParameterRemovalDetails = TypedDict(
    'ParameterRemovalDetails',
    {
    'parameters': NotRequired["list[str]"],
    'scheme_id': NotRequired["int"],
    'work_type_ids': NotRequired["list[int]"],
    },
)

type ParseJqlQueriesValidation = Literal['strict', 'warn', 'none']

ParsedJqlQueries = TypedDict(
    'ParsedJqlQueries',
    {
    'queries': "list[ParsedJqlQuery]",
    },
)
"""A list of parsed JQL queries."""

ParsedJqlQuery = TypedDict(
    'ParsedJqlQuery',
    {
    'errors': NotRequired["list[str]"],
    'query': "str",
    'structure': NotRequired["JqlQuery"],
    'warnings': NotRequired["list[str]"],
    },
)
"""Details of a parsed JQL query."""

PermissionDetails = TypedDict(
    'PermissionDetails',
    {
    'edit_permissions': "list[SharePermission]",
    'share_permissions': "list[SharePermission]",
    },
)
"""Details for permissions of shareable entities"""

PermissionGrant = TypedDict(
    'PermissionGrant',
    {
    'holder': NotRequired["PermissionHolder"],
    'id': NotRequired["int"],
    'permission': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details about a permission granted to a user or group."""

PermissionGrantDto = TypedDict(
    'PermissionGrantDto',
    {
    'application_access': NotRequired["list[str]"],
    'group_custom_fields': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'groups': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'permission_keys': NotRequired["list[str]"],
    'project_roles': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'special_grants': NotRequired["list[str]"],
    'user_custom_fields': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'users': NotRequired["list[ProjectCreateResourceIdentifier]"],
    },
)
"""List of permission grants"""

PermissionGrants = TypedDict(
    'PermissionGrants',
    {
    'expand': NotRequired["str"],
    'permissions': NotRequired["list[PermissionGrant]"],
    },
)
"""List of permission grants."""

PermissionHolder = TypedDict(
    'PermissionHolder',
    {
    'expand': NotRequired["str"],
    'parameter': NotRequired["str"],
    'type': "str",
    'value': NotRequired["str"],
    },
)
"""Details of a user, group, field, or project role that holds a permission. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information."""

PermissionPayloadDto = TypedDict(
    'PermissionPayloadDto',
    {
    'add_addon_role': NotRequired["bool"],
    'description': NotRequired["str"],
    'grants': NotRequired["list[PermissionGrantDto]"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["PermissionPayloadDtoOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload to create a permission scheme"""

type PermissionPayloadDtoOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use when there is a conflict with an existing permission scheme. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - If the entity exist, try and create a new one with a different name"""

PermissionScheme = TypedDict(
    'PermissionScheme',
    {
    'description': NotRequired["str"],
    'expand': NotRequired["str"],
    'id': NotRequired["int"],
    'name': "str",
    'permissions': NotRequired["list[PermissionGrant]"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    },
)
"""Details of a permission scheme."""

PermissionSchemes = TypedDict(
    'PermissionSchemes',
    {
    'permission_schemes': NotRequired["list[PermissionScheme]"],
    },
)
"""List of all permission schemes."""

Permissions = TypedDict(
    'Permissions',
    {
    'permissions': NotRequired["dict[str, UserPermission]"],
    },
)
"""Details about permissions."""

PermissionsKeysBean = TypedDict(
    'PermissionsKeysBean',
    {
    'permissions': "list[str]",
    },
)

PermittedProjects = TypedDict(
    'PermittedProjects',
    {
    'projects': NotRequired["list[ProjectIdentifierBean]"],
    },
)
"""A list of projects in which a user is granted permissions."""

PolicyApplicationViolation = TypedDict(
    'PolicyApplicationViolation',
    {
    'entity_id': NotRequired["str"],
    'entity_name': NotRequired["str"],
    'entity_type': NotRequired["str"],
    'remediation_hint': NotRequired["str"],
    'rule_type_id': NotRequired["str"],
    },
)

PolicySummary = TypedDict(
    'PolicySummary',
    {
    'applied_project_ids': NotRequired["list[int]"],
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'policy_description': NotRequired["str"],
    'policy_name': NotRequired["str"],
    'version': NotRequired["int"],
    },
)

PolicySummaryResponse = TypedDict(
    'PolicySummaryResponse',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page_cursor': NotRequired["str"],
    'start_at': NotRequired["int"],
    'total': NotRequired["int"],
    'values': NotRequired["list[PolicySummary]"],
    },
)

PreviewConditionGroupConfiguration = TypedDict(
    'PreviewConditionGroupConfiguration',
    {
    'condition_groups': NotRequired["list[PreviewConditionGroupConfiguration | None]"],
    'conditions': NotRequired["list[PreviewRuleConfiguration | None]"],
    'operation': NotRequired["PreviewConditionGroupConfigurationOperation"],
    },
)
"""Condition group configuration for workflow transitions."""

type PreviewConditionGroupConfigurationOperation = Literal['ANY', 'ALL']
"""Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."""

PreviewRuleConfiguration = TypedDict(
    'PreviewRuleConfiguration',
    {
    'id': NotRequired["str"],
    'parameters': NotRequired["dict[str, str]"],
    'rule_key': NotRequired["str"],
    },
)
"""Rule configuration for workflow transitions."""

PreviewTrigger = TypedDict(
    'PreviewTrigger',
    {
    'id': NotRequired["str"],
    'rule_key': NotRequired["str"],
    },
)
"""Trigger configuration for workflow transitions."""

Priority = TypedDict(
    'Priority',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'name': NotRequired["str"],
    'schemes': NotRequired["ExpandPrioritySchemePage"],
    'self': NotRequired["str"],
    'status_color': NotRequired["str"],
    },
)
"""An issue priority."""

PriorityId = TypedDict(
    'PriorityId',
    {
    'id': "str",
    },
)
"""The ID of an issue priority."""

PriorityMapping = TypedDict(
    'PriorityMapping',
    {
    'in': NotRequired["dict[str, int]"],
    'out': NotRequired["dict[str, int]"],
    },
)
"""Mapping of issue priorities for changes in priority schemes."""

PrioritySchemeChangesWithoutMappings = TypedDict(
    'PrioritySchemeChangesWithoutMappings',
    {
    'ids': "list[int]",
    },
)

PrioritySchemeId = TypedDict(
    'PrioritySchemeId',
    {
    'id': NotRequired["str"],
    'task': NotRequired["TaskProgressBeanJsonNode"],
    },
)
"""The ID of a priority scheme."""

PrioritySchemeWithPaginatedPrioritiesAndProjects = TypedDict(
    'PrioritySchemeWithPaginatedPrioritiesAndProjects',
    {
    'default': NotRequired["bool"],
    'default_priority_id': NotRequired["str"],
    'description': NotRequired["str"],
    'id': "str",
    'is_default': NotRequired["bool"],
    'name': "str",
    'priorities': NotRequired["PageBeanPriorityWithSequence"],
    'projects': NotRequired["PageBeanProjectDetails"],
    'self': NotRequired["str"],
    },
)
"""A priority scheme with paginated priorities and projects."""

PriorityWithSequence = TypedDict(
    'PriorityWithSequence',
    {
    'description': NotRequired["str"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    'sequence': NotRequired["str"],
    'status_color': NotRequired["str"],
    },
)
"""An issue priority with sequence information."""

Project = TypedDict(
    'Project',
    {
    'archived': NotRequired["bool"],
    'archived_by': NotRequired["User"],
    'archived_date': NotRequired["str"],
    'assignee_type': NotRequired["ProjectAssigneeType"],
    'avatar_urls': NotRequired["AvatarUrlsBean"],
    'components': NotRequired["list[ProjectComponent]"],
    'deleted': NotRequired["bool"],
    'deleted_by': NotRequired["User"],
    'deleted_date': NotRequired["str"],
    'description': NotRequired["str"],
    'email': NotRequired["str"],
    'expand': NotRequired["str"],
    'favourite': NotRequired["bool"],
    'id': NotRequired["str"],
    'insight': NotRequired["ProjectInsight"],
    'is_private': NotRequired["bool"],
    'issue_type_hierarchy': NotRequired["Hierarchy"],
    'issue_types': NotRequired["list[IssueTypeDetails]"],
    'key': NotRequired["str"],
    'landing_page_info': NotRequired["ProjectLandingPageInfo"],
    'lead': NotRequired["User"],
    'name': NotRequired["str"],
    'permissions': NotRequired["ProjectPermissions"],
    'project_category': NotRequired["ProjectCategory"],
    'project_type_key': NotRequired["ProjectProjectTypeKey"],
    'properties': NotRequired["dict[str, Any]"],
    'retention_till_date': NotRequired["str"],
    'roles': NotRequired["dict[str, str]"],
    'self': NotRequired["str"],
    'simplified': NotRequired["bool"],
    'style': NotRequired["ProjectStyle"],
    'url': NotRequired["str"],
    'uuid': NotRequired["str"],
    'versions': NotRequired["list[Version]"],
    },
)
"""Details about a project."""

ProjectAndIssueTypePair = TypedDict(
    'ProjectAndIssueTypePair',
    {
    'issue_type_id': "str",
    'project_id': "str",
    },
)
"""A project and issueType ID pair that identifies a status mapping."""

ProjectArchetype = TypedDict(
    'ProjectArchetype',
    {
    'real_type': NotRequired["ProjectArchetypeRealType"],
    'style': NotRequired["ProjectArchetypeStyle"],
    'type': NotRequired["ProjectArchetypeType"],
    },
)

type ProjectArchetypeRealType = Literal['BUSINESS', 'SOFTWARE', 'PRODUCT_DISCOVERY', 'SERVICE_DESK', 'CUSTOMER_SERVICE', 'OPS']

type ProjectArchetypeStyle = Literal['classic', 'next-gen']

type ProjectArchetypeType = Literal['BUSINESS', 'SOFTWARE', 'PRODUCT_DISCOVERY', 'SERVICE_DESK', 'CUSTOMER_SERVICE', 'OPS']

type ProjectAssigneeType = Literal['PROJECT_LEAD', 'UNASSIGNED']
"""The default assignee when creating issues for this project."""

ProjectAvatars = TypedDict(
    'ProjectAvatars',
    {
    'custom': NotRequired["list[Avatar]"],
    'system': NotRequired["list[Avatar]"],
    },
)
"""List of project avatars."""

ProjectCategory = TypedDict(
    'ProjectCategory',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""A project category."""

ProjectComponent = TypedDict(
    'ProjectComponent',
    {
    'ari': NotRequired["str"],
    'assignee': NotRequired["User"],
    'assignee_type': NotRequired["ProjectComponentAssigneeType"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'is_assignee_type_valid': NotRequired["bool"],
    'lead': NotRequired["User"],
    'lead_account_id': NotRequired["str"],
    'lead_user_name': NotRequired["str"],
    'metadata': NotRequired["dict[str, str]"],
    'name': NotRequired["str"],
    'project': NotRequired["str"],
    'project_id': NotRequired["int"],
    'real_assignee': NotRequired["User"],
    'real_assignee_type': NotRequired["ProjectComponentRealAssigneeType"],
    'self': NotRequired["str"],
    },
)
"""Details about a project component."""

type ProjectComponentAssigneeType = Literal['PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED']
"""
The nominal user type used to determine the assignee for issues created with this component. See `realAssigneeType` for details on how the type of the user, and hence the user, assigned to issues is determined. Can take the following values:

 *  `PROJECT_LEAD` the assignee to any issues created with this component is nominally the lead for the project the component is in.
 *  `COMPONENT_LEAD` the assignee to any issues created with this component is nominally the lead for the component.
 *  `UNASSIGNED` an assignee is not set for issues created with this component.
 *  `PROJECT_DEFAULT` the assignee to any issues created with this component is nominally the default assignee for the project that the component is in.

Default value: `PROJECT_DEFAULT`.  
Optional when creating or updating a component.
"""

type ProjectComponentRealAssigneeType = Literal['PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED']
"""
The type of the assignee that is assigned to issues created with this component, when an assignee cannot be set from the `assigneeType`. For example, `assigneeType` is set to `COMPONENT_LEAD` but no component lead is set. This property is set to one of the following values:

 *  `PROJECT_LEAD` when `assigneeType` is `PROJECT_LEAD` and the project lead has permission to be assigned issues in the project that the component is in.
 *  `COMPONENT_LEAD` when `assignee`Type is `COMPONENT_LEAD` and the component lead has permission to be assigned issues in the project that the component is in.
 *  `UNASSIGNED` when `assigneeType` is `UNASSIGNED` and Jira is configured to allow unassigned issues.
 *  `PROJECT_DEFAULT` when none of the preceding cases are true.
"""

ProjectCreateResourceIdentifier = TypedDict(
    'ProjectCreateResourceIdentifier',
    {
    'an_id': NotRequired["bool"],
    'areference': NotRequired["bool"],
    'entity_id': NotRequired["str"],
    'entity_type': NotRequired["str"],
    'id': NotRequired["str"],
    'type': NotRequired["ProjectCreateResourceIdentifierType"],
    },
)
"""Every project-created entity has an ID that must be unique within the scope of the project creation. PCRI (Project Create Resource Identifier) is a standard format for creating IDs and references to other project entities. PCRI format is defined as follows: pcri:\\[entityType\\]:\\[type\\]:\\[entityId\\] entityType - the type of an entity, e.g. status, role, workflow type - PCRI type, either `id` - The ID of an entity that already exists in the target site, or `ref` - A unique reference to an entity that is being created entityId - entity identifier, if type is `id` - must be an existing entity ID that exists in the Jira site, if `ref` - must be unique across all entities in the scope of this project template creation"""

type ProjectCreateResourceIdentifierType = Literal['id', 'ref']

ProjectCustomTemplateCreateRequestDto = TypedDict(
    'ProjectCustomTemplateCreateRequestDto',
    {
    'details': NotRequired["CustomTemplatesProjectDetails"],
    'template': NotRequired["CustomTemplateRequestDto"],
    },
)
"""Request to create a project using a custom template"""

ProjectDataPolicies = TypedDict(
    'ProjectDataPolicies',
    {
    'project_data_policies': NotRequired["list[ProjectWithDataPolicy]"],
    },
)
"""Details about data policies for a list of projects."""

ProjectDataPolicy = TypedDict(
    'ProjectDataPolicy',
    {
    'any_content_blocked': NotRequired["bool"],
    },
)
"""Details about data policy."""

ProjectDetails = TypedDict(
    'ProjectDetails',
    {
    'avatar_urls': NotRequired["AvatarUrlsBean"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'project_category': NotRequired["UpdatedProjectCategory"],
    'project_type_key': NotRequired["ProjectDetailsProjectTypeKey"],
    'self': NotRequired["str"],
    'simplified': NotRequired["bool"],
    },
)
"""Details about a project."""

type ProjectDetailsProjectTypeKey = Literal['software', 'service_desk', 'business', 'product_discovery']
"""The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project."""

ProjectEmailAddress = TypedDict(
    'ProjectEmailAddress',
    {
    'email_address': NotRequired["str"],
    'email_address_status': NotRequired["list[str]"],
    },
)
"""A project's sender email address."""

ProjectFeature = TypedDict(
    'ProjectFeature',
    {
    'feature': NotRequired["str"],
    'image_uri': NotRequired["str"],
    'localised_description': NotRequired["str"],
    'localised_name': NotRequired["str"],
    'prerequisites': NotRequired["list[str]"],
    'project_id': NotRequired["int"],
    'state': NotRequired["ProjectFeatureState"],
    'toggle_locked': NotRequired["bool"],
    },
)
"""Details of a project feature."""

type ProjectFeatureState = Literal['ENABLED', 'DISABLED', 'COMING_SOON']
"""The state of the feature. When updating the state of a feature, only ENABLED and DISABLED are supported. Responses can contain all values"""

ProjectFieldBean = TypedDict(
    'ProjectFieldBean',
    {
    'description': NotRequired["str"],
    'field_id': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'project_id': NotRequired["int"],
    'work_type_id': NotRequired["int"],
    },
)

ProjectId = TypedDict(
    'ProjectId',
    {
    'id': "str",
    },
)
"""Project ID details."""

ProjectIdentifierBean = TypedDict(
    'ProjectIdentifierBean',
    {
    'id': NotRequired["int"],
    'key': NotRequired["str"],
    },
)
"""The identifiers for a project."""

ProjectIdentifiers = TypedDict(
    'ProjectIdentifiers',
    {
    'id': "int",
    'key': "str",
    'self': "str",
    },
)
"""Identifiers for a project."""

ProjectIds = TypedDict(
    'ProjectIds',
    {
    'project_ids': "list[str]",
    },
)
"""A list of project IDs."""

ProjectInsight = TypedDict(
    'ProjectInsight',
    {
    'last_issue_update_time': NotRequired["str"],
    'total_issue_count': NotRequired["int"],
    },
)
"""Additional details about a project."""

ProjectIssueCreateMetadata = TypedDict(
    'ProjectIssueCreateMetadata',
    {
    'avatar_urls': NotRequired["AvatarUrlsBean"],
    'expand': NotRequired["str"],
    'id': NotRequired["str"],
    'issuetypes': NotRequired["list[IssueTypeIssueCreateMetadata]"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details of the issue creation metadata for a project."""

ProjectIssueSecurityLevels = TypedDict(
    'ProjectIssueSecurityLevels',
    {
    'levels': "list[SecurityLevel]",
    },
)
"""List of issue level security items in a project."""

ProjectIssueTypeHierarchy = TypedDict(
    'ProjectIssueTypeHierarchy',
    {
    'hierarchy': NotRequired["list[ProjectIssueTypesHierarchyLevel]"],
    'project_id': NotRequired["int"],
    },
)
"""The hierarchy of issue types within a project."""

ProjectIssueTypeMapping = TypedDict(
    'ProjectIssueTypeMapping',
    {
    'issue_type_id': "str",
    'project_id': "str",
    },
)
"""The project and issue type mapping."""

ProjectIssueTypeMappings = TypedDict(
    'ProjectIssueTypeMappings',
    {
    'mappings': "list[ProjectIssueTypeMapping]",
    },
)
"""The project and issue type mappings."""

ProjectIssueTypeQueryContext = TypedDict(
    'ProjectIssueTypeQueryContext',
    {
    'issue_types': NotRequired["list[str]"],
    'project': NotRequired["str"],
    },
)
"""Project and issue type context for workflow queries made using issue types."""

ProjectIssueTypesHierarchyLevel = TypedDict(
    'ProjectIssueTypesHierarchyLevel',
    {
    'entity_id': NotRequired["str"],
    'issue_types': NotRequired["list[IssueTypeInfo]"],
    'level': NotRequired["int"],
    'name': NotRequired["str"],
    },
)
"""Details of an issue type hierarchy level."""

ProjectLandingPageInfo = TypedDict(
    'ProjectLandingPageInfo',
    {
    'attributes': NotRequired["dict[str, str]"],
    'board_id': NotRequired["int"],
    'board_name': NotRequired["str"],
    'project_key': NotRequired["str"],
    'project_type': NotRequired["str"],
    'queue_category': NotRequired["str"],
    'queue_id': NotRequired["int"],
    'queue_name': NotRequired["str"],
    'simple_board': NotRequired["bool"],
    'simplified': NotRequired["bool"],
    'url': NotRequired["str"],
    },
)

ProjectPayload = TypedDict(
    'ProjectPayload',
    {
    'field_layout_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'issue_security_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'issue_type_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'issue_type_screen_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'notification_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'permission_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    'project_type_key': NotRequired["ProjectPayloadProjectTypeKey"],
    'workflow_scheme_id': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating a project"""

type ProjectPayloadProjectTypeKey = Literal['software', 'business', 'service_desk', 'product_discovery']
"""The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type."""

ProjectPermissions = TypedDict(
    'ProjectPermissions',
    {
    'can_edit': NotRequired["bool"],
    },
)
"""Permissions which a user has on a project."""

ProjectPinAction = TypedDict(
    'ProjectPinAction',
    {
    'action': "ProjectPinActionAction",
    'project_id_or_key': "str",
    },
)
"""The list of projects to pin or unpin the issue panel to or from."""

type ProjectPinActionAction = Literal['PIN', 'UNPIN']
"""The action to perform: PIN or UNPIN."""

type ProjectProjectTypeKey = Literal['software', 'service_desk', 'business', 'product_discovery']
"""The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project."""

ProjectResult = TypedDict(
    'ProjectResult',
    {
    'errors': NotRequired["list[PolicyApplicationViolation]"],
    'message': NotRequired["str"],
    'project_id': NotRequired["int"],
    },
)

ProjectRole = TypedDict(
    'ProjectRole',
    {
    'actors': NotRequired["list[RoleActor]"],
    'admin': NotRequired["bool"],
    'current_user_role': NotRequired["bool"],
    'default': NotRequired["bool"],
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'role_configurable': NotRequired["bool"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    'translated_name': NotRequired["str"],
    },
)
"""Details about the roles in a project."""

ProjectRoleActorsUpdateBean = TypedDict(
    'ProjectRoleActorsUpdateBean',
    {
    'categorised_actors': NotRequired["dict[str, list[str]]"],
    'id': NotRequired["int"],
    },
)

ProjectRoleDetails = TypedDict(
    'ProjectRoleDetails',
    {
    'admin': NotRequired["bool"],
    'default': NotRequired["bool"],
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'role_configurable': NotRequired["bool"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    'translated_name': NotRequired["str"],
    'type': NotRequired["ProjectRoleDetailsType"],
    },
)
"""Details about a project role."""

type ProjectRoleDetailsType = Literal['DEFAULT', 'GUEST_ROLE', 'AI_AGENT_ROLE']
"""The type of the project role. This is "DEFAULT" or "GUEST\\_ROLE"."""

ProjectRoleGroup = TypedDict(
    'ProjectRoleGroup',
    {
    'display_name': NotRequired["str"],
    'group_id': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of the group associated with the role."""

ProjectRoleUser = TypedDict(
    'ProjectRoleUser',
    {
    'account_id': NotRequired["str"],
    },
)
"""Details of the user associated with the role."""

ProjectScopeBean = TypedDict(
    'ProjectScopeBean',
    {
    'attributes': NotRequired["list[ProjectScopeBeanAttributesItem]"],
    'id': NotRequired["int"],
    },
)

type ProjectScopeBeanAttributesItem = Literal['notSelectable', 'defaultValue']

type ProjectStyle = Literal['classic', 'next-gen']
"""The type of the project."""

ProjectTemplateKey = TypedDict(
    'ProjectTemplateKey',
    {
    'key': NotRequired["str"],
    'uuid': NotRequired["str"],
    },
)

ProjectTemplateModel = TypedDict(
    'ProjectTemplateModel',
    {
    'archetype': NotRequired["ProjectArchetype"],
    'default_board_view': NotRequired["str"],
    'description': NotRequired["str"],
    'live_template_project_id_reference': NotRequired["int"],
    'name': NotRequired["str"],
    'project_template_key': NotRequired["ProjectTemplateKey"],
    'snapshot_template': NotRequired["dict[str, Any]"],
    'template_generation_options': NotRequired["CustomTemplateOptions"],
    'type': NotRequired["ProjectTemplateModelType"],
    },
)

type ProjectTemplateModelType = Literal['LIVE', 'SNAPSHOT']

ProjectType = TypedDict(
    'ProjectType',
    {
    'color': NotRequired["str"],
    'description_i_18_n_key': NotRequired["str"],
    'formatted_key': NotRequired["str"],
    'icon': NotRequired["str"],
    'key': NotRequired["str"],
    },
)
"""Details about a project type."""

ProjectUsage = TypedDict(
    'ProjectUsage',
    {
    'id': NotRequired["str"],
    },
)
"""The project."""

ProjectUsagePage = TypedDict(
    'ProjectUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[ProjectUsage]"],
    },
)
"""A page of projects."""

ProjectWithDataPolicy = TypedDict(
    'ProjectWithDataPolicy',
    {
    'data_policy': NotRequired["ProjectDataPolicy"],
    'id': NotRequired["int"],
    },
)
"""Details about data policies for a project."""

PropertyKey = TypedDict(
    'PropertyKey',
    {
    'key': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Property key details."""

PropertyKeys = TypedDict(
    'PropertyKeys',
    {
    'keys': NotRequired["list[PropertyKey]"],
    },
)
"""List of property keys."""

PublishDraftWorkflowScheme = TypedDict(
    'PublishDraftWorkflowScheme',
    {
    'status_mappings': NotRequired["list[StatusMapping]"],
    },
)
"""Details about the status mappings for publishing a draft workflow scheme."""

PublishedWorkflowId = TypedDict(
    'PublishedWorkflowId',
    {
    'entity_id': NotRequired["str"],
    'name': "str",
    },
)
"""Properties that identify a published workflow."""

QuickFilterPayload = TypedDict(
    'QuickFilterPayload',
    {
    'description': NotRequired["str"],
    'jql_query': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""The payload for defining quick filters"""

RedactionJobStatusResponse = TypedDict(
    'RedactionJobStatusResponse',
    {
    'bulk_redaction_response': NotRequired["BulkRedactionResponse"],
    'job_status': NotRequired["RedactionJobStatusResponseJobStatus"],
    },
)

type RedactionJobStatusResponseJobStatus = Literal['PENDING', 'IN_PROGRESS', 'COMPLETED']

RedactionPosition = TypedDict(
    'RedactionPosition',
    {
    'adf_pointer': NotRequired["str"],
    'expected_text': "str",
    'from': "int",
    'to': "int",
    },
)
"""Represents the position of the redaction"""

RegisteredWebhook = TypedDict(
    'RegisteredWebhook',
    {
    'created_webhook_id': NotRequired["int"],
    'errors': NotRequired["list[str]"],
    },
)
"""ID of a registered webhook or error messages explaining why a webhook wasn't registered."""

RemoteIssueLink = TypedDict(
    'RemoteIssueLink',
    {
    'application': NotRequired["Application"],
    'global_id': NotRequired["str"],
    'id': NotRequired["int"],
    'object': NotRequired["RemoteObject"],
    'relationship': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details of an issue remote link."""

RemoteIssueLinkIdentifies = TypedDict(
    'RemoteIssueLinkIdentifies',
    {
    'id': NotRequired["int"],
    'self': NotRequired["str"],
    },
)
"""Details of the identifiers for a created or updated remote issue link."""

RemoteIssueLinkRequest = TypedDict(
    'RemoteIssueLinkRequest',
    {
    'application': NotRequired["Application"],
    'global_id': NotRequired["str"],
    'object': "RemoteObject",
    'relationship': NotRequired["str"],
    },
)
"""Details of a remote issue link."""

RemoteObject = TypedDict(
    'RemoteObject',
    {
    'icon': NotRequired["Icon"],
    'status': NotRequired["Status"],
    'summary': NotRequired["str"],
    'title': "str",
    'url': "str",
    },
)
"""The linked item."""

RemoveFieldAssociationsRequestItem = TypedDict(
    'RemoveFieldAssociationsRequestItem',
    {
    'scheme_ids': "list[int]",
    },
)
"""Request item for removing field associations."""

RemoveOptionFromIssuesResult = TypedDict(
    'RemoveOptionFromIssuesResult',
    {
    'errors': NotRequired["SimpleErrorCollection"],
    'modified_issues': NotRequired["list[int]"],
    'unmodified_issues': NotRequired["list[int]"],
    },
)

ReorderIssuePriorities = TypedDict(
    'ReorderIssuePriorities',
    {
    'after': NotRequired["str"],
    'ids': "list[str]",
    'position': NotRequired["str"],
    },
)
"""Change the order of issue priorities."""

ReorderIssueResolutionsRequest = TypedDict(
    'ReorderIssueResolutionsRequest',
    {
    'after': NotRequired["str"],
    'ids': "list[str]",
    'position': NotRequired["str"],
    },
)
"""Change the order of issue resolutions."""

RequiredMappingByIssueType = TypedDict(
    'RequiredMappingByIssueType',
    {
    'issue_type_id': NotRequired["str"],
    'status_ids': NotRequired["list[str]"],
    },
)
"""The list of required status mappings by issue type."""

RequiredMappingByWorkflows = TypedDict(
    'RequiredMappingByWorkflows',
    {
    'source_workflow_id': NotRequired["str"],
    'status_ids': NotRequired["list[str]"],
    'target_workflow_id': NotRequired["str"],
    },
)
"""The list of required status mappings by workflow."""

Resolution = TypedDict(
    'Resolution',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details of an issue resolution."""

ResolutionId = TypedDict(
    'ResolutionId',
    {
    'id': "str",
    },
)
"""The ID of an issue resolution."""

ResolutionJsonBean = TypedDict(
    'ResolutionJsonBean',
    {
    'default': NotRequired["bool"],
    'description': NotRequired["str"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)

RestrictedPermission = TypedDict(
    'RestrictedPermission',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    },
)
"""Details of the permission."""

RoleActor = TypedDict(
    'RoleActor',
    {
    'actor_group': NotRequired["ProjectRoleGroup"],
    'actor_user': NotRequired["ProjectRoleUser"],
    'avatar_url': NotRequired["str"],
    'display_name': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'type': NotRequired["RoleActorType"],
    },
)
"""Details about a user assigned to a project role."""

type RoleActorType = Literal['atlassian-group-role-actor', 'atlassian-user-role-actor']
"""The type of role actor."""

RolePayload = TypedDict(
    'RolePayload',
    {
    'default_actors': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["RolePayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'type': NotRequired["RolePayloadType"],
    },
)
"""The payload used to create a project role. It is optional for CMP projects, as a default role actor will be provided. TMP will add new role actors to the table."""

type RolePayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use when there is a conflict with an existing project role. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters"""

type RolePayloadType = Literal['HIDDEN', 'VIEWABLE', 'AI_AGENT', 'EDITABLE', 'GUEST']
"""The type of the role. Only used by project-scoped project"""

RolesCapabilityPayload = TypedDict(
    'RolesCapabilityPayload',
    {
    'role_to_project_actors': NotRequired["dict[str, list[ProjectCreateResourceIdentifier]]"],
    'roles': NotRequired["list[RolePayload]"],
    },
)

RuleConfiguration = TypedDict(
    'RuleConfiguration',
    {
    'disabled': NotRequired["bool"],
    'tag': NotRequired["str"],
    'value': "str",
    },
)
"""A rule configuration."""

RulePayload = TypedDict(
    'RulePayload',
    {
    'parameters': NotRequired["dict[str, str]"],
    'rule_key': NotRequired["str"],
    },
)
"""The payload for creating rules in a workflow"""

SanitizedJqlQueries = TypedDict(
    'SanitizedJqlQueries',
    {
    'queries': NotRequired["list[SanitizedJqlQuery]"],
    },
)
"""The sanitized JQL queries for the given account IDs."""

SanitizedJqlQuery = TypedDict(
    'SanitizedJqlQuery',
    {
    'account_id': NotRequired["str | None"],
    'errors': NotRequired["ErrorCollection"],
    'initial_query': NotRequired["str"],
    'sanitized_query': NotRequired["str | None"],
    },
)
"""Details of the sanitized JQL query."""

SaveProjectTemplateRequest = TypedDict(
    'SaveProjectTemplateRequest',
    {
    'project_id': NotRequired["int"],
    'template_generation_options': NotRequired["CustomTemplateOptions"],
    'template_type': NotRequired["SaveProjectTemplateRequestTemplateType"],
    },
)
"""The request details to generate template from a project"""

type SaveProjectTemplateRequestTemplateType = Literal['LIVE', 'SNAPSHOT']
"""The type of the template: LIVE | SNAPSHOT"""

SaveTemplateRequest = TypedDict(
    'SaveTemplateRequest',
    {
    'template_description': NotRequired["str"],
    'template_from_project_request': NotRequired["SaveProjectTemplateRequest"],
    'template_name': NotRequired["str"],
    },
)
"""Request to save a custom template"""

SaveTemplateResponse = TypedDict(
    'SaveTemplateResponse',
    {
    'project_template_key': NotRequired["ProjectTemplateKey"],
    },
)

Scope = TypedDict(
    'Scope',
    {
    'project': NotRequired["ProjectDetails"],
    'type': NotRequired["ScopeType"],
    },
)
"""The projects the item is associated with. Indicated for items associated with [next-gen projects](https://confluence.atlassian.com/x/loMyO)."""

ScopePayload = TypedDict(
    'ScopePayload',
    {
    'type': NotRequired["ScopePayloadType"],
    },
)
"""The payload for creating a scope. Defines if a project is team-managed project or company-managed project"""

type ScopePayloadType = Literal['GLOBAL', 'PROJECT']
"""The type of the scope. Use `GLOBAL` or empty for company-managed project, and `PROJECT` for team-managed project"""

type ScopeType = Literal['PROJECT', 'TEMPLATE']
"""The type of scope."""

Screen = TypedDict(
    'Screen',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    },
)
"""A screen."""

ScreenDetails = TypedDict(
    'ScreenDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""Details of a screen."""

ScreenPayload = TypedDict(
    'ScreenPayload',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'tabs': NotRequired["list[TabPayload]"],
    },
)
"""Defines the payload for the field screens. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screens/\\#api-rest-api-3-screens-post"""

ScreenScheme = TypedDict(
    'ScreenScheme',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'issue_type_screen_schemes': NotRequired["PageBeanIssueTypeScreenScheme"],
    'name': NotRequired["str"],
    'screens': NotRequired["ScreenTypes"],
    },
)
"""A screen scheme."""

ScreenSchemeDetails = TypedDict(
    'ScreenSchemeDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    'screens': "ScreenTypes",
    },
)
"""Details of a screen scheme."""

ScreenSchemeId = TypedDict(
    'ScreenSchemeId',
    {
    'id': "int",
    },
)
"""The ID of a screen scheme."""

ScreenSchemePayload = TypedDict(
    'ScreenSchemePayload',
    {
    'default_screen': NotRequired["ProjectCreateResourceIdentifier"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'screens': NotRequired["dict[str, ProjectCreateResourceIdentifier]"],
    },
)
"""Defines the payload for the screen schemes. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-schemes/\\#api-rest-api-3-screenscheme-post"""

ScreenTypes = TypedDict(
    'ScreenTypes',
    {
    'create': NotRequired["int"],
    'default': "int",
    'edit': NotRequired["int"],
    'view': NotRequired["int"],
    },
)
"""The IDs of the screens for the screen types of the screen scheme."""

ScreenWithTab = TypedDict(
    'ScreenWithTab',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    'tab': NotRequired["ScreenableTab"],
    },
)
"""A screen with tab details."""

ScreenableField = TypedDict(
    'ScreenableField',
    {
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""A screen tab field."""

ScreenableTab = TypedDict(
    'ScreenableTab',
    {
    'id': NotRequired["int"],
    'name': "str",
    },
)
"""A screen tab."""

SearchAndReconcileRequestBean = TypedDict(
    'SearchAndReconcileRequestBean',
    {
    'expand': NotRequired["str"],
    'fields': NotRequired["list[str]"],
    'fields_by_keys': NotRequired["bool"],
    'include_archived_projects': NotRequired["bool"],
    'jql': NotRequired["str"],
    'max_results': NotRequired["int"],
    'next_page_token': NotRequired["str"],
    'properties': NotRequired["list[str]"],
    'reconcile_issues': NotRequired["list[int]"],
    },
)

SearchAndReconcileResults = TypedDict(
    'SearchAndReconcileResults',
    {
    'is_last': NotRequired["bool"],
    'issues': NotRequired["list[IssueBean]"],
    'names': NotRequired["dict[str, str]"],
    'next_page_token': NotRequired["str"],
    'schema': NotRequired["dict[str, JsonTypeBean]"],
    'warnings': NotRequired["list[SearchWarning]"],
    },
)
"""The result of a JQL search with issues reconsilation."""

SearchAutoCompleteFilter = TypedDict(
    'SearchAutoCompleteFilter',
    {
    'include_collapsed_fields': NotRequired["bool"],
    'project_ids': NotRequired["list[int]"],
    },
)
"""Details of how to filter and list search auto complete information."""

type SearchProjectsAction = Literal['view', 'browse', 'edit', 'create']

type SearchProjectsOrderBy = Literal['category', '-category', '+category', 'key', '-key', '+key', 'name', '-name', '+name', 'owner', '-owner', '+owner', 'issueCount', '-issueCount', '+issueCount', 'lastIssueUpdatedDate', '-lastIssueUpdatedDate', '+lastIssueUpdatedDate', 'archivedDate', '+archivedDate', '-archivedDate', 'deletedDate', '+deletedDate', '-deletedDate']

type SearchProjectsStatusItem = Literal['live', 'archived', 'deleted']

SearchResultFieldParameters = TypedDict(
    'SearchResultFieldParameters',
    {
    'description': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'renderer_type': NotRequired["str"],
    },
)

SearchResultWorkTypeParameters = TypedDict(
    'SearchResultWorkTypeParameters',
    {
    'description': NotRequired["str"],
    'is_required': NotRequired["bool"],
    'renderer_type': NotRequired["str"],
    'work_type_id': NotRequired["str"],
    },
)

SearchWarning = TypedDict(
    'SearchWarning',
    {
    'details': NotRequired["SearchWarningLimitDetails"],
    'message': NotRequired["str"],
    'type': NotRequired["str"],
    },
)
"""Experimental. A warning returned alongside successful search results."""

SearchWarningLimitDetails = TypedDict(
    'SearchWarningLimitDetails',
    {
    'actual': NotRequired["int"],
    'arguments': NotRequired["str"],
    'clause': NotRequired["str"],
    'limit': NotRequired["int"],
    },
)
"""Experimental. Structured details about a JQL clause exceeding its argument limit."""

SecurityLevel = TypedDict(
    'SecurityLevel',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'issue_security_scheme_id': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details of an issue level security item."""

SecurityLevelMember = TypedDict(
    'SecurityLevelMember',
    {
    'holder': "PermissionHolder",
    'id': "str",
    'issue_security_level_id': "str",
    'issue_security_scheme_id': "str",
    'managed': NotRequired["bool"],
    },
)
"""Issue security level member."""

SecurityLevelMemberPayload = TypedDict(
    'SecurityLevelMemberPayload',
    {
    'parameter': NotRequired["str"],
    'type': NotRequired["SecurityLevelMemberPayloadType"],
    },
)
"""The payload for creating a security level member. See https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/"""

type SecurityLevelMemberPayloadType = Literal['group', 'reporter', 'users']
"""The type of the security level member"""

SecurityLevelPayload = TypedDict(
    'SecurityLevelPayload',
    {
    'description': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'security_level_members': NotRequired["list[SecurityLevelMemberPayload]"],
    },
)
"""The payload for creating a security level. See https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/"""

SecurityScheme = TypedDict(
    'SecurityScheme',
    {
    'default_security_level_id': NotRequired["int"],
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'levels': NotRequired["list[SecurityLevel]"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""Details about a security scheme."""

SecuritySchemeId = TypedDict(
    'SecuritySchemeId',
    {
    'id': "str",
    },
)
"""The ID of the issue security scheme."""

SecuritySchemeLevelBean = TypedDict(
    'SecuritySchemeLevelBean',
    {
    'description': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'members': NotRequired["list[SecuritySchemeLevelMemberBean]"],
    'name': "str",
    },
)

SecuritySchemeLevelMemberBean = TypedDict(
    'SecuritySchemeLevelMemberBean',
    {
    'parameter': NotRequired["str"],
    'type': "str",
    },
)

SecuritySchemeMembersRequest = TypedDict(
    'SecuritySchemeMembersRequest',
    {
    'members': NotRequired["list[SecuritySchemeLevelMemberBean]"],
    },
)
"""Details of issue security scheme level new members."""

SecuritySchemePayload = TypedDict(
    'SecuritySchemePayload',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'security_levels': NotRequired["list[SecurityLevelPayload]"],
    },
)
"""The payload for creating a security scheme. See https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/"""

SecuritySchemeWithProjects = TypedDict(
    'SecuritySchemeWithProjects',
    {
    'default_level': NotRequired["int"],
    'description': NotRequired["str"],
    'id': "int",
    'name': "str",
    'project_ids': NotRequired["list[int]"],
    'self': "str",
    },
)
"""Details about an issue security scheme."""

SecuritySchemes = TypedDict(
    'SecuritySchemes',
    {
    'issue_security_schemes': NotRequired["list[SecurityScheme]"],
    },
)
"""List of security schemes."""

ServerInformation = TypedDict(
    'ServerInformation',
    {
    'base_url': NotRequired["str"],
    'build_date': NotRequired["str"],
    'build_number': NotRequired["int"],
    'deployment_type': NotRequired["str"],
    'display_url': NotRequired["str"],
    'display_url_confluence': NotRequired["str"],
    'display_url_servicedesk_help_center': NotRequired["str"],
    'health_checks': NotRequired["list[HealthCheckResult]"],
    'scm_info': NotRequired["str"],
    'server_time': NotRequired["str"],
    'server_time_zone': NotRequired["str"],
    'server_title': NotRequired["str"],
    'version': NotRequired["str"],
    'version_numbers': NotRequired["list[int]"],
    },
)
"""Details about the Jira instance."""

ServiceRegistry = TypedDict(
    'ServiceRegistry',
    {
    'description': NotRequired["str | None"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'organization_id': NotRequired["str"],
    'revision': NotRequired["str"],
    'service_tier': NotRequired["ServiceRegistryTier"],
    },
)

ServiceRegistryTier = TypedDict(
    'ServiceRegistryTier',
    {
    'description': NotRequired["str | None"],
    'id': NotRequired["str"],
    'level': NotRequired["int"],
    'name': NotRequired["str | None"],
    'name_key': NotRequired["str"],
    },
)

SetDefaultLevelsRequest = TypedDict(
    'SetDefaultLevelsRequest',
    {
    'default_values': "list[DefaultLevelValue]",
    },
)
"""Details of new default levels."""

SetDefaultPriorityRequest = TypedDict(
    'SetDefaultPriorityRequest',
    {
    'id': "str",
    },
)
"""The new default issue priority."""

SetDefaultResolutionRequest = TypedDict(
    'SetDefaultResolutionRequest',
    {
    'id': "str",
    },
)
"""The new default issue resolution."""

SetProjectPoliciesRequest = TypedDict(
    'SetProjectPoliciesRequest',
    {
    'policy_ids': NotRequired["list[str]"],
    },
)

SharePermission = TypedDict(
    'SharePermission',
    {
    'group': NotRequired["GroupName"],
    'id': NotRequired["int"],
    'project': NotRequired["Project"],
    'role': NotRequired["ProjectRole"],
    'type': "SharePermissionType",
    'user': NotRequired["UserBean"],
    },
)
"""Details of a share permission for the filter."""

SharePermissionInputBean = TypedDict(
    'SharePermissionInputBean',
    {
    'account_id': NotRequired["str"],
    'group_id': NotRequired["str"],
    'groupname': NotRequired["str"],
    'project_id': NotRequired["str"],
    'project_role_id': NotRequired["str"],
    'rights': NotRequired["int"],
    'type': "SharePermissionInputBeanType",
    },
)

type SharePermissionInputBeanType = Literal['user', 'project', 'group', 'projectRole', 'global', 'authenticated']
"""
The type of the share permission.Specify the type as follows:

 *  `user` Share with a user.
 *  `group` Share with a group. Specify `groupname` as well.
 *  `project` Share with a project. Specify `projectId` as well.
 *  `projectRole` Share with a project role in a project. Specify `projectId` and `projectRoleId` as well.
 *  `global` Share globally, including anonymous users. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set.
 *  `authenticated` Share with all logged-in users. This shows as `loggedin` in the response. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set.
"""

type SharePermissionType = Literal['user', 'group', 'project', 'projectRole', 'global', 'loggedin', 'authenticated', 'project-unknown']
"""
The type of share permission:

 *  `user` Shared with a user.
 *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.
 *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.
 *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.
 *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.
 *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.
 *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
"""

SimpleApplicationPropertyBean = TypedDict(
    'SimpleApplicationPropertyBean',
    {
    'id': NotRequired["str"],
    'value': NotRequired["str"],
    },
)

SimpleErrorCollection = TypedDict(
    'SimpleErrorCollection',
    {
    'error_messages': NotRequired["list[str]"],
    'errors': NotRequired["dict[str, str]"],
    'http_status_code': NotRequired["int"],
    },
)

SimpleLink = TypedDict(
    'SimpleLink',
    {
    'href': NotRequired["str"],
    'icon_class': NotRequired["str"],
    'id': NotRequired["str"],
    'label': NotRequired["str"],
    'style_class': NotRequired["str"],
    'title': NotRequired["str"],
    'weight': NotRequired["int"],
    },
)
"""Details about the operations available in this version."""

SimpleListWrapperApplicationRole = TypedDict(
    'SimpleListWrapperApplicationRole',
    {
    'callback': NotRequired["ListWrapperCallbackApplicationRole"],
    'items': NotRequired["list[ApplicationRole]"],
    'max_results': NotRequired["int"],
    'paging_callback': NotRequired["ListWrapperCallbackApplicationRole"],
    'size': NotRequired["int"],
    },
)

SimpleListWrapperGroupName = TypedDict(
    'SimpleListWrapperGroupName',
    {
    'callback': NotRequired["ListWrapperCallbackGroupName"],
    'items': NotRequired["list[GroupName]"],
    'max_results': NotRequired["int"],
    'paging_callback': NotRequired["ListWrapperCallbackGroupName"],
    'size': NotRequired["int"],
    },
)

SimplifiedHierarchyLevel = TypedDict(
    'SimplifiedHierarchyLevel',
    {
    'above_level_id': NotRequired["int"],
    'below_level_id': NotRequired["int"],
    'external_uuid': NotRequired["str"],
    'hierarchy_level_number': NotRequired["int"],
    'id': NotRequired["int"],
    'issue_type_ids': NotRequired["list[int]"],
    'level': NotRequired["int"],
    'name': NotRequired["str"],
    'project_configuration_id': NotRequired["int"],
    },
)

SimplifiedIssueTransition = TypedDict(
    'SimplifiedIssueTransition',
    {
    'to': NotRequired["IssueTransitionStatus"],
    'transition_id': NotRequired["int"],
    'transition_name': NotRequired["str"],
    },
)

SingleRedactionRequest = TypedDict(
    'SingleRedactionRequest',
    {
    'content_item': "ContentItem",
    'external_id': "str",
    'reason': "str",
    'redaction_position': "RedactionPosition",
    },
)

SingleRedactionResponse = TypedDict(
    'SingleRedactionResponse',
    {
    'external_id': "str",
    'successful': "bool",
    },
)
"""Result for requested redactions"""

StatePolicyDocument = TypedDict(
    'StatePolicyDocument',
    {
    'id': NotRequired["str"],
    'is_default': NotRequired["bool"],
    'policy_description': NotRequired["str"],
    'policy_name': NotRequired["str"],
    'rules_by_domain': NotRequired["dict[str, list[StatePolicyRule]]"],
    'version': NotRequired["int"],
    },
)

StatePolicyRule = TypedDict(
    'StatePolicyRule',
    {
    'description': NotRequired["str"],
    'domain': NotRequired["str"],
    'properties': NotRequired["dict[str, Any]"],
    'rule_id': NotRequired["str"],
    'rule_type_id': NotRequired["str"],
    },
)

Status = TypedDict(
    'Status',
    {
    'icon': NotRequired["Icon"],
    'resolved': NotRequired["bool"],
    },
)
"""The status of the item."""

StatusCategory = TypedDict(
    'StatusCategory',
    {
    'color_name': NotRequired["str"],
    'id': NotRequired["int"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""A status category."""

StatusCreate = TypedDict(
    'StatusCreate',
    {
    'description': NotRequired["str"],
    'name': "str",
    'status_category': "StatusCreateStatusCategory",
    },
)
"""Details of the status being created."""

StatusCreateRequest = TypedDict(
    'StatusCreateRequest',
    {
    'scope': "StatusScope",
    'statuses': "list[StatusCreate]",
    },
)
"""Details of the statuses being created and their scope."""

type StatusCreateStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

StatusDetails = TypedDict(
    'StatusDetails',
    {
    'description': NotRequired["str"],
    'icon_url': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["Scope"],
    'self': NotRequired["str"],
    'status_category': NotRequired["StatusCategory"],
    },
)
"""A status."""

StatusLayoutUpdate = TypedDict(
    'StatusLayoutUpdate',
    {
    'approval_configuration': NotRequired["ApprovalConfiguration | None"],
    'layout': NotRequired["WorkflowLayout | None"],
    'properties': "dict[str, str]",
    'status_reference': "str",
    },
)
"""The statuses associated with this workflow."""

StatusMapping = TypedDict(
    'StatusMapping',
    {
    'issue_type_id': "str",
    'new_status_id': "str",
    'status_id': "str",
    },
)
"""Details about the mapping from a status to a new status for an issue type."""

StatusMappingDto = TypedDict(
    'StatusMappingDto',
    {
    'issue_type_id': "str",
    'project_id': "str",
    'status_migrations': "list[StatusMigration]",
    },
)
"""The mapping of old to new status ID for a specific project and issue type."""

StatusMetadata = TypedDict(
    'StatusMetadata',
    {
    'category': NotRequired["StatusMetadataCategory"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""The details of the statuses in the associated workflows."""

type StatusMetadataCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

StatusMigration = TypedDict(
    'StatusMigration',
    {
    'new_status_reference': "str",
    'old_status_reference': "str",
    },
)
"""The mapping of old to new status ID."""

StatusPayload = TypedDict(
    'StatusPayload',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["StatusPayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'scope': NotRequired["StatusPayloadScope"],
    'status_category': NotRequired["StatusPayloadStatusCategory"],
    },
)
"""The payload for creating a status"""

type StatusPayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The conflict strategy for the status already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - Create a new entity"""

type StatusPayloadScope = Literal['GLOBAL']
"""The scope of the status. Set to GLOBAL to make the status shared across projects. Leave null for the default (project-scoped) behaviour."""

type StatusPayloadStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The status category of the status. The value is case-sensitive."""

StatusProjectIssueTypeUsage = TypedDict(
    'StatusProjectIssueTypeUsage',
    {
    'id': NotRequired["str"],
    },
)
"""The list of issue types."""

StatusProjectIssueTypeUsageDto = TypedDict(
    'StatusProjectIssueTypeUsageDto',
    {
    'issue_types': NotRequired["StatusProjectIssueTypeUsagePage"],
    'project_id': NotRequired["str"],
    'status_id': NotRequired["str"],
    },
)
"""The issue types using this status in a project."""

StatusProjectIssueTypeUsagePage = TypedDict(
    'StatusProjectIssueTypeUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[StatusProjectIssueTypeUsage]"],
    },
)
"""A page of issue types."""

StatusProjectUsage = TypedDict(
    'StatusProjectUsage',
    {
    'id': NotRequired["str"],
    },
)
"""The project."""

StatusProjectUsageDto = TypedDict(
    'StatusProjectUsageDto',
    {
    'projects': NotRequired["StatusProjectUsagePage"],
    'status_id': NotRequired["str"],
    },
)
"""The projects using this status."""

StatusProjectUsagePage = TypedDict(
    'StatusProjectUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[StatusProjectUsage]"],
    },
)
"""A page of projects."""

StatusScope = TypedDict(
    'StatusScope',
    {
    'project': NotRequired["ProjectId | None"],
    'type': "StatusScopeType",
    },
)
"""The scope of the status."""

type StatusScopeType = Literal['PROJECT', 'GLOBAL']
"""The scope of the status. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."""

StatusUpdate = TypedDict(
    'StatusUpdate',
    {
    'description': NotRequired["str"],
    'id': "str",
    'name': "str",
    'status_category': "StatusUpdateStatusCategory",
    },
)
"""Details of the status being updated."""

StatusUpdateRequest = TypedDict(
    'StatusUpdateRequest',
    {
    'statuses': "list[StatusUpdate]",
    },
)
"""The list of statuses that will be updated."""

type StatusUpdateStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

StatusWorkflowUsageDto = TypedDict(
    'StatusWorkflowUsageDto',
    {
    'status_id': NotRequired["str"],
    'workflows': NotRequired["StatusWorkflowUsagePage"],
    },
)
"""Workflows using the status."""

StatusWorkflowUsagePage = TypedDict(
    'StatusWorkflowUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[StatusWorkflowUsageWorkflow]"],
    },
)
"""A page of workflows."""

StatusWorkflowUsageWorkflow = TypedDict(
    'StatusWorkflowUsageWorkflow',
    {
    'id': NotRequired["str"],
    },
)
"""The worflow."""

StatusesPerWorkflow = TypedDict(
    'StatusesPerWorkflow',
    {
    'initial_status_id': NotRequired["str"],
    'statuses': NotRequired["list[str]"],
    'workflow_id': NotRequired["str"],
    },
)
"""The statuses associated with each workflow."""

type StoreAvatarType = Literal['project', 'issuetype', 'priority']

type StreamingResponseBody = dict[str, Any]

type StringList = dict[str, Any]

SubmittedBulkOperation = TypedDict(
    'SubmittedBulkOperation',
    {
    'task_id': NotRequired["str"],
    },
)

SuggestedIssue = TypedDict(
    'SuggestedIssue',
    {
    'id': NotRequired["int"],
    'img': NotRequired["str"],
    'key': NotRequired["str"],
    'key_html': NotRequired["str"],
    'summary': NotRequired["str"],
    'summary_text': NotRequired["str"],
    },
)
"""An issue suggested for use in the issue picker auto-completion."""

SuggestedMappingsForPrioritiesRequestBean = TypedDict(
    'SuggestedMappingsForPrioritiesRequestBean',
    {
    'add': NotRequired["list[int]"],
    'remove': NotRequired["list[int]"],
    },
)
"""Details of changes to a priority scheme's priorities that require suggested priority mappings."""

SuggestedMappingsForProjectsRequestBean = TypedDict(
    'SuggestedMappingsForProjectsRequestBean',
    {
    'add': NotRequired["list[int]"],
    },
)
"""Details of changes to a priority scheme's projects that require suggested priority mappings."""

SuggestedMappingsRequestBean = TypedDict(
    'SuggestedMappingsRequestBean',
    {
    'max_results': NotRequired["int"],
    'priorities': NotRequired["SuggestedMappingsForPrioritiesRequestBean"],
    'projects': NotRequired["SuggestedMappingsForProjectsRequestBean"],
    'scheme_id': NotRequired["int"],
    'start_at': NotRequired["int"],
    },
)
"""Details of changes to a priority scheme that require suggested priority mappings."""

SwimlanePayload = TypedDict(
    'SwimlanePayload',
    {
    'description': NotRequired["str"],
    'jql_query': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""The payload for custom swimlanes"""

SwimlanesPayload = TypedDict(
    'SwimlanesPayload',
    {
    'custom_swimlanes': NotRequired["list[SwimlanePayload]"],
    'default_custom_swimlane_name': NotRequired["str"],
    'swimlane_strategy': NotRequired["SwimlanesPayloadSwimlaneStrategy"],
    },
)
"""The payload for customising a swimlanes on a board"""

type SwimlanesPayloadSwimlaneStrategy = Literal['none', 'custom', 'parentChild', 'assignee', 'assigneeUnassignedFirst', 'epic', 'project', 'issueparent', 'issuechildren', 'request_type']
"""The swimlane strategy for the board."""

SystemAvatars = TypedDict(
    'SystemAvatars',
    {
    'system': NotRequired["list[Avatar]"],
    },
)
"""List of system avatars."""

TabPayload = TypedDict(
    'TabPayload',
    {
    'fields': NotRequired["list[ProjectCreateResourceIdentifier]"],
    'name': NotRequired["str"],
    },
)
"""Defines the payload for the tabs of the screen. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/\\#api-rest-api-3-screens-screenid-tabs-tabid-fields-post"""

TargetClassification = TypedDict(
    'TargetClassification',
    {
    'classifications': "dict[str, list[str]]",
    'issue_type': NotRequired["str"],
    'project_key_or_id': NotRequired["str"],
    },
)
"""Classification mapping for classifications in source issues to respective target classification."""

TargetMandatoryFields = TypedDict(
    'TargetMandatoryFields',
    {
    'fields': "dict[str, Fields]",
    },
)
"""Field mapping for mandatory fields in target"""

TargetStatus = TypedDict(
    'TargetStatus',
    {
    'statuses': "dict[str, list[str]]",
    },
)
"""Status mapping for statuses in source workflow to respective target status in target workflow."""

TargetToSourcesMapping = TypedDict(
    'TargetToSourcesMapping',
    {
    'infer_classification_defaults': "bool",
    'infer_field_defaults': "bool",
    'infer_status_defaults': "bool",
    'infer_subtask_type_default': "bool",
    'issue_ids_or_keys': NotRequired["list[str]"],
    'target_classification': NotRequired["list[TargetClassification | None] | None"],
    'target_mandatory_fields': NotRequired["list[TargetMandatoryFields | None] | None"],
    'target_status': NotRequired["list[TargetStatus | None] | None"],
    },
)
"""An object representing the mapping of issues and data related to destination entities, like fields and statuses, that are required during a bulk move."""

TaskProgress = TypedDict(
    'TaskProgress',
    {
    'description': NotRequired["str"],
    'elapsed_runtime': "int",
    'finished': NotRequired["str"],
    'id': "str",
    'last_update': "str",
    'message': NotRequired["str"],
    'progress': "int",
    'result': NotRequired["Any"],
    'self': "str",
    'started': NotRequired["str"],
    'status': "TaskProgressStatus",
    'submitted': NotRequired["str"],
    'submitted_by': "int",
    },
)
"""Details about a task."""

TaskProgressBeanJsonNode = TypedDict(
    'TaskProgressBeanJsonNode',
    {
    'description': NotRequired["str"],
    'elapsed_runtime': "int",
    'finished': NotRequired["int"],
    'id': "str",
    'last_update': "int",
    'message': NotRequired["str"],
    'progress': "int",
    'result': NotRequired["JsonNode"],
    'self': "str",
    'started': NotRequired["int"],
    'status': "TaskProgressBeanJsonNodeStatus",
    'submitted': "int",
    'submitted_by': "int",
    },
)
"""Details about a task."""

type TaskProgressBeanJsonNodeStatus = Literal['ENQUEUED', 'RUNNING', 'COMPLETE', 'FAILED', 'CANCEL_REQUESTED', 'CANCELLED', 'DEAD']
"""The status of the task."""

TaskProgressBeanObject = TypedDict(
    'TaskProgressBeanObject',
    {
    'description': NotRequired["str"],
    'elapsed_runtime': "int",
    'finished': NotRequired["int"],
    'id': "str",
    'last_update': "int",
    'message': NotRequired["str"],
    'progress': "int",
    'result': NotRequired["Any"],
    'self': "str",
    'started': NotRequired["int"],
    'status': "TaskProgressBeanObjectStatus",
    'submitted': "int",
    'submitted_by': "int",
    },
)
"""Details about a task."""

type TaskProgressBeanObjectStatus = Literal['ENQUEUED', 'RUNNING', 'COMPLETE', 'FAILED', 'CANCEL_REQUESTED', 'CANCELLED', 'DEAD']
"""The status of the task."""

TaskProgressBeanRemoveOptionFromIssuesResult = TypedDict(
    'TaskProgressBeanRemoveOptionFromIssuesResult',
    {
    'description': NotRequired["str"],
    'elapsed_runtime': "int",
    'finished': NotRequired["int"],
    'id': "str",
    'last_update': "int",
    'message': NotRequired["str"],
    'progress': "int",
    'result': NotRequired["RemoveOptionFromIssuesResult"],
    'self': "str",
    'started': NotRequired["int"],
    'status': "TaskProgressBeanRemoveOptionFromIssuesResultStatus",
    'submitted': "int",
    'submitted_by': "int",
    },
)
"""Details about a task."""

type TaskProgressBeanRemoveOptionFromIssuesResultStatus = Literal['ENQUEUED', 'RUNNING', 'COMPLETE', 'FAILED', 'CANCEL_REQUESTED', 'CANCELLED', 'DEAD']
"""The status of the task."""

type TaskProgressStatus = Literal['ENQUEUED', 'RUNNING', 'COMPLETE', 'FAILED', 'CANCEL_REQUESTED', 'CANCELLED', 'DEAD']
"""The status of the task."""

TimeTrackingConfiguration = TypedDict(
    'TimeTrackingConfiguration',
    {
    'default_unit': "TimeTrackingConfigurationDefaultUnit",
    'time_format': "TimeTrackingConfigurationTimeFormat",
    'working_days_per_week': "float",
    'working_hours_per_day': "float",
    },
)
"""Details of the time tracking configuration."""

type TimeTrackingConfigurationDefaultUnit = Literal['minute', 'hour', 'day', 'week']
"""The default unit of time applied to logged time."""

type TimeTrackingConfigurationTimeFormat = Literal['pretty', 'days', 'hours']
"""The format that will appear on an issue's *Time Spent* field."""

TimeTrackingDetails = TypedDict(
    'TimeTrackingDetails',
    {
    'original_estimate': NotRequired["str"],
    'original_estimate_seconds': NotRequired["int"],
    'remaining_estimate': NotRequired["str"],
    'remaining_estimate_seconds': NotRequired["int"],
    'time_spent': NotRequired["str"],
    'time_spent_seconds': NotRequired["int"],
    },
)
"""Time tracking details."""

TimeTrackingProvider = TypedDict(
    'TimeTrackingProvider',
    {
    'key': "str",
    'name': NotRequired["str"],
    'url': NotRequired["str"],
    },
)
"""Details about the time tracking provider."""

ToLayoutPayload = TypedDict(
    'ToLayoutPayload',
    {
    'port': NotRequired["int"],
    'status': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for the layout details for the destination end of a transition"""

Transition = TypedDict(
    'Transition',
    {
    'description': "str",
    'from': "list[str]",
    'id': "str",
    'name': "str",
    'properties': NotRequired["dict[str, Any]"],
    'rules': NotRequired["WorkflowRules"],
    'screen': NotRequired["TransitionScreenDetails"],
    'to': "str",
    'type': "TransitionType",
    },
)
"""Details of a workflow transition."""

TransitionLink = TypedDict(
    'TransitionLink',
    {
    'from_port': NotRequired["int"],
    'from_status_reference': NotRequired["str"],
    'to_port': NotRequired["int"],
    },
)
"""Link information for workflow transitions."""

TransitionPayload = TypedDict(
    'TransitionPayload',
    {
    'actions': NotRequired["list[RulePayload]"],
    'conditions': NotRequired["ConditionGroupPayload"],
    'custom_issue_event_id': NotRequired["str"],
    'description': NotRequired["str"],
    'from': NotRequired["list[FromLayoutPayload]"],
    'id': NotRequired["int"],
    'name': NotRequired["str"],
    'properties': NotRequired["dict[str, str]"],
    'to': NotRequired["ToLayoutPayload"],
    'transition_screen': NotRequired["RulePayload"],
    'triggers': NotRequired["list[RulePayload]"],
    'type': NotRequired["TransitionPayloadType"],
    'validators': NotRequired["list[RulePayload]"],
    },
)
"""The payload for creating a transition in a workflow. Can be DIRECTED, GLOBAL, SELF-LOOPED, GLOBAL LOOPED"""

type TransitionPayloadType = Literal['global', 'initial', 'directed']
"""The type of the transition"""

TransitionPreview = TypedDict(
    'TransitionPreview',
    {
    'actions': NotRequired["list[PreviewRuleConfiguration | None]"],
    'conditions': NotRequired["PreviewConditionGroupConfiguration | None"],
    'custom_issue_event_id': NotRequired["str"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'links': NotRequired["list[TransitionLink]"],
    'name': NotRequired["str"],
    'to_status_reference': NotRequired["str"],
    'transition_screen': NotRequired["PreviewRuleConfiguration | None"],
    'triggers': NotRequired["list[PreviewTrigger]"],
    'type': NotRequired["TransitionPreviewType"],
    'validators': NotRequired["list[PreviewRuleConfiguration | None]"],
    },
)
"""Details about a workflow transition in preview context."""

type TransitionPreviewType = Literal['INITIAL', 'GLOBAL', 'DIRECTED']
"""The transition type."""

TransitionScreenDetails = TypedDict(
    'TransitionScreenDetails',
    {
    'id': "str",
    'name': NotRequired["str"],
    },
)
"""The details of a transition screen."""

type TransitionType = Literal['global', 'initial', 'directed']
"""The type of the transition."""

TransitionUpdateDto = TypedDict(
    'TransitionUpdateDto',
    {
    'actions': NotRequired["list[WorkflowRuleConfiguration | None]"],
    'conditions': NotRequired["ConditionGroupUpdate | None"],
    'custom_issue_event_id': NotRequired["str"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'links': NotRequired["list[WorkflowTransitionLinks | None]"],
    'name': NotRequired["str"],
    'properties': NotRequired["dict[str, str]"],
    'to_status_reference': NotRequired["str"],
    'transition_screen': NotRequired["WorkflowRuleConfiguration | None"],
    'triggers': NotRequired["list[WorkflowTrigger]"],
    'type': NotRequired["TransitionUpdateDtoType"],
    'validators': NotRequired["list[WorkflowRuleConfiguration | None]"],
    },
)
"""The transition update data."""

type TransitionUpdateDtoType = Literal['INITIAL', 'GLOBAL', 'DIRECTED']
"""The transition type."""

Transitions = TypedDict(
    'Transitions',
    {
    'expand': NotRequired["str"],
    'transitions': NotRequired["list[IssueTransition]"],
    },
)
"""List of issue transitions."""

UiModificationContextDetails = TypedDict(
    'UiModificationContextDetails',
    {
    'id': NotRequired["str"],
    'is_available': NotRequired["bool"],
    'issue_type_id': NotRequired["str"],
    'portal_id': NotRequired["str"],
    'project_id': NotRequired["str"],
    'request_type_id': NotRequired["str"],
    'view_type': NotRequired["UiModificationContextDetailsViewType"],
    },
)
"""The details of a UI modification's context, which define where to activate the UI modification."""

type UiModificationContextDetailsViewType = Literal['GIC', 'IssueView', 'IssueTransition', 'JSMRequestCreate', 'GICAgentView', 'IssueViewAgentView', 'IssueTransitionAgentView']
"""
The view type of the context.  
Supported values:

 *  `GIC` \\- Jira global issue create
 *  `IssueView` \\- Jira issue view
 *  `IssueTransition` \\- Jira issue transition
 *  `JSMRequestCreate` \\- Jira Service Management request create portal view
 *  `GICAgentView` \\- Agent view variant of Jira global issue create
 *  `IssueViewAgentView` \\- Agent view variant of Jira issue view
 *  `IssueTransitionAgentView` \\- Agent view variant of Jira issue transition

For Jira and Agent view types (`GIC`, `IssueView`, `IssueTransition`, `GICAgentView`, `IssueViewAgentView`, `IssueTransitionAgentView`), null is treated as a wildcard, meaning the UI modification will be applied to all view types. Each Jira or Agent context can have a maximum of one wildcard.  
  
Agent view contexts use `projectId` and `issueTypeId` like Jira contexts, and may optionally also set `requestTypeId`. Agent view contexts must not set `portalId`.  
  
Wildcards are not applicable for JSM contexts.
"""

UiModificationDetails = TypedDict(
    'UiModificationDetails',
    {
    'contexts': NotRequired["list[UiModificationContextDetails]"],
    'data': NotRequired["str"],
    'description': NotRequired["str"],
    'id': "str",
    'name': "str",
    'self': "str",
    },
)
"""The details of a UI modification."""

UiModificationIdentifiers = TypedDict(
    'UiModificationIdentifiers',
    {
    'id': "str",
    'self': "str",
    },
)
"""Identifiers for a UI modification."""

UnrestrictedUserEmail = TypedDict(
    'UnrestrictedUserEmail',
    {
    'account_id': NotRequired["str"],
    'email': NotRequired["str"],
    },
)

UpdateCustomFieldDetails = TypedDict(
    'UpdateCustomFieldDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'searcher_key': NotRequired["UpdateCustomFieldDetailsSearcherKey"],
    },
)
"""Details of a custom field."""

type UpdateCustomFieldDetailsSearcherKey = Literal['com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:daterange', 'com.atlassian.jira.plugin.system.customfieldtypes:datetimerange', 'com.atlassian.jira.plugin.system.customfieldtypes:exactnumber', 'com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:numberrange', 'com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:textsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher', 'com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher']
"""
The searcher that defines the way the field is searched in Jira. It can be set to `null`, otherwise you must specify the valid searcher for the field type, as listed below (abbreviated values shown):

 *  `cascadingselect`: `cascadingselectsearcher`
 *  `datepicker`: `daterange`
 *  `datetime`: `datetimerange`
 *  `float`: `exactnumber` or `numberrange`
 *  `grouppicker`: `grouppickersearcher`
 *  `importid`: `exactnumber` or `numberrange`
 *  `labels`: `labelsearcher`
 *  `multicheckboxes`: `multiselectsearcher`
 *  `multigrouppicker`: `multiselectsearcher`
 *  `multiselect`: `multiselectsearcher`
 *  `multiuserpicker`: `userpickergroupsearcher`
 *  `multiversion`: `versionsearcher`
 *  `project`: `projectsearcher`
 *  `radiobuttons`: `multiselectsearcher`
 *  `readonlyfield`: `textsearcher`
 *  `select`: `multiselectsearcher`
 *  `textarea`: `textsearcher`
 *  `textfield`: `textsearcher`
 *  `url`: `exacttextsearcher`
 *  `userpicker`: `userpickergroupsearcher`
 *  `version`: `versionsearcher`
"""

UpdateDefaultProjectClassificationBean = TypedDict(
    'UpdateDefaultProjectClassificationBean',
    {
    'id': "str",
    },
)
"""The request for updating the default project classification level."""

UpdateDefaultScreenScheme = TypedDict(
    'UpdateDefaultScreenScheme',
    {
    'screen_scheme_id': "str",
    },
)
"""The ID of a screen scheme."""

UpdateFieldAssociationSchemeLinksBean = TypedDict(
    'UpdateFieldAssociationSchemeLinksBean',
    {
    'associations': NotRequired["str"],
    'projects': NotRequired["str"],
    },
)

UpdateFieldAssociationSchemeRequest = TypedDict(
    'UpdateFieldAssociationSchemeRequest',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Request object for updating an existing field association scheme."""

UpdateFieldAssociationSchemeResponse = TypedDict(
    'UpdateFieldAssociationSchemeResponse',
    {
    'description': NotRequired["str"],
    'id': NotRequired["int"],
    'links': NotRequired["UpdateFieldAssociationSchemeLinksBean"],
    'name': NotRequired["str"],
    },
)
"""Response object after successfully updating an existing field association scheme."""

UpdateFieldAssociationsRequestItem = TypedDict(
    'UpdateFieldAssociationsRequestItem',
    {
    'restricted_to_work_types': NotRequired["list[int]"],
    'scheme_ids': "list[int]",
    },
)
"""Represents an association between a field and its operations."""

UpdateFieldConfigurationSchemeDetails = TypedDict(
    'UpdateFieldConfigurationSchemeDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""The details of the field configuration scheme."""

UpdateFieldSchemeParametersPartialFailure = TypedDict(
    'UpdateFieldSchemeParametersPartialFailure',
    {
    'error': NotRequired["str"],
    'field_id': "str",
    'scheme_id': "int",
    'success': "bool",
    'work_type_id': NotRequired["int"],
    },
)
"""Result of updating field scheme parameters for a specific field, scheme, and optional work type."""

UpdateFieldSchemeParametersRequest = TypedDict(
    'UpdateFieldSchemeParametersRequest',
    {
    'parameters': NotRequired["FieldsSchemeItemParameter"],
    'scheme_ids': NotRequired["list[int]"],
    'work_type_parameters': NotRequired["list[FieldsSchemeItemWorkTypeParameter]"],
    },
)
"""Request bean for updating field scheme parameters across multiple schemes and work types."""

UpdateFieldSchemeParametersResponse = TypedDict(
    'UpdateFieldSchemeParametersResponse',
    {
    'results': "list[UpdateFieldSchemeParametersPartialFailure]",
    },
)
"""Response bean for field scheme parameter update operations."""

UpdateIssueSecurityLevelDetails = TypedDict(
    'UpdateIssueSecurityLevelDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of issue security scheme level."""

UpdateIssueSecuritySchemeRequestBean = TypedDict(
    'UpdateIssueSecuritySchemeRequestBean',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)

UpdateNotificationSchemeDetails = TypedDict(
    'UpdateNotificationSchemeDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of a notification scheme."""

UpdatePrioritiesInSchemeRequestBean = TypedDict(
    'UpdatePrioritiesInSchemeRequestBean',
    {
    'add': NotRequired["PrioritySchemeChangesWithoutMappings"],
    'remove': NotRequired["PrioritySchemeChangesWithoutMappings"],
    },
)
"""Update priorities in a scheme"""

UpdatePriorityDetails = TypedDict(
    'UpdatePriorityDetails',
    {
    'avatar_id': NotRequired["int"],
    'description': NotRequired["str | None"],
    'icon_url': NotRequired["UpdatePriorityDetailsIconUrl | None"],
    'name': NotRequired["str | None"],
    'status_color': NotRequired["str | None"],
    },
)
"""Details of an issue priority."""

type UpdatePriorityDetailsIconUrl = Literal['/images/icons/priorities/blocker.png', '/images/icons/priorities/critical.png', '/images/icons/priorities/high.png', '/images/icons/priorities/highest.png', '/images/icons/priorities/low.png', '/images/icons/priorities/lowest.png', '/images/icons/priorities/major.png', '/images/icons/priorities/medium.png', '/images/icons/priorities/minor.png', '/images/icons/priorities/trivial.png', '/images/icons/priorities/blocker_new.png', '/images/icons/priorities/critical_new.png', '/images/icons/priorities/high_new.png', '/images/icons/priorities/highest_new.png', '/images/icons/priorities/low_new.png', '/images/icons/priorities/lowest_new.png', '/images/icons/priorities/major_new.png', '/images/icons/priorities/medium_new.png', '/images/icons/priorities/minor_new.png', '/images/icons/priorities/trivial_new.png']
"""The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Both iconUrl and avatarId cannot be defined."""

UpdatePrioritySchemeRequestBean = TypedDict(
    'UpdatePrioritySchemeRequestBean',
    {
    'default_priority_id': NotRequired["int"],
    'description': NotRequired["str"],
    'mappings': NotRequired["PriorityMapping"],
    'name': NotRequired["str"],
    'priorities': NotRequired["UpdatePrioritiesInSchemeRequestBean"],
    'projects': NotRequired["UpdateProjectsInSchemeRequestBean"],
    },
)
"""Details of a priority scheme."""

UpdatePrioritySchemeResponseBean = TypedDict(
    'UpdatePrioritySchemeResponseBean',
    {
    'priority_scheme': NotRequired["PrioritySchemeWithPaginatedPrioritiesAndProjects"],
    'task': NotRequired["TaskProgressBeanJsonNode"],
    },
)
"""Details of the updated priority scheme."""

UpdateProjectDetails = TypedDict(
    'UpdateProjectDetails',
    {
    'assignee_type': NotRequired["UpdateProjectDetailsAssigneeType"],
    'avatar_id': NotRequired["int"],
    'category_id': NotRequired["int"],
    'description': NotRequired["str"],
    'issue_security_scheme': NotRequired["int"],
    'key': NotRequired["str"],
    'lead': NotRequired["str"],
    'lead_account_id': NotRequired["str"],
    'name': NotRequired["str"],
    'notification_scheme': NotRequired["int"],
    'permission_scheme': NotRequired["int"],
    'released_project_keys': NotRequired["list[str]"],
    'url': NotRequired["str"],
    },
)
"""Details about the project."""

type UpdateProjectDetailsAssigneeType = Literal['PROJECT_LEAD', 'UNASSIGNED']
"""The default assignee when creating issues for this project."""

UpdateProjectsInSchemeRequestBean = TypedDict(
    'UpdateProjectsInSchemeRequestBean',
    {
    'add': NotRequired["PrioritySchemeChangesWithoutMappings"],
    'remove': NotRequired["PrioritySchemeChangesWithoutMappings"],
    },
)
"""Update projects in a scheme"""

UpdateResolutionDetails = TypedDict(
    'UpdateResolutionDetails',
    {
    'description': NotRequired["str"],
    'name': "str",
    },
)
"""Details of an issue resolution."""

UpdateScreenDetails = TypedDict(
    'UpdateScreenDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""Details of a screen."""

UpdateScreenSchemeDetails = TypedDict(
    'UpdateScreenSchemeDetails',
    {
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    'screens': NotRequired["UpdateScreenTypes"],
    },
)
"""Details of a screen scheme."""

UpdateScreenTypes = TypedDict(
    'UpdateScreenTypes',
    {
    'create': NotRequired["str"],
    'default': NotRequired["str"],
    'edit': NotRequired["str"],
    'view': NotRequired["str"],
    },
)
"""The IDs of the screens for the screen types of the screen scheme."""

UpdateUiModificationDetails = TypedDict(
    'UpdateUiModificationDetails',
    {
    'contexts': NotRequired["list[UiModificationContextDetails]"],
    'data': NotRequired["str"],
    'description': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""The details of a UI modification."""

UpdateUserToGroupBean = TypedDict(
    'UpdateUserToGroupBean',
    {
    'account_id': NotRequired["str"],
    'name': NotRequired["str"],
    },
)

type UpdateWorklogAdjustEstimate = Literal['new', 'leave', 'manual', 'auto']

UpdatedProjectCategory = TypedDict(
    'UpdatedProjectCategory',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)
"""A project category."""

User = TypedDict(
    'User',
    {
    'account_id': NotRequired["str"],
    'account_type': NotRequired["UserAccountType"],
    'active': NotRequired["bool"],
    'app_type': NotRequired["str"],
    'application_roles': NotRequired["SimpleListWrapperApplicationRole"],
    'avatar_urls': NotRequired["AvatarUrlsBean"],
    'display_name': NotRequired["str"],
    'email_address': NotRequired["str"],
    'expand': NotRequired["str"],
    'groups': NotRequired["SimpleListWrapperGroupName"],
    'guest': NotRequired["bool"],
    'key': NotRequired["str"],
    'locale': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    'time_zone': NotRequired["str"],
    },
)
"""
A user with details as permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case, `displayName` provides an indication and other parameters have default values or are blank (for example, email is blank).
 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values.
"""

type UserAccountType = Literal['atlassian', 'app', 'customer', 'unknown']
"""
The user account type. Can take the following values:

 *  `atlassian` regular Atlassian user account
 *  `app` system account used for Connect applications and OAuth to represent external systems
 *  `customer` Jira Service Desk account representing an external service desk
"""

UserBean = TypedDict(
    'UserBean',
    {
    'account_id': NotRequired["str"],
    'active': NotRequired["bool"],
    'avatar_urls': NotRequired["UserBeanAvatarUrls"],
    'display_name': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    },
)

UserBeanAvatarUrls = TypedDict(
    'UserBeanAvatarUrls',
    {
    'n16_x_16': NotRequired["str"],
    'n24_x_24': NotRequired["str"],
    'n32_x_32': NotRequired["str"],
    'n48_x_48': NotRequired["str"],
    },
)

UserColumnRequestBody = TypedDict(
    'UserColumnRequestBody',
    {
    'columns': NotRequired["list[str]"],
    },
)

UserContextVariable = TypedDict(
    'UserContextVariable',
    {
    'account_id': "str",
    'type': "str",
    },
)
"""A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID."""

UserDetails = TypedDict(
    'UserDetails',
    {
    'account_id': NotRequired["str"],
    'account_type': NotRequired["str"],
    'active': NotRequired["bool"],
    'avatar_urls': NotRequired["AvatarUrlsBean"],
    'display_name': NotRequired["str"],
    'email_address': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'self': NotRequired["str"],
    'time_zone': NotRequired["str"],
    },
)
"""
User details permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case, `displayName` provides an indication and other parameters have default values or are blank (for example, email is blank).
 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values.
"""

UserFilter = TypedDict(
    'UserFilter',
    {
    'enabled': "bool",
    'groups': NotRequired["list[str]"],
    'role_ids': NotRequired["list[int]"],
    },
)
"""Filter for a User Picker (single) custom field."""

UserKey = TypedDict(
    'UserKey',
    {
    'account_id': NotRequired["str"],
    'key': NotRequired["str"],
    },
)
"""List of user account IDs."""

UserList = TypedDict(
    'UserList',
    {
    'end_index': NotRequired["int"],
    'items': NotRequired["list[User]"],
    'max_results': NotRequired["int"],
    'size': NotRequired["int"],
    'start_index': NotRequired["int"],
    },
)
"""A paginated list of users sharing the filter. This includes users that are members of the groups or can browse the projects that the filter is shared with."""

UserMigrationBean = TypedDict(
    'UserMigrationBean',
    {
    'account_id': NotRequired["str"],
    'key': NotRequired["str"],
    'username': NotRequired["str"],
    },
)

UserPermission = TypedDict(
    'UserPermission',
    {
    'deprecated_key': NotRequired["bool"],
    'description': NotRequired["str"],
    'have_permission': NotRequired["bool"],
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["UserPermissionType"],
    },
)
"""Details of a permission and its availability to a user."""

type UserPermissionType = Literal['GLOBAL', 'PROJECT']
"""The type of the permission."""

UserPickerUser = TypedDict(
    'UserPickerUser',
    {
    'account_id': NotRequired["str"],
    'account_type': NotRequired["UserPickerUserAccountType"],
    'avatar_url': NotRequired["str"],
    'display_name': NotRequired["str"],
    'html': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    },
)
"""A user found in a search."""

type UserPickerUserAccountType = Literal['atlassian', 'app', 'customer', 'unknown']
"""
The user account type. Can take the following values:

 *  `atlassian` regular Atlassian user account
 *  `app` system account used for Connect applications and OAuth to represent external systems
 *  `customer` Jira Service Desk account representing an external service desk
"""

ValidatePolicyRequest = TypedDict(
    'ValidatePolicyRequest',
    {
    'policy_ids': NotRequired["list[str]"],
    },
)

ValidationOptionsForCreate = TypedDict(
    'ValidationOptionsForCreate',
    {
    'levels': NotRequired["list[ValidationOptionsForCreateLevelsItem]"],
    },
)
"""The level of validation to return from the API. If no values are provided, the default would return `WARNING` and `ERROR` level validation results."""

type ValidationOptionsForCreateLevelsItem = Literal['WARNING', 'ERROR']

ValidationOptionsForUpdate = TypedDict(
    'ValidationOptionsForUpdate',
    {
    'levels': NotRequired["list[ValidationOptionsForUpdateLevelsItem]"],
    },
)
"""The level of validation to return from the API. If no values are provided, the default would return `WARNING` and `ERROR` level validation results."""

type ValidationOptionsForUpdateLevelsItem = Literal['WARNING', 'ERROR']

ValueOperand = TypedDict(
    'ValueOperand',
    {
    'encoded_value': NotRequired["str"],
    'value': "str",
    },
)
"""An operand that is a user-provided value."""

Version = TypedDict(
    'Version',
    {
    'approvers': NotRequired["list[VersionApprover]"],
    'archived': NotRequired["bool"],
    'description': NotRequired["str"],
    'driver': NotRequired["str"],
    'expand': NotRequired["str"],
    'id': NotRequired["str"],
    'issues_status_for_fix_version': NotRequired["VersionIssuesStatus"],
    'move_unfixed_issues_to': NotRequired["str"],
    'name': NotRequired["str"],
    'operations': NotRequired["list[SimpleLink]"],
    'overdue': NotRequired["bool"],
    'project': NotRequired["str"],
    'project_id': NotRequired["int"],
    'release_date': NotRequired["str"],
    'released': NotRequired["bool"],
    'self': NotRequired["str"],
    'start_date': NotRequired["str"],
    'user_release_date': NotRequired["str"],
    'user_start_date': NotRequired["str"],
    },
)
"""Details about a project version."""

VersionApprover = TypedDict(
    'VersionApprover',
    {
    'account_id': NotRequired["str"],
    'decline_reason': NotRequired["str"],
    'description': NotRequired["str"],
    'status': NotRequired["str"],
    },
)
"""Contains details about a version approver."""

VersionIssueCounts = TypedDict(
    'VersionIssueCounts',
    {
    'custom_field_usage': NotRequired["list[VersionUsageInCustomField]"],
    'issue_count_with_custom_fields_showing_version': NotRequired["int"],
    'issues_affected_count': NotRequired["int"],
    'issues_fixed_count': NotRequired["int"],
    'self': NotRequired["str"],
    },
)
"""Various counts of issues within a version."""

VersionIssuesStatus = TypedDict(
    'VersionIssuesStatus',
    {
    'done': NotRequired["int"],
    'in_progress': NotRequired["int"],
    'to_do': NotRequired["int"],
    'unmapped': NotRequired["int"],
    },
)
"""Counts of the number of issues in various statuses."""

VersionMoveBean = TypedDict(
    'VersionMoveBean',
    {
    'after': NotRequired["str"],
    'position': NotRequired["VersionMoveBeanPosition"],
    },
)

type VersionMoveBeanPosition = Literal['Earlier', 'Later', 'First', 'Last']
"""An absolute position in which to place the moved version. Cannot be used with `after`."""

VersionRelatedWork = TypedDict(
    'VersionRelatedWork',
    {
    'category': "str",
    'issue_id': NotRequired["int"],
    'related_work_id': NotRequired["str"],
    'title': NotRequired["str"],
    'url': NotRequired["str"],
    },
)
"""Associated related work to a version"""

VersionUnresolvedIssuesCount = TypedDict(
    'VersionUnresolvedIssuesCount',
    {
    'issues_count': NotRequired["int"],
    'issues_unresolved_count': NotRequired["int"],
    'self': NotRequired["str"],
    },
)
"""Count of a version's unresolved issues."""

VersionUsageInCustomField = TypedDict(
    'VersionUsageInCustomField',
    {
    'custom_field_id': NotRequired["int"],
    'field_name': NotRequired["str"],
    'issue_count_with_version_in_custom_field': NotRequired["int"],
    },
)
"""List of custom fields using the version."""

Visibility = TypedDict(
    'Visibility',
    {
    'identifier': NotRequired["str | None"],
    'type': NotRequired["VisibilityType"],
    'value': NotRequired["str"],
    },
)
"""The group or role to which this item is visible."""

type VisibilityType = Literal['group', 'role']
"""Whether visibility of this item is restricted to a group or role."""

Votes = TypedDict(
    'Votes',
    {
    'has_voted': NotRequired["bool"],
    'self': NotRequired["str"],
    'voters': NotRequired["list[User]"],
    'votes': NotRequired["int"],
    },
)
"""The details of votes on an issue."""

WarningCollection = TypedDict(
    'WarningCollection',
    {
    'warnings': NotRequired["list[str]"],
    },
)

Watchers = TypedDict(
    'Watchers',
    {
    'is_watching': NotRequired["bool"],
    'self': NotRequired["str"],
    'watch_count': NotRequired["int"],
    'watchers': NotRequired["list[UserDetails]"],
    },
)
"""The details of watchers on an issue."""

Webhook = TypedDict(
    'Webhook',
    {
    'events': "list[WebhookEventsItem]",
    'expiration_date': NotRequired["int"],
    'field_ids_filter': NotRequired["list[str]"],
    'id': "int",
    'issue_property_keys_filter': NotRequired["list[str]"],
    'jql_filter': "str",
    'url': "str",
    },
)
"""A webhook."""

WebhookDetails = TypedDict(
    'WebhookDetails',
    {
    'events': "list[WebhookDetailsEventsItem]",
    'field_ids_filter': NotRequired["list[str]"],
    'issue_property_keys_filter': NotRequired["list[str]"],
    'jql_filter': "str",
    },
)
"""A list of webhooks."""

type WebhookDetailsEventsItem = Literal['jira:issue_created', 'jira:issue_updated', 'jira:issue_deleted', 'comment_created', 'comment_updated', 'comment_deleted', 'issue_property_set', 'issue_property_deleted', 'sprint_created', 'sprint_updated', 'sprint_closed', 'sprint_deleted', 'sprint_started', 'jira:version_released', 'jira:version_unreleased', 'jira:version_created', 'jira:version_moved', 'jira:version_updated', 'jira:version_merged', 'jira:version_deleted']

type WebhookEventsItem = Literal['jira:issue_created', 'jira:issue_updated', 'jira:issue_deleted', 'comment_created', 'comment_updated', 'comment_deleted', 'issue_property_set', 'issue_property_deleted', 'sprint_created', 'sprint_updated', 'sprint_closed', 'sprint_deleted', 'sprint_started', 'jira:version_released', 'jira:version_unreleased', 'jira:version_created', 'jira:version_moved', 'jira:version_updated', 'jira:version_merged', 'jira:version_deleted']

WebhookRegistrationDetails = TypedDict(
    'WebhookRegistrationDetails',
    {
    'url': "str",
    'webhooks': "list[WebhookDetails]",
    },
)
"""Details of webhooks to register."""

WebhooksExpirationDate = TypedDict(
    'WebhooksExpirationDate',
    {
    'expiration_date': "int",
    },
)
"""The date the refreshed webhooks expire."""

WorkTypeParameters = TypedDict(
    'WorkTypeParameters',
    {
    'description': NotRequired["str"],
    'is_required': "bool",
    'renderer_type': NotRequired["str"],
    'work_type_id': "int",
    },
)

Workflow = TypedDict(
    'Workflow',
    {
    'created': NotRequired["str"],
    'description': "str",
    'has_draft_workflow': NotRequired["bool"],
    'id': "PublishedWorkflowId",
    'is_default': NotRequired["bool"],
    'operations': NotRequired["WorkflowOperations"],
    'projects': NotRequired["list[ProjectDetails]"],
    'schemes': NotRequired["list[WorkflowSchemeIdName]"],
    'statuses': NotRequired["list[WorkflowStatus]"],
    'transitions': NotRequired["list[Transition]"],
    'updated': NotRequired["str"],
    },
)
"""Details about a workflow."""

WorkflowAssociationStatusMapping = TypedDict(
    'WorkflowAssociationStatusMapping',
    {
    'new_status_id': NotRequired["str"],
    'old_status_id': NotRequired["str"],
    },
)

WorkflowCapabilities = TypedDict(
    'WorkflowCapabilities',
    {
    'connect_rules': NotRequired["list[AvailableWorkflowConnectRule]"],
    'editor_scope': NotRequired["WorkflowCapabilitiesEditorScope"],
    'forge_rules': NotRequired["list[AvailableWorkflowForgeRule]"],
    'project_types': NotRequired["list[WorkflowCapabilitiesProjectTypesItem]"],
    'system_rules': NotRequired["list[AvailableWorkflowSystemRule]"],
    'trigger_rules': NotRequired["list[AvailableWorkflowTriggers]"],
    },
)

type WorkflowCapabilitiesEditorScope = Literal['PROJECT', 'GLOBAL']
"""The scope of the workflow capabilities. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."""

type WorkflowCapabilitiesProjectTypesItem = Literal['software', 'service_desk', 'product_discovery', 'business', 'unknown']

WorkflowCapabilityPayload = TypedDict(
    'WorkflowCapabilityPayload',
    {
    'statuses': NotRequired["list[StatusPayload]"],
    'workflow_scheme': NotRequired["WorkflowSchemePayload"],
    'workflows': NotRequired["list[WorkflowPayload]"],
    },
)
"""The payload for creating a workflows. See https://www.atlassian.com/software/jira/guides/workflows/overview\\#what-is-a-jira-workflow"""

WorkflowCompoundCondition = TypedDict(
    'WorkflowCompoundCondition',
    {
    'conditions': "list[WorkflowCondition]",
    'node_type': "str",
    'operator': "WorkflowCompoundConditionOperator",
    },
)
"""A compound workflow transition rule condition. This object returns `nodeType` as `compound`."""

type WorkflowCompoundConditionOperator = Literal['AND', 'OR']
"""The compound condition operator."""

type WorkflowCondition = WorkflowSimpleCondition | WorkflowCompoundCondition
"""The workflow transition rule conditions tree."""

WorkflowCopyRequest = TypedDict(
    'WorkflowCopyRequest',
    {
    'description': NotRequired["str"],
    'workflow_id': "str",
    'workflow_name': "str",
    },
)
"""The copy workflow payload."""

WorkflowCreate = TypedDict(
    'WorkflowCreate',
    {
    'description': NotRequired["str"],
    'looped_transition_container_layout': NotRequired["WorkflowLayout | None"],
    'name': "str",
    'start_point_layout': NotRequired["WorkflowLayout | None"],
    'statuses': "list[StatusLayoutUpdate]",
    'transitions': "list[TransitionUpdateDto]",
    },
)
"""The details of the workflows to create."""

WorkflowCreateRequest = TypedDict(
    'WorkflowCreateRequest',
    {
    'scope': NotRequired["WorkflowScope"],
    'statuses': NotRequired["list[WorkflowStatusUpdate]"],
    'workflows': NotRequired["list[WorkflowCreate]"],
    },
)
"""The create workflows payload."""

WorkflowCreateResponse = TypedDict(
    'WorkflowCreateResponse',
    {
    'statuses': NotRequired["list[JiraWorkflowStatus]"],
    'workflows': NotRequired["list[JiraWorkflow]"],
    },
)
"""Details of the created workflows and statuses."""

WorkflowCreateValidateRequest = TypedDict(
    'WorkflowCreateValidateRequest',
    {
    'payload': "WorkflowCreateRequest",
    'validation_options': NotRequired["ValidationOptionsForCreate"],
    },
)

WorkflowDocumentDto = TypedDict(
    'WorkflowDocumentDto',
    {
    'created': NotRequired["str"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'last_update_author_aaid': NotRequired["str"],
    'looped_transition_container_layout': NotRequired["WorkflowLayout | None"],
    'name': NotRequired["str"],
    'scope': NotRequired["WorkflowScope"],
    'start_point_layout': NotRequired["WorkflowLayout | None"],
    'statuses': NotRequired["list[WorkflowReferenceStatus]"],
    'transitions': NotRequired["list[WorkflowTransitions]"],
    'updated': NotRequired["str"],
    'version': NotRequired["DocumentVersion"],
    },
)
"""The workflow stored for the specified version."""

WorkflowDocumentStatusDto = TypedDict(
    'WorkflowDocumentStatusDto',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'scope': NotRequired["WorkflowScope"],
    'status_category': NotRequired["str"],
    'status_reference': NotRequired["str"],
    },
)
"""The statuses stored for the specified version."""

WorkflowDocumentVersionBean = TypedDict(
    'WorkflowDocumentVersionBean',
    {
    'id': NotRequired["str"],
    'version_number': NotRequired["int"],
    },
)
"""The version details of the workflow."""

WorkflowElementReference = TypedDict(
    'WorkflowElementReference',
    {
    'property_key': NotRequired["str"],
    'rule_id': NotRequired["str"],
    'status_mapping_reference': NotRequired["ProjectAndIssueTypePair"],
    'status_reference': NotRequired["str"],
    'transition_id': NotRequired["str"],
    },
)
"""A reference to the location of the error. This will be null if the error does not refer to a specific element."""

WorkflowHistoryItemDto = TypedDict(
    'WorkflowHistoryItemDto',
    {
    'is_intermediate': NotRequired["bool"],
    'workflow_id': NotRequired["str"],
    'workflow_version': NotRequired["int"],
    'written_at': NotRequired["str"],
    },
)
"""A single entry in the WorkflowHistoryPage."""

WorkflowHistoryListRequest = TypedDict(
    'WorkflowHistoryListRequest',
    {
    'workflow_id': NotRequired["str"],
    },
)
"""A request to read all the workflow history entries for a specific workflow."""

WorkflowHistoryListResponseDto = TypedDict(
    'WorkflowHistoryListResponseDto',
    {
    'entries': NotRequired["list[WorkflowHistoryItemDto]"],
    },
)
"""A list of workflow history entries."""

WorkflowHistoryReadRequest = TypedDict(
    'WorkflowHistoryReadRequest',
    {
    'version': NotRequired["int"],
    'workflow_id': NotRequired["str"],
    },
)
"""A request to read a specific workflow version from history."""

WorkflowHistoryReadResponseDto = TypedDict(
    'WorkflowHistoryReadResponseDto',
    {
    'statuses': NotRequired["list[WorkflowDocumentStatusDto]"],
    'workflows': NotRequired["list[WorkflowDocumentDto]"],
    },
)
"""The specified workflow version read from history."""

WorkflowId = TypedDict(
    'WorkflowId',
    {
    'draft': NotRequired["bool"],
    'name': "str",
    },
)
"""Properties that identify a workflow."""

WorkflowLayout = TypedDict(
    'WorkflowLayout',
    {
    'x': NotRequired["float"],
    'y': NotRequired["float"],
    },
)
"""The starting point for the statuses in the workflow."""

WorkflowMetadataAndIssueTypeRestModel = TypedDict(
    'WorkflowMetadataAndIssueTypeRestModel',
    {
    'issue_type_ids': "list[str]",
    'workflow': "WorkflowMetadataRestModel",
    },
)
"""The workflow metadata and issue type IDs which use this workflow."""

WorkflowMetadataRestModel = TypedDict(
    'WorkflowMetadataRestModel',
    {
    'description': "str",
    'id': "str",
    'name': "str",
    'version': "DocumentVersion",
    },
)
"""Workflow metadata and usage detail."""

WorkflowOperations = TypedDict(
    'WorkflowOperations',
    {
    'can_delete': "bool",
    'can_edit': "bool",
    },
)
"""Operations allowed on a workflow"""

WorkflowPayload = TypedDict(
    'WorkflowPayload',
    {
    'description': NotRequired["str"],
    'looped_transition_container_layout': NotRequired["WorkflowStatusLayoutPayload"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["WorkflowPayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'start_point_layout': NotRequired["WorkflowStatusLayoutPayload"],
    'statuses': NotRequired["list[WorkflowStatusPayload]"],
    'transitions': NotRequired["list[TransitionPayload]"],
    },
)
"""The payload for creating workflow, see https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\\#api-rest-api-3-workflows-create-post"""

type WorkflowPayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use if there is a conflict with another workflow"""

WorkflowPreview = TypedDict(
    'WorkflowPreview',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'looped_transition_container_layout': NotRequired["WorkflowPreviewLayout"],
    'name': NotRequired["str"],
    'query_context': NotRequired["list[ProjectIssueTypeQueryContext]"],
    'scope': NotRequired["WorkflowPreviewScope"],
    'start_point_layout': NotRequired["WorkflowPreviewLayout"],
    'statuses': NotRequired["list[WorkflowPreviewStatus]"],
    'transitions': NotRequired["list[TransitionPreview]"],
    'version': NotRequired["WorkflowDocumentVersionBean"],
    },
)
"""Details of a workflow."""

WorkflowPreviewLayout = TypedDict(
    'WorkflowPreviewLayout',
    {
    'x': NotRequired["float"],
    'y': NotRequired["float"],
    },
)
"""Layout coordinates for workflow elements."""

WorkflowPreviewRequest = TypedDict(
    'WorkflowPreviewRequest',
    {
    'issue_type_ids': NotRequired["list[str]"],
    'project_id': "str",
    'workflow_ids': NotRequired["list[str]"],
    'workflow_names': NotRequired["list[str]"],
    },
)
"""The details of the preview workflow request."""

WorkflowPreviewResponse = TypedDict(
    'WorkflowPreviewResponse',
    {
    'statuses': NotRequired["list[JiraWorkflowPreviewStatus]"],
    'workflows': NotRequired["list[WorkflowPreview]"],
    },
)
"""The preview workflow response containing workflows and statuses."""

WorkflowPreviewScope = TypedDict(
    'WorkflowPreviewScope',
    {
    'project': NotRequired["WorkflowProjectIdScope | None"],
    'type': NotRequired["WorkflowPreviewScopeType"],
    },
)
"""The scope of the workflow."""

type WorkflowPreviewScopeType = Literal['PROJECT', 'GLOBAL']
"""The scope of the workflow. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."""

WorkflowPreviewStatus = TypedDict(
    'WorkflowPreviewStatus',
    {
    'approval_configuration': NotRequired["ApprovalConfigurationPreview"],
    'deprecated': NotRequired["bool"],
    'layout': NotRequired["WorkflowPreviewLayout"],
    'status_reference': NotRequired["str"],
    },
)
"""Details about a workflow status in preview context."""

WorkflowProjectIdScope = TypedDict(
    'WorkflowProjectIdScope',
    {
    'id': NotRequired["str"],
    },
)
"""Project ID details."""

WorkflowProjectIssueTypeUsage = TypedDict(
    'WorkflowProjectIssueTypeUsage',
    {
    'id': NotRequired["str"],
    },
)
"""The issue type."""

WorkflowProjectIssueTypeUsageDto = TypedDict(
    'WorkflowProjectIssueTypeUsageDto',
    {
    'issue_types': NotRequired["WorkflowProjectIssueTypeUsagePage"],
    'project_id': NotRequired["str"],
    'workflow_id': NotRequired["str"],
    },
)
"""Issue types associated with the workflow for a project."""

WorkflowProjectIssueTypeUsagePage = TypedDict(
    'WorkflowProjectIssueTypeUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[WorkflowProjectIssueTypeUsage]"],
    },
)
"""A page of issue types."""

WorkflowProjectUsageDto = TypedDict(
    'WorkflowProjectUsageDto',
    {
    'projects': NotRequired["ProjectUsagePage"],
    'workflow_id': NotRequired["str"],
    },
)
"""Projects using the workflow."""

WorkflowReadRequest = TypedDict(
    'WorkflowReadRequest',
    {
    'project_and_issue_types': NotRequired["list[ProjectAndIssueTypePair]"],
    'workflow_ids': NotRequired["list[str]"],
    'workflow_names': NotRequired["list[str]"],
    },
)

WorkflowReadResponse = TypedDict(
    'WorkflowReadResponse',
    {
    'statuses': NotRequired["list[JiraWorkflowStatus]"],
    'workflows': NotRequired["list[JiraWorkflow]"],
    },
)
"""Details of workflows and related statuses."""

WorkflowReferenceStatus = TypedDict(
    'WorkflowReferenceStatus',
    {
    'approval_configuration': NotRequired["ApprovalConfiguration | None"],
    'deprecated': NotRequired["bool"],
    'layout': NotRequired["WorkflowStatusLayout | None"],
    'properties': NotRequired["dict[str, str]"],
    'status_reference': NotRequired["str"],
    },
)
"""The statuses referenced in the workflow."""

WorkflowRuleConfiguration = TypedDict(
    'WorkflowRuleConfiguration',
    {
    'id': NotRequired["str | None"],
    'parameters': NotRequired["dict[str, str]"],
    'rule_key': "str",
    },
)
"""The configuration of the rule."""

WorkflowRules = TypedDict(
    'WorkflowRules',
    {
    'conditions_tree': NotRequired["WorkflowCondition"],
    'post_functions': NotRequired["list[WorkflowTransitionRule]"],
    'validators': NotRequired["list[WorkflowTransitionRule]"],
    },
)
"""A collection of transition rules."""

WorkflowRulesSearch = TypedDict(
    'WorkflowRulesSearch',
    {
    'expand': NotRequired["str"],
    'rule_ids': "list[str]",
    'workflow_entity_id': "str",
    },
)
"""Details of the workflow and its transition rules."""

WorkflowRulesSearchDetails = TypedDict(
    'WorkflowRulesSearchDetails',
    {
    'invalid_rules': NotRequired["list[str]"],
    'valid_rules': NotRequired["list[WorkflowTransitionRules]"],
    'workflow_entity_id': NotRequired["str"],
    },
)
"""Details of workflow transition rules."""

WorkflowScheme = TypedDict(
    'WorkflowScheme',
    {
    'default_workflow': NotRequired["str"],
    'description': NotRequired["str"],
    'draft': NotRequired["bool"],
    'id': NotRequired["int"],
    'issue_type_mappings': NotRequired["dict[str, str]"],
    'issue_types': NotRequired["dict[str, IssueTypeDetails]"],
    'last_modified': NotRequired["str"],
    'last_modified_user': NotRequired["User"],
    'name': NotRequired["str"],
    'original_default_workflow': NotRequired["str"],
    'original_issue_type_mappings': NotRequired["dict[str, str]"],
    'self': NotRequired["str"],
    'update_draft_if_needed': NotRequired["bool"],
    },
)
"""Details about a workflow scheme."""

WorkflowSchemeAssociation = TypedDict(
    'WorkflowSchemeAssociation',
    {
    'issue_type_ids': "list[str]",
    'workflow_id': "str",
    },
)
"""The explicit association between issue types and a workflow in a workflow scheme."""

WorkflowSchemeAssociations = TypedDict(
    'WorkflowSchemeAssociations',
    {
    'project_ids': "list[str]",
    'workflow_scheme': "WorkflowScheme",
    },
)
"""A workflow scheme along with a list of projects that use it."""

WorkflowSchemeIdName = TypedDict(
    'WorkflowSchemeIdName',
    {
    'id': "str",
    'name': "str",
    },
)
"""The ID and the name of the workflow scheme."""

WorkflowSchemePayload = TypedDict(
    'WorkflowSchemePayload',
    {
    'default_workflow': NotRequired["ProjectCreateResourceIdentifier"],
    'description': NotRequired["str"],
    'explicit_mappings': NotRequired["dict[str, ProjectCreateResourceIdentifier]"],
    'name': NotRequired["str"],
    'on_conflict': NotRequired["WorkflowSchemePayloadOnConflict"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    },
)
"""The payload for creating a workflow scheme. See https://www.atlassian.com/software/jira/guides/workflows/overview\\#what-is-a-jira-workflow-scheme"""

type WorkflowSchemePayloadOnConflict = Literal['FAIL', 'USE', 'NEW']
"""The strategy to use if there is a conflict with another workflow scheme"""

WorkflowSchemeProjectAssociation = TypedDict(
    'WorkflowSchemeProjectAssociation',
    {
    'project_id': "str",
    'workflow_scheme_id': NotRequired["str"],
    },
)
"""An associated workflow scheme and project."""

WorkflowSchemeProjectSwitchBean = TypedDict(
    'WorkflowSchemeProjectSwitchBean',
    {
    'mappings_by_issue_type_override': NotRequired["list[MappingsByIssueTypeOverride]"],
    'project_id': NotRequired["str"],
    'target_scheme_id': NotRequired["str"],
    },
)
"""Request to switch a project's workflow scheme"""

WorkflowSchemeProjectUsageDto = TypedDict(
    'WorkflowSchemeProjectUsageDto',
    {
    'projects': NotRequired["ProjectUsagePage"],
    'workflow_scheme_id': NotRequired["str"],
    },
)
"""Projects using the workflow scheme."""

WorkflowSchemeReadRequest = TypedDict(
    'WorkflowSchemeReadRequest',
    {
    'project_ids': NotRequired["list[str | None] | None"],
    'workflow_scheme_ids': NotRequired["list[str | None] | None"],
    },
)
"""The workflow scheme read request body."""

WorkflowSchemeReadResponse = TypedDict(
    'WorkflowSchemeReadResponse',
    {
    'default_workflow': NotRequired["WorkflowMetadataRestModel"],
    'description': NotRequired["str | None"],
    'id': "str",
    'name': "str",
    'scope': "WorkflowScope",
    'task_id': NotRequired["str | None"],
    'version': "DocumentVersion",
    'workflows_for_issue_types': "list[WorkflowMetadataAndIssueTypeRestModel]",
    },
)

WorkflowSchemeUpdateRequest = TypedDict(
    'WorkflowSchemeUpdateRequest',
    {
    'default_workflow_id': NotRequired["str"],
    'description': "str",
    'id': "str",
    'name': "str",
    'status_mappings_by_issue_type_override': NotRequired["list[MappingsByIssueTypeOverride]"],
    'status_mappings_by_workflows': NotRequired["list[MappingsByWorkflow]"],
    'version': "DocumentVersion",
    'workflows_for_issue_types': NotRequired["list[WorkflowSchemeAssociation]"],
    },
)
"""The update workflow scheme payload."""

WorkflowSchemeUpdateRequiredMappingsRequest = TypedDict(
    'WorkflowSchemeUpdateRequiredMappingsRequest',
    {
    'default_workflow_id': NotRequired["str | None"],
    'id': "str",
    'workflows_for_issue_types': "list[WorkflowSchemeAssociation]",
    },
)
"""The request payload to get the required mappings for updating a workflow scheme."""

WorkflowSchemeUpdateRequiredMappingsResponse = TypedDict(
    'WorkflowSchemeUpdateRequiredMappingsResponse',
    {
    'status_mappings_by_issue_types': NotRequired["list[RequiredMappingByIssueType]"],
    'status_mappings_by_workflows': NotRequired["list[RequiredMappingByWorkflows]"],
    'statuses': NotRequired["list[StatusMetadata]"],
    'statuses_per_workflow': NotRequired["list[StatusesPerWorkflow]"],
    },
)

WorkflowSchemeUsage = TypedDict(
    'WorkflowSchemeUsage',
    {
    'id': NotRequired["str"],
    },
)
"""The worflow scheme."""

WorkflowSchemeUsageDto = TypedDict(
    'WorkflowSchemeUsageDto',
    {
    'workflow_id': NotRequired["str"],
    'workflow_schemes': NotRequired["WorkflowSchemeUsagePage"],
    },
)
"""Workflow schemes using the workflow."""

WorkflowSchemeUsagePage = TypedDict(
    'WorkflowSchemeUsagePage',
    {
    'next_page_token': NotRequired["str"],
    'values': NotRequired["list[WorkflowSchemeUsage]"],
    },
)
"""A page of workflow schemes."""

WorkflowScope = TypedDict(
    'WorkflowScope',
    {
    'project': NotRequired["ProjectId | None"],
    'type': NotRequired["WorkflowScopeType"],
    },
)
"""The scope of the workflow."""

type WorkflowScopeType = Literal['PROJECT', 'GLOBAL']
"""The scope of the workflow. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."""

WorkflowSearchResponse = TypedDict(
    'WorkflowSearchResponse',
    {
    'is_last': NotRequired["bool"],
    'max_results': NotRequired["int"],
    'next_page': NotRequired["str"],
    'self': NotRequired["str"],
    'start_at': NotRequired["int"],
    'statuses': NotRequired["list[JiraWorkflowStatus]"],
    'total': NotRequired["int"],
    'values': NotRequired["list[JiraWorkflow]"],
    },
)
"""Page of items, including workflows and related statuses."""

WorkflowSimpleCondition = TypedDict(
    'WorkflowSimpleCondition',
    {
    'configuration': NotRequired["dict[str, Any]"],
    'node_type': "str",
    'type': "str",
    },
)
"""A workflow transition rule condition. This object returns `nodeType` as `simple`."""

WorkflowStatus = TypedDict(
    'WorkflowStatus',
    {
    'id': "str",
    'name': "str",
    'properties': NotRequired["dict[str, Any]"],
    },
)
"""Details of a workflow status."""

WorkflowStatusLayout = TypedDict(
    'WorkflowStatusLayout',
    {
    'x': NotRequired["float | None"],
    'y': NotRequired["float | None"],
    },
)
"""The x and y location of the status in the workflow."""

WorkflowStatusLayoutPayload = TypedDict(
    'WorkflowStatusLayoutPayload',
    {
    'x': NotRequired["float"],
    'y': NotRequired["float"],
    },
)
"""The layout of the workflow status."""

WorkflowStatusPayload = TypedDict(
    'WorkflowStatusPayload',
    {
    'layout': NotRequired["WorkflowStatusLayoutPayload"],
    'pcri': NotRequired["ProjectCreateResourceIdentifier"],
    'properties': NotRequired["dict[str, str]"],
    },
)
"""The statuses to be used in the workflow"""

WorkflowStatusUpdate = TypedDict(
    'WorkflowStatusUpdate',
    {
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'name': "str",
    'status_category': "WorkflowStatusUpdateStatusCategory",
    'status_reference': "str",
    },
)
"""Details of the status being updated."""

type WorkflowStatusUpdateStatusCategory = Literal['TODO', 'IN_PROGRESS', 'DONE']
"""The category of the status."""

WorkflowTransition = TypedDict(
    'WorkflowTransition',
    {
    'id': "int",
    'name': "str",
    },
)
"""A workflow transition."""

WorkflowTransitionLinks = TypedDict(
    'WorkflowTransitionLinks',
    {
    'from_port': NotRequired["int | None"],
    'from_status_reference': NotRequired["str | None"],
    'to_port': NotRequired["int | None"],
    },
)
"""The statuses the transition can start from, and the mapping of ports between the statuses."""

WorkflowTransitionRule = TypedDict(
    'WorkflowTransitionRule',
    {
    'configuration': NotRequired["Any"],
    'type': "str",
    },
)
"""A workflow transition rule."""

WorkflowTransitionRules = TypedDict(
    'WorkflowTransitionRules',
    {
    'conditions': NotRequired["list[AppWorkflowTransitionRule]"],
    'post_functions': NotRequired["list[AppWorkflowTransitionRule]"],
    'validators': NotRequired["list[AppWorkflowTransitionRule]"],
    'workflow_id': "WorkflowId",
    },
)
"""A workflow with transition rules."""

WorkflowTransitionRulesDetails = TypedDict(
    'WorkflowTransitionRulesDetails',
    {
    'workflow_id': "WorkflowId",
    'workflow_rule_ids': "list[str]",
    },
)
"""Details about a workflow configuration update request."""

WorkflowTransitionRulesUpdate = TypedDict(
    'WorkflowTransitionRulesUpdate',
    {
    'workflows': "list[WorkflowTransitionRules]",
    },
)
"""Details about a workflow configuration update request."""

WorkflowTransitionRulesUpdateErrorDetails = TypedDict(
    'WorkflowTransitionRulesUpdateErrorDetails',
    {
    'rule_update_errors': "dict[str, list[str]]",
    'update_errors': "list[str]",
    'workflow_id': "WorkflowId",
    },
)
"""Details of any errors encountered while updating workflow transition rules for a workflow."""

WorkflowTransitionRulesUpdateErrors = TypedDict(
    'WorkflowTransitionRulesUpdateErrors',
    {
    'update_results': "list[WorkflowTransitionRulesUpdateErrorDetails]",
    },
)
"""Details of any errors encountered while updating workflow transition rules."""

WorkflowTransitions = TypedDict(
    'WorkflowTransitions',
    {
    'actions': NotRequired["list[WorkflowRuleConfiguration | None]"],
    'conditions': NotRequired["ConditionGroupConfiguration | None"],
    'custom_issue_event_id': NotRequired["str | None"],
    'description': NotRequired["str"],
    'id': NotRequired["str"],
    'links': NotRequired["list[WorkflowTransitionLinks | None]"],
    'name': NotRequired["str"],
    'properties': NotRequired["dict[str, str]"],
    'to_status_reference': NotRequired["str"],
    'transition_screen': NotRequired["WorkflowRuleConfiguration | None"],
    'triggers': NotRequired["list[WorkflowTrigger]"],
    'type': NotRequired["WorkflowTransitionsType"],
    'validators': NotRequired["list[WorkflowRuleConfiguration | None]"],
    },
)
"""The transitions of the workflow."""

type WorkflowTransitionsType = Literal['INITIAL', 'GLOBAL', 'DIRECTED']
"""The transition type."""

WorkflowTrigger = TypedDict(
    'WorkflowTrigger',
    {
    'id': NotRequired["str"],
    'parameters': "dict[str, str]",
    'rule_key': "str",
    },
)
"""The trigger configuration associated with a workflow."""

WorkflowUpdate = TypedDict(
    'WorkflowUpdate',
    {
    'default_status_mappings': NotRequired["list[StatusMigration]"],
    'description': NotRequired["str"],
    'id': "str",
    'looped_transition_container_layout': NotRequired["WorkflowLayout | None"],
    'start_point_layout': NotRequired["WorkflowLayout | None"],
    'status_mappings': NotRequired["list[StatusMappingDto]"],
    'statuses': "list[StatusLayoutUpdate]",
    'transitions': "list[TransitionUpdateDto]",
    'version': "DocumentVersion",
    },
)
"""The details of the workflows to update."""

WorkflowUpdateRequest = TypedDict(
    'WorkflowUpdateRequest',
    {
    'statuses': NotRequired["list[WorkflowStatusUpdate]"],
    'workflows': NotRequired["list[WorkflowUpdate]"],
    },
)
"""The update workflows payload."""

WorkflowUpdateResponse = TypedDict(
    'WorkflowUpdateResponse',
    {
    'statuses': NotRequired["list[JiraWorkflowStatus]"],
    'task_id': NotRequired["str | None"],
    'workflows': NotRequired["list[JiraWorkflow]"],
    },
)

WorkflowUpdateValidateRequestBean = TypedDict(
    'WorkflowUpdateValidateRequestBean',
    {
    'payload': "WorkflowUpdateRequest",
    'validation_options': NotRequired["ValidationOptionsForUpdate"],
    },
)

WorkflowValidationError = TypedDict(
    'WorkflowValidationError',
    {
    'additional_details': NotRequired["str"],
    'code': NotRequired["str"],
    'element_reference': NotRequired["WorkflowElementReference"],
    'level': NotRequired["WorkflowValidationErrorLevel"],
    'message': NotRequired["str"],
    'type': NotRequired["WorkflowValidationErrorType"],
    },
)
"""The details about a workflow validation error."""

type WorkflowValidationErrorLevel = Literal['WARNING', 'ERROR']
"""The validation error level."""

WorkflowValidationErrorList = TypedDict(
    'WorkflowValidationErrorList',
    {
    'errors': NotRequired["list[WorkflowValidationError]"],
    },
)

type WorkflowValidationErrorType = Literal['RULE', 'STATUS', 'STATUS_LAYOUT', 'STATUS_PROPERTY', 'WORKFLOW', 'TRANSITION', 'TRANSITION_PROPERTY', 'SCOPE', 'STATUS_MAPPING', 'TRIGGER']
"""The type of element the error or warning references."""

WorkflowsWithTransitionRulesDetails = TypedDict(
    'WorkflowsWithTransitionRulesDetails',
    {
    'workflows': "list[WorkflowTransitionRulesDetails]",
    },
)
"""Details of workflows and their transition rules to delete."""

WorkingDaysConfig = TypedDict(
    'WorkingDaysConfig',
    {
    'friday': NotRequired["bool"],
    'id': NotRequired["int"],
    'monday': NotRequired["bool"],
    'non_working_days': NotRequired["list[NonWorkingDay]"],
    'saturday': NotRequired["bool"],
    'sunday': NotRequired["bool"],
    'thursday': NotRequired["bool"],
    'timezone_id': NotRequired["str"],
    'tuesday': NotRequired["bool"],
    'wednesday': NotRequired["bool"],
    },
)
"""Working days configuration"""

Worklog = TypedDict(
    'Worklog',
    {
    'author': NotRequired["UserDetails"],
    'comment': NotRequired["Any"],
    'created': NotRequired["str"],
    'id': NotRequired["str"],
    'issue_id': NotRequired["str"],
    'properties': NotRequired["list[EntityProperty]"],
    'self': NotRequired["str"],
    'started': NotRequired["str"],
    'time_spent': NotRequired["str"],
    'time_spent_seconds': NotRequired["int"],
    'update_author': NotRequired["UserDetails"],
    'updated': NotRequired["str"],
    'visibility': NotRequired["Visibility"],
    },
)
"""Details of a worklog."""

WorklogCompositeKey = TypedDict(
    'WorklogCompositeKey',
    {
    'issue_id': NotRequired["int"],
    'worklog_id': NotRequired["int"],
    },
)

WorklogIdsRequestBean = TypedDict(
    'WorklogIdsRequestBean',
    {
    'ids': "list[int]",
    },
)

WorklogKeyResult = TypedDict(
    'WorklogKeyResult',
    {
    'issue_id': NotRequired["int"],
    'worklog_id': NotRequired["int"],
    },
)

WorklogsMoveRequestBean = TypedDict(
    'WorklogsMoveRequestBean',
    {
    'ids': NotRequired["list[int]"],
    'issue_id_or_key': NotRequired["str"],
    },
)

WorkspaceDataPolicy = TypedDict(
    'WorkspaceDataPolicy',
    {
    'any_content_blocked': NotRequired["bool"],
    },
)
"""Details about data policy."""
