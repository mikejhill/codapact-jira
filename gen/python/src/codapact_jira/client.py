"""Client generated from the library surface. Do not edit."""

# ruff: noqa: E501
from __future__ import annotations

import builtins  # noqa: F401
from collections.abc import Iterator, Mapping, Sequence
from functools import cache
from importlib.resources import files
from os import PathLike  # noqa: F401
from typing import Any, Literal, cast  # noqa: F401

from codapact.runtime import (
    AuthProvider,
    Middleware,
    RuntimeClient,
    Transport,
    load_model,
)
from codapact.runtime.arguments import UNSET, Unset, call_args

from codapact.runtime.arguments import fields as _fields  # noqa: F401

from . import types as _t


PROTOCOLS: dict[str, Any] = {}
"""Custom protocol handlers (``module:attribute``) this client registers by default."""


@cache
def _model() -> Any:
    return load_model(files(__package__).joinpath("_model.json"))


class _AgentsResource:
    """Operations under ``agents``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def start_batch(self, *, client_mutation_id: str, invocations: builtins.list[_t.BulkAgentSessionInvocation]) -> _t.BulkAgentSessionsResponse:
        """
        Bulk start agent sessions (batch)

        Starts agent sessions for a batch of issues, with an agent and optional prompt specified per invocation. You can submit between 1 and 50 invocations in one request, including multiple invocations for the same issue. Supply numeric issue-ID strings and Rovo agent IDs. Session-start outcomes are returned inline; the agent's work continues asynchronously.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.BulkAgentSessionsResponse', self._runtime.call('start_batch', call_args({}, {'body': {'client_mutation_id': client_mutation_id, 'invocations': invocations}}, required=frozenset({'body'}))))

    def start_uniform(self, *, agent_id: str, client_mutation_id: str, issue_ids: builtins.list[str], user_prompt: str | None | Unset = UNSET) -> _t.BulkAgentSessionsResponse:
        """
        Bulk start agent sessions (uniform)

        Starts the same agent on between 1 and 50 issues, with an optional prompt shared by every invocation. Supply numeric issue-ID strings, and a Rovo agent ID. Session-start outcomes are returned inline; the agent's work continues asynchronously.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.BulkAgentSessionsResponse', self._runtime.call('start_uniform', call_args({}, {'body': {'agent_id': agent_id, 'client_mutation_id': client_mutation_id, 'issue_ids': issue_ids, 'user_prompt': user_prompt}}, required=frozenset({'body'}))))

class _AnnouncementBannerResource:
    """Operations under ``announcement_banner``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_banner(self) -> _t.AnnouncementBannerConfiguration:
        """
        Get announcement banner configuration

        Returns the current announcement banner configuration.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.AnnouncementBannerConfiguration', self._runtime.call('get_banner', call_args({})))

    def set_banner(self, *, is_dismissible: bool | Unset = UNSET, is_enabled: bool | Unset = UNSET, message: str | Unset = UNSET, visibility: str | Unset = UNSET) -> Any:
        """
        Update announcement banner configuration

        Updates the announcement banner configuration.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('set_banner', call_args({}, {'body': {'is_dismissible': is_dismissible, 'is_enabled': is_enabled, 'message': message, 'visibility': visibility}})))

class _AppDataPoliciesResource:
    """Operations under ``app_data_policies``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_policy(self) -> _t.WorkspaceDataPolicy:
        """
        Get data policy for the workspace

        Returns data policy for the workspace.
        """
        return cast('_t.WorkspaceDataPolicy', self._runtime.call('get_policy', call_args({})))

    def list_policies(self, *, ids: str | Unset = UNSET) -> _t.ProjectDataPolicies:
        """
        Get data policy for projects

        Returns data policies for the projects specified in the request.
        """
        return cast('_t.ProjectDataPolicies', self._runtime.call('get_policies', call_args({'ids': ids})))

class _AppMigrationResource:
    """Operations under ``app_migration``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def app_issue_field_value_update_resource_update_issue_fields_put(self, *, atlassian_transfer_id: str, update_value_list: builtins.list[_t.ConnectCustomFieldValue] | Unset = UNSET) -> Any:
        """
        Bulk update custom field value

        Updates the value of a custom field added by Connect apps on one or more issues.
        The values of up to 200 custom fields can be updated.

        **[Permissions](#permissions) required:** Only Connect apps can make this request
        """
        return cast('Any', self._runtime.call('app_issue_field_value_update_resource_update_issue_fields_put', call_args({'atlassian_transfer_id': atlassian_transfer_id}, {'body': {'update_value_list': update_value_list}})))

    def migration_resource_update_entity_properties_value_put(self, *, atlassian_transfer_id: str, entity_type: _t.MigrationResourceUpdateEntityPropertiesValuePutEntityType, body: builtins.list[_t.EntityPropertyDetails]) -> None:
        """
        Bulk update entity properties

        Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.
        """
        self._runtime.call('migration_resource_update_entity_properties_value_put', call_args({'atlassian_transfer_id': atlassian_transfer_id, 'entity_type': entity_type, 'body': body}))

    def migration_resource_workflow_rule_search_post(self, *, atlassian_transfer_id: str, rule_ids: builtins.list[str], workflow_entity_id: str, expand: str | Unset = UNSET) -> _t.WorkflowRulesSearchDetails:
        """
        Get workflow transition rule configurations

        Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.
        """
        return cast('_t.WorkflowRulesSearchDetails', self._runtime.call('migration_resource_workflow_rule_search_post', call_args({'atlassian_transfer_id': atlassian_transfer_id}, {'body': {'expand': expand, 'rule_ids': rule_ids, 'workflow_entity_id': workflow_entity_id}}, required=frozenset({'body'}))))

class _AppPropertiesResource:
    """Operations under ``app_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def addon_properties_resource_get_addon_properties_get(self, *, addon_key: str) -> _t.PropertyKeys:
        """
        Get app properties

        Gets all the properties of an app. The reserved key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8` is not returned.

        **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
        Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
        """
        return cast('_t.PropertyKeys', self._runtime.call('addon_properties_resource_get_addon_properties_get', call_args({'addon_key': addon_key})))

    def addon_properties_resource_get_addon_property_get(self, *, addon_key: str, property_key: str) -> _t.EntityProperty:
        """
        Get app property

        Returns the key and value of an app's property. The property key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8`
        is reserved. It returns a synthetic, read-only property containing the Connect `clientKey` for the requested tenant.
        This is intended for Forge apps with `app.connect.key` to retrieve the Connect client key during migration.

        **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
        Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
        """
        return cast('_t.EntityProperty', self._runtime.call('addon_properties_resource_get_addon_property_get', call_args({'addon_key': addon_key, 'property_key': property_key})))

    def addon_properties_resource_put_addon_property_put(self, *, addon_key: str, property_key: str, body: Any) -> _t.OperationMessage:
        """
        Set app property

        Sets the value of an app's property. Use this resource to store custom data for your app.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
        Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
        """
        return cast('_t.OperationMessage', self._runtime.call('addon_properties_resource_put_addon_property_put', call_args({'addon_key': addon_key, 'property_key': property_key, 'body': body})))

    def addon_properties_resource_delete_addon_property_delete(self, *, addon_key: str, property_key: str) -> None:
        """
        Delete app property

        Deletes an app's property.

        **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
        Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
        """
        self._runtime.call('addon_properties_resource_delete_addon_property_delete', call_args({'addon_key': addon_key, 'property_key': property_key}))

    def list_forge_keys(self) -> _t.GetForgeAppPropertyKeysResponse:
        """
        Get app property keys (Forge)

        Returns all property keys for the Forge app.

        **[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.
        """
        return cast('_t.GetForgeAppPropertyKeysResponse', self._runtime.call('get_forge_app_property_keys', call_args({})))

    def get(self, *, property_key: str) -> _t.GetForgeAppPropertyResponse:
        """
        Get app property (Forge)

        Returns the value of a Forge app's property.

        **[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.
        """
        return cast('_t.GetForgeAppPropertyResponse', self._runtime.call('get_forge_app_property', call_args({'property_key': property_key})))

    def put(self, *, property_key: str, body: Any) -> _t.OperationMessage:
        """
        Set app property (Forge)

        Sets the value of a Forge app's property.
        These values can be retrieved in [Jira expressions](/cloud/jira/platform/jira-expressions/)
        through the `app` [context variable](/cloud/jira/platform/jira-expressions/#context-variables).
        They are also available in [entity property display conditions](/platform/forge/manifest-reference/display-conditions/entity-property-conditions/).

        For other use cases, use the [Storage API](/platform/forge/runtime-reference/storage-api/).

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        **[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.OperationMessage', self._runtime.call('put_forge_app_property', call_args({'property_key': property_key, 'body': body})))

    def delete(self, *, property_key: str) -> None:
        """
        Delete app property (Forge)

        Deletes a Forge app's property.

        **[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        self._runtime.call('delete_forge_app_property', call_args({'property_key': property_key}))

class _ApplicationRolesResource:
    """Operations under ``application_roles``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self) -> builtins.list[_t.ApplicationRole]:
        """
        Get all application roles

        Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ApplicationRole]', self._runtime.call('get_all_application_roles', call_args({})))

    def get(self, *, key: str) -> _t.ApplicationRole:
        """
        Get application role

        Returns an application role.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ApplicationRole', self._runtime.call('get_application_role', call_args({'key': key})))

class _AuditRecordsResource:
    """Operations under ``audit_records``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, offset: int | Unset = UNSET, limit: int | Unset = UNSET, filter: str | Unset = UNSET, from_: str | Unset = UNSET, to: str | Unset = UNSET) -> _t.AuditRecords:
        """
        Get audit records

        Returns a list of audit records. The list can be filtered to include items:

         *  where each item in `filter` has at least one match in any of these fields:
            
             *  `summary`
             *  `category`
             *  `eventSource`
             *  `objectItem.name` If the object is a user, account ID is available to filter.
             *  `objectItem.parentName`
             *  `objectItem.typeName`
             *  `changedValues.changedFrom`
             *  `changedValues.changedTo`
             *  `remoteAddress`
            
            For example, if `filter` contains *man ed*, an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned.
         *  created on or after a date and time.
         *  created or or before a date and time.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.AuditRecords', self._runtime.call('get_audit_records', call_args({'offset': offset, 'limit': limit, 'filter': filter, 'from': from_, 'to': to})))

class _AvatarsResource:
    """Operations under ``avatars``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_all_system(self, *, type_: _t.GetAllSystemAvatarsType) -> _t.SystemAvatars:
        """
        Get system avatars by type

        Returns a list of system avatar details by owner type, where the owner types are issue type, project, user or priority.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.SystemAvatars', self._runtime.call('get_all_system_avatars', call_args({'type': type_})))

    def list(self, *, type_: _t.GetAvatarsType, entity_id: str) -> _t.Avatars:
        """
        Get avatars

        Returns the system and custom avatars for a project, issue type or priority.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
         *  for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
         *  for system avatars, none.
         *  for priority avatars, none.
        """
        return cast('_t.Avatars', self._runtime.call('get_avatars', call_args({'type': type_, 'entity_id': entity_id})))

    def store(self, *, type_: _t.StoreAvatarType, entity_id: str, size: int, body: str | bytes | PathLike[str], x: int | Unset = UNSET, y: int | Unset = UNSET) -> _t.Avatar:
        """
        Load avatar

        Loads a custom avatar for a project, issue type or priority.

        Specify the avatar's local file location in the body of the request. Also, include the following headers:

         *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
         *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

        For example:  
        `curl --request POST `

        `--user email@example.com:<api_token> `

        `--header 'X-Atlassian-Token: no-check' `

        `--header 'Content-Type: image/< image_type>' `

        `--data-binary "<@/path/to/file/with/your/avatar>" `

        `--url 'https://your-domain.atlassian.net/rest/api/3/universal_avatar/type/{type}/owner/{entityId}'`

        The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

        The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

        After creating the avatar use:

         *  [Update issue type](#api-rest-api-3-issuetype-id-put) to set it as the issue type's displayed avatar.
         *  [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project's displayed avatar.
         *  [Update priority](#api-rest-api-3-priority-id-put) to set it as the priority's displayed avatar.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.Avatar', self._runtime.call('store_avatar', call_args({'type': type_, 'entity_id': entity_id, 'x': x, 'y': y, 'size': size, 'body': body})))

    def delete(self, *, type_: _t.DeleteAvatarType, owning_object_id: str, id: int) -> None:
        """
        Delete avatar

        Deletes an avatar from a project, issue type or priority.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_avatar', call_args({'type': type_, 'owning_object_id': owning_object_id, 'id': id}))

    def get_image_by_type(self, *, type_: _t.GetAvatarImageByTypeType, size: _t.GetAvatarImageByTypeSize | Unset = UNSET, format: _t.GetAvatarImageByTypeFormat | Unset = UNSET) -> _t.StreamingResponseBody:
        """
        Get avatar image by type

        Returns the default project, issue type or priority avatar image.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.StreamingResponseBody', self._runtime.call('get_avatar_image_by_type', call_args({'type': type_, 'size': size, 'format': format})))

    def get_image(self, *, type_: _t.GetAvatarImageByIdType, id: int, size: _t.GetAvatarImageByIdSize | Unset = UNSET, format: _t.GetAvatarImageByIdFormat | Unset = UNSET) -> _t.StreamingResponseBody:
        """
        Get avatar image by ID

        Returns a project, issue type or priority avatar image by ID.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  For system avatars, none.
         *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
         *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
         *  For priority avatars, none.
        """
        return cast('_t.StreamingResponseBody', self._runtime.call('get_avatar_image_by_id', call_args({'type': type_, 'id': id, 'size': size, 'format': format})))

    def get_image_by_owner(self, *, type_: _t.GetAvatarImageByOwnerType, entity_id: str, size: _t.GetAvatarImageByOwnerSize | Unset = UNSET, format: _t.GetAvatarImageByOwnerFormat | Unset = UNSET) -> _t.StreamingResponseBody:
        """
        Get avatar image by owner

        Returns the avatar image for a project, issue type or priority.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  For system avatars, none.
         *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
         *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
         *  For priority avatars, none.
        """
        return cast('_t.StreamingResponseBody', self._runtime.call('get_avatar_image_by_owner', call_args({'type': type_, 'entity_id': entity_id, 'size': size, 'format': format})))

class _ClassificationLevelsResource:
    """Operations under ``classification_levels``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, status: builtins.list[_t.GetAllUserDataClassificationLevelsStatusItem] | Unset = UNSET, order_by: _t.GetAllUserDataClassificationLevelsOrderBy | Unset = UNSET) -> _t.DataClassificationLevelsBean:
        """
        Get all classification levels

        Returns all classification levels.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.DataClassificationLevelsBean', self._runtime.call('get_all_user_data_classification_levels', call_args({'status': status, 'order_by': order_by})))

class _DashboardsResource:
    """Operations under ``dashboards``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, filter: _t.GetAllDashboardsFilter | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageOfDashboards:
        """
        Get all dashboards

        Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.PageOfDashboards', self._runtime.call('get_all_dashboards', call_args({'filter': filter, 'start_at': start_at, 'max_results': max_results})))

    def create(self, *, edit_permissions: builtins.list[_t.SharePermission], name: str, share_permissions: builtins.list[_t.SharePermission], extend_admin_permissions: bool | Unset = UNSET, description: str | Unset = UNSET) -> _t.Dashboard:
        """
        Create dashboard

        Creates a dashboard.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.Dashboard', self._runtime.call('create_dashboard', call_args({'extend_admin_permissions': extend_admin_permissions}, {'body': {'description': description, 'edit_permissions': edit_permissions, 'name': name, 'share_permissions': share_permissions}}, required=frozenset({'body'}))))

    def bulk(self, *, action: _t.BulkEditShareableEntityRequestAction, entity_ids: builtins.list[int], change_owner_details: _t.BulkChangeOwnerDetails | Unset = UNSET, extend_admin_permissions: bool | Unset = UNSET, permission_details: _t.PermissionDetails | Unset = UNSET) -> _t.BulkEditShareableEntityResponse:
        """
        Bulk edit dashboards

        Bulk edit dashboards. Maximum number of dashboards to be edited at the same time is 100.

        **[Permissions](#permissions) required:** None

        The dashboards to be updated must be owned by the user, or the user must be an administrator.
        """
        return cast('_t.BulkEditShareableEntityResponse', self._runtime.call('bulk_edit_dashboards', call_args({}, {'body': {'action': action, 'change_owner_details': change_owner_details, 'entity_ids': entity_ids, 'extend_admin_permissions': extend_admin_permissions, 'permission_details': permission_details}}, required=frozenset({'body'}))))

    def list_all_available_gadgets(self) -> _t.AvailableDashboardGadgetsResponse:
        """
        Get available gadgets

        Gets a list of all available gadgets that can be added to all dashboards.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.AvailableDashboardGadgetsResponse', self._runtime.call('get_all_available_dashboard_gadgets', call_args({})))

    def get_paginated(self, *, dashboard_name: str | Unset = UNSET, account_id: str | Unset = UNSET, owner: str | Unset = UNSET, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, project_id: int | Unset = UNSET, order_by: _t.GetDashboardsPaginatedOrderBy | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, status: _t.GetDashboardsPaginatedStatus | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanDashboard:
        """
        Search for dashboards

        Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned:

         *  Dashboards owned by the user. Not returned for anonymous users.
         *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
         *  Dashboards shared with a private project that the user can browse. Not returned for anonymous users.
         *  Dashboards shared with a public project.
         *  Dashboards shared with the public.
        """
        return cast('_t.PageBeanDashboard', self._runtime.call('get_dashboards_paginated', call_args({'dashboard_name': dashboard_name, 'account_id': account_id, 'owner': owner, 'groupname': groupname, 'group_id': group_id, 'project_id': project_id, 'order_by': order_by, 'start_at': start_at, 'max_results': max_results, 'status': status, 'expand': expand})))

    def list_all_gadgets(self, *, dashboard_id: int, module_key: builtins.list[str] | Unset = UNSET, uri: builtins.list[str] | Unset = UNSET, gadget_id: builtins.list[int] | Unset = UNSET) -> _t.DashboardGadgetResponse:
        """
        Get gadgets

        Returns a list of dashboard gadgets on a dashboard.

        This operation returns:

         *  Gadgets from a list of IDs, when `id` is set.
         *  Gadgets with a module key, when `moduleKey` is set.
         *  Gadgets from a list of URIs, when `uri` is set.
         *  All gadgets, when no other parameters are set.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.DashboardGadgetResponse', self._runtime.call('get_all_gadgets', call_args({'dashboard_id': dashboard_id, 'module_key': module_key, 'uri': uri, 'gadget_id': gadget_id})))

    def add_gadget(self, *, dashboard_id: int, color: str | Unset = UNSET, ignore_uri_and_module_key_validation: bool | Unset = UNSET, module_key: str | Unset = UNSET, position: _t.DashboardGadgetPosition | Unset = UNSET, title: str | Unset = UNSET, uri: str | Unset = UNSET) -> _t.DashboardGadget:
        """
        Add gadget to dashboard

        Adds a gadget to a dashboard.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.DashboardGadget', self._runtime.call('add_gadget', call_args({'dashboard_id': dashboard_id}, {'body': {'color': color, 'ignore_uri_and_module_key_validation': ignore_uri_and_module_key_validation, 'module_key': module_key, 'position': position, 'title': title, 'uri': uri}})))

    def update_gadget(self, *, dashboard_id: int, gadget_id: int, color: str | Unset = UNSET, position: _t.DashboardGadgetPosition | Unset = UNSET, title: str | Unset = UNSET) -> Any:
        """
        Update gadget on dashboard

        Changes the title, position, and color of the gadget on a dashboard.

        **[Permissions](#permissions) required:** None.
        """
        return cast('Any', self._runtime.call('update_gadget', call_args({'dashboard_id': dashboard_id, 'gadget_id': gadget_id}, {'body': {'color': color, 'position': position, 'title': title}})))

    def remove_gadget(self, *, dashboard_id: int, gadget_id: int) -> Any:
        """
        Remove gadget from dashboard

        Removes a dashboard gadget from a dashboard.

        When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position.

        **[Permissions](#permissions) required:** None.
        """
        return cast('Any', self._runtime.call('remove_gadget', call_args({'dashboard_id': dashboard_id, 'gadget_id': gadget_id})))

    def list_item_property_keys(self, *, dashboard_id: str, item_id: str) -> _t.PropertyKeys:
        """
        Get dashboard item property keys

        Returns the keys of all properties for a dashboard item.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_dashboard_item_property_keys', call_args({'dashboard_id': dashboard_id, 'item_id': item_id})))

    def get_item_property(self, *, dashboard_id: str, item_id: str, property_key: str) -> _t.EntityProperty:
        """
        Get dashboard item property

        Returns the key and value of a dashboard item property.

        A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).

        When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

        There is no resource to set or get dashboard items.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_dashboard_item_property', call_args({'dashboard_id': dashboard_id, 'item_id': item_id, 'property_key': property_key})))

    def set_item_property(self, *, dashboard_id: str, item_id: str, property_key: str, body: Any) -> Any:
        """
        Set dashboard item property

        Sets the value of a dashboard item property. Use this resource in apps to store custom data against a dashboard item.

        A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).

        When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

        There is no resource to set or get dashboard items.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The user must have edit permisson of the dashboard.
        """
        return cast('Any', self._runtime.call('set_dashboard_item_property', call_args({'dashboard_id': dashboard_id, 'item_id': item_id, 'property_key': property_key, 'body': body})))

    def delete_item_property(self, *, dashboard_id: str, item_id: str, property_key: str) -> Any:
        """
        Delete dashboard item property

        Deletes a dashboard item property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The user must have edit permission of the dashboard.
        """
        return cast('Any', self._runtime.call('delete_dashboard_item_property', call_args({'dashboard_id': dashboard_id, 'item_id': item_id, 'property_key': property_key})))

    def get(self, *, id: str) -> _t.Dashboard:
        """
        Get dashboard

        Returns a dashboard.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.

        However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.
        """
        return cast('_t.Dashboard', self._runtime.call('get_dashboard', call_args({'id': id})))

    def update(self, *, id: str, edit_permissions: builtins.list[_t.SharePermission], name: str, share_permissions: builtins.list[_t.SharePermission], extend_admin_permissions: bool | Unset = UNSET, description: str | Unset = UNSET) -> _t.Dashboard:
        """
        Update dashboard

        Updates a dashboard, replacing all the dashboard details with those provided.

        **[Permissions](#permissions) required:** None

        The dashboard to be updated must be owned by the user.
        """
        return cast('_t.Dashboard', self._runtime.call('update_dashboard', call_args({'id': id, 'extend_admin_permissions': extend_admin_permissions}, {'body': {'description': description, 'edit_permissions': edit_permissions, 'name': name, 'share_permissions': share_permissions}}, required=frozenset({'body'}))))

    def delete(self, *, id: str) -> None:
        """
        Delete dashboard

        Deletes a dashboard.

        **[Permissions](#permissions) required:** None

        The dashboard to be deleted must be owned by the user.
        """
        self._runtime.call('delete_dashboard', call_args({'id': id}))

    def copy(self, *, id: str, edit_permissions: builtins.list[_t.SharePermission], name: str, share_permissions: builtins.list[_t.SharePermission], extend_admin_permissions: bool | Unset = UNSET, description: str | Unset = UNSET) -> _t.Dashboard:
        """
        Copy dashboard

        Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied dashboard.

        **[Permissions](#permissions) required:** None

        The dashboard to be copied must be owned by or shared with the user.
        """
        return cast('_t.Dashboard', self._runtime.call('copy_dashboard', call_args({'id': id, 'extend_admin_permissions': extend_admin_permissions}, {'body': {'description': description, 'edit_permissions': edit_permissions, 'name': name, 'share_permissions': share_permissions}}, required=frozenset({'body'}))))

class _DynamicModulesResource:
    """Operations under ``dynamic_modules``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def resource_get_modules_get(self) -> _t.ConnectModules:
        """
        Get modules

        Returns all modules registered dynamically by the calling app.

        **[Permissions](#permissions) required:** Only Connect apps can make this request.
        """
        return cast('_t.ConnectModules', self._runtime.call('dynamic_modules_resource_get_modules_get', call_args({})))

    def resource_register_modules_post(self, *, modules: builtins.list[_t.ConnectModule]) -> None:
        """
        Register modules

        Registers a list of modules.

        **[Permissions](#permissions) required:** Only Connect apps can make this request.
        """
        self._runtime.call('dynamic_modules_resource_register_modules_post', call_args({}, {'body': {'modules': modules}}, required=frozenset({'body'})))

    def resource_remove_modules_delete(self, *, module_key: builtins.list[str] | Unset = UNSET) -> None:
        """
        Remove modules

        Remove all or a list of modules registered by the calling app.

        **[Permissions](#permissions) required:** Only Connect apps can make this request.
        """
        self._runtime.call('dynamic_modules_resource_remove_modules_delete', call_args({'module_key': module_key}))

class _FieldSchemesResource:
    """Operations under ``field_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_field_association_schemes(self, *, project_id: builtins.list[int] | Unset = UNSET, query: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBean2GetFieldAssociationSchemeResponse:
        """
        Get field schemes

        REST endpoint for retrieving a paginated list of field association schemes with optional filtering.

        This endpoint allows clients to fetch field association schemes with optional filtering by project IDs and text queries. The response includes scheme details with navigation links and filter metadata when applicable.

        Filtering Behavior:

         *  When projectId or query parameters are provided, the response includes matchedFilters metadata showing which filters were applied.
         *  When no filters are applied, matchedFilters is omitted from individual scheme objects

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBean2GetFieldAssociationSchemeResponse', self._runtime.call('get_field_association_schemes', call_args({'project_id': project_id, 'query': query, 'start_at': start_at, 'max_results': max_results})))

    def create_field_association_scheme(self, *, name: str, description: str | Unset = UNSET) -> _t.CreateFieldAssociationSchemeResponse:
        """
        Create field scheme

        Endpoint for creating a new field association scheme.

        A new scheme is **not** copied from, or based on, any existing field association scheme. Instead, it is initialised with a minimal default set of critical fields sourced from the instance's own *system* and *product* fields (the fields returned by the product's field API), rather than from a scheme you specify.

        To create a scheme that is based on an existing one, use the *Clone field scheme* endpoint instead.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.CreateFieldAssociationSchemeResponse', self._runtime.call('create_field_association_scheme', call_args({}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def update_fields_associated_with_schemes(self, *, body: builtins.dict[str, builtins.list[_t.UpdateFieldAssociationsRequestItem]]) -> _t.FieldSchemeToFieldsResponse:
        """
        Update fields associated with field schemes

        Update fields associated with field association schemes.

        **Request body limits:** a single request can update associations for at most **100 fields** (the top-level field ID keys of the request body), and each field association item may reference at most 50 field schemes. Exceeding a limit returns a 400 response with an error such as "The fieldIds must contain no more than 100 items."

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.FieldSchemeToFieldsResponse', self._runtime.call('update_fields_associated_with_schemes', call_args({'body': body})))

    def remove_fields_associated_with_schemes(self, *, body: builtins.dict[str, _t.RemoveFieldAssociationsRequestItem]) -> _t.MinimalFieldSchemeToFieldsResponse:
        """
        Remove fields associated with field schemes

        Remove fields associated with field association schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.MinimalFieldSchemeToFieldsResponse', self._runtime.call('remove_fields_associated_with_schemes', call_args({'body': body})))

    def update_field_association_scheme_item_parameters(self, *, body: builtins.dict[str, builtins.list[_t.UpdateFieldSchemeParametersRequest]]) -> _t.UpdateFieldSchemeParametersResponse:
        """
        Update field parameters

        Update field association item parameters in field association schemes.

        **Request body limits:** a single request can update parameters for at most **100 fields** (the top-level field ID keys of the request body). In addition, each field may include at most 50 update items, and each update item may reference at most 50 field schemes. Exceeding any of these limits returns a 400 response with an error such as "The fieldIds must contain no more than 100 items."

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.UpdateFieldSchemeParametersResponse', self._runtime.call('update_field_association_scheme_item_parameters', call_args({'body': body})))

    def remove_field_association_scheme_item_parameters(self, *, body: builtins.dict[str, builtins.list[_t.ParameterRemovalDetails]]) -> Any:
        """
        Remove field parameters

        Remove field association parameters overrides for work types.

        **Request body limits:** a single request can remove at most **100 parameters**. The number of removals is counted as the sum, across every removal entry, of the number of work types multiplied by the number of parameter names in that entry. Exceeding this limit returns a 400 response with the error "Request exceeds maximum number of parameters that can be removed 100".

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_field_association_scheme_item_parameters', call_args({'body': body})))

    def list(self, *, project_id: builtins.list[int], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBean2GetProjectsWithFieldSchemesResponse:
        """
        Get projects with field schemes

        Get projects with field association schemes. This will be a temporary API but useful when transitioning from the legacy field configuration APIs to the new ones.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBean2GetProjectsWithFieldSchemesResponse', self._runtime.call('get_projects_with_field_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id})))

    def associate_projects_to_field_association_schemes(self, *, body: builtins.dict[str, _t.FieldSchemeToProjectsRequest]) -> _t.FieldSchemeToProjectsResponse:
        """
        Associate projects to field schemes

        Associate projects to field association schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.FieldSchemeToProjectsResponse', self._runtime.call('associate_projects_to_field_association_schemes', call_args({'body': body})))

    def get_field_association_scheme(self, *, id: int) -> _t.GetFieldAssociationSchemeByIdResponse:
        """
        Get field scheme

        Endpoint for fetching a field association scheme by its ID

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.GetFieldAssociationSchemeByIdResponse', self._runtime.call('get_field_association_scheme_by_id', call_args({'id': id})))

    def update_field_association_scheme(self, *, id: int, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.UpdateFieldAssociationSchemeResponse:
        """
        Update field scheme

        Endpoint for updating an existing field association scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.UpdateFieldAssociationSchemeResponse', self._runtime.call('update_field_association_scheme', call_args({'id': id}, {'body': {'description': description, 'name': name}})))

    def delete_field_association_scheme(self, *, id: int) -> _t.DeleteFieldAssociationSchemeResponse:
        """
        Delete a field scheme

        Delete a specified field association scheme

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.DeleteFieldAssociationSchemeResponse', self._runtime.call('delete_field_association_scheme', call_args({'id': id})))

    def clone_field_association_scheme(self, *, id: int, name: str, description: str | Unset = UNSET) -> _t.CreateFieldAssociationSchemeResponse:
        """
        Clone field scheme

        Endpoint for cloning an existing field association scheme into a new one.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.CreateFieldAssociationSchemeResponse', self._runtime.call('clone_field_association_scheme', call_args({'id': id}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def search_field_association_scheme_fields(self, *, id: int, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, field_id: builtins.list[str] | Unset = UNSET) -> _t.PageBean2FieldAssociationSchemeFieldSearchResult:
        """
        Search field scheme fields

        Search for fields belonging to a given field association scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBean2FieldAssociationSchemeFieldSearchResult', self._runtime.call('search_field_association_scheme_fields', call_args({'start_at': start_at, 'max_results': max_results, 'field_id': field_id, 'id': id})))

    def list_field_association_scheme_item_parameters(self, *, id: int, field_id: str) -> _t.GetFieldAssociationParametersResponse:
        """
        Get field parameters

        Retrieve field association parameters on a field association scheme

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.GetFieldAssociationParametersResponse', self._runtime.call('get_field_association_scheme_item_parameters', call_args({'id': id, 'field_id': field_id})))

    def search_field_association_scheme_projects(self, *, id: int, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, project_id: builtins.list[int] | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBean2FieldAssociationSchemeProjectSearchResult:
        """
        Search field scheme projects

        REST Endpoint for searching for projects belonging to a given field association scheme

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBean2FieldAssociationSchemeProjectSearchResult', self._runtime.call('search_field_association_scheme_projects', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id, 'query': query, 'id': id})))

class _FilterSharingResource:
    """Operations under ``filter_sharing``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_default_share_scope(self) -> _t.DefaultShareScope:
        """
        Get default share scope

        Returns the default sharing settings for new filters and dashboards for a user.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.DefaultShareScope', self._runtime.call('get_default_share_scope', call_args({})))

    def set_default_share_scope(self, *, scope: _t.DefaultShareScopeScope) -> _t.DefaultShareScope:
        """
        Set default share scope

        Sets the default sharing for new filters and dashboards for a user.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.DefaultShareScope', self._runtime.call('set_default_share_scope', call_args({}, {'body': {'scope': scope}}, required=frozenset({'body'}))))

    def list_share_permissions(self, *, id: int) -> builtins.list[_t.SharePermission]:
        """
        Get share permissions

        Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None, however, share permissions are only returned for:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('builtins.list[_t.SharePermission]', self._runtime.call('get_share_permissions', call_args({'id': id})))

    def add_share_permission(self, *, id: int, type_: _t.SharePermissionInputBeanType, account_id: str | Unset = UNSET, group_id: str | Unset = UNSET, groupname: str | Unset = UNSET, project_id: str | Unset = UNSET, project_role_id: str | Unset = UNSET, rights: int | Unset = UNSET) -> builtins.list[_t.SharePermission]:
        """
        Add share permission

        Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter.

        Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put).

        **[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.
        """
        return cast('builtins.list[_t.SharePermission]', self._runtime.call('add_share_permission', call_args({'id': id}, {'body': {'account_id': account_id, 'group_id': group_id, 'groupname': groupname, 'project_id': project_id, 'project_role_id': project_role_id, 'rights': rights, 'type': type_}}, required=frozenset({'body'}))))

    def get_share_permission(self, *, id: int, permission_id: int) -> _t.SharePermission:
        """
        Get share permission

        Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None, however, a share permission is only returned for:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('_t.SharePermission', self._runtime.call('get_share_permission', call_args({'id': id, 'permission_id': permission_id})))

    def delete_share_permission(self, *, id: int, permission_id: int) -> None:
        """
        Delete share permission

        Deletes a share permission from a filter.

        **[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.
        """
        self._runtime.call('delete_share_permission', call_args({'id': id, 'permission_id': permission_id}))

class _FiltersResource:
    """Operations under ``filters``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create(self, *, name: str, expand: str | Unset = UNSET, override_share_permissions: bool | Unset = UNSET, approximate_last_used: str | Unset = UNSET, description: str | Unset = UNSET, edit_permissions: builtins.list[_t.SharePermission] | Unset = UNSET, favourite: bool | Unset = UNSET, favourited_count: int | Unset = UNSET, id: str | Unset = UNSET, jql: str | Unset = UNSET, owner: _t.User | Unset = UNSET, search_url: str | Unset = UNSET, self_: str | Unset = UNSET, share_permissions: builtins.list[_t.SharePermission] | Unset = UNSET, shared_users: _t.UserList | Unset = UNSET, subscriptions: _t.FilterSubscriptionsList | Unset = UNSET, view_url: str | Unset = UNSET) -> _t.Filter:
        """
        Create filter

        Creates a filter. The filter is shared according to the [default share scope](#api-rest-api-3-filter-post). The filter is not selected as a favorite.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.Filter', self._runtime.call('create_filter', call_args({'expand': expand, 'override_share_permissions': override_share_permissions}, {'body': {'approximate_last_used': approximate_last_used, 'description': description, 'edit_permissions': edit_permissions, 'favourite': favourite, 'favourited_count': favourited_count, 'id': id, 'jql': jql, 'name': name, 'owner': owner, 'search_url': search_url, 'self': self_, 'share_permissions': share_permissions, 'shared_users': shared_users, 'subscriptions': subscriptions, 'view_url': view_url}}, required=frozenset({'body'}))))

    def list_favourite(self, *, expand: str | Unset = UNSET) -> builtins.list[_t.Filter]:
        """
        Get favorite filters

        Returns the visible favorite filters of the user.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is:

         *  owned by the user.
         *  shared with a group that the user is a member of.
         *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  shared with a public project.
         *  shared with the public.

        For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.
        """
        return cast('builtins.list[_t.Filter]', self._runtime.call('get_favourite_filters', call_args({'expand': expand})))

    def list_my(self, *, expand: str | Unset = UNSET, include_favourites: bool | Unset = UNSET) -> builtins.list[_t.Filter]:
        """
        Get my filters

        Returns the filters owned by the user. If `includeFavourites` is `true`, the user's visible favorite filters are also returned.

        **[Permissions](#permissions) required:** Permission to access Jira, however, a favorite filters is only visible to the user where the filter is:

         *  owned by the user.
         *  shared with a group that the user is a member of.
         *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  shared with a public project.
         *  shared with the public.

        For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.
        """
        return cast('builtins.list[_t.Filter]', self._runtime.call('get_my_filters', call_args({'expand': expand, 'include_favourites': include_favourites})))

    def get_paginated(self, *, filter_name: str | Unset = UNSET, account_id: str | Unset = UNSET, owner: str | Unset = UNSET, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, project_id: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, order_by: _t.GetFiltersPaginatedOrderBy | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET, override_share_permissions: bool | Unset = UNSET, is_substring_match: bool | Unset = UNSET) -> _t.PageBeanFilterDetails:
        """
        Search for filters

        Returns a [paginated](#pagination) list of filters. Use this operation to get:

         *  specific filters, by defining `id` only.
         *  filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None, however, only the following filters that match the query parameters are returned:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('_t.PageBeanFilterDetails', self._runtime.call('get_filters_paginated', call_args({'filter_name': filter_name, 'account_id': account_id, 'owner': owner, 'groupname': groupname, 'group_id': group_id, 'project_id': project_id, 'id': id, 'order_by': order_by, 'start_at': start_at, 'max_results': max_results, 'expand': expand, 'override_share_permissions': override_share_permissions, 'is_substring_match': is_substring_match})))

    def get(self, *, id: int, expand: str | Unset = UNSET, override_share_permissions: bool | Unset = UNSET) -> _t.Filter:
        """
        Get filter

        Returns a filter.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None, however, the filter is only returned where it is:

         *  owned by the user.
         *  shared with a group that the user is a member of.
         *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  shared with a public project.
         *  shared with the public.
        """
        return cast('_t.Filter', self._runtime.call('get_filter', call_args({'id': id, 'expand': expand, 'override_share_permissions': override_share_permissions})))

    def update(self, *, id: int, body: _t.Filter, expand: str | Unset = UNSET, override_share_permissions: bool | Unset = UNSET) -> _t.Filter:
        """
        Update filter

        Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing.

        **[Permissions](#permissions) required:** Permission to access Jira, however the user must own the filter.
        """
        return cast('_t.Filter', self._runtime.call('update_filter', call_args({'id': id, 'expand': expand, 'override_share_permissions': override_share_permissions, 'body': body})))

    def delete(self, *, id: int) -> None:
        """
        Delete filter

        Delete a filter.

        **[Permissions](#permissions) required:** Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_filter', call_args({'id': id}))

    def list_columns(self, *, id: int) -> builtins.list[_t.ColumnItem]:
        """
        Get columns

        Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in *List View* with the *Columns* set to *Filter*.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None, however, column details are only returned for:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('builtins.list[_t.ColumnItem]', self._runtime.call('get_columns', call_args({'id': id})))

    def set_columns(self, *, id: int, columns: builtins.list[str] | Unset = UNSET) -> Any:
        """
        Set columns

        Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to `true`.

        Send the columns as a JSON request body, for example `{"columns": ["summary", "description"]}`. To remove all columns from the filter, send an empty `columns` array or omit `columns` from the request body.

        **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only set for:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('Any', self._runtime.call('set_columns', call_args({'id': id}, {'body': {'columns': columns}})))

    def reset_columns(self, *, id: int) -> None:
        """
        Reset columns

        Reset the user's column configuration for the filter to the default.

        **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only reset for:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        self._runtime.call('reset_columns', call_args({'id': id}))

    def set(self, *, id: int, expand: str | Unset = UNSET) -> _t.Filter:
        """
        Add filter as favorite

        Add a filter as a favorite for the user.

        **[Permissions](#permissions) required:** Permission to access Jira, however, the user can only favorite:

         *  filters owned by the user.
         *  filters shared with a group that the user is a member of.
         *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
         *  filters shared with a public project.
         *  filters shared with the public.
        """
        return cast('_t.Filter', self._runtime.call('set_favourite_for_filter', call_args({'id': id, 'expand': expand})))

    def delete_favourite_for(self, *, id: int, expand: str | Unset = UNSET) -> _t.Filter:
        """
        Remove filter as favorite

        Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user's favorites list. For example, if the user favorites a public filter that is subsequently made private (and is therefore no longer visible on their favorites list) they cannot remove it from their favorites list.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.Filter', self._runtime.call('delete_favourite_for_filter', call_args({'id': id, 'expand': expand})))

    def change_owner(self, *, id: int, account_id: str) -> Any:
        """
        Change filter owner

        Changes the owner of the filter.

        **[Permissions](#permissions) required:** Permission to access Jira. However, the user must own the filter or have the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('change_filter_owner', call_args({'id': id}, {'body': {'account_id': account_id}}, required=frozenset({'body'}))))

class _GroupAndUserPickerResource:
    """Operations under ``group_and_user_picker``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def find_users_and_groups(self, *, query: str, max_results: int | Unset = UNSET, show_avatar: bool | Unset = UNSET, field_id: str | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET, issue_type_id: builtins.list[str] | Unset = UNSET, avatar_size: _t.FindUsersAndGroupsAvatarSize | Unset = UNSET, case_insensitive: bool | Unset = UNSET, exclude_connect_addons: bool | Unset = UNSET, include_ai_agents: bool | Unset = UNSET) -> _t.FoundUsersAndGroups:
        """
        Find users and groups

        Returns a list of users and groups matching a string. The string is used:

         *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.
         *  for groups, to find a case-sensitive match with group name.

        For example, if the string *tin* is used, records with the display name *Tina*, email address *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

        Optionally, the search can be refined to:

         *  the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific:
            
             *  projects.
             *  issue types.
            
            If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned.
         *  not return Connect app users and groups.
         *  return groups that have a case-insensitive match with the query.

        The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an `html` field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically *Showing X of Y matching groups*.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('_t.FoundUsersAndGroups', self._runtime.call('find_users_and_groups', call_args({'query': query, 'max_results': max_results, 'show_avatar': show_avatar, 'field_id': field_id, 'project_id': project_id, 'issue_type_id': issue_type_id, 'avatar_size': avatar_size, 'case_insensitive': case_insensitive, 'exclude_connect_addons': exclude_connect_addons, 'include_ai_agents': include_ai_agents})))

class _GroupsResource:
    """Operations under ``groups``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self, *, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, expand: str | Unset = UNSET) -> _t.Group:
        """
        Get group

        This operation is deprecated, use [`group/member`](#api-rest-api-3-group-member-get).

        Returns all users in a group.

        **[Permissions](#permissions) required:** either of:

         *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.Group', self._runtime.call('get_group', call_args({'groupname': groupname, 'group_id': group_id, 'expand': expand})))

    def create(self, *, name: str) -> _t.Group:
        """
        Create group

        Creates a group.

        **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
        """
        return cast('_t.Group', self._runtime.call('create_group', call_args({}, {'body': {'name': name}}, required=frozenset({'body'}))))

    def remove(self, *, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, swap_group: str | Unset = UNSET, swap_group_id: str | Unset = UNSET) -> None:
        """
        Remove group

        Deletes a group.

        **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* strategic [group](https://confluence.atlassian.com/x/24xjL)).
        """
        self._runtime.call('remove_group', call_args({'groupname': groupname, 'group_id': group_id, 'swap_group': swap_group, 'swap_group_id': swap_group_id}))

    def bulk(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, group_id: builtins.list[str] | Unset = UNSET, group_name: builtins.list[str] | Unset = UNSET, access_type: str | Unset = UNSET, application_key: str | Unset = UNSET) -> _t.PageBeanGroupDetails:
        """
        Bulk get groups

        Returns a [paginated](#pagination) list of groups.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanGroupDetails', self._runtime.call('bulk_get_groups', call_args({'start_at': start_at, 'max_results': max_results, 'group_id': group_id, 'group_name': group_name, 'access_type': access_type, 'application_key': application_key})))

    def get_users_from(self, *, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, include_inactive_users: bool | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanUserDetails:
        """
        Get users from group

        Returns a [paginated](#pagination) list of all users in a group.

        Note that users are ordered by username, however the username is not returned in the results due to privacy reasons.

        **[Permissions](#permissions) required:** either of:

         *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanUserDetails', self._runtime.call('get_users_from_group', call_args({'groupname': groupname, 'group_id': group_id, 'include_inactive_users': include_inactive_users, 'start_at': start_at, 'max_results': max_results})))

    def add(self, *, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, account_id: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.Group:
        """
        Add user to group

        Adds a user to a group.

        **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
        """
        return cast('_t.Group', self._runtime.call('add_user_to_group', call_args({'groupname': groupname, 'group_id': group_id}, {'body': {'account_id': account_id, 'name': name}})))

    def remove_user_from(self, *, account_id: str, groupname: str | Unset = UNSET, group_id: str | Unset = UNSET, username: str | Unset = UNSET) -> None:
        """
        Remove user from group

        Removes a user from a group.

        **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
        """
        self._runtime.call('remove_user_from_group', call_args({'groupname': groupname, 'group_id': group_id, 'username': username, 'account_id': account_id}))

    def find(self, *, account_id: str | Unset = UNSET, query: str | Unset = UNSET, exclude: builtins.list[str] | Unset = UNSET, exclude_id: builtins.list[str] | Unset = UNSET, max_results: int | Unset = UNSET, case_insensitive: bool | Unset = UNSET, user_name: str | Unset = UNSET) -> _t.FoundGroups:
        """
        Find groups

        Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results.

        The primary use case for this resource is to populate a group picker suggestions list. To this end, the returned object includes the `html` field where the matched query term is highlighted in the group name with the HTML strong tag. Also, the groups list is wrapped in a response object that contains a header for use in the picker, specifically *Showing X of Y matching groups*.

        The list returns with the groups sorted. If no groups match the list criteria, an empty list is returned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without the required permission return an empty list.

        *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without this permission, calls where query is not an exact match to an existing group will return an empty list.
        """
        return cast('_t.FoundGroups', self._runtime.call('find_groups', call_args({'account_id': account_id, 'query': query, 'exclude': exclude, 'exclude_id': exclude_id, 'max_results': max_results, 'case_insensitive': case_insensitive, 'user_name': user_name})))

class _IssueAttachmentsResource:
    """Operations under ``issue_attachments``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_attachment_content(self, *, id: str, redirect: bool | Unset = UNSET) -> None:
        """
        Get attachment content

        Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details.

        To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-thumbnail-id-get).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** For the issue containing the attachment:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If attachments are added in private comments, the comment-level restriction will be applied.
        """
        self._runtime.call('get_attachment_content', call_args({'id': id, 'redirect': redirect}))

    def get_attachment_meta(self) -> _t.AttachmentSettings:
        """
        Get Jira attachment settings

        Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed.

        Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.AttachmentSettings', self._runtime.call('get_attachment_meta', call_args({})))

    def get_attachment_thumbnail(self, *, id: str, redirect: bool | Unset = UNSET, fallback_to_default: bool | Unset = UNSET, width: int | Unset = UNSET, height: int | Unset = UNSET) -> None:
        """
        Get attachment thumbnail

        Returns the thumbnail of an attachment.

        To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-id-get).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** For the issue containing the attachment:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If attachments are added in private comments, the comment-level restriction will be applied.
        """
        self._runtime.call('get_attachment_thumbnail', call_args({'id': id, 'redirect': redirect, 'fallback_to_default': fallback_to_default, 'width': width, 'height': height}))

    def get_attachment(self, *, id: str) -> _t.AttachmentMetadata:
        """
        Get attachment metadata

        Returns the metadata for an attachment. Note that the attachment itself is not returned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If attachments are added in private comments, the comment-level restriction will be applied.
        """
        return cast('_t.AttachmentMetadata', self._runtime.call('get_attachment', call_args({'id': id})))

    def remove_attachment(self, *, id: str) -> None:
        """
        Delete attachment

        Deletes an attachment from an issue.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** For the project holding the issue containing the attachment:

         *  *Delete own attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by the calling user.
         *  *Delete all attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by any user.
        """
        self._runtime.call('remove_attachment', call_args({'id': id}))

    def expand_attachment_for_humans(self, *, id: str) -> _t.AttachmentArchiveMetadataReadable:
        """
        Get all metadata for an expanded attachment

        Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the attachment itself. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format is supported.

        Use this operation to retrieve data that is presented to the user, as this operation returns the metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which only returns the metadata for the attachment's contents.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** For the issue containing the attachment:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If attachments are added in private comments, the comment-level restriction will be applied.
        """
        return cast('_t.AttachmentArchiveMetadataReadable', self._runtime.call('expand_attachment_for_humans', call_args({'id': id})))

    def expand_attachment_for_machines(self, *, id: str) -> _t.AttachmentArchiveImpl:
        """
        Get contents metadata for an expanded attachment

        Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported.

        Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** For the issue containing the attachment:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If attachments are added in private comments, the comment-level restriction will be applied.
        """
        return cast('_t.AttachmentArchiveImpl', self._runtime.call('expand_attachment_for_machines', call_args({'id': id})))

    def add_attachment(self, *, issue_id_or_key: str, body: builtins.list[str | bytes | PathLike[str]]) -> builtins.list[_t.Attachment]:
        """
        Add attachment

        Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC 1867](https://www.ietf.org/rfc/rfc1867.txt)).

        Note that:

         *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special headers](#special-request-headers) for more information.
         *  The name of the multipart/form-data parameter that contains the attachments must be `file`.

        The following examples upload a file called *myfile.txt* to the issue *TEST-123*:

        #### curl ####

            curl --location --request POST 'https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
             -u 'email@example.com:<api_token>'
             -H 'X-Atlassian-Token: no-check'
             --form 'file=@"myfile.txt"'

        #### Node.js ####

            // This code sample uses the 'node-fetch' and 'form-data' libraries:
             // https://www.npmjs.com/package/node-fetch
             // https://www.npmjs.com/package/form-data
             const fetch = require('node-fetch');
             const FormData = require('form-data');
             const fs = require('fs');
            
             const filePath = 'myfile.txt';
             const form = new FormData();
             const stats = fs.statSync(filePath);
             const fileSizeInBytes = stats.size;
             const fileStream = fs.createReadStream(filePath);
            
             form.append('file', fileStream, {knownLength: fileSizeInBytes});
            
             fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
                 method: 'POST',
                 body: form,
                 headers: {
                     'Authorization': `Basic ${Buffer.from(
                         'email@example.com:'
                     ).toString('base64')}`,
                     'Accept': 'application/json',
                     'X-Atlassian-Token': 'no-check'
                 }
             })
                 .then(response => {
                     console.log(
                         `Response: ${response.status} ${response.statusText}`
                     );
                     return response.text();
                 })
                 .then(text => console.log(text))
                 .catch(err => console.error(err));

        #### Java ####

            // This code sample uses the  'Unirest' library:
             // http://unirest.io/java.html
             HttpResponse response = Unirest.post("https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments")
                     .basicAuth("email@example.com", "")
                     .header("Accept", "application/json")
                     .header("X-Atlassian-Token", "no-check")
                     .field("file", new File("myfile.txt"))
                     .asJson();
            
                     System.out.println(response.getBody());

        #### Python ####

            # This code sample uses the 'requests' library:
             # http://docs.python-requests.org
             import requests
             from requests.auth import HTTPBasicAuth
             import json
            
             url = "https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments"
            
             auth = HTTPBasicAuth("email@example.com", "")
            
             headers = {
                "Accept": "application/json",
                "X-Atlassian-Token": "no-check"
             }
            
             response = requests.request(
                "POST",
                url,
                headers = headers,
                auth = auth,
                files = {
                     "file": ("myfile.txt", open("myfile.txt","rb"), "application-type")
                }
             )
            
             print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

        #### PHP ####

            // This code sample uses the 'Unirest' library:
             // http://unirest.io/php.html
             Unirest\\Request::auth('email@example.com', '');
            
             $headers = array(
               'Accept' => 'application/json',
               'X-Atlassian-Token' => 'no-check'
             );
            
             $parameters = array(
               'file' => File::add('myfile.txt')
             );
            
             $response = Unirest\\Request::post(
               'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
               $headers,
               $parameters
             );
            
             var_dump($response)

        #### Forge ####

            // This sample uses Atlassian Forge and the `form-data` library.
             // https://developer.atlassian.com/platform/forge/
             // https://www.npmjs.com/package/form-data
             import api from "@forge/api";
             import FormData from "form-data";
            
             const form = new FormData();
             form.append('file', fileStream, {knownLength: fileSizeInBytes});
            
             const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments', {
                 method: 'POST',
                 body: form,
                 headers: {
                     'Accept': 'application/json',
                     'X-Atlassian-Token': 'no-check'
                 }
             });
            
             console.log(`Response: ${response.status} ${response.statusText}`);
             console.log(await response.json());

        Tip: Use a client library. Many client libraries have classes for handling multipart POST operations. For example, in Java, the Apache HTTP Components library provides a [MultiPartEntity](http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST operations.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** 

         *  *Browse Projects* and *Create attachments* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('builtins.list[_t.Attachment]', self._runtime.call('add_attachment', call_args({'issue_id_or_key': issue_id_or_key, 'body': body})))

class _IssueBulkOperationsResource:
    """Operations under ``issue_bulk_operations``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def submit_bulk_delete(self, *, selected_issue_ids_or_keys: builtins.list[str], send_bulk_notification: bool | None | Unset = UNSET) -> _t.SubmittedBulkOperation:
        """
        Bulk delete issues

        Use this API to submit a bulk delete request. You can delete up to 1,000 issues in a single operation.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Delete [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Delete-issues/) in all projects that contain the selected issues.
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_delete', call_args({}, {'body': {'selected_issue_ids_or_keys': selected_issue_ids_or_keys, 'send_bulk_notification': send_bulk_notification}}, required=frozenset({'body'}))))

    def list_bulk_editable_fields(self, *, issue_ids_or_keys: str, search_text: str | Unset = UNSET, ending_before: str | Unset = UNSET, starting_after: str | Unset = UNSET) -> _t.BulkEditGetFields:
        """
        Get bulk editable fields

        Use this API to get a list of fields visible to the user to perform bulk edit operations. You can pass single or multiple issues in the query to get eligible editable fields. This API uses pagination to return responses, delivering 50 fields at a time.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  Depending on the field, any field-specific permissions required to edit it.
        """
        return cast('_t.BulkEditGetFields', self._runtime.call('get_bulk_editable_fields', call_args({'issue_ids_or_keys': issue_ids_or_keys, 'search_text': search_text, 'ending_before': ending_before, 'starting_after': starting_after})))

    def submit_bulk_edit(self, *, edited_fields_input: _t.JiraIssueFields, selected_actions: builtins.list[str], selected_issue_ids_or_keys: builtins.list[str], send_bulk_notification: bool | None | Unset = UNSET) -> _t.SubmittedBulkOperation:
        """
        Bulk edit issues

        Use this API to submit a bulk edit request and simultaneously edit multiple issues. There are limits applied to the number of issues and fields that can be edited. A single request can accommodate a maximum of 1000 issues (including subtasks) and 200 fields.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  Edit [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_edit', call_args({}, {'body': {'edited_fields_input': edited_fields_input, 'selected_actions': selected_actions, 'selected_issue_ids_or_keys': selected_issue_ids_or_keys, 'send_bulk_notification': send_bulk_notification}}, required=frozenset({'body'}))))

    def submit_bulk_move(self, *, send_bulk_notification: bool | None | Unset = UNSET, target_to_sources_mapping: builtins.dict[str, _t.TargetToSourcesMapping] | Unset = UNSET) -> _t.SubmittedBulkOperation:
        """
        Bulk move issues

        Use this API to submit a bulk issue move request. You can move multiple issues from multiple projects in a single request, but they must all be moved to a single project, issue type, and parent. You can't move more than 1000 issues (including subtasks) at once.

        #### Scenarios: ####

        This is an early version of the API and it doesn't have full feature parity with the Bulk Move UI experience.

         *  Moving issue of type A to issue of type B in the same project or a different project: `SUPPORTED`
         *  Moving multiple issues of type A in one or more projects to multiple issues of type B in one of the source projects or a different project: `SUPPORTED`
         *  Moving issues of multiple issue types in one or more projects to issues of a single issue type in one of the source project or a different project: **`SUPPORTED`**  
            E.g. Moving issues of story and task issue types in project 1 and project 2 to issues of task issue type in project 3
         *  Moving a standard parent issue of type A with its multiple subtask issue types in one project to standard issue of type B and multiple subtask issue types in the same project or a different project: `SUPPORTED`
         *  Moving standard issues with their subtasks to a parent issue in the same project or a different project without losing their relation: `SUPPORTED`
         *  Moving an epic issue with its child issues to a different project without losing their relation: `SUPPORTED`  
            This usecase is **supported using multiple requests**. Move the epic in one request and then move the children in a separate request with target parent set to the epic issue id  
              
            (Alternatively, move them individually and stitch the relationship back with the Bulk Edit API)

        #### Limits applied to bulk issue moves: ####

        When using the bulk move, keep in mind that there are limits on the number of issues and fields you can include.

         *  You can move up to 1,000 issues in a single operation, including any subtasks.
         *  The total combined number of fields across all issues must not exceed 1,500,000. For example, if each issue includes 15,000 fields, then the maximum number of issues that can be moved is 100.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Move [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in source projects.
         *  Create [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects.
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects, if moving subtasks only.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_move', call_args({}, {'body': {'send_bulk_notification': send_bulk_notification, 'target_to_sources_mapping': target_to_sources_mapping}})))

    def list_available_transitions(self, *, issue_ids_or_keys: str, ending_before: str | Unset = UNSET, starting_after: str | Unset = UNSET) -> _t.BulkTransitionGetAvailableTransitions:
        """
        Get available transitions

        Use this API to retrieve a list of transitions available for the specified issues that can be used or bulk transition operations. You can submit either single or multiple issues in the query to obtain the available transitions.

        The response will provide the available transitions for issues, organized by their respective workflows. **Only the transitions that are common among the issues within that workflow and do not involve any additional field updates will be included.** For bulk transitions that require additional field updates, please utilise the Jira Cloud UI.

        You can request available transitions for up to 1,000 issues in a single operation. This API uses pagination to return responses, delivering 50 workflows at a time.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.BulkTransitionGetAvailableTransitions', self._runtime.call('get_available_transitions', call_args({'issue_ids_or_keys': issue_ids_or_keys, 'ending_before': ending_before, 'starting_after': starting_after})))

    def submit_bulk_transition(self, *, bulk_transition_inputs: builtins.list[_t.BulkTransitionSubmitInput], send_bulk_notification: bool | None | Unset = UNSET) -> _t.SubmittedBulkOperation:
        """
        Bulk transition issue statuses

        Use this API to submit a bulk issue status transition request. You can transition multiple issues, alongside with their valid transition Ids. You can transition up to 1,000 issues in a single operation.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_transition', call_args({}, {'body': {'bulk_transition_inputs': bulk_transition_inputs, 'send_bulk_notification': send_bulk_notification}}, required=frozenset({'body'}))))

    def submit_bulk_unwatch(self, *, selected_issue_ids_or_keys: builtins.list[str]) -> _t.SubmittedBulkOperation:
        """
        Bulk unwatch issues

        Use this API to submit a bulk unwatch request. You can unwatch up to 1,000 issues in a single operation.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_unwatch', call_args({}, {'body': {'selected_issue_ids_or_keys': selected_issue_ids_or_keys}}, required=frozenset({'body'}))))

    def submit_bulk_watch(self, *, selected_issue_ids_or_keys: builtins.list[str]) -> _t.SubmittedBulkOperation:
        """
        Bulk watch issues

        Use this API to submit a bulk watch request. You can watch up to 1,000 issues in a single operation.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
         *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SubmittedBulkOperation', self._runtime.call('submit_bulk_watch', call_args({}, {'body': {'selected_issue_ids_or_keys': selected_issue_ids_or_keys}}, required=frozenset({'body'}))))

    def get_bulk_operation_progress(self, *, task_id: str) -> _t.BulkOperationProgress:
        """
        Get bulk issue operation progress

        Use this to get the progress state for the specified bulk operation `taskId`.

        **[Permissions](#permissions) required:**

         *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).

        If the task is running, this resource will return:

            {"taskId":"10779","status":"RUNNING","progressPercent":65,"submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"created":1690180055963,"started":1690180056206,"updated":169018005829}

        If the task has completed, then this resource will return:

            {"processedAccessibleIssues":[10001,10002],"created":1709189449954,"progressPercent":100,"started":1709189450154,"status":"COMPLETE","submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"invalidOrInaccessibleIssueCount":0,"taskId":"10000","totalIssueCount":2,"updated":1709189450354}

        **Note:** You can view task progress for up to 14 days from creation.
        """
        return cast('_t.BulkOperationProgress', self._runtime.call('get_bulk_operation_progress', call_args({'task_id': task_id})))

class _IssueCommentPropertiesResource:
    """Operations under ``issue_comment_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_comment_property_keys(self, *, comment_id: str) -> _t.PropertyKeys:
        """
        Get comment property keys

        Returns the keys of all the properties of a comment.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_comment_property_keys', call_args({'comment_id': comment_id})))

    def get_comment_property(self, *, comment_id: str, property_key: str) -> _t.EntityProperty:
        """
        Get comment property

        Returns the value of a comment property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_comment_property', call_args({'comment_id': comment_id, 'property_key': property_key})))

    def set_comment_property(self, *, comment_id: str, property_key: str, body: Any) -> Any:
        """
        Set comment property

        Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        **[Permissions](#permissions) required:** either of:

         *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on any comment.
         *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on a comment created by the user.
        """
        return cast('Any', self._runtime.call('set_comment_property', call_args({'comment_id': comment_id, 'property_key': property_key, 'body': body})))

    def delete_comment_property(self, *, comment_id: str, property_key: str) -> None:
        """
        Delete comment property

        Deletes a comment property.

        **[Permissions](#permissions) required:** either of:

         *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from any comment.
         *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from a comment created by the user.
        """
        self._runtime.call('delete_comment_property', call_args({'comment_id': comment_id, 'property_key': property_key}))

class _IssueCommentsResource:
    """Operations under ``issue_comments``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_comments_by_ids(self, *, ids: builtins.list[int], expand: str | Unset = UNSET) -> _t.PageBeanComment:
        """
        Get comments by IDs

        Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Comments are returned where the user:

         *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.PageBeanComment', self._runtime.call('get_comments_by_ids', call_args({'expand': expand}, {'body': {'ids': ids}}, required=frozenset({'body'}))))

    def list_comments(self, *, issue_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: _t.GetCommentsOrderBy | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageOfComments:
        """
        Get comments

        Returns all comments for an issue.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Comments are included in the response where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, belongs to the group or has the role visibility is role visibility is restricted to.
        """
        return cast('_t.PageOfComments', self._runtime.call('get_comments', call_args({'issue_id_or_key': issue_id_or_key, 'start_at': start_at, 'max_results': max_results, 'order_by': order_by, 'expand': expand})))

    def add_comment(self, *, issue_id_or_key: str, expand: str | Unset = UNSET, author: _t.UserDetails | Unset = UNSET, body: Any | Unset = UNSET, created: str | Unset = UNSET, id: str | Unset = UNSET, jsd_author_can_see_request: bool | Unset = UNSET, jsd_public: bool | Unset = UNSET, properties: builtins.list[_t.EntityProperty] | Unset = UNSET, rendered_body: str | Unset = UNSET, self_: str | Unset = UNSET, update_author: _t.UserDetails | Unset = UNSET, updated: str | Unset = UNSET, visibility: _t.Visibility | Unset = UNSET) -> _t.Comment:
        """
        Add comment

        Adds a comment to an issue.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Add comments* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.Comment', self._runtime.call('add_comment', call_args({'issue_id_or_key': issue_id_or_key, 'expand': expand}, {'body': {'author': author, 'body': body, 'created': created, 'id': id, 'jsd_author_can_see_request': jsd_author_can_see_request, 'jsd_public': jsd_public, 'properties': properties, 'rendered_body': rendered_body, 'self': self_, 'update_author': update_author, 'updated': updated, 'visibility': visibility}})))

    def get_comment(self, *, issue_id_or_key: str, id: str, expand: str | Unset = UNSET) -> _t.Comment:
        """
        Get comment

        Returns a comment.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.Comment', self._runtime.call('get_comment', call_args({'issue_id_or_key': issue_id_or_key, 'id': id, 'expand': expand})))

    def update_comment(self, *, issue_id_or_key: str, id: str, body: _t.Comment, notify_users: bool | Unset = UNSET, override_editable_flag: bool | Unset = UNSET, expand: str | Unset = UNSET) -> _t.Comment:
        """
        Update comment

        Updates a comment.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Edit all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any comment or *Edit own comments* to update comment created by the user.
         *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

        **WARNING:** Child comments inherit visibility from their parent comment. Attempting to update a child comment's visibility will result in a 400 (Bad Request) error.
        """
        return cast('_t.Comment', self._runtime.call('update_comment', call_args({'issue_id_or_key': issue_id_or_key, 'id': id, 'notify_users': notify_users, 'override_editable_flag': override_editable_flag, 'expand': expand, 'body': body})))

    def delete_comment(self, *, issue_id_or_key: str, id: str) -> None:
        """
        Delete comment

        Deletes a comment.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Delete all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any comment or *Delete own comments* to delete comment created by the user,
         *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.
        """
        self._runtime.call('delete_comment', call_args({'issue_id_or_key': issue_id_or_key, 'id': id}))

class _IssueCustomFieldAssociationsResource:
    """Operations under ``issue_custom_field_associations``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create_associations(self, *, association_contexts: builtins.list[_t.AssociationContextObject], fields: builtins.list[_t.FieldIdentifierObject]) -> Any:
        """
        Create associations

        Associates fields with projects.

        Fields will be associated with each issue type on the requested projects.

        Fields will be associated with all projects that share the same field configuration which the provided projects are using. This means that while the field will be associated with the requested projects, it will also be associated with any other projects that share the same field configuration.

        If a success response is returned it means that the field association has been created in any applicable contexts where it wasn't already present.

        Up to 50 fields and up to 100 projects can be associated in a single request. If more fields or projects are provided a 400 response will be returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('create_associations', call_args({}, {'body': {'association_contexts': association_contexts, 'fields': fields}}, required=frozenset({'body'}))))

    def remove_associations(self, *, association_contexts: builtins.list[_t.AssociationContextObject], fields: builtins.list[_t.FieldIdentifierObject]) -> Any:
        """
        Remove associations

        Unassociates a set of fields with a project and issue type context.

        Fields will be unassociated with all projects/issue types that share the same field configuration which the provided project and issue types are using. This means that while the field will be unassociated with the provided project and issue types, it will also be unassociated with any other projects and issue types that share the same field configuration.

        If a success response is returned it means that the field association has been removed in any applicable contexts where it was present.

        Up to 50 fields and up to 100 projects and issue types can be unassociated in a single request. If more fields or projects are provided a 400 response will be returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_associations', call_args({}, {'body': {'association_contexts': association_contexts, 'fields': fields}}, required=frozenset({'body'}))))

class _IssueCustomFieldConfigurationAppsResource:
    """Operations under ``issue_custom_field_configuration_apps``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_custom_fields_configurations(self, *, field_ids_or_keys: builtins.list[str], id: builtins.list[int] | Unset = UNSET, field_context_id: builtins.list[int] | Unset = UNSET, issue_id: int | Unset = UNSET, project_key_or_id: str | Unset = UNSET, issue_type_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanBulkContextualConfiguration:
        """
        Bulk get custom field configurations

        Returns a [paginated](#pagination) list of configurations for list of custom fields of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

        The result can be filtered by one of these criteria:

         *  `id`.
         *  `fieldContextId`.
         *  `issueId`.
         *  `projectKeyOrId` and `issueTypeId`.

        Otherwise, all configurations for the provided list of custom fields are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that provided the custom field type.
        """
        return cast('_t.PageBeanBulkContextualConfiguration', self._runtime.call('get_custom_fields_configurations', call_args({'id': id, 'field_context_id': field_context_id, 'issue_id': issue_id, 'project_key_or_id': project_key_or_id, 'issue_type_id': issue_type_id, 'start_at': start_at, 'max_results': max_results}, {'body': {'field_ids_or_keys': field_ids_or_keys}}, required=frozenset({'body'}))))

    def get_custom_field_configuration(self, *, field_id_or_key: str, id: builtins.list[int] | Unset = UNSET, field_context_id: builtins.list[int] | Unset = UNSET, issue_id: int | Unset = UNSET, project_key_or_id: str | Unset = UNSET, issue_type_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanContextualConfiguration:
        """
        Get custom field configurations

        Returns a [paginated](#pagination) list of configurations for a custom field of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

        The result can be filtered by one of these criteria:

         *  `id`.
         *  `fieldContextId`.
         *  `issueId`.
         *  `projectKeyOrId` and `issueTypeId`.

        Otherwise, all configurations are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that provided the custom field type.
        """
        return cast('_t.PageBeanContextualConfiguration', self._runtime.call('get_custom_field_configuration', call_args({'field_id_or_key': field_id_or_key, 'id': id, 'field_context_id': field_context_id, 'issue_id': issue_id, 'project_key_or_id': project_key_or_id, 'issue_type_id': issue_type_id, 'start_at': start_at, 'max_results': max_results})))

    def update_custom_field_configuration(self, *, field_id_or_key: str, configurations: builtins.list[_t.ContextualConfiguration]) -> Any:
        """
        Update custom field configurations

        Update the configuration for contexts of a custom field of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field type.
        """
        return cast('Any', self._runtime.call('update_custom_field_configuration', call_args({'field_id_or_key': field_id_or_key}, {'body': {'configurations': configurations}}, required=frozenset({'body'}))))

class _IssueCustomFieldContextsResource:
    """Operations under ``issue_custom_field_contexts``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_contexts_for_field(self, *, field_id: str, is_any_issue_type: bool | Unset = UNSET, is_global_context: bool | Unset = UNSET, context_id: builtins.list[int] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanCustomFieldContext:
        """
        Get custom field contexts

        Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:

         *  With no other parameters set, all contexts.
         *  By defining `id` only, all contexts from the list of IDs.
         *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)
         *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)
        """
        return cast('_t.PageBeanCustomFieldContext', self._runtime.call('get_contexts_for_field', call_args({'field_id': field_id, 'is_any_issue_type': is_any_issue_type, 'is_global_context': is_global_context, 'context_id': context_id, 'start_at': start_at, 'max_results': max_results})))

    def create_custom_field_context(self, *, field_id: str, name: str, description: str | Unset = UNSET, id: str | Unset = UNSET, issue_type_ids: builtins.list[str] | Unset = UNSET, project_ids: builtins.list[str] | Unset = UNSET) -> _t.CreateCustomFieldContext:
        """
        Create custom field context

        Creates a custom field context.

        If `projectIds` is empty, a global context is created. A global context is one that applies to all project. If `issueTypeIds` is empty, the context applies to all issue types.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.CreateCustomFieldContext', self._runtime.call('create_custom_field_context', call_args({'field_id': field_id}, {'body': {'description': description, 'id': id, 'issue_type_ids': issue_type_ids, 'name': name, 'project_ids': project_ids}}, required=frozenset({'body'}))))

    def list_default_values(self, *, field_id: str, context_id: builtins.list[int] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanCustomFieldContextDefaultValue:
        """
        Get custom field contexts default values

        Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is returned.  
        The returned object depends on type of the custom field:

         *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
         *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
         *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.
         *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.
         *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.
         *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
         *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
         *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.
         *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.
         *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
         *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
         *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
         *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
         *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
         *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
         *  `CustomFieldContextDefaultValueLongText` (type `longtext`) for plain text paragraph fields.
         *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
         *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.
         *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.

        Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

         *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.
         *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.
         *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.
         *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.
         *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
         *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.
         *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.
         *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
         *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.

        **Deprecated:** This API is deprecated and will be removed in October 2026. A replacement API that supports multiple default values per issue type within a context is coming soon. See the deprecation notice [CHANGE-3082](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3082) for more details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanCustomFieldContextDefaultValue', self._runtime.call('get_default_values', call_args({'field_id': field_id, 'context_id': context_id, 'start_at': start_at, 'max_results': max_results})))

    def set_default_values(self, *, field_id: str, default_values: builtins.list[_t.CustomFieldContextDefaultValue] | Unset = UNSET) -> Any:
        """
        Set custom field contexts default values

        Sets default for contexts of a custom field. Default are defined using these objects:

         *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
         *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
         *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.
         *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.
         *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.
         *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
         *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
         *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.
         *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.
         *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
         *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
         *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
         *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
         *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
         *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
         *  `CustomFieldContextDefaultValueLongText` (type `longtext`) for plain text paragraph fields.
         *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
         *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.
         *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.

        Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

         *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.
         *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.
         *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.
         *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.
         *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
         *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.
         *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.
         *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
         *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.

        Only one type of default object can be included in a request. To remove a default for a context, set the default parameter to `null`.

        **Deprecated:** This API is deprecated and will be removed in October 2026. A replacement API that supports multiple default values per issue type within a context is coming soon. See the deprecation notice [CHANGE-3082](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3082) for more details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('set_default_values', call_args({'field_id': field_id}, {'body': {'default_values': default_values}})))

    def list_context_default_values(self, *, field_id: str, context_id: builtins.list[int] | Unset = UNSET, issue_type_id: builtins.list[str] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanContextDefaultValues:
        """
        Get default values for a custom field grouped by context and issue type

        Returns a paginated list of default values grouped by custom field context.

        Each returned `ContextDefaultValuesBean` has a `contextId` and a `defaultValues` list of `IssueTypeDefaultValueBean` entries - one per issue-type-scoped default value configured for the context. An entry with `"isAnyIssueType": true` represents the catch-all default that applies to every issue type covered by the context that is not covered by a more specific entry; a non-null `issueTypeId` represents a default that only applies to that issue type.

        For contexts that have not been converted to the multiple-contexts data model, exactly one entry is returned per context with `isAnyIssueType=true`. For converted contexts, one entry is returned per configured per-issue-type default.

        The value object on each entry is the same polymorphic `CustomFieldContextDefaultValueBean` exposed by the deprecated `GET /defaultValue` endpoint - its concrete subtype depends on the custom field's type (see the list of supported types on that endpoint).

        Only tenants enrolled in the early access program (EAP) can access this resource. See the [EAP announcement](https://ecosystem.atlassian.net/browse/CHANGE-3082) for details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanContextDefaultValues', self._runtime.call('get_context_default_values', call_args({'field_id': field_id, 'context_id': context_id, 'issue_type_id': issue_type_id, 'start_at': start_at, 'max_results': max_results})))

    def set_context_default_values(self, *, field_id: str, default_values: builtins.list[_t.IssueTypeDefaultValueUpdate] | Unset = UNSET) -> Any:
        """
        Set default values for a custom field by context and issue type

        Updates default values for individual issue types in custom field contexts.

        Only tenants enrolled in the early access program (EAP) can access this resource. See the [EAP announcement](https://ecosystem.atlassian.net/browse/CHANGE-3082) for details.

        Each entry targets either one issue type through \\{@code issueTypeId\\}, or the catch-all configuration through \\{@code isAnyIssueType=true\\}. A null value removes the default for that target. Entries not included in the request are left unchanged.
        """
        return cast('Any', self._runtime.call('set_context_default_values', call_args({'field_id': field_id}, {'body': {'default_values': default_values}})))

    def list_issue_type_mappings_for_contexts(self, *, field_id: str, context_id: builtins.list[int] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanIssueTypeToContextMapping:
        """
        Get issue types for custom field context

        Returns a [paginated](#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeToContextMapping', self._runtime.call('get_issue_type_mappings_for_contexts', call_args({'field_id': field_id, 'context_id': context_id, 'start_at': start_at, 'max_results': max_results})))

    def list_custom_field_contexts_for_projects_and_issue_types(self, *, field_id: str, mappings: builtins.list[_t.ProjectIssueTypeMapping], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanContextForProjectAndIssueType:
        """
        Get custom field contexts for projects and issue types

        Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type.

        If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is `null`.

        Duplicate project and issue type mappings cannot be provided in the request.

        The order of the returned values is the same as provided in the request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanContextForProjectAndIssueType', self._runtime.call('get_custom_field_contexts_for_projects_and_issue_types', call_args({'field_id': field_id, 'start_at': start_at, 'max_results': max_results}, {'body': {'mappings': mappings}}, required=frozenset({'body'}))))

    def get_project_context_mapping(self, *, field_id: str, context_id: builtins.list[int] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanCustomFieldContextProjectMapping:
        """
        Get project mappings for custom field context

        Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored.

        **Note:** Jira is adding support for multiple field contexts per project. On sites where this is enabled, a custom field can have more than one context associated with the same project, so this operation can return several mappings that share the same `projectId`, each with a different `contextId`. Do not assume that a project appears at most once in the response. See [CHANGE-3082](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3082) for more details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanCustomFieldContextProjectMapping', self._runtime.call('get_project_context_mapping', call_args({'field_id': field_id, 'context_id': context_id, 'start_at': start_at, 'max_results': max_results})))

    def update_custom_field_context(self, *, field_id: str, context_id: int, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update custom field context

        Updates a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_custom_field_context', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'description': description, 'name': name}})))

    def delete_custom_field_context(self, *, field_id: str, context_id: int) -> Any:
        """
        Delete custom field context

        Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

        This API will not allow removing the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_custom_field_context', call_args({'field_id': field_id, 'context_id': context_id})))

    def add_issue_types_to_context(self, *, field_id: str, context_id: int, default_value: _t.CustomFieldContextDefaultValue | Unset = UNSET, is_any_issue_type: bool | Unset = UNSET, issue_type_ids: builtins.list[str | None] | None | Unset = UNSET) -> Any:
        """
        Add issue types to context

        Adds issue types to a custom field context, appending the issue types to the issue types list.

        A custom field context without any issue types applies to all issue types. Adding issue types replaces the any-issue-type mapping unless \\{@code isAnyIssueType\\} is true. A supplied \\{@code defaultValue\\} applies to newly added mappings. If omitted, the default value of the first existing issue type mapping is copied. Existing mappings retain their defaults.

        If any of the issue types exists in the custom field context, the operation fails and no issue types are added.

        This API will not allow adding issue types to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_issue_types_to_context', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'default_value': default_value, 'is_any_issue_type': is_any_issue_type, 'issue_type_ids': issue_type_ids}})))

    def remove_issue_types_from_context(self, *, field_id: str, context_id: int, issue_type_ids: builtins.list[str]) -> Any:
        """
        Remove issue types from context

        Removes issue types from a custom field context.

        A custom field context without any issue types applies to all issue types.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_issue_types_from_context', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'issue_type_ids': issue_type_ids}}, required=frozenset({'body'}))))

    def assign_projects_to_custom_field_context(self, *, field_id: str, context_id: int, project_ids: builtins.list[str]) -> Any:
        """
        Assign custom field context to projects

        Assigns a custom field context to projects.

        If any project in the request is assigned to any context of the custom field, the operation fails.

        This API will not allow adding projects to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('assign_projects_to_custom_field_context', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'project_ids': project_ids}}, required=frozenset({'body'}))))

    def remove_custom_field_context_from_projects(self, *, field_id: str, context_id: int, project_ids: builtins.list[str]) -> Any:
        """
        Remove custom field context from projects

        Removes a custom field context from projects.

        A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects.

        If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_custom_field_context_from_projects', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'project_ids': project_ids}}, required=frozenset({'body'}))))

class _IssueCustomFieldOptionsResource:
    """Operations under ``issue_custom_field_options``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_custom_field_option(self, *, id: str) -> _t.CustomFieldOption:
        """
        Get custom field option

        Returns a custom field option. For example, an option in a select list.

        Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** The custom field option is returned as follows:

         *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.
        """
        return cast('_t.CustomFieldOption', self._runtime.call('get_custom_field_option', call_args({'id': id})))

    def get_options_for_context(self, *, field_id: str, context_id: int, option_id: int | Unset = UNSET, query: str | Unset = UNSET, only_options: bool | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanCustomFieldContextOption:
        """
        Get custom field options (context)

        Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.

        This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)
        """
        return cast('_t.PageBeanCustomFieldContextOption', self._runtime.call('get_options_for_context', call_args({'field_id': field_id, 'context_id': context_id, 'option_id': option_id, 'query': query, 'only_options': only_options, 'start_at': start_at, 'max_results': max_results})))

    def update_custom_field_option(self, *, field_id: str, context_id: int, options: builtins.list[_t.CustomFieldOptionUpdate] | Unset = UNSET) -> _t.CustomFieldUpdatedContextOptionsList:
        """
        Update custom field options (context)

        Updates the options of a custom field.

        If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response.

        Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.CustomFieldUpdatedContextOptionsList', self._runtime.call('update_custom_field_option', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'options': options}})))

    def create_custom_field_option(self, *, field_id: str, context_id: int, options: builtins.list[_t.CustomFieldOptionCreate] | Unset = UNSET) -> _t.CustomFieldCreatedContextOptionsList:
        """
        Create custom field options (context)

        Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.

        The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.

        This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.CustomFieldCreatedContextOptionsList', self._runtime.call('create_custom_field_option', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'options': options}})))

    def reorder_custom_field_options(self, *, field_id: str, context_id: int, custom_field_option_ids: builtins.list[str], after: str | Unset = UNSET, position: _t.OrderOfCustomFieldOptionsPosition | Unset = UNSET) -> Any:
        """
        Reorder custom field options (context)

        Changes the order of custom field options or cascading options in a context.

        This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('reorder_custom_field_options', call_args({'field_id': field_id, 'context_id': context_id}, {'body': {'after': after, 'custom_field_option_ids': custom_field_option_ids, 'position': position}}, required=frozenset({'body'}))))

    def delete_custom_field_option(self, *, field_id: str, context_id: int, option_id: int) -> None:
        """
        Delete custom field options (context)

        Deletes a custom field option.

        Options with cascading options cannot be deleted without deleting the cascading options first.

        This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_custom_field_option', call_args({'field_id': field_id, 'context_id': context_id, 'option_id': option_id}))

    def replace_custom_field_option(self, *, field_id: str, option_id: int, context_id: int, replace_with: int | Unset = UNSET, jql: str | Unset = UNSET) -> None:
        """
        Replace custom field options

        Replaces the options of a custom field.

        Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect or Forge apps.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('replace_custom_field_option', call_args({'replace_with': replace_with, 'jql': jql, 'field_id': field_id, 'option_id': option_id, 'context_id': context_id}))

class _IssueCustomFieldOptionsAppsResource:
    """Operations under ``issue_custom_field_options_apps``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_all_issue_field_options(self, *, field_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanIssueFieldOption:
        """
        Get all issue field options

        Returns a [paginated](#pagination) list of all the options of a select list issue field. A select list issue field is a type of [issue field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user to select a value from a list of options.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        return cast('_t.PageBeanIssueFieldOption', self._runtime.call('get_all_issue_field_options', call_args({'start_at': start_at, 'max_results': max_results, 'field_key': field_key})))

    def create_issue_field_option(self, *, field_key: str, value: str, config: _t.IssueFieldOptionConfiguration | Unset = UNSET, properties: builtins.dict[str, Any] | Unset = UNSET) -> _t.IssueFieldOption:
        """
        Create issue field option

        Creates an option for a select list issue field.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        Each field can have a maximum of 10000 options, and each option can have a maximum of 10000 scopes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        return cast('_t.IssueFieldOption', self._runtime.call('create_issue_field_option', call_args({'field_key': field_key}, {'body': {'config': config, 'properties': properties, 'value': value}}, required=frozenset({'body'}))))

    def list_selectable_issue_field_options(self, *, field_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, project_id: int | Unset = UNSET) -> _t.PageBeanIssueFieldOption:
        """
        Get selectable issue field options

        Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed and selected by the user.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanIssueFieldOption', self._runtime.call('get_selectable_issue_field_options', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id, 'field_key': field_key})))

    def list_visible_issue_field_options(self, *, field_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, project_id: int | Unset = UNSET) -> _t.PageBeanIssueFieldOption:
        """
        Get visible issue field options

        Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed by the user.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanIssueFieldOption', self._runtime.call('get_visible_issue_field_options', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id, 'field_key': field_key})))

    def get_issue_field_option(self, *, field_key: str, option_id: int) -> _t.IssueFieldOption:
        """
        Get issue field option

        Returns an option from a select list issue field.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        return cast('_t.IssueFieldOption', self._runtime.call('get_issue_field_option', call_args({'field_key': field_key, 'option_id': option_id})))

    def update_issue_field_option(self, *, field_key: str, option_id: int, id: int, value: str, config: _t.IssueFieldOptionConfiguration | Unset = UNSET, properties: builtins.dict[str, Any] | Unset = UNSET) -> _t.IssueFieldOption:
        """
        Update issue field option

        Updates or creates an option for a select list issue field. This operation requires that the option ID is provided when creating an option, therefore, the option ID needs to be specified as a path and body parameter. The option ID provided in the path and body must be identical.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        return cast('_t.IssueFieldOption', self._runtime.call('update_issue_field_option', call_args({'field_key': field_key, 'option_id': option_id}, {'body': {'config': config, 'id': id, 'properties': properties, 'value': value}}, required=frozenset({'body'}))))

    def delete_issue_field_option(self, *, field_key: str, option_id: int) -> Any:
        """
        Delete issue field option

        Deletes an option from a select list issue field.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        return cast('Any', self._runtime.call('delete_issue_field_option', call_args({'field_key': field_key, 'option_id': option_id})))

    def replace_issue_field_option(self, *, field_key: str, option_id: int, replace_with: int | Unset = UNSET, jql: str | Unset = UNSET, override_screen_security: bool | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> None:
        """
        Replace issue field option

        Deselects an issue-field select-list option from all issues where it is selected. A different option can be selected to replace the deselected option. The update can also be limited to a smaller set of issues by using a JQL query.

        Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

        This is an [asynchronous operation](#async). The response object contains a link to the long-running task.

        Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
        """
        self._runtime.call('replace_issue_field_option', call_args({'replace_with': replace_with, 'jql': jql, 'override_screen_security': override_screen_security, 'override_editable_flag': override_editable_flag, 'field_key': field_key, 'option_id': option_id}))

class _IssueCustomFieldValuesAppsResource:
    """Operations under ``issue_custom_field_values_apps``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def update_multiple_custom_field_values(self, *, generate_changelog: bool | Unset = UNSET, generate_app_events: bool | Unset = UNSET, updates: builtins.list[_t.MultipleCustomFieldValuesUpdate] | Unset = UNSET) -> Any:
        """
        Update custom fields

        Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request.

        Apps can only perform this operation on [custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) and [custom field types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) declared in their own manifests.

        **[Permissions](#permissions) required:** Only the app that owns the custom field or custom field type can update its values with this operation.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('Any', self._runtime.call('update_multiple_custom_field_values', call_args({'generate_changelog': generate_changelog, 'generate_app_events': generate_app_events}, {'body': {'updates': updates}})))

    def update_custom_field_value(self, *, field_id_or_key: str, generate_changelog: bool | Unset = UNSET, generate_app_events: bool | Unset = UNSET, updates: builtins.list[_t.CustomFieldValueUpdate] | Unset = UNSET) -> Any:
        """
        Update custom field value

        Updates the value of a custom field on one or more issues.

        Apps can only perform this operation on [custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) and [custom field types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) declared in their own manifests.

        **[Permissions](#permissions) required:** Only the app that owns the custom field or custom field type can update its values with this operation.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('Any', self._runtime.call('update_custom_field_value', call_args({'field_id_or_key': field_id_or_key, 'generate_changelog': generate_changelog, 'generate_app_events': generate_app_events}, {'body': {'updates': updates}})))

class _IssueFieldConfigurationsResource:
    """Operations under ``issue_field_configurations``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_all_field_configurations(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, is_default: bool | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBeanFieldConfigurationDetails:
        """
        Get all field configurations

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Returns a [paginated](#pagination) list of field configurations. The list can be for all field configurations or a subset determined by any combination of these criteria:

         *  a list of field configuration item IDs.
         *  whether the field configuration is a default.
         *  whether the field configuration name or description contains a query string.

        Only field configurations used in company-managed (classic) projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanFieldConfigurationDetails', self._runtime.call('get_all_field_configurations', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'is_default': is_default, 'query': query})))

    def create_field_configuration(self, *, name: str, description: str | Unset = UNSET) -> _t.FieldConfiguration:
        """
        Create field configuration

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Creates a field configuration. The field configuration is created with the same field properties as the default configuration, with all the fields being optional.

        This operation can only create configurations for use in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.FieldConfiguration', self._runtime.call('create_field_configuration', call_args({}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def update_field_configuration(self, *, id: int, name: str, description: str | Unset = UNSET) -> Any:
        """
        Update field configuration

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Updates a field configuration. The name and the description provided in the request override the existing values.

        This operation can only update configurations used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('update_field_configuration', call_args({'id': id}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def delete_field_configuration(self, *, id: int) -> Any:
        """
        Delete field configuration

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Deletes a field configuration.

        This operation can only delete configurations used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('delete_field_configuration', call_args({'id': id})))

    def list_field_configuration_items(self, *, id: int, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanFieldConfigurationItem:
        """
        Get field configuration items

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Returns a [paginated](#pagination) list of all fields for a configuration.

        Only the fields from configurations used in company-managed (classic) projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanFieldConfigurationItem', self._runtime.call('get_field_configuration_items', call_args({'id': id, 'start_at': start_at, 'max_results': max_results})))

    def update_field_configuration_items(self, *, id: int, field_configuration_items: builtins.list[_t.FieldConfigurationItem]) -> Any:
        """
        Update field configuration items

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Updates fields in a field configuration. The properties of the field configuration fields provided override the existing values.

        This operation can only update field configurations used in company-managed (classic) projects.

        The operation can set the renderer for text fields to the default text renderer (`text-renderer`) or wiki style renderer (`wiki-renderer`). However, the renderer cannot be updated for fields using the autocomplete renderer (`autocomplete-renderer`).

        Hiding a field deletes it from the field configuration - deleting the required, description and renderer type values as well. As a result, hiding and unhiding will not restore the other values but use their default values.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('update_field_configuration_items', call_args({'id': id}, {'body': {'field_configuration_items': field_configuration_items}}, required=frozenset({'body'}))))

    def list_all_field_configuration_schemes(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET) -> _t.PageBeanFieldConfigurationScheme:
        """
        Get all field configuration schemes

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Returns a [paginated](#pagination) list of field configuration schemes.

        Only field configuration schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanFieldConfigurationScheme', self._runtime.call('get_all_field_configuration_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id})))

    def create_field_configuration_scheme(self, *, name: str, description: str | Unset = UNSET) -> _t.FieldConfigurationScheme:
        """
        Create field configuration scheme

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Creates a field configuration scheme.

        This operation can only create field configuration schemes used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.FieldConfigurationScheme', self._runtime.call('create_field_configuration_scheme', call_args({}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def list_field_configuration_scheme_mappings(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, field_configuration_scheme_id: builtins.list[int] | Unset = UNSET) -> _t.PageBeanFieldConfigurationIssueTypeItem:
        """
        Get field configuration issue type items

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Returns a [paginated](#pagination) list of field configuration issue type items.

        Only items used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanFieldConfigurationIssueTypeItem', self._runtime.call('get_field_configuration_scheme_mappings', call_args({'start_at': start_at, 'max_results': max_results, 'field_configuration_scheme_id': field_configuration_scheme_id})))

    def get_field_configuration_scheme_project_mapping(self, *, project_id: builtins.list[int], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanFieldConfigurationSchemeProjects:
        """
        Get field configuration schemes for projects

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list of the projects that use it.

        The list is sorted by field configuration scheme ID. The first item contains the list of project IDs assigned to the default field configuration scheme.

        Only field configuration schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanFieldConfigurationSchemeProjects', self._runtime.call('get_field_configuration_scheme_project_mapping', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id})))

    def assign_field_configuration_scheme_to_project(self, *, project_id: str, field_configuration_scheme_id: str | Unset = UNSET) -> Any:
        """
        Assign field configuration scheme to project

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Assigns a field configuration scheme to a project. If the field configuration scheme ID is `null`, the operation assigns the default field configuration scheme.

        Field configuration schemes can only be assigned to classic projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('assign_field_configuration_scheme_to_project', call_args({}, {'body': {'field_configuration_scheme_id': field_configuration_scheme_id, 'project_id': project_id}}, required=frozenset({'body'}))))

    def update_field_configuration_scheme(self, *, id: int, name: str, description: str | Unset = UNSET) -> Any:
        """
        Update field configuration scheme

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Updates a field configuration scheme.

        This operation can only update field configuration schemes used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('update_field_configuration_scheme', call_args({'id': id}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def delete_field_configuration_scheme(self, *, id: int) -> Any:
        """
        Delete field configuration scheme

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Deletes a field configuration scheme.

        This operation can only delete field configuration schemes used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('delete_field_configuration_scheme', call_args({'id': id})))

    def set_field_configuration_scheme_mapping(self, *, id: int, mappings: builtins.list[_t.FieldConfigurationToIssueTypeMapping]) -> Any:
        """
        Assign issue types to field configurations

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Assigns issue types to field configurations on field configuration scheme.

        This operation can only modify field configuration schemes used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('set_field_configuration_scheme_mapping', call_args({'id': id}, {'body': {'mappings': mappings}}, required=frozenset({'body'}))))

    def remove_issue_types_from_global_field_configuration_scheme(self, *, id: int, issue_type_ids: builtins.list[str]) -> Any:
        """
        Remove issue types from field configuration scheme

        Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

        Removes issue types from the field configuration scheme.

        This operation can only modify field configuration schemes used in company-managed (classic) projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('Any', self._runtime.call('remove_issue_types_from_global_field_configuration_scheme', call_args({'id': id}, {'body': {'issue_type_ids': issue_type_ids}}, required=frozenset({'body'}))))

class _IssueFieldsResource:
    """Operations under ``issue_fields``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_fields(self) -> builtins.list[_t.FieldDetails]:
        """
        Get fields

        Returns system and custom issue fields according to the following rules:

         *  Fields that cannot be added to the issue navigator are always returned.
         *  Fields that cannot be placed on an issue screen are always returned.
         *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches.
         *  Fields that are not associated to any used field configurations or screens are not returned.
         *  For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('builtins.list[_t.FieldDetails]', self._runtime.call('get_fields', call_args({})))

    def create_custom_field(self, *, name: str, type_: str, description: str | Unset = UNSET, searcher_key: _t.CustomFieldDefinitionJsonBeanSearcherKey | Unset = UNSET) -> _t.FieldDetails:
        """
        Create custom field

        Creates a custom field.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.FieldDetails', self._runtime.call('create_custom_field', call_args({}, {'body': {'description': description, 'name': name, 'searcher_key': searcher_key, 'type': type_}}, required=frozenset({'body'}))))

    def get_fields_paginated(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, type_: builtins.list[_t.GetFieldsPaginatedTypeItem] | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, query: str | Unset = UNSET, order_by: _t.GetFieldsPaginatedOrderBy | Unset = UNSET, expand: str | Unset = UNSET, project_ids: builtins.list[int] | Unset = UNSET) -> _t.PageBeanField:
        """
        Get fields paginated

        Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

         *  all fields
         *  specific fields, by defining `id`
         *  fields that contain a string in the field name or description, by defining `query`
         *  specific fields that contain a string in the field name or description, by defining `id` and `query`

        Use `type` must be set to `custom` to show custom fields only.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanField', self._runtime.call('get_fields_paginated', call_args({'start_at': start_at, 'max_results': max_results, 'type': type_, 'id': id, 'query': query, 'order_by': order_by, 'expand': expand, 'project_ids': project_ids})))

    def get_trashed_fields_paginated(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, query: str | Unset = UNSET, expand: _t.GetTrashedFieldsPaginatedExpand | Unset = UNSET, order_by: str | Unset = UNSET) -> _t.PageBeanField:
        """
        Get fields in trash paginated

        Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string.

        Only custom fields can be queried, `type` must be set to `custom`.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanField', self._runtime.call('get_trashed_fields_paginated', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'query': query, 'expand': expand, 'order_by': order_by})))

    def update_custom_field(self, *, field_id: str, description: str | Unset = UNSET, name: str | Unset = UNSET, searcher_key: _t.UpdateCustomFieldDetailsSearcherKey | Unset = UNSET) -> Any:
        """
        Update custom field

        Updates a custom field.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_custom_field', call_args({'field_id': field_id}, {'body': {'description': description, 'name': name, 'searcher_key': searcher_key}})))

    def list_field_project_associations(self, *, field_id: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanFieldProjectAssociation:
        """
        Get field project associations

        Returns a [paginated](#pagination) list of project associations for the given custom field. Each association contains the ID of a project the field is associated with.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanFieldProjectAssociation', self._runtime.call('get_field_project_associations', call_args({'field_id': field_id, 'start_at': start_at, 'max_results': max_results})))

    def get_contexts_for_field_deprecated(self, *, field_id: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanContext:
        """
        Get contexts for a field

        Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](#api-rest-api-3-field-fieldId-context-get).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanContext', self._runtime.call('get_contexts_for_field_deprecated', call_args({'field_id': field_id, 'start_at': start_at, 'max_results': max_results})))

    def delete_custom_field(self, *, id: str) -> None:
        """
        Delete custom field

        Deletes a custom field. The custom field is deleted whether it is in the trash or not. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_custom_field', call_args({'id': id}))

    def restore_custom_field(self, *, id: str) -> Any:
        """
        Restore custom field from trash

        Restores a custom field from trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('restore_custom_field', call_args({'id': id})))

    def trash_custom_field(self, *, id: str) -> Any:
        """
        Move custom field to trash

        Moves a custom field to trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('trash_custom_field', call_args({'id': id})))

    def list_project_fields(self, *, project_id: builtins.list[int], work_type_id: builtins.list[int], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, field_id: builtins.list[str] | Unset = UNSET) -> _t.PageBean2ProjectFieldBean:
        """
        Get fields for projects

        Returns a [paginated](#pagination) list of fields for the requested projects and work types.

        Only fields that are available for the specified combination of projects and work types are returned. This endpoint allows filtering to specific fields if field IDs are provided.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBean2ProjectFieldBean', self._runtime.call('get_project_fields', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id, 'work_type_id': work_type_id, 'field_id': field_id})))

class _IssueLinkTypesResource:
    """Operations under ``issue_link_types``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self) -> _t.IssueLinkTypes:
        """
        Get issue link types

        Returns a list of all issue link types.

        To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
        """
        return cast('_t.IssueLinkTypes', self._runtime.call('get_issue_link_types', call_args({})))

    def create(self, *, id: str | Unset = UNSET, inward: str | Unset = UNSET, name: str | Unset = UNSET, outward: str | Unset = UNSET, self_: str | Unset = UNSET) -> _t.IssueLinkType:
        """
        Create issue link type

        Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link's inward and outward relationships.

        To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueLinkType', self._runtime.call('create_issue_link_type', call_args({}, {'body': {'id': id, 'inward': inward, 'name': name, 'outward': outward, 'self': self_}})))

    def get(self, *, issue_link_type_id: str) -> _t.IssueLinkType:
        """
        Get issue link type

        Returns an issue link type.

        To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
        """
        return cast('_t.IssueLinkType', self._runtime.call('get_issue_link_type', call_args({'issue_link_type_id': issue_link_type_id})))

    def update(self, *, issue_link_type_id: str, id: str | Unset = UNSET, inward: str | Unset = UNSET, name: str | Unset = UNSET, outward: str | Unset = UNSET, self_: str | Unset = UNSET) -> _t.IssueLinkType:
        """
        Update issue link type

        Updates an issue link type.

        To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueLinkType', self._runtime.call('update_issue_link_type', call_args({'issue_link_type_id': issue_link_type_id}, {'body': {'id': id, 'inward': inward, 'name': name, 'outward': outward, 'self': self_}})))

    def delete(self, *, issue_link_type_id: str) -> None:
        """
        Delete issue link type

        Deletes an issue link type.

        To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_issue_link_type', call_args({'issue_link_type_id': issue_link_type_id}))

class _IssueLinksResource:
    """Operations under ``issue_links``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def link_issues(self, *, inward_issue: _t.LinkedIssue, outward_issue: _t.LinkedIssue, type_: _t.IssueLinkType, comment: _t.Comment | Unset = UNSET) -> Any:
        """
        Create issue link

        Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

        This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

        If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked,
         *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue,
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('Any', self._runtime.call('link_issues', call_args({}, {'body': {'comment': comment, 'inward_issue': inward_issue, 'outward_issue': outward_issue, 'type': type_}}, required=frozenset({'body'}))))

    def get(self, *, link_id: str) -> _t.IssueLink:
        """
        Get issue link

        Returns an issue link.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.
        """
        return cast('_t.IssueLink', self._runtime.call('get_issue_link', call_args({'link_id': link_id})))

    def delete(self, *, link_id: str) -> None:
        """
        Delete issue link

        Deletes an issue link.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link.
         *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.
        """
        self._runtime.call('delete_issue_link', call_args({'link_id': link_id}))

class _IssueNavigatorSettingsResource:
    """Operations under ``issue_navigator_settings``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_issue_navigator_default_columns(self) -> builtins.list[_t.ColumnItem]:
        """
        Get issue navigator default columns

        Returns the default issue navigator columns.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ColumnItem]', self._runtime.call('get_issue_navigator_default_columns', call_args({})))

    def set_issue_navigator_default_columns(self, *, columns: builtins.list[str] | Unset = UNSET) -> None:
        """
        Set issue navigator default columns

        Sets the default issue navigator columns.

        The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple `columns` parameters. For example, in curl:

        `curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/settings/columns`

        If no column details are sent, then all default columns are removed.

        A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get fields](#api-rest-api-3-field-get).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('set_issue_navigator_default_columns', call_args({}, {'body': {'columns': columns}}))

class _IssueNotificationSchemesResource:
    """Operations under ``issue_notification_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_notification_schemes(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET, only_default: bool | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanNotificationScheme:
        """
        Get notification schemes paginated

        Returns a [paginated](#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

        *Note that you should allow for events without recipients to appear in responses.*

        **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.
        """
        return cast('_t.PageBeanNotificationScheme', self._runtime.call('get_notification_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'project_id': project_id, 'only_default': only_default, 'expand': expand})))

    def create_notification_scheme(self, *, name: str, description: str | Unset = UNSET, notification_scheme_events: builtins.list[_t.NotificationSchemeEventDetails] | Unset = UNSET) -> _t.NotificationSchemeId:
        """
        Create notification scheme

        Creates a notification scheme with notifications. You can create up to 1000 notifications per request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.NotificationSchemeId', self._runtime.call('create_notification_scheme', call_args({}, {'body': {'description': description, 'name': name, 'notification_scheme_events': notification_scheme_events}}, required=frozenset({'body'}))))

    def list_notification_scheme_to_project_mappings(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, notification_scheme_id: builtins.list[str] | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET) -> _t.PageBeanNotificationSchemeAndProjectMappingJsonBean:
        """
        Get projects using notification schemes paginated

        Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don't have a concept of a default notification scheme. The mappings are ordered by projectId.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanNotificationSchemeAndProjectMappingJsonBean', self._runtime.call('get_notification_scheme_to_project_mappings', call_args({'start_at': start_at, 'max_results': max_results, 'notification_scheme_id': notification_scheme_id, 'project_id': project_id})))

    def get_notification_scheme(self, *, id: int, expand: str | Unset = UNSET) -> _t.NotificationScheme:
        """
        Get notification scheme

        Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events.

        **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.
        """
        return cast('_t.NotificationScheme', self._runtime.call('get_notification_scheme', call_args({'id': id, 'expand': expand})))

    def update_notification_scheme(self, *, id: str, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update notification scheme

        Updates a notification scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_notification_scheme', call_args({'id': id}, {'body': {'description': description, 'name': name}})))

    def add_notifications(self, *, id: str, notification_scheme_events: builtins.list[_t.NotificationSchemeEventDetails]) -> Any:
        """
        Add notifications to notification scheme

        Adds notifications to a notification scheme. You can add up to 1000 notifications per request.

        *Deprecated: The notification type `EmailAddress` is no longer supported in Cloud. Refer to the [changelog](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1031) for more details.*

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_notifications', call_args({'id': id}, {'body': {'notification_scheme_events': notification_scheme_events}}, required=frozenset({'body'}))))

    def delete_notification_scheme(self, *, notification_scheme_id: str) -> Any:
        """
        Delete notification scheme

        Deletes a notification scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_notification_scheme', call_args({'notification_scheme_id': notification_scheme_id})))

    def remove_notification_from_notification_scheme(self, *, notification_scheme_id: str, notification_id: str) -> Any:
        """
        Remove notification from notification scheme

        Removes a notification from a notification scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_notification_from_notification_scheme', call_args({'notification_scheme_id': notification_scheme_id, 'notification_id': notification_id})))

class _IssuePanelsResource:
    """Operations under ``issue_panels``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def bulk_pin_unpin_projects_async(self, *, module_id: str, project_list: builtins.list[_t.ProjectPinAction]) -> _t.ForgePanelProjectPinAsyncResponse:
        """
        Bulk pin or unpin issue panel to projects

        Bulk pin or unpin an issue panel (added by a Forge app) to or from multiple projects.

        The operation runs asynchronously. The response includes a task ID - use the [Get task](#api-rest-api-3-task-taskId-get) endpoint to check progress.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ForgePanelProjectPinAsyncResponse', self._runtime.call('bulk_pin_unpin_projects_async', call_args({}, {'body': {'module_id': module_id, 'project_list': project_list}}, required=frozenset({'body'}))))

    def get_bulk_pin_status(self, *, module_id: str, project_list: builtins.list[str]) -> _t.ForgePanelProjectPinStatusResponse:
        """
        Get issue panel pin status for projects

        Get the pin status of an issue panel (added by a Forge app) for multiple projects.

        The operation is read-only and runs synchronously. Projects that do not exist, or that you do not have permission to access, are returned in the response with the panel reported as not pinned and the reason in the `error` field; the request itself still succeeds.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ForgePanelProjectPinStatusResponse', self._runtime.call('get_bulk_pin_status', call_args({}, {'body': {'module_id': module_id, 'project_list': project_list}}, required=frozenset({'body'}))))

class _IssuePrioritiesResource:
    """Operations under ``issue_priorities``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_priorities(self) -> builtins.list[_t.Priority]:
        """
        Get priorities

        Returns the list of all issue priorities.

        **Deprecated:** Use [Search priorities](#api-rest-api-3-priority-search-get) instead. **[Permissions](#permissions) required:** Permission to access Jira.

        Deprecated.
        """
        return cast('builtins.list[_t.Priority]', self._runtime.call('get_priorities', call_args({})))

    def create_priority(self, *, name: str, status_color: str, avatar_id: int | Unset = UNSET, description: str | None | Unset = UNSET, icon_url: _t.CreatePriorityDetailsIconUrl | None | Unset = UNSET) -> _t.PriorityId:
        """
        Create priority

        Creates an issue priority.

        **Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PriorityId', self._runtime.call('create_priority', call_args({}, {'body': {'avatar_id': avatar_id, 'description': description, 'icon_url': icon_url, 'name': name, 'status_color': status_color}}, required=frozenset({'body'}))))

    def set_default_priority(self, *, id: str) -> Any:
        """
        Set default priority

        Sets default issue priority.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('set_default_priority', call_args({}, {'body': {'id': id}}, required=frozenset({'body'}))))

    def move_priorities(self, *, ids: builtins.list[str], after: str | Unset = UNSET, position: str | Unset = UNSET) -> Any:
        """
        Move priorities

        Changes the order of issue priorities.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('move_priorities', call_args({}, {'body': {'after': after, 'ids': ids, 'position': position}}, required=frozenset({'body'}))))

    def search_priorities(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET, priority_name: str | Unset = UNSET, only_default: bool | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanPriority:
        """
        Search priorities

        Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:

         *  a list of priority IDs. Any invalid priority IDs are ignored.
         *  a list of project IDs. Only priorities that are available in these projects will be returned. Any invalid project IDs are ignored.
         *  whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.

        **Deprecation notice:** The `onlyDefault` parameter is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

        **Deprecation notice:** The `isDefault` property of priorities is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanPriority', self._runtime.call('search_priorities', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'project_id': project_id, 'priority_name': priority_name, 'only_default': only_default, 'expand': expand})))

    def get_priority(self, *, id: str) -> _t.Priority:
        """
        Get priority

        Returns an issue priority. To fetch multiple priorities at once, use [Search priorities](#api-rest-api-3-priority-search-get) instead.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.Priority', self._runtime.call('get_priority', call_args({'id': id})))

    def update_priority(self, *, id: str, avatar_id: int | Unset = UNSET, description: str | None | Unset = UNSET, icon_url: _t.UpdatePriorityDetailsIconUrl | None | Unset = UNSET, name: str | None | Unset = UNSET, status_color: str | None | Unset = UNSET) -> Any:
        """
        Update priority

        Updates an issue priority.

        At least one request body parameter must be defined.

        **Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_priority', call_args({'id': id}, {'body': {'avatar_id': avatar_id, 'description': description, 'icon_url': icon_url, 'name': name, 'status_color': status_color}})))

    def delete_priority(self, *, id: str) -> None:
        """
        Delete priority

        Deletes an issue priority.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_priority', call_args({'id': id}))

class _IssuePropertiesResource:
    """Operations under ``issue_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def bulk_set_issues_properties_list(self, *, entities_ids: builtins.list[int] | Unset = UNSET, properties: builtins.dict[str, _t.JsonNode] | Unset = UNSET) -> None:
        """
        Bulk set issues properties by list

        Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously.

        This operation is:

         *  transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated.
         *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('bulk_set_issues_properties_list', call_args({}, {'body': {'entities_ids': entities_ids, 'properties': properties}}))

    def bulk_by_issue(self, *, issues: builtins.list[_t.IssueEntityPropertiesForMultiUpdate] | Unset = UNSET) -> None:
        """
        Bulk set issue properties by issue

        Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.

        This operation is:

         *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.
         *  non-transactional. Updating some entities may fail. Such information will available in the task result.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('bulk_set_issue_properties_by_issue', call_args({}, {'body': {'issues': issues}}))

    def bulk_set(self, *, property_key: str, expression: str | Unset = UNSET, filter: _t.IssueFilterForBulkPropertySet | Unset = UNSET, value: Any | Unset = UNSET) -> None:
        """
        Bulk set issue property

        Sets a property value on multiple issues.

        The value set can be a constant or determined by a [Jira expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must be computable with constant complexity when applied to a set of issues. Expressions must also comply with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions) that apply to all Jira expressions.

        The issues to be updated can be specified by a filter.

        The filter identifies issues eligible for update using these criteria:

         *  `entityIds` Only issues from this list are eligible.
         *  `currentValue` Only issues with the property set to this value are eligible.
         *  `hasProperty`:
            
             *  If *true*, only issues with the property are eligible.
             *  If *false*, only issues without the property are eligible.

        If more than one criteria is specified, they are joined with the logical *AND*: only issues that satisfy all criteria are eligible.

        If an invalid combination of criteria is provided, an error is returned. For example, specifying a `currentValue` and `hasProperty` as *false* would not match any issues (because without the property the property cannot have a value).

        The filter is optional. Without the filter all the issues visible to the user and where the user has the EDIT\\_ISSUES permission for the issue are considered eligible.

        This operation is:

         *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
         *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.
        """
        self._runtime.call('bulk_set_issue_property', call_args({'property_key': property_key}, {'body': {'expression': expression, 'filter': filter, 'value': value}}))

    def bulk_delete(self, *, property_key: str, current_value: Any | Unset = UNSET, entity_ids: builtins.list[int] | Unset = UNSET) -> None:
        """
        Bulk delete issue property

        Deletes a property value from multiple issues. The issues to be updated can be specified by filter criteria.

        The criteria the filter used to identify eligible issues are:

         *  `entityIds` Only issues from this list are eligible.
         *  `currentValue` Only issues with the property set to this value are eligible.

        If both criteria is specified, they are joined with the logical *AND*: only issues that satisfy both criteria are considered eligible.

        If no filter criteria are specified, all the issues visible to the user and where the user has the EDIT\\_ISSUES permission for the issue are considered eligible.

        This operation is:

         *  transactional, either the property is deleted from all eligible issues or, when errors occur, no properties are deleted.
         *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [ project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.
        """
        self._runtime.call('bulk_delete_issue_property', call_args({'property_key': property_key}, {'body': {'current_value': current_value, 'entity_ids': entity_ids}}))

    def list_keys(self, *, issue_id_or_key: str) -> _t.PropertyKeys:
        """
        Get issue property keys

        Returns the URLs and keys of an issue's properties.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Property details are only returned where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_issue_property_keys', call_args({'issue_id_or_key': issue_id_or_key})))

    def get(self, *, issue_id_or_key: str, property_key: str) -> _t.EntityProperty:
        """
        Get issue property

        Returns the key and value of an issue's property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_issue_property', call_args({'issue_id_or_key': issue_id_or_key, 'property_key': property_key})))

    def set(self, *, issue_id_or_key: str, property_key: str, body: Any) -> Any:
        """
        Set issue property

        Sets the value of an issue's property. Use this resource to store custom data against an issue.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('set_issue_property', call_args({'issue_id_or_key': issue_id_or_key, 'property_key': property_key, 'body': body})))

    def delete(self, *, issue_id_or_key: str, property_key: str) -> None:
        """
        Delete issue property

        Deletes an issue's property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('delete_issue_property', call_args({'issue_id_or_key': issue_id_or_key, 'property_key': property_key}))

class _IssueRedactionResource:
    """Operations under ``issue_redaction``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def redact(self, *, redactions: builtins.list[_t.SingleRedactionRequest] | Unset = UNSET) -> str:
        """
        Redact

        Submit a job to redact issue field data. This will trigger the redaction of the data in the specified fields asynchronously.

        The redaction status can be polled using the job id.
        """
        return cast('str', self._runtime.call('redact', call_args({}, {'body': {'redactions': redactions}})))

    def get_redaction_status(self, *, job_id: str) -> _t.RedactionJobStatusResponse:
        """
        Get redaction status

        Retrieves the current status of a redaction job ID.

        The jobStatus will be one of the following:

         *  IN\\_PROGRESS - The redaction job is currently in progress
         *  COMPLETED - The redaction job has completed successfully.
         *  PENDING - The redaction job has not started yet
        """
        return cast('_t.RedactionJobStatusResponse', self._runtime.call('get_redaction_status', call_args({'job_id': job_id})))

class _IssueRemoteLinksResource:
    """Operations under ``issue_remote_links``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_remote_issue_links(self, *, issue_id_or_key: str, global_id: str | Unset = UNSET) -> _t.GetRemoteIssueLinksResponse:
        """
        Get remote issue links

        Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.GetRemoteIssueLinksResponse', self._runtime.call('get_remote_issue_links', call_args({'issue_id_or_key': issue_id_or_key, 'global_id': global_id})))

    def create_or_update_remote_issue_link(self, *, issue_id_or_key: str, object: _t.RemoteObject, application: _t.Application | Unset = UNSET, global_id: str | Unset = UNSET, relationship: str | Unset = UNSET) -> _t.RemoteIssueLinkIdentifies:
        """
        Create or update remote issue link

        Creates or updates a remote issue link for an issue.

        If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.RemoteIssueLinkIdentifies', self._runtime.call('create_or_update_remote_issue_link', call_args({'issue_id_or_key': issue_id_or_key}, {'body': {'application': application, 'global_id': global_id, 'object': object, 'relationship': relationship}}, required=frozenset({'body'}))))

    def delete_remote_issue_link_by_global_id(self, *, issue_id_or_key: str, global_id: str) -> None:
        """
        Delete remote issue link by global ID

        Deletes the remote issue link from the issue using the link's global ID. Where the global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is implemented, issue-level security permission to view the issue.
        """
        self._runtime.call('delete_remote_issue_link_by_global_id', call_args({'issue_id_or_key': issue_id_or_key, 'global_id': global_id}))

    def get_remote_issue_link(self, *, issue_id_or_key: str, link_id: str) -> _t.RemoteIssueLink:
        """
        Get remote issue link by ID

        Returns a remote issue link for an issue.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.RemoteIssueLink', self._runtime.call('get_remote_issue_link_by_id', call_args({'issue_id_or_key': issue_id_or_key, 'link_id': link_id})))

    def update_remote_issue_link(self, *, issue_id_or_key: str, link_id: str, object: _t.RemoteObject, application: _t.Application | Unset = UNSET, global_id: str | Unset = UNSET, relationship: str | Unset = UNSET) -> Any:
        """
        Update remote issue link by ID

        Updates a remote issue link for an issue.

        Note: Fields without values in the request are set to null.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('update_remote_issue_link', call_args({'issue_id_or_key': issue_id_or_key, 'link_id': link_id}, {'body': {'application': application, 'global_id': global_id, 'object': object, 'relationship': relationship}}, required=frozenset({'body'}))))

    def delete_remote_issue_link(self, *, issue_id_or_key: str, link_id: str) -> None:
        """
        Delete remote issue link by ID

        Deletes a remote issue link from an issue.

        This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects*, *Edit issues*, and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('delete_remote_issue_link_by_id', call_args({'issue_id_or_key': issue_id_or_key, 'link_id': link_id}))

class _IssueResolutionsResource:
    """Operations under ``issue_resolutions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_resolutions(self) -> builtins.list[_t.Resolution]:
        """
        Get resolutions

        Returns a list of all issue resolution values.

        **[Permissions](#permissions) required:** Permission to access Jira.

        Deprecated.
        """
        return cast('builtins.list[_t.Resolution]', self._runtime.call('get_resolutions', call_args({})))

    def create_resolution(self, *, name: str, description: str | Unset = UNSET) -> _t.ResolutionId:
        """
        Create resolution

        Creates an issue resolution.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ResolutionId', self._runtime.call('create_resolution', call_args({}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def set_default_resolution(self, *, id: str) -> Any:
        """
        Set default resolution

        Sets default issue resolution.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('set_default_resolution', call_args({}, {'body': {'id': id}}, required=frozenset({'body'}))))

    def move_resolutions(self, *, ids: builtins.list[str], after: str | Unset = UNSET, position: str | Unset = UNSET) -> Any:
        """
        Move resolutions

        Changes the order of issue resolutions.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('move_resolutions', call_args({}, {'body': {'after': after, 'ids': ids, 'position': position}}, required=frozenset({'body'}))))

    def search_resolutions(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, only_default: bool | Unset = UNSET) -> _t.PageBeanResolutionJsonBean:
        """
        Search resolutions

        Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:

         *  a list of resolutions IDs.
         *  whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanResolutionJsonBean', self._runtime.call('search_resolutions', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'only_default': only_default})))

    def get_resolution(self, *, id: str) -> _t.Resolution:
        """
        Get resolution

        Returns an issue resolution value.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.Resolution', self._runtime.call('get_resolution', call_args({'id': id})))

    def update_resolution(self, *, id: str, name: str, description: str | Unset = UNSET) -> Any:
        """
        Update resolution

        Updates an issue resolution.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_resolution', call_args({'id': id}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def delete_resolution(self, *, id: str, replace_with: str) -> None:
        """
        Delete resolution

        Deletes an issue resolution.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_resolution', call_args({'id': id, 'replace_with': replace_with}))

class _IssueSearchResource:
    """Operations under ``issue_search``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_issue_picker_resource(self, *, query: str | Unset = UNSET, current_jql: str | Unset = UNSET, current_issue_key: str | Unset = UNSET, current_project_id: str | Unset = UNSET, show_sub_tasks: bool | Unset = UNSET, show_sub_task_parent: bool | Unset = UNSET) -> _t.IssuePickerSuggestions:
        """
        Get issue picker suggestions

        Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string.

        This operation returns two lists:

         *  `History Search` which includes issues from the user's history of created, edited, or viewed issues that contain the string in the `query` parameter.
         *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain the string in the `query` parameter.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.IssuePickerSuggestions', self._runtime.call('get_issue_picker_resource', call_args({'query': query, 'current_jql': current_jql, 'current_issue_key': current_issue_key, 'current_project_id': current_project_id, 'show_sub_tasks': show_sub_tasks, 'show_sub_task_parent': show_sub_task_parent})))

    def match_issues(self, *, issue_ids: builtins.list[int], jqls: builtins.list[str]) -> _t.IssueMatches:
        """
        Check issues against JQL

        Checks whether one or more issues would be returned by one or more JQL queries. Up to 10 JQL queries can be specified and up to 50 issue IDs included in the request.

        **[Permissions](#permissions) required:** None, however, issues are only matched against JQL queries where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.IssueMatches', self._runtime.call('match_issues', call_args({}, {'body': {'issue_ids': issue_ids, 'jqls': jqls}}, required=frozenset({'body'}))))

    def count_issues(self, *, jql: str | Unset = UNSET) -> _t.JqlCountResultsBean:
        """
        Count issues using JQL

        Provide an estimated count of the issues that match the [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned output. This endpoint requires JQL to be bounded.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Issues are included in the response where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.JqlCountResultsBean', self._runtime.call('count_issues', call_args({}, {'body': {'jql': jql}})))

    def search_issues(self, *, jql: str | Unset = UNSET, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET, fields: builtins.list[str] | Unset = UNSET, expand: str | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET, fields_by_keys: bool | Unset = UNSET, fail_fast: bool | Unset = UNSET, reconcile_issues: builtins.list[int] | Unset = UNSET, include_archived_projects: bool | Unset = UNSET) -> _t.SearchAndReconcileResults:
        """
        Search for issues using JQL enhanced search (GET)

        Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned search results. If you need [read-after-write](https://developer.atlassian.com/cloud/jira/platform/search-and-reconcile/) consistency, you can utilize the `reconcileIssues` parameter to ensure stronger consistency assurances. This operation can be accessed anonymously.

        If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-rest-api-3-search-post) version of this resource.

        **[Permissions](#permissions) required:** Issues are included in the response where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SearchAndReconcileResults', self._runtime.call('search_issues', call_args({'jql': jql, 'next_page_token': next_page_token, 'max_results': max_results, 'fields': fields, 'expand': expand, 'properties': properties, 'fields_by_keys': fields_by_keys, 'fail_fast': fail_fast, 'reconcile_issues': reconcile_issues, 'include_archived_projects': include_archived_projects})))

    def search_issues_post(self, *, expand: str | Unset = UNSET, fields: builtins.list[str] | Unset = UNSET, fields_by_keys: bool | Unset = UNSET, include_archived_projects: bool | Unset = UNSET, jql: str | Unset = UNSET, max_results: int | Unset = UNSET, next_page_token: str | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET, reconcile_issues: builtins.list[int] | Unset = UNSET) -> _t.SearchAndReconcileResults:
        """
        Search for issues using JQL enhanced search (POST)

        Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned search results. If you need [read-after-write](https://developer.atlassian.com/cloud/jira/platform/search-and-reconcile/) consistency, you can utilize the `reconcileIssues` parameter to ensure stronger consistency assurances. This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Issues are included in the response where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.SearchAndReconcileResults', self._runtime.call('search_issues_post', call_args({}, {'body': {'expand': expand, 'fields': fields, 'fields_by_keys': fields_by_keys, 'include_archived_projects': include_archived_projects, 'jql': jql, 'max_results': max_results, 'next_page_token': next_page_token, 'properties': properties, 'reconcile_issues': reconcile_issues}})))

class _IssueSecurityLevelResource:
    """Operations under ``issue_security_level``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_members(self, *, issue_security_scheme_id: int, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, issue_security_level_id: builtins.list[str] | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanIssueSecurityLevelMember:
        """
        Get issue security level members by issue security scheme

        Returns issue security level members.

        Only issue security level members in context of classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueSecurityLevelMember', self._runtime.call('get_issue_security_level_members', call_args({'issue_security_scheme_id': issue_security_scheme_id, 'start_at': start_at, 'max_results': max_results, 'issue_security_level_id': issue_security_level_id, 'expand': expand})))

    def get(self, *, id: str) -> _t.SecurityLevel:
        """
        Get issue security level

        Returns details of an issue security level.

        Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.SecurityLevel', self._runtime.call('get_issue_security_level', call_args({'id': id})))

class _IssueSecuritySchemesResource:
    """Operations under ``issue_security_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self) -> _t.SecuritySchemes:
        """
        Get issue security schemes

        Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.SecuritySchemes', self._runtime.call('get_issue_security_schemes', call_args({})))

    def create(self, *, name: str, description: str | Unset = UNSET, levels: builtins.list[_t.SecuritySchemeLevelBean] | Unset = UNSET) -> _t.SecuritySchemeId:
        """
        Create issue security scheme

        Creates a security scheme with security scheme levels and levels' members. You can create up to 100 security scheme levels and security scheme levels' members per request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.SecuritySchemeId', self._runtime.call('create_issue_security_scheme', call_args({}, {'body': {'description': description, 'levels': levels, 'name': name}}, required=frozenset({'body'}))))

    def list_security_levels(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, scheme_id: builtins.list[str] | Unset = UNSET, only_default: bool | Unset = UNSET) -> _t.PageBeanSecurityLevel:
        """
        Get issue security levels

        Returns a [paginated](#pagination) list of issue security levels.

        Only issue security levels in the context of classic projects are returned.

        Filtering using IDs is inclusive: if you specify both security scheme IDs and level IDs, the result will include both specified issue security levels and all issue security levels from the specified schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanSecurityLevel', self._runtime.call('get_security_levels', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'scheme_id': scheme_id, 'only_default': only_default})))

    def set_default_levels(self, *, default_values: builtins.list[_t.DefaultLevelValue]) -> Any:
        """
        Set default issue security levels

        Sets default issue security levels for schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('set_default_levels', call_args({}, {'body': {'default_values': default_values}}, required=frozenset({'body'}))))

    def list_security_level_members(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, scheme_id: builtins.list[str] | Unset = UNSET, level_id: builtins.list[str] | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanSecurityLevelMember:
        """
        Get issue security level members

        Returns a [paginated](#pagination) list of issue security level members.

        Only issue security level members in the context of classic projects are returned.

        Filtering using parameters is inclusive: if you specify both security scheme IDs and level IDs, the result will include all issue security level members from the specified schemes and levels.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanSecurityLevelMember', self._runtime.call('get_security_level_members', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'scheme_id': scheme_id, 'level_id': level_id, 'expand': expand})))

    def search_projects_using_security_schemes(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, issue_security_scheme_id: builtins.list[str] | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET) -> _t.PageBeanIssueSecuritySchemeToProjectMapping:
        """
        Get projects using issue security schemes

        Returns a [paginated](#pagination) mapping of projects that are using security schemes. You can provide either one or multiple security scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Only issue security schemes in the context of classic projects are supported. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueSecuritySchemeToProjectMapping', self._runtime.call('search_projects_using_security_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'issue_security_scheme_id': issue_security_scheme_id, 'project_id': project_id})))

    def associate_schemes_to_projects(self, *, project_id: str, scheme_id: str, old_to_new_security_level_mappings: builtins.list[_t.OldToNewSecurityLevelMappingsBean] | Unset = UNSET) -> None:
        """
        Associate security scheme to project

        Associates an issue security scheme with a project and remaps security levels of issues to the new levels, if provided.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('associate_schemes_to_projects', call_args({}, {'body': {'old_to_new_security_level_mappings': old_to_new_security_level_mappings, 'project_id': project_id, 'scheme_id': scheme_id}}, required=frozenset({'body'})))

    def search_security_schemes(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, id: builtins.list[str] | Unset = UNSET, project_id: builtins.list[str] | Unset = UNSET) -> _t.PageBeanSecuritySchemeWithProjects:
        """
        Search issue security schemes

        Returns a [paginated](#pagination) list of issue security schemes.  
        If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Use \\{@link IssueSecuritySchemeResource\\#searchProjectsUsingSecuritySchemes(String, String, Set, Set)\\} to obtain all projects related to scheme.

        Only issue security schemes in the context of classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanSecuritySchemeWithProjects', self._runtime.call('search_security_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'project_id': project_id})))

    def get(self, *, id: int) -> _t.SecurityScheme:
        """
        Get issue security scheme

        Returns an issue security scheme along with its security levels.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.
        """
        return cast('_t.SecurityScheme', self._runtime.call('get_issue_security_scheme', call_args({'id': id})))

    def update(self, *, id: str, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update issue security scheme

        Updates the issue security scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_issue_security_scheme', call_args({'id': id}, {'body': {'description': description, 'name': name}})))

    def delete_security_scheme(self, *, scheme_id: str) -> Any:
        """
        Delete issue security scheme

        Deletes an issue security scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_security_scheme', call_args({'scheme_id': scheme_id})))

    def add_security_level(self, *, scheme_id: str, levels: builtins.list[_t.SecuritySchemeLevelBean] | Unset = UNSET) -> Any:
        """
        Add issue security levels

        Adds levels and levels' members to the issue security scheme. You can add up to 100 levels per request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_security_level', call_args({'scheme_id': scheme_id}, {'body': {'levels': levels}})))

    def update_security_level(self, *, scheme_id: str, level_id: str, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update issue security level

        Updates the issue security level.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_security_level', call_args({'scheme_id': scheme_id, 'level_id': level_id}, {'body': {'description': description, 'name': name}})))

    def remove_level(self, *, scheme_id: str, level_id: str, replace_with: str | Unset = UNSET) -> None:
        """
        Remove issue security level

        Deletes an issue security level.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('remove_level', call_args({'scheme_id': scheme_id, 'level_id': level_id, 'replace_with': replace_with}))

    def add_security_level_members(self, *, scheme_id: str, level_id: str, members: builtins.list[_t.SecuritySchemeLevelMemberBean] | Unset = UNSET) -> Any:
        """
        Add issue security level members

        Adds members to the issue security level. You can add up to 100 members per request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_security_level_members', call_args({'scheme_id': scheme_id, 'level_id': level_id}, {'body': {'members': members}})))

    def remove_member_from_security_level(self, *, scheme_id: str, level_id: str, member_id: str) -> Any:
        """
        Remove member from issue security level

        Removes an issue security level member from an issue security scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_member_from_security_level', call_args({'scheme_id': scheme_id, 'level_id': level_id, 'member_id': member_id})))

class _IssueTypePropertiesResource:
    """Operations under ``issue_type_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_keys(self, *, issue_type_id: str) -> _t.PropertyKeys:
        """
        Get issue type property keys

        Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.
         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_issue_type_property_keys', call_args({'issue_type_id': issue_type_id})))

    def get(self, *, issue_type_id: str, property_key: str) -> _t.EntityProperty:
        """
        Get issue type property

        Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type.
         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_issue_type_property', call_args({'issue_type_id': issue_type_id, 'property_key': property_key})))

    def set(self, *, issue_type_id: str, property_key: str, body: Any) -> Any:
        """
        Set issue type property

        Creates or updates the value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against an issue type.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('set_issue_type_property', call_args({'issue_type_id': issue_type_id, 'property_key': property_key, 'body': body})))

    def delete(self, *, issue_type_id: str, property_key: str) -> None:
        """
        Delete issue type property

        Deletes the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_issue_type_property', call_args({'issue_type_id': issue_type_id, 'property_key': property_key}))

class _IssueTypeSchemesResource:
    """Operations under ``issue_type_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, order_by: _t.GetAllIssueTypeSchemesOrderBy | Unset = UNSET, expand: str | Unset = UNSET, query_string: str | Unset = UNSET) -> _t.PageBeanIssueTypeScheme:
        """
        Get all issue type schemes

        Returns a [paginated](#pagination) list of issue type schemes.

        Only issue type schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeScheme', self._runtime.call('get_all_issue_type_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'order_by': order_by, 'expand': expand, 'query_string': query_string})))

    def create(self, *, issue_type_ids: builtins.list[str], name: str, default_issue_type_id: str | Unset = UNSET, description: str | Unset = UNSET) -> _t.IssueTypeSchemeId:
        """
        Create issue type scheme

        Creates an issue type scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeSchemeId', self._runtime.call('create_issue_type_scheme', call_args({}, {'body': {'default_issue_type_id': default_issue_type_id, 'description': description, 'issue_type_ids': issue_type_ids, 'name': name}}, required=frozenset({'body'}))))

    def get_mapping(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, issue_type_scheme_id: builtins.list[int] | Unset = UNSET) -> _t.PageBeanIssueTypeSchemeMapping:
        """
        Get issue type scheme items

        Returns a [paginated](#pagination) list of issue type scheme items.

        Only issue type scheme items used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeSchemeMapping', self._runtime.call('get_issue_type_schemes_mapping', call_args({'start_at': start_at, 'max_results': max_results, 'issue_type_scheme_id': issue_type_scheme_id})))

    def list_for_projects(self, *, project_id: builtins.list[int], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanIssueTypeSchemeProjects:
        """
        Get issue type schemes for projects

        Returns a [paginated](#pagination) list of issue type schemes and, for each issue type scheme, a list of the projects that use it.

        Only issue type schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeSchemeProjects', self._runtime.call('get_issue_type_scheme_for_projects', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id})))

    def assign_to_project(self, *, issue_type_scheme_id: str, project_id: str) -> Any:
        """
        Assign issue type scheme to project

        Assigns an issue type scheme to a project.

        If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme.

        Issue type schemes can only be assigned to classic projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('assign_issue_type_scheme_to_project', call_args({}, {'body': {'issue_type_scheme_id': issue_type_scheme_id, 'project_id': project_id}}, required=frozenset({'body'}))))

    def update(self, *, issue_type_scheme_id: int, default_issue_type_id: str | Unset = UNSET, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update issue type scheme

        Updates an issue type scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_issue_type_scheme', call_args({'issue_type_scheme_id': issue_type_scheme_id}, {'body': {'default_issue_type_id': default_issue_type_id, 'description': description, 'name': name}})))

    def delete(self, *, issue_type_scheme_id: int) -> Any:
        """
        Delete issue type scheme

        Deletes an issue type scheme.

        Only issue type schemes used in classic projects can be deleted. Only issue type schemes not associated with a project can be deleted

        A validation error will be returned if the specified scheme is associated with one or more projects. Use [Get issue type scheme API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-get) (with the projects expand, and id query parameter) to get a list of projects. Then, use [Assign issue type scheme to project API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-put) to associate all projects to another scheme before deleting.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_issue_type_scheme', call_args({'issue_type_scheme_id': issue_type_scheme_id})))

    def add(self, *, issue_type_scheme_id: int, issue_type_ids: builtins.list[str]) -> Any:
        """
        Add issue types to issue type scheme

        Adds issue types to an issue type scheme.

        The added issue types are appended to the issue types list.

        If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_issue_types_to_issue_type_scheme', call_args({'issue_type_scheme_id': issue_type_scheme_id}, {'body': {'issue_type_ids': issue_type_ids}}, required=frozenset({'body'}))))

    def reorder(self, *, issue_type_scheme_id: int, issue_type_ids: builtins.list[str], after: str | Unset = UNSET, position: _t.OrderOfIssueTypesPosition | Unset = UNSET) -> Any:
        """
        Change order of issue types

        Changes the order of issue types in an issue type scheme.

        The request body parameters must meet the following requirements:

         *  all of the issue types must belong to the issue type scheme.
         *  either `after` or `position` must be provided.
         *  the issue type in `after` must not be in the issue type list.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('reorder_issue_types_in_issue_type_scheme', call_args({'issue_type_scheme_id': issue_type_scheme_id}, {'body': {'after': after, 'issue_type_ids': issue_type_ids, 'position': position}}, required=frozenset({'body'}))))

    def remove(self, *, issue_type_scheme_id: int, issue_type_id: int) -> Any:
        """
        Remove issue type from issue type scheme

        Removes an issue type from an issue type scheme.

        This operation cannot remove:

         *  any issue type used by issues.
         *  any issue types from the default issue type scheme.
         *  the last standard issue type from an issue type scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_issue_type_from_issue_type_scheme', call_args({'issue_type_scheme_id': issue_type_scheme_id, 'issue_type_id': issue_type_id})))

class _IssueTypeScreenSchemesResource:
    """Operations under ``issue_type_screen_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, query_string: str | Unset = UNSET, order_by: _t.GetIssueTypeScreenSchemesOrderBy | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanIssueTypeScreenScheme:
        """
        Get issue type screen schemes

        Returns a [paginated](#pagination) list of issue type screen schemes.

        Only issue type screen schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeScreenScheme', self._runtime.call('get_issue_type_screen_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'query_string': query_string, 'order_by': order_by, 'expand': expand})))

    def create(self, *, issue_type_mappings: builtins.list[_t.IssueTypeScreenSchemeMapping], name: str, description: str | Unset = UNSET) -> _t.IssueTypeScreenSchemeId:
        """
        Create issue type screen scheme

        Creates an issue type screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeScreenSchemeId', self._runtime.call('create_issue_type_screen_scheme', call_args({}, {'body': {'description': description, 'issue_type_mappings': issue_type_mappings, 'name': name}}, required=frozenset({'body'}))))

    def list_mappings(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, issue_type_screen_scheme_id: builtins.list[int] | Unset = UNSET) -> _t.PageBeanIssueTypeScreenSchemeItem:
        """
        Get issue type screen scheme items

        Returns a [paginated](#pagination) list of issue type screen scheme items.

        Only issue type screen schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeScreenSchemeItem', self._runtime.call('get_issue_type_screen_scheme_mappings', call_args({'start_at': start_at, 'max_results': max_results, 'issue_type_screen_scheme_id': issue_type_screen_scheme_id})))

    def list_project_associations(self, *, project_id: builtins.list[int], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanIssueTypeScreenSchemesProjects:
        """
        Get issue type screen schemes for projects

        Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it.

        Only issue type screen schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanIssueTypeScreenSchemesProjects', self._runtime.call('get_issue_type_screen_scheme_project_associations', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id})))

    def assign_to_project(self, *, issue_type_screen_scheme_id: str | Unset = UNSET, project_id: str | Unset = UNSET) -> Any:
        """
        Assign issue type screen scheme to project

        Assigns an issue type screen scheme to a project.

        Issue type screen schemes can only be assigned to classic projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('assign_issue_type_screen_scheme_to_project', call_args({}, {'body': {'issue_type_screen_scheme_id': issue_type_screen_scheme_id, 'project_id': project_id}})))

    def update(self, *, issue_type_screen_scheme_id: str, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update issue type screen scheme

        Updates an issue type screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_issue_type_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id}, {'body': {'description': description, 'name': name}})))

    def delete(self, *, issue_type_screen_scheme_id: str) -> Any:
        """
        Delete issue type screen scheme

        Deletes an issue type screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_issue_type_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id})))

    def append(self, *, issue_type_screen_scheme_id: str, issue_type_mappings: builtins.list[_t.IssueTypeScreenSchemeMapping]) -> Any:
        """
        Append mappings to issue type screen scheme

        Appends issue type to screen scheme mappings to an issue type screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('append_mappings_for_issue_type_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id}, {'body': {'issue_type_mappings': issue_type_mappings}}, required=frozenset({'body'}))))

    def update_default_screen_scheme(self, *, issue_type_screen_scheme_id: str, screen_scheme_id: str) -> Any:
        """
        Update issue type screen scheme default screen scheme

        Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_default_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id}, {'body': {'screen_scheme_id': screen_scheme_id}}, required=frozenset({'body'}))))

    def remove(self, *, issue_type_screen_scheme_id: str, issue_type_ids: builtins.list[str]) -> Any:
        """
        Remove mappings from issue type screen scheme

        Removes issue type to screen scheme mappings from an issue type screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_mappings_from_issue_type_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id}, {'body': {'issue_type_ids': issue_type_ids}}, required=frozenset({'body'}))))

    def get(self, *, issue_type_screen_scheme_id: int, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBeanProjectDetails:
        """
        Get issue type screen scheme projects

        Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

        Only company-managed projects associated with an issue type screen scheme are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanProjectDetails', self._runtime.call('get_projects_for_issue_type_screen_scheme', call_args({'issue_type_screen_scheme_id': issue_type_screen_scheme_id, 'start_at': start_at, 'max_results': max_results, 'query': query})))

class _IssueTypesResource:
    """Operations under ``issue_types``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_issue_all_types(self) -> builtins.list[_t.IssueTypeDetails]:
        """
        Get all issue types for user

        Returns all issue types.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Issue types are only returned as follows:

         *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
         *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.
         *  if the user is anonymous then they will be able to access projects with the *Browse projects* for anonymous users
         *  if the user authentication is incorrect they will fall back to anonymous
        """
        return cast('builtins.list[_t.IssueTypeDetails]', self._runtime.call('get_issue_all_types', call_args({})))

    def create(self, *, name: str, description: str | Unset = UNSET, hierarchy_level: int | Unset = UNSET, type_: _t.IssueTypeCreateBeanType | Unset = UNSET) -> _t.IssueTypeDetails:
        """
        Create issue type

        Creates an issue type.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeDetails', self._runtime.call('create_issue_type', call_args({}, {'body': {'description': description, 'hierarchy_level': hierarchy_level, 'name': name, 'type': type_}}, required=frozenset({'body'}))))

    def get_for_project(self, *, project_id: int, level: int | Unset = UNSET) -> builtins.list[_t.IssueTypeDetails]:
        """
        Get issue types for project

        Returns issue types for a project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.IssueTypeDetails]', self._runtime.call('get_issue_types_for_project', call_args({'project_id': project_id, 'level': level})))

    def get(self, *, id: str) -> _t.IssueTypeDetails:
        """
        Get issue type

        Returns an issue type.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeDetails', self._runtime.call('get_issue_type', call_args({'id': id})))

    def update(self, *, id: str, avatar_id: int | Unset = UNSET, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.IssueTypeDetails:
        """
        Update issue type

        Updates the issue type.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeDetails', self._runtime.call('update_issue_type', call_args({'id': id}, {'body': {'avatar_id': avatar_id, 'description': description, 'name': name}})))

    def delete(self, *, id: str, alternative_issue_type_id: str | Unset = UNSET) -> None:
        """
        Delete issue type

        Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (`alternativeIssueTypeId`). A list of alternative issue types are obtained from the [Get alternative issue types](#api-rest-api-3-issuetype-id-alternatives-get) resource.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_issue_type', call_args({'id': id, 'alternative_issue_type_id': alternative_issue_type_id}))

    def list(self, *, id: str) -> builtins.list[_t.IssueTypeDetails]:
        """
        Get alternative issue types

        Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('builtins.list[_t.IssueTypeDetails]', self._runtime.call('get_alternative_issue_types', call_args({'id': id})))

    def create_avatar(self, *, id: str, size: int, body: str | bytes | PathLike[str], x: int | Unset = UNSET, y: int | Unset = UNSET) -> _t.Avatar:
        """
        Load issue type avatar

        Loads an avatar for the issue type.

        Specify the avatar's local file location in the body of the request. Also, include the following headers:

         *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
         *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

        For example:  
        `curl --request POST \\ --user email@example.com:<api_token> \\ --header 'X-Atlassian-Token: no-check' \\ --header 'Content-Type: image/< image_type>' \\ --data-binary "<@/path/to/file/with/your/avatar>" \\ --url 'https://your-domain.atlassian.net/rest/api/3/issuetype/{issueTypeId}'This`

        The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

        The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

        After creating the avatar, use [ Update issue type](#api-rest-api-3-issuetype-id-put) to set it as the issue type's displayed avatar.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.Avatar', self._runtime.call('create_issue_type_avatar', call_args({'id': id, 'x': x, 'y': y, 'size': size, 'body': body})))

class _IssueVotesResource:
    """Operations under ``issue_votes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_votes(self, *, issue_id_or_key: str) -> _t.Votes:
        """
        Get votes

        Returns details about the votes on an issue.

        This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

        Note that users with the necessary permissions for this operation but without the *View voters and watchers* project permissions are not returned details in the `voters` field.
        """
        return cast('_t.Votes', self._runtime.call('get_votes', call_args({'issue_id_or_key': issue_id_or_key})))

    def add_vote(self, *, issue_id_or_key: str) -> Any:
        """
        Add vote

        Adds the user's vote to an issue. This is the equivalent of the user clicking *Vote* on an issue in Jira.

        This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('add_vote', call_args({'issue_id_or_key': issue_id_or_key})))

    def remove_vote(self, *, issue_id_or_key: str) -> None:
        """
        Delete vote

        Deletes a user's vote from an issue. This is the equivalent of the user clicking *Unvote* on an issue in Jira.

        This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('remove_vote', call_args({'issue_id_or_key': issue_id_or_key}))

class _IssueWatchersResource:
    """Operations under ``issue_watchers``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_is_watching_issue_bulk(self, *, issue_ids: builtins.list[str]) -> _t.BulkIssueIsWatching:
        """
        Get is watching issue bulk

        Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is `false`.

        This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.BulkIssueIsWatching', self._runtime.call('get_is_watching_issue_bulk', call_args({}, {'body': {'issue_ids': issue_ids}}, required=frozenset({'body'}))))

    def list(self, *, issue_id_or_key: str) -> _t.Watchers:
        """
        Get issue watchers

        Returns the watchers for an issue.

        This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  To see details of users on the watchlist other than themselves, *View voters and watchers* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
        """
        return cast('_t.Watchers', self._runtime.call('get_issue_watchers', call_args({'issue_id_or_key': issue_id_or_key})))

    def add_watcher(self, *, issue_id_or_key: str, body: str) -> Any:
        """
        Add watcher

        Adds a user as a watcher of an issue by passing the account ID of the user. For example, `"5b10ac8d82e05b22cc7d4ef5"`. If no user is specified the calling user is added.

        This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  To add users other than themselves to the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
        """
        return cast('Any', self._runtime.call('add_watcher', call_args({'issue_id_or_key': issue_id_or_key, 'body': body})))

    def remove_watcher(self, *, issue_id_or_key: str, username: str | Unset = UNSET, account_id: str | Unset = UNSET) -> None:
        """
        Delete watcher

        Deletes a user as a watcher of an issue.

        This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  To remove users other than themselves from the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
        """
        self._runtime.call('remove_watcher', call_args({'issue_id_or_key': issue_id_or_key, 'username': username, 'account_id': account_id}))

class _IssueWorklogPropertiesResource:
    """Operations under ``issue_worklog_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_worklog_property_keys(self, *, issue_id_or_key: str, worklog_id: str) -> _t.PropertyKeys:
        """
        Get worklog property keys

        Returns the keys of all properties for a worklog.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_worklog_property_keys', call_args({'issue_id_or_key': issue_id_or_key, 'worklog_id': worklog_id})))

    def get_worklog_property(self, *, issue_id_or_key: str, worklog_id: str, property_key: str) -> _t.EntityProperty:
        """
        Get worklog property

        Returns the value of a worklog property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_worklog_property', call_args({'issue_id_or_key': issue_id_or_key, 'worklog_id': worklog_id, 'property_key': property_key})))

    def set_worklog_property(self, *, issue_id_or_key: str, worklog_id: str, property_key: str, body: Any) -> Any:
        """
        Set worklog property

        Sets the value of a worklog property. Use this operation to store custom data against the worklog.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('Any', self._runtime.call('set_worklog_property', call_args({'issue_id_or_key': issue_id_or_key, 'worklog_id': worklog_id, 'property_key': property_key, 'body': body})))

    def delete_worklog_property(self, *, issue_id_or_key: str, worklog_id: str, property_key: str) -> None:
        """
        Delete worklog property

        Deletes a worklog property.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        self._runtime.call('delete_worklog_property', call_args({'issue_id_or_key': issue_id_or_key, 'worklog_id': worklog_id, 'property_key': property_key}))

class _IssueWorklogsResource:
    """Operations under ``issue_worklogs``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self, *, issue_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, started_after: int | Unset = UNSET, started_before: int | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageOfWorklogs:
        """
        Get issue worklogs

        Returns worklogs for an issue (ordered by created time), starting from the oldest worklog or from the worklog started on or after a date and time.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Workloads are only returned where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.PageOfWorklogs', self._runtime.call('get_issue_worklog', call_args({'issue_id_or_key': issue_id_or_key, 'start_at': start_at, 'max_results': max_results, 'started_after': started_after, 'started_before': started_before, 'expand': expand})))

    def add_worklog(self, *, issue_id_or_key: str, notify_users: bool | Unset = UNSET, adjust_estimate: _t.AddWorklogAdjustEstimate | Unset = UNSET, new_estimate: str | Unset = UNSET, reduce_by: str | Unset = UNSET, expand: str | Unset = UNSET, override_editable_flag: bool | Unset = UNSET, author: _t.UserDetails | Unset = UNSET, comment: Any | Unset = UNSET, created: str | Unset = UNSET, id: str | Unset = UNSET, issue_id: str | Unset = UNSET, properties: builtins.list[_t.EntityProperty] | Unset = UNSET, self_: str | Unset = UNSET, started: str | Unset = UNSET, time_spent: str | Unset = UNSET, time_spent_seconds: int | Unset = UNSET, update_author: _t.UserDetails | Unset = UNSET, updated: str | Unset = UNSET, visibility: _t.Visibility | Unset = UNSET) -> _t.Worklog:
        """
        Add worklog

        Adds a worklog to an issue.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.Worklog', self._runtime.call('add_worklog', call_args({'issue_id_or_key': issue_id_or_key, 'notify_users': notify_users, 'adjust_estimate': adjust_estimate, 'new_estimate': new_estimate, 'reduce_by': reduce_by, 'expand': expand, 'override_editable_flag': override_editable_flag}, {'body': {'author': author, 'comment': comment, 'created': created, 'id': id, 'issue_id': issue_id, 'properties': properties, 'self': self_, 'started': started, 'time_spent': time_spent, 'time_spent_seconds': time_spent_seconds, 'update_author': update_author, 'updated': updated, 'visibility': visibility}})))

    def bulk_delete_worklogs(self, *, issue_id_or_key: str, ids: builtins.list[int], adjust_estimate: _t.BulkDeleteWorklogsAdjustEstimate | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> None:
        """
        Bulk delete worklogs

        Deletes a list of worklogs from an issue. This is an experimental API with limitations:

         *  You can't delete more than 5000 worklogs at once.
         *  No notifications will be sent for deleted worklogs.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog.
         *  If any worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        self._runtime.call('bulk_delete_worklogs', call_args({'issue_id_or_key': issue_id_or_key, 'adjust_estimate': adjust_estimate, 'override_editable_flag': override_editable_flag}, {'body': {'ids': ids}}, required=frozenset({'body'})))

    def bulk_move_worklogs(self, *, issue_id_or_key: str, body: _t.WorklogsMoveRequestBean, adjust_estimate: _t.BulkMoveWorklogsAdjustEstimate | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> None:
        """
        Bulk move worklogs

        Moves a list of worklogs from one issue to another. This is an experimental API with several limitations:

         *  You can't move more than 5000 worklogs at once.
         *  You can't move worklogs containing an attachment.
         *  You can't move worklogs restricted by project roles.
         *  No notifications will be sent for moved worklogs.
         *  No webhooks or events will be sent for moved worklogs.
         *  No issue history will be recorded for moved worklogs.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects containing the source and destination issues.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Delete all worklogs* [project permission](https://confluence.atlassian.com/x/yodKLg)
         *  *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) to log work on an issue, that is to create a worklog entry, if time tracking is enabled. This permission is required as a prerequisite for applying the other time-tracking permissions
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        self._runtime.call('bulk_move_worklogs', call_args({'issue_id_or_key': issue_id_or_key, 'adjust_estimate': adjust_estimate, 'override_editable_flag': override_editable_flag, 'body': body}))

    def get_worklog(self, *, issue_id_or_key: str, id: str, expand: str | Unset = UNSET) -> _t.Worklog:
        """
        Get worklog

        Returns a worklog.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.Worklog', self._runtime.call('get_worklog', call_args({'issue_id_or_key': issue_id_or_key, 'id': id, 'expand': expand})))

    def update_worklog(self, *, issue_id_or_key: str, id: str, body: _t.Worklog, notify_users: bool | Unset = UNSET, adjust_estimate: _t.UpdateWorklogAdjustEstimate | Unset = UNSET, new_estimate: str | Unset = UNSET, expand: str | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> _t.Worklog:
        """
        Update worklog

        Updates a worklog.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        return cast('_t.Worklog', self._runtime.call('update_worklog', call_args({'issue_id_or_key': issue_id_or_key, 'id': id, 'notify_users': notify_users, 'adjust_estimate': adjust_estimate, 'new_estimate': new_estimate, 'expand': expand, 'override_editable_flag': override_editable_flag, 'body': body})))

    def delete_worklog(self, *, issue_id_or_key: str, id: str, notify_users: bool | Unset = UNSET, adjust_estimate: _t.DeleteWorklogAdjustEstimate | Unset = UNSET, new_estimate: str | Unset = UNSET, increase_by: str | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> None:
        """
        Delete worklog

        Deletes a worklog from an issue.

        Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
         *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or *Delete own worklogs* to delete worklogs created by the user,
         *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
        """
        self._runtime.call('delete_worklog', call_args({'issue_id_or_key': issue_id_or_key, 'id': id, 'notify_users': notify_users, 'adjust_estimate': adjust_estimate, 'new_estimate': new_estimate, 'increase_by': increase_by, 'override_editable_flag': override_editable_flag}))

    def get_ids_of_worklogs_deleted_since(self, *, since: int | Unset = UNSET) -> _t.ChangedWorklogs:
        """
        Get IDs of deleted worklogs

        Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

        This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

        This resource does not return worklogs deleted during the minute preceding the request.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.ChangedWorklogs', self._runtime.call('get_ids_of_worklogs_deleted_since', call_args({'since': since})))

    def list_worklogs_for_ids(self, *, ids: builtins.list[int], expand: str | Unset = UNSET) -> builtins.list[_t.Worklog]:
        """
        Get worklogs

        Returns worklog details for a list of worklog IDs.

        The returned list of worklogs is limited to 1000 items.

        **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

         *  the worklog is set as *Viewable by All Users*.
         *  the user is a member of a project role or group with permission to view the worklog.
        """
        return cast('builtins.list[_t.Worklog]', self._runtime.call('get_worklogs_for_ids', call_args({'expand': expand}, {'body': {'ids': ids}}, required=frozenset({'body'}))))

    def get_ids_of_worklogs_modified_since(self, *, since: int | Unset = UNSET, expand: str | Unset = UNSET) -> _t.ChangedWorklogs:
        """
        Get IDs of updated worklogs

        Returns a list of IDs and update timestamps for worklogs updated after a date and time.

        This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

        This resource does not return worklogs updated during the minute preceding the request.

        **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

         *  the worklog is set as *Viewable by All Users*.
         *  the user is a member of a project role or group with permission to view the worklog.
        """
        return cast('_t.ChangedWorklogs', self._runtime.call('get_ids_of_worklogs_modified_since', call_args({'since': since, 'expand': expand})))

class _IssuesResource:
    """Operations under ``issues``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_bulk_changelogs(self, *, issue_ids_or_keys: builtins.list[str], field_ids: builtins.list[str] | Unset = UNSET, max_results: int | Unset = UNSET, next_page_token: str | Unset = UNSET) -> _t.BulkChangelogResponseBean:
        """
        Bulk fetch changelogs

        Bulk fetch changelogs for multiple issues and filter by fields

        Returns a paginated list of all changelogs for given issues sorted by changelog date and issue IDs, starting from the oldest changelog and smallest issue ID.

        Issues are identified by their ID or key, and optionally changelogs can be filtered by their field IDs. You can request the changelogs of up to 1000 issues and can filter them by up to 10 field IDs.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects that the issues are in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issues.
        """
        return cast('_t.BulkChangelogResponseBean', self._runtime.call('get_bulk_changelogs', call_args({}, {'body': {'field_ids': field_ids, 'issue_ids_or_keys': issue_ids_or_keys, 'max_results': max_results, 'next_page_token': next_page_token}}, required=frozenset({'body'}))))

    def list_events(self) -> builtins.list[_t.IssueEvent]:
        """
        Get events

        Returns all issue events.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.IssueEvent]', self._runtime.call('get_events', call_args({})))

    def create(self, *, update_history: bool | Unset = UNSET, fields: builtins.dict[str, Any] | Unset = UNSET, history_metadata: _t.HistoryMetadata | Unset = UNSET, properties: builtins.list[_t.EntityProperty] | Unset = UNSET, transition: _t.IssueTransition | Unset = UNSET, update: builtins.dict[str, builtins.list[_t.FieldUpdateOperation]] | Unset = UNSET) -> _t.CreatedIssue:
        """
        Create issue

        Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition may be applied, to move the issue or subtask to a workflow step other than the default start step, and issue properties set.

        The content of the issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

        Creating a subtask differs from creating an issue as follows:

         *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types).
         *  `parent` must contain the ID or key of the parent issue.

        In a next-gen project any issue may be made a child providing that the parent and child are members of the same project.

        **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or subtask is created.
        """
        return cast('_t.CreatedIssue', self._runtime.call('create_issue', call_args({'update_history': update_history}, {'body': {'fields': fields, 'history_metadata': history_metadata, 'properties': properties, 'transition': transition, 'update': update}})))

    def archive(self, *, issue_ids_or_keys: builtins.list[str] | Unset = UNSET) -> _t.IssueArchivalSyncResponse:
        """
        Archive issue(s) by issue ID/key

        Enables admins to archive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) archived in the process and the errors encountered, if any.

        **Note that:**

         *  you can't archive subtasks directly, only through their parent issues
         *  you can only archive issues from software, service management, and business projects

        **[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

        **License required:** Premium or Enterprise

        **Signed-in users only:** This API can't be accessed anonymously.
        """
        return cast('_t.IssueArchivalSyncResponse', self._runtime.call('archive_issues', call_args({}, {'body': {'issue_ids_or_keys': issue_ids_or_keys}})))

    def archive_async(self, *, jql: str | Unset = UNSET) -> str:
        """
        Archive issue(s) by JQL

        Enables admins to archive up to 100,000 issues in a single request using JQL, returning the URL to check the status of the submitted request.

        You can use the [get task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) and [cancel task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-cancel-post) APIs to manage the request.

        **Note that:**

         *  you can't archive subtasks directly, only through their parent issues
         *  you can only archive issues from software, service management, and business projects

        **[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

        **License required:** Premium or Enterprise

        **Signed-in users only:** This API can't be accessed anonymously.

        **Rate limiting:** Only a single request per jira instance can be active at any given time.
        """
        return cast('str', self._runtime.call('archive_issues_async', call_args({}, {'body': {'jql': jql}})))

    def create_many(self, *, issue_updates: builtins.list[_t.IssueUpdateDetails] | Unset = UNSET) -> _t.CreatedIssues:
        """
        Bulk create issue

        Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks. Transitions may be applied, to move the issues or subtasks to a workflow step other than the default start step, and issue properties set.

        The content of each issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

        Creating a subtask differs from creating an issue as follows:

         *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types).
         *  `parent` the must contain the ID or key of the parent issue.

        **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or subtask is created.
        """
        return cast('_t.CreatedIssues', self._runtime.call('create_issues', call_args({}, {'body': {'issue_updates': issue_updates}})))

    def bulk(self, *, issue_ids_or_keys: builtins.list[str], expand: builtins.list[str] | Unset = UNSET, fields: builtins.list[str] | Unset = UNSET, fields_by_keys: bool | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET) -> _t.BulkIssueResults:
        """
        Bulk fetch issues

        Returns the details for a set of requested issues.

        By default you can request up to 100 issues in a single call. You can request up to 1000 issues in a single call when the request is shaped so that it can be served efficiently, that is, when *all* of the following are true:

         *  the `fields` parameter explicitly names at least one field to include — a request that contains only exclusions is **not** eligible, and neither are the `*all` and `*navigable` wildcards or the default navigable field set, because the number of resolved fields depends on the site's configuration;
         *  no more than 100 fields are explicitly included;
         *  none of the included fields returns multiple values (for example `comment`, `worklog`, or `attachment`); and
         *  the `expand` parameter does not include `changelog`, `editmeta`, `operations`, `renderedFields`, `transitions`, or `versionedRepresentations`.

        Requests that do not meet all of these conditions can include at most 100 issues; larger requests are rejected with a 400 error.

        Each issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned.

        Issues will be returned in ascending `id` order. If there are errors, Jira will return a list of issues which couldn't be fetched along with error messages.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Issues are included in the response where the user has:

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.BulkIssueResults', self._runtime.call('bulk_fetch_issues', call_args({}, {'body': {'expand': expand, 'fields': fields, 'fields_by_keys': fields_by_keys, 'issue_ids_or_keys': issue_ids_or_keys, 'properties': properties}}, required=frozenset({'body'}))))

    def get_create_meta(self, *, project_ids: builtins.list[str] | Unset = UNSET, project_keys: builtins.list[str] | Unset = UNSET, issuetype_ids: builtins.list[str] | Unset = UNSET, issuetype_names: builtins.list[str] | Unset = UNSET, expand: str | Unset = UNSET) -> _t.IssueCreateMetadata:
        """
        Get create issue metadata

        Returns details of projects, issue types within projects, and, when requested, the create screen fields for each issue type for the user. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

        Deprecated, see [Create Issue Meta Endpoint Deprecation Notice](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1304).

        The request can be restricted to specific projects or issue types using the query parameters. The response will contain information for the valid projects, issue types, or project and issue type combinations requested. Note that invalid project, issue type, or project and issue type combinations do not generate errors.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

        Deprecated.
        """
        return cast('_t.IssueCreateMetadata', self._runtime.call('get_create_issue_meta', call_args({'project_ids': project_ids, 'project_keys': project_keys, 'issuetype_ids': issuetype_ids, 'issuetype_names': issuetype_names, 'expand': expand})))

    def list_create_meta_issue_types(self, *, project_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageOfCreateMetaIssueTypes:
        """
        Get create metadata issue types for a project

        Returns a page of issue type metadata for a specified project. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
        """
        return cast('_t.PageOfCreateMetaIssueTypes', self._runtime.call('get_create_issue_meta_issue_types', call_args({'project_id_or_key': project_id_or_key, 'start_at': start_at, 'max_results': max_results})))

    def get_create_meta_issue_type_id(self, *, project_id_or_key: str, issue_type_id: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageOfCreateMetaIssueTypeWithField:
        """
        Get create field metadata for a project and issue type id

        Returns a page of field metadata for a specified project and issuetype id. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
        """
        return cast('_t.PageOfCreateMetaIssueTypeWithField', self._runtime.call('get_create_issue_meta_issue_type_id', call_args({'project_id_or_key': project_id_or_key, 'issue_type_id': issue_type_id, 'start_at': start_at, 'max_results': max_results})))

    def get_adf_limit_report(self, *, is_returning_keys: bool | Unset = UNSET, field_type: builtins.list[str] | Unset = UNSET) -> _t.IssueLimitReportResponseBean:
        """
        Get issue adf limit report

        Returns all issues whose ADF (rich text) field data breaches the universal ADF size limit.

        Unlike the issue limit report, which reports issues breaching per-issue entity *count* limits, this endpoint reports issues whose ADF field *byte size* exceeds that limit. The reported ADF field types are `comment_adf`, `worklog_adf`, `customfield_adf`, `description_adf` and `environment_adf`. The reported value for each issue is the number of breaching entities for that field (always 1 for the single-value description and environment fields).

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueLimitReportResponseBean', self._runtime.call('get_issue_adf_limit_report', call_args({'is_returning_keys': is_returning_keys, 'field_type': field_type})))

    def get_limit_report(self, *, is_returning_keys: bool | Unset = UNSET) -> _t.IssueLimitReportResponseBean:
        """
        Get issue limit report

        Returns all issues breaching and approaching per-issue limits.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueLimitReportResponseBean', self._runtime.call('get_issue_limit_report', call_args({'is_returning_keys': is_returning_keys})))

    def unarchive(self, *, issue_ids_or_keys: builtins.list[str] | Unset = UNSET) -> _t.IssueArchivalSyncResponse:
        """
        Unarchive issue(s) by issue keys/ID

        Enables admins to unarchive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) unarchived in the process and the errors encountered, if any.

        **Note that:**

         *  you can't unarchive subtasks directly, only through their parent issues
         *  you can only unarchive issues from software, service management, and business projects

        **[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

        **License required:** Premium or Enterprise

        **Signed-in users only:** This API can't be accessed anonymously.
        """
        return cast('_t.IssueArchivalSyncResponse', self._runtime.call('unarchive_issues', call_args({}, {'body': {'issue_ids_or_keys': issue_ids_or_keys}})))

    def get(self, *, issue_id_or_key: str, fields: builtins.list[str] | Unset = UNSET, fields_by_keys: bool | Unset = UNSET, expand: str | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET, update_history: bool | Unset = UNSET, fail_fast: bool | Unset = UNSET) -> _t.IssueBean:
        """
        Get issue

        Returns the details for an issue.

        The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is the key of the issue found.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.IssueBean', self._runtime.call('get_issue', call_args({'issue_id_or_key': issue_id_or_key, 'fields': fields, 'fields_by_keys': fields_by_keys, 'expand': expand, 'properties': properties, 'update_history': update_history, 'fail_fast': fail_fast})))

    def edit(self, *, issue_id_or_key: str, notify_users: bool | Unset = UNSET, override_screen_security: bool | Unset = UNSET, override_editable_flag: bool | Unset = UNSET, return_issue: bool | Unset = UNSET, expand: str | Unset = UNSET, fields: builtins.dict[str, Any] | Unset = UNSET, history_metadata: _t.HistoryMetadata | Unset = UNSET, properties: builtins.list[_t.EntityProperty] | Unset = UNSET, transition: _t.IssueTransition | Unset = UNSET, update: builtins.dict[str, builtins.list[_t.FieldUpdateOperation]] | Unset = UNSET) -> Any:
        """
        Edit issue

        Edits an issue. Issue properties may be updated as part of the edit. Please note that issue transition is not supported and is ignored here. To transition an issue, please use [Transition issue](#api-rest-api-3-issue-issueIdOrKey-transitions-post).

        The edits to the issue's fields are defined using `update` and `fields`. The fields that can be edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-get).

        **Note:** This endpoint doesn't check screen configurations to determine if a field is editable. For more context, see the [Deprecation of override screen security](https://community.developer.atlassian.com/t/deprecation-of-override-screen-security/97153) announcement.

        The parent field may be set by key or ID. For standard issue types, the parent may be removed by setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

        Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('edit_issue', call_args({'issue_id_or_key': issue_id_or_key, 'notify_users': notify_users, 'override_screen_security': override_screen_security, 'override_editable_flag': override_editable_flag, 'return_issue': return_issue, 'expand': expand}, {'body': {'fields': fields, 'history_metadata': history_metadata, 'properties': properties, 'transition': transition, 'update': update}})))

    def delete(self, *, issue_id_or_key: str, delete_subtasks: _t.DeleteIssueDeleteSubtasks | Unset = UNSET) -> None:
        """
        Delete issue

        Deletes an issue.

        An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set `deleteSubtasks`. This causes the issue's subtasks to be deleted with the issue.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Delete issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        self._runtime.call('delete_issue', call_args({'issue_id_or_key': issue_id_or_key, 'delete_subtasks': delete_subtasks}))

    def assign(self, *, issue_id_or_key: str, account_id: str | Unset = UNSET, account_type: _t.UserAccountType | Unset = UNSET, active: bool | Unset = UNSET, app_type: str | Unset = UNSET, application_roles: _t.SimpleListWrapperApplicationRole | Unset = UNSET, avatar_urls: _t.AvatarUrlsBean | Unset = UNSET, display_name: str | Unset = UNSET, email_address: str | Unset = UNSET, expand: str | Unset = UNSET, groups: _t.SimpleListWrapperGroupName | Unset = UNSET, guest: bool | Unset = UNSET, key: str | Unset = UNSET, locale: str | Unset = UNSET, name: str | Unset = UNSET, self_: str | Unset = UNSET, time_zone: str | Unset = UNSET) -> Any:
        """
        Assign issue

        Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues* permission but has the *Assign issue* permission for the project that the issue is in.

        If `name` or `accountId` is set to:

         *  `"-1"`, the issue is assigned to the default assignee for the project.
         *  `null`, the issue is set to unassigned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse Projects* and *Assign Issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('assign_issue', call_args({'issue_id_or_key': issue_id_or_key}, {'body': {'account_id': account_id, 'account_type': account_type, 'active': active, 'app_type': app_type, 'application_roles': application_roles, 'avatar_urls': avatar_urls, 'display_name': display_name, 'email_address': email_address, 'expand': expand, 'groups': groups, 'guest': guest, 'key': key, 'locale': locale, 'name': name, 'self': self_, 'time_zone': time_zone}})))

    def list_change_logs(self, *, issue_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanChangelog:
        """
        Get changelogs

        Returns a [paginated](#pagination) list of all changelogs for an issue sorted by date, starting from the oldest.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.PageBeanChangelog', self._runtime.call('get_change_logs', call_args({'issue_id_or_key': issue_id_or_key, 'start_at': start_at, 'max_results': max_results})))

    def list_change_logs_by_ids(self, *, issue_id_or_key: str, changelog_ids: builtins.list[int]) -> _t.PageOfChangelogs:
        """
        Get changelogs by IDs

        Returns changelogs for an issue specified by a list of changelog IDs.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('_t.PageOfChangelogs', self._runtime.call('get_change_logs_by_ids', call_args({'issue_id_or_key': issue_id_or_key}, {'body': {'changelog_ids': changelog_ids}}, required=frozenset({'body'}))))

    def get_edit_meta(self, *, issue_id_or_key: str, override_screen_security: bool | Unset = UNSET, override_editable_flag: bool | Unset = UNSET) -> _t.IssueUpdateMetadata:
        """
        Get edit issue metadata

        Returns the edit screen fields for an issue that are visible to and editable by the user. Use the information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).

        This endpoint will check for these conditions:

        1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme, and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.
        2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this condition.
        3.  Field is shown on the issue: each field has different conditions here. For example: Attachment field only shows if attachments are enabled. Assignee only shows if user has permissions to assign the issue.
        4.  If a field is custom then it must have valid custom field context, applicable for its project and issue type. All system fields are assumed to have context in all projects and all issue types.
        5.  Issue has a project, issue type, and status defined.
        6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step. `overrideEditableFlag=true` skips this condition.
        7.  The current workflow step is editable. This is true by default, but [can be disabled by setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition.
        8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/).
        9.  Workflow permissions allow editing a field. This is true by default but [can be modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) using `jira.permission.*` workflow properties.

        Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.

        Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return additional details using:

         *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields are available through screens, and field configuration (conditions 1. and 2. from the list above).
         *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow is present and if the current step is editable (conditions 6. and 7. from the list above).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

        Note: For any fields to be editable the user must have the *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the issue.
        """
        return cast('_t.IssueUpdateMetadata', self._runtime.call('get_edit_issue_meta', call_args({'issue_id_or_key': issue_id_or_key, 'override_screen_security': override_screen_security, 'override_editable_flag': override_editable_flag})))

    def notify(self, *, issue_id_or_key: str, html_body: str | Unset = UNSET, restrict: _t.NotificationRecipientsRestrictions | Unset = UNSET, subject: str | Unset = UNSET, text_body: str | Unset = UNSET, to: _t.NotificationRecipients | Unset = UNSET) -> Any:
        """
        Send notification for issue

        Creates an email notification for an issue and adds it to the mail queue.

        **[Permissions](#permissions) required:**

         *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('notify', call_args({'issue_id_or_key': issue_id_or_key}, {'body': {'html_body': html_body, 'restrict': restrict, 'subject': subject, 'text_body': text_body, 'to': to}})))

    def list_transitions(self, *, issue_id_or_key: str, expand: str | Unset = UNSET, transition_id: str | Unset = UNSET, skip_remote_only_condition: bool | Unset = UNSET, include_unavailable_transitions: bool | Unset = UNSET, sort_by_ops_bar_and_status: bool | Unset = UNSET) -> _t.Transitions:
        """
        Get transitions

        Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status.

        Note, if a request is made for a transition that does not exist or cannot be performed on the issue, given its status, the response will return any empty transitions list.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required: A list or transition is returned only when the user has:**

         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

        However, if the user does not have the *Transition issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.
        """
        return cast('_t.Transitions', self._runtime.call('get_transitions', call_args({'issue_id_or_key': issue_id_or_key, 'expand': expand, 'transition_id': transition_id, 'skip_remote_only_condition': skip_remote_only_condition, 'include_unavailable_transitions': include_unavailable_transitions, 'sort_by_ops_bar_and_status': sort_by_ops_bar_and_status})))

    def do_transition(self, *, issue_id_or_key: str, fields: builtins.dict[str, Any] | Unset = UNSET, history_metadata: _t.HistoryMetadata | Unset = UNSET, properties: builtins.list[_t.EntityProperty] | Unset = UNSET, transition: _t.IssueTransition | Unset = UNSET, update: builtins.dict[str, builtins.list[_t.FieldUpdateOperation]] | Unset = UNSET) -> Any:
        """
        Transition issue

        Performs an issue transition and, if the transition has a screen, updates the fields from the transition screen.

        sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Browse projects* and *Transition issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
         *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
        """
        return cast('Any', self._runtime.call('do_transition', call_args({'issue_id_or_key': issue_id_or_key}, {'body': {'fields': fields, 'history_metadata': history_metadata, 'properties': properties, 'transition': transition, 'update': update}})))

    def export(self, *, archived_by: builtins.list[str] | Unset = UNSET, archived_date_range: _t.DateRangeFilterRequest | Unset = UNSET, issue_types: builtins.list[str] | Unset = UNSET, projects: builtins.list[str] | Unset = UNSET, reporters: builtins.list[str] | Unset = UNSET) -> _t.ExportArchivedIssuesTaskProgressResponse:
        """
        Export archived issue(s)

        Enables admins to retrieve details of all archived issues. Upon a successful request, the admin who submitted it will receive an email with a link to download a CSV file with the issue details.

        Note that this API only exports the values of system fields and archival-specific fields (`ArchivedBy` and `ArchivedDate`). Custom fields aren't supported.

        **[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

        **License required:** Premium or Enterprise

        **Signed-in users only:** This API can't be accessed anonymously.

        **Rate limiting:** Only a single request can be active at any given time.
        """
        return cast('_t.ExportArchivedIssuesTaskProgressResponse', self._runtime.call('export_archived_issues', call_args({}, {'body': {'archived_by': archived_by, 'archived_date_range': archived_date_range, 'issue_types': issue_types, 'projects': projects, 'reporters': reporters}})))

class _JiraExpressionsResource:
    """Operations under ``jira_expressions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def analyse_expression(self, *, expressions: builtins.list[str], check: _t.AnalyseExpressionCheck | Unset = UNSET, context_variables: builtins.dict[str, str] | Unset = UNSET) -> _t.JiraExpressionsAnalysis:
        """
        Analyse Jira expression

        Analyses and validates Jira expressions.

        As an experimental feature, this operation can also attempt to type-check the expressions.

        Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

        **[Permissions](#permissions) required**: None.
        """
        return cast('_t.JiraExpressionsAnalysis', self._runtime.call('analyse_expression', call_args({'check': check}, {'body': {'context_variables': context_variables, 'expressions': expressions}}, required=frozenset({'body'}))))

    def evaluate(self, *, expression: str, expand: str | Unset = UNSET, context: _t.JiraExpressionEvalContextBean | Unset = UNSET) -> _t.JiraExpressionResult:
        """
        Currently being removed. Evaluate Jira expression

        Endpoint is currently being removed. [More details](https://developer.atlassian.com/changelog/#CHANGE-2046)

        Evaluates a Jira expression and returns its value.

        This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.

        #### Context variables ####

        The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.

         *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to `null` if the request is anonymous.
         *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect Apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
         *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.
         *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.
         *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.
         *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.
         *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.
         *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.
         *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.

        Also, custom context variables can be passed in the request with their types. Those variables can be accessed by key in the Jira expression. These variable types are available for use in a custom context:

         *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.
         *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.
         *  `json`: A JSON object containing custom content.
         *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.  
        Permission to access Jira Software is required to access Jira Software context variables (`board` and `sprint`) or fields (for example, `issue.sprint`).

        Deprecated.
        """
        return cast('_t.JiraExpressionResult', self._runtime.call('evaluate_jira_expression', call_args({'expand': expand}, {'body': {'context': context, 'expression': expression}}, required=frozenset({'body'}))))

    def evaluate_jsis(self, *, expression: str, expand: str | Unset = UNSET, context: _t.JiraExpressionEvaluateContextBean | Unset = UNSET) -> _t.JExpEvaluateJiraExpressionResultBean:
        """
        Evaluate Jira expression using enhanced search API

        Evaluates a Jira expression and returns its value. The difference between this and `eval` is that this endpoint uses the enhanced search API when evaluating JQL queries. This API is eventually consistent, unlike the strongly consistent `eval` API. This allows for better performance and scalability. In addition, this API's response for JQL evaluation is based on a scrolling view (backed by a `nextPageToken`) instead of a paginated view (backed by `startAt` and `totalCount`).

        This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.

        #### Context variables ####

        The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.

         *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to `null` if the request is anonymous.
         *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
         *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.
         *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.
         *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.
         *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.
         *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.
         *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.
         *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.

        In addition, you can pass custom context variables along with their types. You can then access them from the Jira expression by key. You can use the following variables in a custom context:

         *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.
         *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.
         *  `json`: A JSON object containing custom content.
         *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.  
        Permission to access Jira Software is required to access Jira Software context variables (`board` and `sprint`) or fields (for example, `issue.sprint`).
        """
        return cast('_t.JExpEvaluateJiraExpressionResultBean', self._runtime.call('evaluate_jsis_jira_expression', call_args({'expand': expand}, {'body': {'context': context, 'expression': expression}}, required=frozenset({'body'}))))

class _JiraSettingsResource:
    """Operations under ``jira_settings``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_application_property(self, *, key: str | Unset = UNSET, permission_level: str | Unset = UNSET, key_filter: str | Unset = UNSET) -> builtins.list[_t.ApplicationProperty]:
        """
        Get application property

        Returns all application properties or an application property.

        If you specify a value for the `key` parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of editable properties.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ApplicationProperty]', self._runtime.call('get_application_property', call_args({'key': key, 'permission_level': permission_level, 'key_filter': key_filter})))

    def list_advanced_settings(self) -> builtins.list[_t.ApplicationProperty]:
        """
        Get advanced settings

        Returns the application properties that are accessible on the *Advanced Settings* page. To navigate to the *Advanced Settings* page in Jira, choose the Jira icon > **Jira settings** > **System**, **General Configuration** and then click **Advanced Settings** (in the upper right).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ApplicationProperty]', self._runtime.call('get_advanced_settings', call_args({})))

    def set_application_property(self, *, id: str, body: _t.SimpleApplicationPropertyBean) -> _t.ApplicationProperty:
        """
        Set application property

        Changes the value of an application property. For example, you can change the value of the `jira.clone.prefix` from its default value of *CLONE -* to *Clone -* if you prefer sentence case capitalization. Editable properties are described below along with their default values.

        #### Advanced settings ####

        The advanced settings below are also accessible in [Jira](https://confluence.atlassian.com/x/vYXKM).

        | Key | Description | Default value |  
        | -- | -- | -- |  
        | `jira.clone.prefix` | The string of text prefixed to the title of a cloned issue. | `CLONE -` |  
        | `jira.date.picker.java.format` | The date format for the Java (server-side) generated dates. This must be the same as the `jira.date.picker.javascript.format` format setting. | `d/MMM/yy` |  
        | `jira.date.picker.javascript.format` | The date format for the JavaScript (client-side) generated dates. This must be the same as the `jira.date.picker.java.format` format setting. | `%e/%b/%y` |  
        | `jira.date.time.picker.java.format` | The date format for the Java (server-side) generated date times. This must be the same as the `jira.date.time.picker.javascript.format` format setting. | `dd/MMM/yy h:mm a` |  
        | `jira.date.time.picker.javascript.format` | The date format for the JavaScript (client-side) generated date times. This must be the same as the `jira.date.time.picker.java.format` format setting. | `%e/%b/%y %I:%M %p` |  
        | `jira.issue.actions.order` | The default order of actions (such as *Comments* or *Change history*) displayed on the issue view. | `asc` |  
        | `jira.view.issue.links.sort.order` | The sort order of the list of issue links on the issue view. | `type, status, priority` |  
        | `jira.comment.collapsing.minimum.hidden` | The minimum number of comments required for comment collapsing to occur. A value of `0` disables comment collapsing. | `4` |  
        | `jira.newsletter.tip.delay.days` | The number of days before a prompt to sign up to the Jira Insiders newsletter is shown. A value of `-1` disables this feature. | `7` |  


        #### Look and feel ####

        The settings listed below adjust the [look and feel](https://confluence.atlassian.com/x/VwCLLg).

        | Key | Description | Default value |  
        | -- | -- | -- |  
        | `jira.lf.date.time` | The [ time format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html). | `h:mm a` |  
        | `jira.lf.date.day` | The [ day format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html). | `EEEE h:mm a` |  
        | `jira.lf.date.complete` | The [ date and time format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html). | `dd/MMM/yy h:mm a` |  
        | `jira.lf.date.dmy` | The [ date format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html). | `dd/MMM/yy` |  
        | `jira.date.time.picker.use.iso8061` | When enabled, sets Monday as the first day of the week in the date picker, as specified by the ISO8601 standard. | `false` |  
        | `jira.lf.logo.url` | The URL of the logo image file. | `/images/icon-jira-logo.png` |  
        | `jira.lf.logo.show.application.title` | Controls the visibility of the application title on the sidebar. | `false` |  
        | `jira.lf.favicon.url` | The URL of the favicon. | `/favicon.ico` |  
        | `jira.lf.favicon.hires.url` | The URL of the high-resolution favicon. | `/images/64jira.png` |  
        | `jira.lf.navigation.bgcolour` | The background color of the sidebar. | `#0747A6` |  
        | `jira.lf.navigation.highlightcolour` | The color of the text and logo of the sidebar. | `#DEEBFF` |  
        | `jira.lf.hero.button.base.bg.colour` | The background color of the hero button. | `#3b7fc4` |  
        | `jira.title` | The text for the application title. The application title can also be set in *General settings*. | `Jira` |  
        | `jira.option.globalsharing` | Whether filters and dashboards can be shared with anyone signed into Jira. | `true` |  
        | `xflow.product.suggestions.enabled` | Whether to expose product suggestions for other Atlassian products within Jira. | `true` |  


        #### Other settings ####

        | Key | Description | Default value |  
        | -- | -- | -- |  
        | `jira.issuenav.criteria.autoupdate` | Whether instant updates to search criteria is active. | `true` |  


        *Note: Be careful when changing [application properties and advanced settings](https://confluence.atlassian.com/x/vYXKM).*

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ApplicationProperty', self._runtime.call('set_application_property', call_args({'id': id, 'body': body})))

    def get_configuration(self) -> _t.Configuration:
        """
        Get global settings

        Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.Configuration', self._runtime.call('get_configuration', call_args({})))

class _JqlResource:
    """Operations under ``jql``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_audit_entries(self, *, user_account_id: str | Unset = UNSET, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.AuditPage:
        """
        Get invalid JQL searches

        Returns JQL searches that need updating because Jira can no longer support them. Use the entries to find affected saved filters and JQL used by apps, automations, scripts, or REST integrations.

        Entries are ordered by creation time, newest first, and retained for three days. Pass the `nextPageToken` returned in a previous response to retrieve the next page. Results may be restricted to a user by external account ID.

        **[Permissions](#permissions) required:** *Administer Jira* global permission.
        """
        return cast('_t.AuditPage', self._runtime.call('get_audit_entries', call_args({'user_account_id': user_account_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def get_auto_complete(self) -> _t.JqlReferenceData:
        """
        Get field reference data (GET)

        Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

        To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.JqlReferenceData', self._runtime.call('get_auto_complete', call_args({})))

    def get_auto_complete_post(self, *, include_collapsed_fields: bool | Unset = UNSET, project_ids: builtins.list[int] | Unset = UNSET) -> _t.JqlReferenceData:
        """
        Get field reference data (POST)

        Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

        This operation can filter the custom fields returned by project. Invalid project IDs in `projectIds` are ignored. System fields are always returned.

        It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field `Component - Component[Dropdown]` enables dropdown fields `Component - cf[10061]` and `Component - cf[10062]` to be searched simultaneously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.JqlReferenceData', self._runtime.call('get_auto_complete_post', call_args({}, {'body': {'include_collapsed_fields': include_collapsed_fields, 'project_ids': project_ids}})))

    def get_field_auto_complete_for_query_string(self, *, field_name: str | Unset = UNSET, field_value: str | Unset = UNSET, predicate_name: str | Unset = UNSET, predicate_value: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.AutoCompleteSuggestions:
        """
        Get field auto complete suggestions

        Returns the JQL search auto complete suggestions for a field.

        Suggestions can be obtained by providing:

         *  `fieldName` to get a list of all values for the field.
         *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
         *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
         *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.AutoCompleteSuggestions', self._runtime.call('get_field_auto_complete_for_query_string', call_args({'field_name': field_name, 'field_value': field_value, 'predicate_name': predicate_name, 'predicate_value': predicate_value, 'max_results': max_results})))

    def parse_queries(self, *, validation: _t.ParseJqlQueriesValidation, queries: builtins.list[str]) -> _t.ParsedJqlQueries:
        """
        Parse JQL query

        Parses and validates JQL queries.

        Validation is performed in context of the current user.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.ParsedJqlQueries', self._runtime.call('parse_jql_queries', call_args({'validation': validation}, {'body': {'queries': queries}}, required=frozenset({'body'}))))

    def migrate_queries(self, *, query_strings: builtins.list[str] | Unset = UNSET) -> _t.ConvertedJqlQueries:
        """
        Convert user identifiers to account IDs in JQL queries

        Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.

        You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.ConvertedJqlQueries', self._runtime.call('migrate_queries', call_args({}, {'body': {'query_strings': query_strings}})))

    def sanitise_queries(self, *, queries: builtins.list[_t.JqlQueryToSanitize]) -> _t.SanitizedJqlQueries:
        """
        Sanitize JQL queries

        Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity.

        For example, if the query contains the clause *project = 'Secret project'*, and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with *project = 12345"* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.

        Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post).

        Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.SanitizedJqlQueries', self._runtime.call('sanitise_jql_queries', call_args({}, {'body': {'queries': queries}}, required=frozenset({'body'}))))

class _JqlFunctionsAppsResource:
    """Operations under ``jql_functions_apps``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_precomputations(self, *, function_key: builtins.list[str] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: str | Unset = UNSET) -> _t.PageBean2JqlFunctionPrecomputationBean:
        """
        Get precomputations (apps)

        Returns the list of a function's precomputations along with information about when they were created, updated, and last used. Each precomputation has a `value` \\- the JQL fragment to replace the custom function clause with.

        **[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

        The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.PageBean2JqlFunctionPrecomputationBean', self._runtime.call('get_precomputations', call_args({'function_key': function_key, 'start_at': start_at, 'max_results': max_results, 'order_by': order_by})))

    def update_precomputations(self, *, skip_not_found_precomputations: bool | Unset = UNSET, values: builtins.list[_t.JqlFunctionPrecomputationUpdateBean] | Unset = UNSET) -> _t.JqlFunctionPrecomputationUpdateResponse:
        """
        Update precomputations (apps)

        Update the precomputation value of a function created by a Forge/Connect app.

        **[Permissions](#permissions) required:** An API for apps to update their own precomputations.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.JqlFunctionPrecomputationUpdateResponse', self._runtime.call('update_precomputations', call_args({'skip_not_found_precomputations': skip_not_found_precomputations}, {'body': {'values': values}})))

    def get_precomputations_by_id(self, *, order_by: str | Unset = UNSET, precomputation_i_ds: builtins.list[str] | Unset = UNSET) -> _t.JqlFunctionPrecomputationGetByIdResponse:
        """
        Get precomputations by ID (apps)

        Returns function precomputations by IDs, along with information about when they were created, updated, and last used. Each precomputation has a `value` \\- the JQL fragment to replace the custom function clause with.

        **[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

        The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.JqlFunctionPrecomputationGetByIdResponse', self._runtime.call('get_precomputations_by_id', call_args({'order_by': order_by}, {'body': {'precomputation_i_ds': precomputation_i_ds}})))

class _LabelsResource:
    """Operations under ``labels``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, query: str | Unset = UNSET, scope: str | Unset = UNSET) -> _t.PageBeanString:
        """
        Get all labels

        Returns a [paginated](#pagination) list of labels.
        """
        return cast('_t.PageBeanString', self._runtime.call('get_all_labels', call_args({'start_at': start_at, 'max_results': max_results, 'query': query, 'scope': scope})))

class _LicenseMetricsResource:
    """Operations under ``license_metrics``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_license(self) -> _t.License:
        """
        Get license

        Returns licensing information about the Jira instance.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.License', self._runtime.call('get_license', call_args({})))

    def get_approximate_license_count(self) -> _t.LicenseMetric:
        """
        Get approximate license count

        Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.LicenseMetric', self._runtime.call('get_approximate_license_count', call_args({})))

    def get_approximate_application_license_count(self, *, application_key: _t.GetApproximateApplicationLicenseCountApplicationKey) -> _t.LicenseMetric:
        """
        Get approximate application license count

        Returns the total approximate number of user accounts for a single Jira license. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.LicenseMetric', self._runtime.call('get_approximate_application_license_count', call_args({'application_key': application_key})))

class _MigrationOfConnectModulesToForgeResource:
    """Operations under ``migration_of_connect_modules_to_forge``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get(self, *, connect_key: str, jira_issue_fields_key: str) -> _t.TaskProgress:
        """
        Get Connect issue field migration task

        Returns the details of a Connect issue field's migration to Forge.

        When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
        must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/). When the
        Forge version of the app is installed, Forge creates a
        [background task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks) to track the
        migration of field data across. This endpoint returns the status and other details of that background task.

        For more details, see
        [Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

        **[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.
        """
        return cast('_t.TaskProgress', self._runtime.call('connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get', call_args({'connect_key': connect_key, 'jira_issue_fields_key': jira_issue_fields_key})))

    def connect_to_forge_migration_task_submission_resource_submit_task_post(self, *, connect_key: str, jira_issue_fields_key: str, retrigger_completed_migration: bool | Unset = UNSET) -> None:
        """
        Submit Connect issue field migration task

        Submits a request to trigger migration of connect issue field to its Forge custom field counterpart.

        When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
        must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) modules.
        This endpoint triggers the background migration of field data. Use the GET endpoint to retrieve
        the status and progress of the task.

        For more details, see
        [Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

        **[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.
        """
        self._runtime.call('connect_to_forge_migration_task_submission_resource_submit_task_post', call_args({'connect_key': connect_key, 'jira_issue_fields_key': jira_issue_fields_key, 'retrigger_completed_migration': retrigger_completed_migration}))

class _MyselfResource:
    """Operations under ``myself``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_preference(self, *, key: str) -> str:
        """
        Get preference

        Returns the value of a preference of the current user.

        Note that these keys are deprecated:

         *  *jira.user.locale* The locale of the user. By default this is not set and the user takes the locale of the instance.
         *  *jira.user.timezone* The time zone of the user. By default this is not set and the user takes the timezone of the instance.

        These system preferences keys will be deprecated by 15/07/2024. You can still retrieve these keys, but it will not have any impact on Notification behaviour.

         *  *user.notifications.watcher* Whether the user gets notified when they are watcher.
         *  *user.notifications.assignee* Whether the user gets notified when they are assignee.
         *  *user.notifications.reporter* Whether the user gets notified when they are reporter.
         *  *user.notifications.mentions* Whether the user gets notified when they are mentions.

        Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('str', self._runtime.call('get_preference', call_args({'key': key})))

    def set_preference(self, *, key: str, body: str) -> Any:
        """
        Set preference

        Creates a preference for the user or updates a preference's value by sending a plain text string. For example, `false`. An arbitrary preference can be created with the value containing up to 255 characters. In addition, the following keys define system preferences that can be set or created:

         *  *user.notifications.mimetype* The mime type used in notifications sent to the user. Defaults to `html`.
         *  *user.default.share.private* Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ) are set to private. Defaults to `true`.
         *  *user.keyboard.shortcuts.disabled* Whether keyboard shortcuts are disabled. Defaults to `false`.
         *  *user.autowatch.disabled* Whether the user automatically watches issues they create or add a comment to. By default, not set: the user takes the instance autowatch setting.
         *  *user.notifiy.own.changes* Whether the user gets notified of their own changes.

        Note that these keys are deprecated:

         *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale.
         *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone.

        These system preferences keys will be deprecated by 15/07/2024. You can still use these keys to create arbitrary preferences, but it will not have any impact on Notification behaviour.

         *  *user.notifications.watcher* Whether the user gets notified when they are watcher.
         *  *user.notifications.assignee* Whether the user gets notified when they are assignee.
         *  *user.notifications.reporter* Whether the user gets notified when they are reporter.
         *  *user.notifications.mentions* Whether the user gets notified when they are mentions.

        Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('Any', self._runtime.call('set_preference', call_args({'key': key, 'body': body})))

    def remove_preference(self, *, key: str) -> None:
        """
        Delete preference

        Deletes a preference of the user, which restores the default value of system defined settings.

        Note that these keys are deprecated:

         *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale.
         *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone.

        Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        self._runtime.call('remove_preference', call_args({'key': key}))

    def get_locale(self) -> _t.Locale:
        """
        Get locale

        Returns the locale for the user.

        If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the *Accept-Language* header in the request. However, if this doesn't match a locale available Jira, the site default locale is returned.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.Locale', self._runtime.call('get_locale', call_args({})))

    def set_locale(self, *, locale: str | Unset = UNSET) -> Any:
        """
        Set locale

        Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API instead.

        Sets the locale of the user. The locale must be one supported by the instance of Jira.

        **[Permissions](#permissions) required:** Permission to access Jira.

        Deprecated.
        """
        return cast('Any', self._runtime.call('set_locale', call_args({}, {'body': {'locale': locale}})))

    def get_current_user(self, *, expand: str | Unset = UNSET) -> _t.User:
        """
        Get current user

        Returns details for the current user.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.User', self._runtime.call('get_current_user', call_args({'expand': expand})))

class _PermissionSchemesResource:
    """Operations under ``permission_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, expand: str | Unset = UNSET) -> _t.PermissionSchemes:
        """
        Get all permission schemes

        Returns all permission schemes.

        ### About permission schemes and grants ###

        A permission scheme is a collection of permission grants. A permission grant consists of a `holder` and a `permission`.

        #### Holder object ####

        The `holder` object contains information about the user or group being granted the permission. For example, the *Administer projects* permission is granted to a group named *Teams in space administrators*. In this case, the type is `"type": "group"`, and the parameter is the group name, `"parameter": "Teams in space administrators"` and the value is group ID, `"value": "ca85fac0-d974-40ca-a615-7af99c48d24f"`.

        The `holder` object is defined by the following properties:

         *  `type` Identifies the user or group (see the list of types below).
         *  `parameter` As a group's name can change, use of `value` is recommended. The value of this property depends on the `type`. For example, if the `type` is a group, then you need to specify the group name.
         *  `value` The value of this property depends on the `type`. If the `type` is a group, then you need to specify the group ID. For other `type` it has the same value as `parameter`

        The following `types` are available. The expected values for `parameter` and `value` are given in parentheses (some types may not have a `parameter` or `value`):

         *  `anyone` Grant for anonymous users.
         *  `applicationRole` Grant for users with access to the specified application (application name, application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL) for more information.
         *  `assignee` Grant for the user currently assigned to an issue.
         *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
         *  `groupCustomField` Grant for a user in the group selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).
         *  `projectLead` Grant for a project lead.
         *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` : project role ID).
         *  `reporter` Grant for the user who reported the issue.
         *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the customer portal but not Jira. See [Customizing Jira Service Desk permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
         *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey but that is deprecated and the account ID should be used, `value` : user ID).
         *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).

        #### Built-in permissions ####

        The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps can also define custom permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information.

        **Administration permissions**

         *  `ADMINISTER_PROJECTS`
         *  `EDIT_WORKFLOW`
         *  `EDIT_ISSUE_LAYOUT`

        **Project permissions**

         *  `BROWSE_PROJECTS`
         *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
         *  `SERVICEDESK_AGENT` (Jira Service Desk only)
         *  `VIEW_DEV_TOOLS` (Jira Software only)
         *  `VIEW_READONLY_WORKFLOW`

        **Issue permissions**

         *  `ASSIGNABLE_USER`
         *  `ASSIGN_ISSUES`
         *  `CLOSE_ISSUES`
         *  `CREATE_ISSUES`
         *  `DELETE_ISSUES`
         *  `EDIT_ISSUES`
         *  `LINK_ISSUES`
         *  `MODIFY_REPORTER`
         *  `MOVE_ISSUES`
         *  `RESOLVE_ISSUES`
         *  `SCHEDULE_ISSUES`
         *  `SET_ISSUE_SECURITY`
         *  `TRANSITION_ISSUES`

        **Voters and watchers permissions**

         *  `MANAGE_WATCHERS`
         *  `VIEW_VOTERS_AND_WATCHERS`

        **Comments permissions**

         *  `ADD_COMMENTS`
         *  `DELETE_ALL_COMMENTS`
         *  `DELETE_OWN_COMMENTS`
         *  `EDIT_ALL_COMMENTS`
         *  `EDIT_OWN_COMMENTS`

        **Attachments permissions**

         *  `CREATE_ATTACHMENTS`
         *  `DELETE_ALL_ATTACHMENTS`
         *  `DELETE_OWN_ATTACHMENTS`

        **Time tracking permissions**

         *  `DELETE_ALL_WORKLOGS`
         *  `DELETE_OWN_WORKLOGS`
         *  `EDIT_ALL_WORKLOGS`
         *  `EDIT_OWN_WORKLOGS`
         *  `WORK_ON_ISSUES`

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PermissionSchemes', self._runtime.call('get_all_permission_schemes', call_args({'expand': expand})))

    def create(self, *, body: _t.PermissionScheme, expand: str | Unset = UNSET) -> _t.PermissionScheme:
        """
        Create permission scheme

        Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PermissionScheme', self._runtime.call('create_permission_scheme', call_args({'expand': expand, 'body': body})))

    def get(self, *, scheme_id: int, expand: str | Unset = UNSET) -> _t.PermissionScheme:
        """
        Get permission scheme

        Returns a permission scheme.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PermissionScheme', self._runtime.call('get_permission_scheme', call_args({'scheme_id': scheme_id, 'expand': expand})))

    def update(self, *, scheme_id: int, body: _t.PermissionScheme, expand: str | Unset = UNSET) -> _t.PermissionScheme:
        """
        Update permission scheme

        Updates a permission scheme. Below are some important things to note when using this resource:

         *  If a permissions list is present in the request, then it is set in the permission scheme, overwriting *all existing* grants.
         *  If you want to update only the name and description, then do not send a permissions list in the request.
         *  Sending an empty list will remove all permission grants from the permission scheme.

        If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

        See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PermissionScheme', self._runtime.call('update_permission_scheme', call_args({'scheme_id': scheme_id, 'expand': expand, 'body': body})))

    def delete(self, *, scheme_id: int) -> None:
        """
        Delete permission scheme

        Deletes a permission scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_permission_scheme', call_args({'scheme_id': scheme_id}))

    def list_grants(self, *, scheme_id: int, expand: str | Unset = UNSET) -> _t.PermissionGrants:
        """
        Get permission scheme grants

        Returns all permission grants for a permission scheme.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PermissionGrants', self._runtime.call('get_permission_scheme_grants', call_args({'scheme_id': scheme_id, 'expand': expand})))

    def create_permission_grant(self, *, scheme_id: int, expand: str | Unset = UNSET, holder: _t.PermissionHolder | Unset = UNSET, id: int | Unset = UNSET, permission: str | Unset = UNSET, self_: str | Unset = UNSET) -> _t.PermissionGrant:
        """
        Create permission grant

        Creates a permission grant in a permission scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PermissionGrant', self._runtime.call('create_permission_grant', call_args({'scheme_id': scheme_id, 'expand': expand}, {'body': {'holder': holder, 'id': id, 'permission': permission, 'self': self_}})))

    def get_grant(self, *, scheme_id: int, permission_id: int, expand: str | Unset = UNSET) -> _t.PermissionGrant:
        """
        Get permission scheme grant

        Returns a permission grant.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PermissionGrant', self._runtime.call('get_permission_scheme_grant', call_args({'scheme_id': scheme_id, 'permission_id': permission_id, 'expand': expand})))

    def delete_entity(self, *, scheme_id: int, permission_id: int) -> None:
        """
        Delete permission scheme grant

        Deletes a permission grant from a permission scheme. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_permission_scheme_entity', call_args({'scheme_id': scheme_id, 'permission_id': permission_id}))

class _PermissionsResource:
    """Operations under ``permissions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_my(self, *, project_key: str | Unset = UNSET, project_id: str | Unset = UNSET, issue_key: str | Unset = UNSET, issue_id: str | Unset = UNSET, permissions: str | Unset = UNSET, project_uuid: str | Unset = UNSET, project_configuration_uuid: str | Unset = UNSET, comment_id: str | Unset = UNSET) -> _t.Permissions:
        """
        Get my permissions

        Returns a list of permissions indicating which permissions the user has. Details of the user's permissions can be obtained in a global, project, issue or comment context.

        The user is reported as having a project permission:

         *  in the global context, if the user has the project permission in any project.
         *  for a project, where the project permission is determined using issue data, if the user meets the permission's criteria for any issue in the project. Otherwise, if the user has the project permission in the project.
         *  for an issue, where a project permission is determined using issue data, if the user has the permission in the issue. Otherwise, if the user has the project permission in the project containing the issue.
         *  for a comment, where the user has both the permission to browse the comment and the project permission for the comment's parent issue. Only the BROWSE\\_PROJECTS permission is supported. If a `commentId` is provided whose `permissions` does not equal BROWSE\\_PROJECTS, a 400 error will be returned.

        This means that users may be shown as having an issue permission (such as EDIT\\_ISSUES) in the global context or a project context but may not have the permission for any or all issues. For example, if Reporters have the EDIT\\_ISSUES permission a user would be shown as having this permission in the global context or the context of a project, because any user can be a reporter. However, if they are not the user who reported the issue queried they would not have EDIT\\_ISSUES permission for that issue.

        For [Jira Service Management project permissions](https://support.atlassian.com/jira-cloud-administration/docs/customize-jira-service-management-permissions/), this will be evaluated similarly to a user in the customer portal. For example, if the BROWSE\\_PROJECTS permission is granted to Service Project Customer - Portal Access, any users with access to the customer portal will have the BROWSE\\_PROJECTS permission.

        Global permissions are unaffected by context.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.Permissions', self._runtime.call('get_my_permissions', call_args({'project_key': project_key, 'project_id': project_id, 'issue_key': issue_key, 'issue_id': issue_id, 'permissions': permissions, 'project_uuid': project_uuid, 'project_configuration_uuid': project_configuration_uuid, 'comment_id': comment_id})))

    def list_all(self) -> _t.Permissions:
        """
        Get all permissions

        Returns all permissions, including:

         *  global permissions.
         *  project permissions.
         *  global permissions added by plugins.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.Permissions', self._runtime.call('get_all_permissions', call_args({})))

    def list_bulk(self, *, account_id: str | Unset = UNSET, global_permissions: builtins.list[str] | Unset = UNSET, project_permissions: builtins.list[_t.BulkProjectPermissions] | Unset = UNSET) -> _t.BulkPermissionGrants:
        """
        Get bulk permissions

        Returns:

         *  for a list of global permissions, the global permissions granted to a user.
         *  for a list of project permissions and lists of projects and issues, for each project permission a list of the projects and issues a user can access or manipulate.

        If no account ID is provided, the operation returns details for the logged in user.

        Note that:

         *  Invalid project and issue IDs are ignored.
         *  A maximum of 1000 projects and 1000 issues can be checked.
         *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and `projectPermissions.issues` are ignored.
         *  Empty strings in `projectPermissions.permissions` are ignored.

        **Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

         *  **Classic**: `read:jira-work`
         *  **Granular**: `read:permission:jira`

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users, otherwise none. However, Connect apps can make a call from the app server to the product to obtain permission details for any user, without admin permission. This Connect app ability doesn't apply to calls made using AP.request() in a browser.
        """
        return cast('_t.BulkPermissionGrants', self._runtime.call('get_bulk_permissions', call_args({}, {'body': {'account_id': account_id, 'global_permissions': global_permissions, 'project_permissions': project_permissions}})))

    def list_permitted_projects(self, *, permissions: builtins.list[str]) -> _t.PermittedProjects:
        """
        Get permitted projects

        Returns all the projects where the user is granted a list of project permissions.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.PermittedProjects', self._runtime.call('get_permitted_projects', call_args({}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

class _PlansResource:
    """Operations under ``plans``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, include_trashed: bool | Unset = UNSET, include_archived: bool | Unset = UNSET, cursor: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageWithCursorGetPlanResponseForPage:
        """
        Get plans paginated

        Returns a [paginated](#pagination) list of plans.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageWithCursorGetPlanResponseForPage', self._runtime.call('get_plans', call_args({'include_trashed': include_trashed, 'include_archived': include_archived, 'cursor': cursor, 'max_results': max_results})))

    def create(self, *, issue_sources: builtins.list[_t.CreateIssueSourceRequest], name: str, scheduling: _t.CreateSchedulingRequest, use_group_id: bool | Unset = UNSET, cross_project_releases: builtins.list[_t.CreateCrossProjectReleaseRequest] | Unset = UNSET, custom_fields: builtins.list[_t.CreateCustomFieldRequest] | Unset = UNSET, exclusion_rules: _t.CreateExclusionRulesRequest | Unset = UNSET, lead_account_id: str | Unset = UNSET, permissions: builtins.list[_t.CreatePermissionRequest] | Unset = UNSET) -> int:
        """
        Create plan

        Creates a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('int', self._runtime.call('create_plan', call_args({'use_group_id': use_group_id}, {'body': {'cross_project_releases': cross_project_releases, 'custom_fields': custom_fields, 'exclusion_rules': exclusion_rules, 'issue_sources': issue_sources, 'lead_account_id': lead_account_id, 'name': name, 'permissions': permissions, 'scheduling': scheduling}}, required=frozenset({'body'}))))

    def get(self, *, plan_id: int, use_group_id: bool | Unset = UNSET) -> _t.GetPlanResponse:
        """
        Get plan

        Returns a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.GetPlanResponse', self._runtime.call('get_plan', call_args({'plan_id': plan_id, 'use_group_id': use_group_id})))

    def update(self, *, plan_id: int, body: builtins.dict[str, Any], use_group_id: bool | Unset = UNSET) -> Any:
        """
        Update plan

        Updates any of the following details of a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

         *  name
         *  leadAccountId
         *  scheduling
            
             *  estimation with StoryPoints, Days or Hours as possible values
             *  startDate
                
                 *  type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
                 *  dateCustomFieldId
             *  endDate
                
                 *  type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
                 *  dateCustomFieldId
             *  inferredDates with None, SprintDates or ReleaseDates as possible values
             *  dependencies with Sequential or Concurrent as possible values
         *  issueSources
            
             *  type with Board, Project or Filter as possible values
             *  value
         *  exclusionRules
            
             *  numberOfDaysToShowCompletedIssues
             *  issueIds
             *  workStatusIds
             *  workStatusCategoryIds
             *  issueTypeIds
             *  releaseIds
         *  crossProjectReleases
            
             *  name
             *  releaseIds
         *  customFields
            
             *  customFieldId
             *  filter
         *  permissions
            
             *  type with View or Edit as possible values
             *  holder
                
                 *  type with Group or AccountId as possible values
                 *  value

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        *Note that "add" operations do not respect array indexes in target locations. Call the "Get plan" endpoint to find out the order of array elements.*
        """
        return cast('Any', self._runtime.call('update_plan', call_args({'plan_id': plan_id, 'use_group_id': use_group_id, 'body': body})))

    def archive(self, *, plan_id: int) -> Any:
        """
        Archive plan

        Archives a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('archive_plan', call_args({'plan_id': plan_id})))

    def duplicate(self, *, plan_id: int, name: str) -> int:
        """
        Duplicate plan

        Duplicates a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('int', self._runtime.call('duplicate_plan', call_args({'plan_id': plan_id}, {'body': {'name': name}}, required=frozenset({'body'}))))

    def trash(self, *, plan_id: int) -> Any:
        """
        Trash plan

        Moves a plan to trash.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('trash_plan', call_args({'plan_id': plan_id})))

class _PoliciesResource:
    """Operations under ``policies``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.PolicySummaryResponse:
        """
        Get all policies

        Returns a paginated summary of all known policies, including their names, descriptions, and which projects each policy is assigned to.

        Omit cursor for the first page and pass the returned \\{@code nextPageCursor\\} for subsequent pages. The legacy \\{@code startAt\\} and \\{@code total\\} fields are null because an offset and total are not available in cursor mode.
        """
        return cast('_t.PolicySummaryResponse', self._runtime.call('list_policies', call_args({'start_at': start_at, 'max_results': max_results, 'cursor': cursor})))

    def get_state(self, *, project_id_or_key: str) -> builtins.list[_t.StatePolicyDocument]:
        """
        Get project policy state

        Returns the policies applied to a project.
        """
        return cast('builtins.list[_t.StatePolicyDocument]', self._runtime.call('get_policy_state', call_args({'project_id_or_key': project_id_or_key})))

    def set(self, *, project_id_or_key: str, policy_ids: builtins.list[str] | Unset = UNSET) -> Any:
        """
        Set the policies applied to a project

        Sets the complete set of policies on a project (full replacement).

        A project may have at most one policy assigned. Jira Admin only.
        """
        return cast('Any', self._runtime.call('set_project_policies', call_args({'project_id_or_key': project_id_or_key}, {'body': {'policy_ids': policy_ids}})))

    def list_project_rules(self, *, project_id_or_key: str, rule_type_ids: builtins.list[str] | Unset = UNSET) -> builtins.list[_t.StatePolicyRule]:
        """
        Get project policy rules

        Returns the configuration of the queried rule type IDs for a given project.

        Use this to check whether specific rules are active on a project, and if so, how they are configured.

        Only rules that are actually active on the project are returned. Rules that are not active are omitted from the response.
        """
        return cast('builtins.list[_t.StatePolicyRule]', self._runtime.call('get_project_rules', call_args({'project_id_or_key': project_id_or_key, 'rule_type_ids': rule_type_ids})))

    def validate_application(self, *, project_id_or_key: str, policy_ids: builtins.list[str] | Unset = UNSET) -> Any:
        """
        Validate policy application to a project

        Validates whether a set of policies can be applied to a project without actually applying them.

        Runs the compliance checks for each specified policy against the project's current configuration. This can be called before applying policies to preview potential issues. Jira Admin only.
        """
        return cast('Any', self._runtime.call('validate_policy_application', call_args({'project_id_or_key': project_id_or_key}, {'body': {'policy_ids': policy_ids}})))

    def add_to_projects(self, *, policy_id: str, project_ids: builtins.list[int] | Unset = UNSET) -> _t.BulkPolicyOperationResponse:
        """
        Apply a policy to projects

        Adds a policy to a set of projects. Handles partial results: each project is processed independently, and failures on individual projects do not prevent the operation from proceeding on the remaining projects.

        Jira Admin only. Returns 200 with the successful and failed project results if at least one project succeeds, or 409 if none do.
        """
        return cast('_t.BulkPolicyOperationResponse', self._runtime.call('add_policy_to_projects', call_args({'policy_id': policy_id}, {'body': {'project_ids': project_ids}})))

    def remove_from_projects(self, *, policy_id: str, project_ids: builtins.list[int] | Unset = UNSET) -> _t.BulkPolicyOperationResponse:
        """
        Remove a policy from projects

        Removes a policy from a set of projects. Handles partial results: each project is processed independently, and failures on individual projects do not prevent the operation from proceeding on the remaining projects.

        Jira Admin only. Returns 200 with the successful and failed project results if at least one project succeeds, or 409 if none do.
        """
        return cast('_t.BulkPolicyOperationResponse', self._runtime.call('remove_policy_from_projects', call_args({'policy_id': policy_id}, {'body': {'project_ids': project_ids}})))

class _PrioritySchemesResource:
    """Operations under ``priority_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_many(self, *, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, priority_id: builtins.list[int] | Unset = UNSET, scheme_id: builtins.list[int] | Unset = UNSET, scheme_name: str | Unset = UNSET, only_default: bool | Unset = UNSET, order_by: _t.GetPrioritySchemesOrderBy | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects:
        """
        Get priority schemes

        Returns a [paginated](#pagination) list of priority schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects', self._runtime.call('get_priority_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'priority_id': priority_id, 'scheme_id': scheme_id, 'scheme_name': scheme_name, 'only_default': only_default, 'order_by': order_by, 'expand': expand})))

    def create(self, *, default_priority_id: int, name: str, priority_ids: builtins.list[int], description: str | Unset = UNSET, mappings: _t.PriorityMapping | Unset = UNSET, project_ids: builtins.list[int] | Unset = UNSET) -> _t.PrioritySchemeId:
        """
        Create priority scheme

        Creates a new priority scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PrioritySchemeId', self._runtime.call('create_priority_scheme', call_args({}, {'body': {'default_priority_id': default_priority_id, 'description': description, 'mappings': mappings, 'name': name, 'priority_ids': priority_ids, 'project_ids': project_ids}}, required=frozenset({'body'}))))

    def suggested_priorities_for_mappings(self, *, max_results: int | Unset = UNSET, priorities: _t.SuggestedMappingsForPrioritiesRequestBean | Unset = UNSET, projects: _t.SuggestedMappingsForProjectsRequestBean | Unset = UNSET, scheme_id: int | Unset = UNSET, start_at: int | Unset = UNSET) -> _t.PageBeanPriorityWithSequence:
        """
        Suggested priorities for mappings

        Returns a [paginated](#pagination) list of priorities that would require mapping, given a change in priorities or projects associated with a priority scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanPriorityWithSequence', self._runtime.call('suggested_priorities_for_mappings', call_args({}, {'body': {'max_results': max_results, 'priorities': priorities, 'projects': projects, 'scheme_id': scheme_id, 'start_at': start_at}})))

    def list_available_priorities_by(self, *, scheme_id: str, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, query: str | Unset = UNSET, exclude: builtins.list[str] | Unset = UNSET) -> _t.PageBeanPriorityWithSequence:
        """
        Get available priorities by priority scheme

        Returns a [paginated](#pagination) list of priorities available for adding to a priority scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanPriorityWithSequence', self._runtime.call('get_available_priorities_by_priority_scheme', call_args({'start_at': start_at, 'max_results': max_results, 'query': query, 'scheme_id': scheme_id, 'exclude': exclude})))

    def update(self, *, scheme_id: int, default_priority_id: int | Unset = UNSET, description: str | Unset = UNSET, mappings: _t.PriorityMapping | Unset = UNSET, name: str | Unset = UNSET, priorities: _t.UpdatePrioritiesInSchemeRequestBean | Unset = UNSET, projects: _t.UpdateProjectsInSchemeRequestBean | Unset = UNSET) -> _t.UpdatePrioritySchemeResponseBean:
        """
        Update priority scheme

        Updates a priority scheme. This includes its details, the lists of priorities and projects in it

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.UpdatePrioritySchemeResponseBean', self._runtime.call('update_priority_scheme', call_args({'scheme_id': scheme_id}, {'body': {'default_priority_id': default_priority_id, 'description': description, 'mappings': mappings, 'name': name, 'priorities': priorities, 'projects': projects}})))

    def delete(self, *, scheme_id: int) -> Any:
        """
        Delete priority scheme

        Deletes a priority scheme.

        This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_priority_scheme', call_args({'scheme_id': scheme_id})))

    def list_priorities_by(self, *, scheme_id: str, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET) -> _t.PageBeanPriorityWithSequence:
        """
        Get priorities by priority scheme

        Returns a [paginated](#pagination) list of priorities by scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanPriorityWithSequence', self._runtime.call('get_priorities_by_priority_scheme', call_args({'start_at': start_at, 'max_results': max_results, 'scheme_id': scheme_id})))

    def list_projects_by(self, *, scheme_id: str, start_at: str | Unset = UNSET, max_results: str | Unset = UNSET, project_id: builtins.list[int] | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBeanProject:
        """
        Get projects by priority scheme

        Returns a [paginated](#pagination) list of projects by scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanProject', self._runtime.call('get_projects_by_priority_scheme', call_args({'start_at': start_at, 'max_results': max_results, 'project_id': project_id, 'scheme_id': scheme_id, 'query': query})))

class _ProjectAvatarsResource:
    """Operations under ``project_avatars``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def update(self, *, project_id_or_key: str, id: str, file_name: str | Unset = UNSET, is_deletable: bool | Unset = UNSET, is_selected: bool | Unset = UNSET, is_system_avatar: bool | Unset = UNSET, owner: str | Unset = UNSET, urls: builtins.dict[str, str] | Unset = UNSET) -> Any:
        """
        Set project avatar

        Sets the avatar displayed for a project.

        Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('Any', self._runtime.call('update_project_avatar', call_args({'project_id_or_key': project_id_or_key}, {'body': {'file_name': file_name, 'id': id, 'is_deletable': is_deletable, 'is_selected': is_selected, 'is_system_avatar': is_system_avatar, 'owner': owner, 'urls': urls}}, required=frozenset({'body'}))))

    def delete(self, *, project_id_or_key: str, id: int) -> None:
        """
        Delete project avatar

        Deletes a custom avatar from a project. Note that system avatars cannot be deleted.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        self._runtime.call('delete_project_avatar', call_args({'project_id_or_key': project_id_or_key, 'id': id}))

    def create(self, *, project_id_or_key: str, body: str | bytes | PathLike[str], x: int | Unset = UNSET, y: int | Unset = UNSET, size: int | Unset = UNSET) -> _t.Avatar:
        """
        Load project avatar

        Loads an avatar for a project.

        Specify the avatar's local file location in the body of the request. Also, include the following headers:

         *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
         *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

        For example:  
        `curl --request POST `

        `--user email@example.com:<api_token> `

        `--header 'X-Atlassian-Token: no-check' `

        `--header 'Content-Type: image/< image_type>' `

        `--data-binary "<@/path/to/file/with/your/avatar>" `

        `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

        The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

        The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

        After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project's displayed avatar.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('_t.Avatar', self._runtime.call('create_project_avatar', call_args({'project_id_or_key': project_id_or_key, 'x': x, 'y': y, 'size': size, 'body': body})))

    def list(self, *, project_id_or_key: str) -> _t.ProjectAvatars:
        """
        Get all project avatars

        Returns all project avatars, grouped by system and custom avatars.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.ProjectAvatars', self._runtime.call('get_all_project_avatars', call_args({'project_id_or_key': project_id_or_key})))

class _ProjectCategoriesResource:
    """Operations under ``project_categories``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self) -> builtins.list[_t.ProjectCategory]:
        """
        Get all project categories

        Returns all project categories.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('builtins.list[_t.ProjectCategory]', self._runtime.call('get_all_project_categories', call_args({})))

    def create(self, *, description: str | Unset = UNSET, id: str | Unset = UNSET, name: str | Unset = UNSET, self_: str | Unset = UNSET) -> _t.ProjectCategory:
        """
        Create project category

        Creates a project category.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectCategory', self._runtime.call('create_project_category', call_args({}, {'body': {'description': description, 'id': id, 'name': name, 'self': self_}})))

    def get(self, *, id: int) -> _t.ProjectCategory:
        """
        Get project category by ID

        Returns a project category.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.ProjectCategory', self._runtime.call('get_project_category_by_id', call_args({'id': id})))

    def update(self, *, id: int, body: _t.ProjectCategory) -> _t.UpdatedProjectCategory:
        """
        Update project category

        Updates a project category.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.UpdatedProjectCategory', self._runtime.call('update_project_category', call_args({'id': id, 'body': body})))

    def remove(self, *, id: int) -> None:
        """
        Delete project category

        Deletes a project category.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('remove_project_category', call_args({'id': id}))

class _ProjectClassificationLevelsResource:
    """Operations under ``project_classification_levels``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_project_classification_config(self, *, project_id_or_key: str) -> Any:
        """
        Get the classification configuration for a project

        Returns the consolidated classification configuration for a project's admin settings page.

        This includes permitted classification levels (with status), the project's default classification level, the organization's default classification level, and the container override setting.

        **[Permissions](#permissions) required:**

         *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('get_project_classification_config', call_args({'project_id_or_key': project_id_or_key})))

    def get_default_project_classification(self, *, project_id_or_key: str) -> Any:
        """
        Get the default data classification level of a project

        Returns the default data classification for a project.

        **[Permissions](#permissions) required:**

         *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('get_default_project_classification', call_args({'project_id_or_key': project_id_or_key})))

    def update_default_project_classification(self, *, project_id_or_key: str, id: str) -> Any:
        """
        Update the default data classification level of a project

        Updates the default data classification level for a project.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_default_project_classification', call_args({'project_id_or_key': project_id_or_key}, {'body': {'id': id}}, required=frozenset({'body'}))))

    def remove_default_project_classification(self, *, project_id_or_key: str) -> Any:
        """
        Remove the default data classification level from a project

        Remove the default data classification level for a project.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_default_project_classification', call_args({'project_id_or_key': project_id_or_key})))

class _ProjectComponentsResource:
    """Operations under ``project_components``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def find_components_for_projects(self, *, project_ids_or_keys: builtins.list[str] | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: _t.FindComponentsForProjectsOrderBy | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBean2ComponentJsonBean:
        """
        Find components for projects

        Returns a [paginated](#pagination) list of all components in a project, including global (Compass) components when applicable.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.PageBean2ComponentJsonBean', self._runtime.call('find_components_for_projects', call_args({'project_ids_or_keys': project_ids_or_keys, 'start_at': start_at, 'max_results': max_results, 'order_by': order_by, 'query': query})))

    def create_component(self, *, ari: str | Unset = UNSET, assignee: _t.User | Unset = UNSET, assignee_type: _t.ProjectComponentAssigneeType | Unset = UNSET, description: str | Unset = UNSET, id: str | Unset = UNSET, is_assignee_type_valid: bool | Unset = UNSET, lead: _t.User | Unset = UNSET, lead_account_id: str | Unset = UNSET, lead_user_name: str | Unset = UNSET, metadata: builtins.dict[str, str] | Unset = UNSET, name: str | Unset = UNSET, project: str | Unset = UNSET, project_id: int | Unset = UNSET, real_assignee: _t.User | Unset = UNSET, real_assignee_type: _t.ProjectComponentRealAssigneeType | Unset = UNSET, self_: str | Unset = UNSET) -> _t.ProjectComponent:
        """
        Create component

        Creates a component. Use components to provide containers for issues within a project. Use components to provide containers for issues within a project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the component is created or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectComponent', self._runtime.call('create_component', call_args({}, {'body': {'ari': ari, 'assignee': assignee, 'assignee_type': assignee_type, 'description': description, 'id': id, 'is_assignee_type_valid': is_assignee_type_valid, 'lead': lead, 'lead_account_id': lead_account_id, 'lead_user_name': lead_user_name, 'metadata': metadata, 'name': name, 'project': project, 'project_id': project_id, 'real_assignee': real_assignee, 'real_assignee_type': real_assignee_type, 'self': self_}})))

    def get_component(self, *, id: str) -> _t.ProjectComponent:
        """
        Get component

        Returns a component.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for project containing the component.
        """
        return cast('_t.ProjectComponent', self._runtime.call('get_component', call_args({'id': id})))

    def update_component(self, *, id: str, body: _t.ProjectComponent) -> _t.ProjectComponent:
        """
        Update component

        Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an empty string ("") the component lead is removed.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectComponent', self._runtime.call('update_component', call_args({'id': id, 'body': body})))

    def delete_component(self, *, id: str, move_issues_to: str | Unset = UNSET) -> None:
        """
        Delete component

        Deletes a component.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_component', call_args({'id': id, 'move_issues_to': move_issues_to}))

    def list_component_related_issues(self, *, id: str) -> _t.ComponentIssuesCount:
        """
        Get component issues count

        Returns the counts of issues assigned to the component.

        This operation can be accessed anonymously.

        **Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

         *  **Classic**: `read:jira-work`
         *  **Granular**: `read:field:jira`, `read:project.component:jira`

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.ComponentIssuesCount', self._runtime.call('get_component_related_issues', call_args({'id': id})))

    def get_paginated(self, *, project_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: _t.GetProjectComponentsPaginatedOrderBy | Unset = UNSET, component_source: _t.GetProjectComponentsPaginatedComponentSource | Unset = UNSET, query: str | Unset = UNSET) -> _t.PageBeanComponentWithIssueCount:
        """
        Get project components paginated

        Returns a [paginated](#pagination) list of all components in a project. See the [Get project components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a full list of versions without pagination.

        If your project uses Compass components, this API will return a list of Compass components that are linked to issues in that project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.PageBeanComponentWithIssueCount', self._runtime.call('get_project_components_paginated', call_args({'project_id_or_key': project_id_or_key, 'start_at': start_at, 'max_results': max_results, 'order_by': order_by, 'component_source': component_source, 'query': query})))

    def list(self, *, project_id_or_key: str, component_source: _t.GetProjectComponentsComponentSource | Unset = UNSET) -> builtins.list[_t.ProjectComponent]:
        """
        Get project components

        Returns all components in a project. See the [Get project components paginated](#api-rest-api-3-project-projectIdOrKey-component-get) resource if you want to get a full list of components with pagination.

        If your project uses Compass components, this API will return a paginated list of Compass components that are linked to issues in that project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('builtins.list[_t.ProjectComponent]', self._runtime.call('get_project_components', call_args({'project_id_or_key': project_id_or_key, 'component_source': component_source})))

class _ProjectEmailResource:
    """Operations under ``project_email``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self, *, project_id: int) -> _t.ProjectEmailAddress:
        """
        Get project's sender email

        Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.ProjectEmailAddress', self._runtime.call('get_project_email', call_args({'project_id': project_id})))

    def update(self, *, project_id: int, email_address: str | Unset = UNSET, email_address_status: builtins.list[str] | Unset = UNSET) -> Any:
        """
        Set project's sender email

        Sets the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

        If `emailAddress` is an empty string, the default email address is restored.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('Any', self._runtime.call('update_project_email', call_args({'project_id': project_id}, {'body': {'email_address': email_address, 'email_address_status': email_address_status}})))

class _ProjectFeaturesResource:
    """Operations under ``project_features``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_features_for_project(self, *, project_id_or_key: str) -> _t.ContainerForProjectFeatures:
        """
        Get project features

        Returns the list of features for a project.
        """
        return cast('_t.ContainerForProjectFeatures', self._runtime.call('get_features_for_project', call_args({'project_id_or_key': project_id_or_key})))

    def toggle_feature_for_project(self, *, project_id_or_key: str, feature_key: str, body: _t.ProjectFeatureState) -> _t.ContainerForProjectFeatures:
        """
        Set project feature state

        Sets the state of a project feature.
        """
        return cast('_t.ContainerForProjectFeatures', self._runtime.call('toggle_feature_for_project', call_args({'project_id_or_key': project_id_or_key, 'feature_key': feature_key, 'body': body})))

class _ProjectKeyAndNameValidationResource:
    """Operations under ``project_key_and_name_validation``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def validate_project_key(self, *, key: str | Unset = UNSET) -> _t.ErrorCollection:
        """
        Validate project key

        Validates a project key by confirming the key is a valid string and not in use.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.ErrorCollection', self._runtime.call('validate_project_key', call_args({'key': key})))

    def get_valid_project_key(self, *, key: str | Unset = UNSET) -> str:
        """
        Get valid project key

        Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.

        **[Permissions](#permissions) required:** None.
        """
        return cast('str', self._runtime.call('get_valid_project_key', call_args({'key': key})))

    def get_valid_project_name(self, *, name: str) -> str:
        """
        Get valid project name

        Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.

        **[Permissions](#permissions) required:** None.
        """
        return cast('str', self._runtime.call('get_valid_project_name', call_args({'name': name})))

class _ProjectPermissionSchemesResource:
    """Operations under ``project_permission_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_project_issue_security_scheme(self, *, project_key_or_id: str) -> _t.SecurityScheme:
        """
        Get project issue security scheme

        Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('_t.SecurityScheme', self._runtime.call('get_project_issue_security_scheme', call_args({'project_key_or_id': project_key_or_id})))

    def get_assigned_permission_scheme(self, *, project_key_or_id: str, expand: str | Unset = UNSET) -> _t.PermissionScheme:
        """
        Get assigned permission scheme

        Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('_t.PermissionScheme', self._runtime.call('get_assigned_permission_scheme', call_args({'project_key_or_id': project_key_or_id, 'expand': expand})))

    def assign_permission_scheme(self, *, project_key_or_id: str, id: int, expand: str | Unset = UNSET) -> _t.PermissionScheme:
        """
        Assign permission scheme

        Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)
        """
        return cast('_t.PermissionScheme', self._runtime.call('assign_permission_scheme', call_args({'project_key_or_id': project_key_or_id, 'expand': expand}, {'body': {'id': id}}, required=frozenset({'body'}))))

    def get_security_levels_for_project(self, *, project_key_or_id: str) -> _t.ProjectIssueSecurityLevels:
        """
        Get project issue security levels

        Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.
        """
        return cast('_t.ProjectIssueSecurityLevels', self._runtime.call('get_security_levels_for_project', call_args({'project_key_or_id': project_key_or_id})))

class _ProjectPropertiesResource:
    """Operations under ``project_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_keys(self, *, project_id_or_key: str) -> _t.PropertyKeys:
        """
        Get project property keys

        Returns all [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys for the project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_project_property_keys', call_args({'project_id_or_key': project_id_or_key})))

    def get(self, *, project_id_or_key: str, property_key: str) -> _t.EntityProperty:
        """
        Get project property

        Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_project_property', call_args({'project_id_or_key': project_id_or_key, 'property_key': property_key})))

    def set(self, *, project_id_or_key: str, property_key: str, body: Any) -> Any:
        """
        Set project property

        Sets the value of the [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). You can use project properties to store custom data against the project.

        The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the property is created.
        """
        return cast('Any', self._runtime.call('set_project_property', call_args({'project_id_or_key': project_id_or_key, 'property_key': property_key, 'body': body})))

    def delete(self, *, project_id_or_key: str, property_key: str) -> None:
        """
        Delete project property

        Deletes the [property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) from a project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.
        """
        self._runtime.call('delete_project_property', call_args({'project_id_or_key': project_id_or_key, 'property_key': property_key}))

class _ProjectRoleActorsResource:
    """Operations under ``project_role_actors``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def set_actors(self, *, project_id_or_key: str, id: int, body: _t.ProjectRoleActorsUpdateBean) -> _t.ProjectRole:
        """
        Set actors for project role

        Sets the actors for a project role for a project, replacing all existing actors.

        To add actors to the project without overwriting the existing list, use [Add actors to project role](#api-rest-api-3-project-projectIdOrKey-role-id-post).

        **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('set_actors', call_args({'project_id_or_key': project_id_or_key, 'id': id, 'body': body})))

    def add_actor_users(self, *, project_id_or_key: str, id: int, group: builtins.list[str] | Unset = UNSET, group_id: builtins.list[str] | Unset = UNSET, user: builtins.list[str] | Unset = UNSET) -> _t.ProjectRole:
        """
        Add actors to project role

        Adds actors to a project role for the project.

        To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-projectIdOrKey-role-id-put).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('add_actor_users', call_args({'project_id_or_key': project_id_or_key, 'id': id}, {'body': {'group': group, 'group_id': group_id, 'user': user}})))

    def delete_actor(self, *, project_id_or_key: str, id: int, user: str | Unset = UNSET, group: str | Unset = UNSET, group_id: str | Unset = UNSET) -> None:
        """
        Delete actors from project role

        Deletes actors from a project role for the project.

        To remove default actors from the project role, use [Delete default actors from project role](#api-rest-api-3-role-id-actors-delete).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_actor', call_args({'project_id_or_key': project_id_or_key, 'id': id, 'user': user, 'group': group, 'group_id': group_id}))

    def get_for_role(self, *, id: int) -> _t.ProjectRole:
        """
        Get default actors for project role

        Returns the [default actors](#api-rest-api-3-resolution-get) for the project role.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('get_project_role_actors_for_role', call_args({'id': id})))

    def add_to_role(self, *, id: int, group: builtins.list[str] | Unset = UNSET, group_id: builtins.list[str] | Unset = UNSET, user: builtins.list[str] | Unset = UNSET) -> _t.ProjectRole:
        """
        Add default actors to project role

        Adds [default actors](#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request.

        Changing a project role's default actors does not affect project role members for projects already created.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('add_project_role_actors_to_role', call_args({'id': id}, {'body': {'group': group, 'group_id': group_id, 'user': user}})))

    def delete_from_role(self, *, id: int, user: str | Unset = UNSET, group_id: str | Unset = UNSET, group: str | Unset = UNSET) -> _t.ProjectRole:
        """
        Delete default actors from project role

        Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request.

        Changing a project role's default actors does not affect project role members for projects already created.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('delete_project_role_actors_from_role', call_args({'id': id, 'user': user, 'group_id': group_id, 'group': group})))

class _ProjectRolesResource:
    """Operations under ``project_roles``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, project_id_or_key: str) -> builtins.dict[str, str]:
        """
        Get project roles for project

        Returns a list of [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) for the project returning the name and self URL for each role.

        Note that all project roles are shared with all projects in Jira Cloud. See [Get all project roles](#api-rest-api-3-role-get) for more information.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.dict[str, str]', self._runtime.call('get_project_roles', call_args({'project_id_or_key': project_id_or_key})))

    def get(self, *, project_id_or_key: str, id: int, exclude_inactive_users: bool | Unset = UNSET) -> _t.ProjectRole:
        """
        Get project role for project

        Returns a project role's details and actors associated with the project. The list of actors is sorted by display name.

        To check whether a user belongs to a role based on their group memberships, use [Get user](#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('get_project_role', call_args({'project_id_or_key': project_id_or_key, 'id': id, 'exclude_inactive_users': exclude_inactive_users})))

    def list_details(self, *, project_id_or_key: str, current_member: bool | Unset = UNSET, exclude_connect_addons: bool | Unset = UNSET, exclude_other_service_roles: bool | Unset = UNSET) -> builtins.list[_t.ProjectRoleDetails]:
        """
        Get project role details

        Returns all [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) and the details for each role. Note that the list of project roles is common to all projects.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('builtins.list[_t.ProjectRoleDetails]', self._runtime.call('get_project_role_details', call_args({'project_id_or_key': project_id_or_key, 'current_member': current_member, 'exclude_connect_addons': exclude_connect_addons, 'exclude_other_service_roles': exclude_other_service_roles})))

    def list_all(self) -> builtins.list[_t.ProjectRole]:
        """
        Get all project roles

        Gets a list of all project roles, complete with project role details and default actors.

        ### About project roles ###

        [Project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) are a flexible way to to associate users and groups with projects. In Jira Cloud, the list of project roles is shared globally with all projects, but each project can have a different set of actors associated with it (unlike groups, which have the same membership throughout all Jira applications).

        Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and workflow conditions.

        #### Members and actors ####

        In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user associated with a project role.

        Actors may be set as [default members](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/#Specifying-'default-members'-for-a-project-role) of the project role or set at the project level:

         *  Default actors: Users and groups that are assigned to the project role for all newly created projects. The default actors can be removed at the project level later if desired.
         *  Actors: Users and groups that are associated with a project role for a project, which may differ from the default actors. This enables you to assign a user to different roles in different projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ProjectRole]', self._runtime.call('get_all_project_roles', call_args({})))

    def create(self, *, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.ProjectRole:
        """
        Create project role

        Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default actors to the project role after creating it.

        *Note that although a new project role is available to all projects upon creation, any default actors that are associated with the project role are not added to projects that existed prior to the role being created.*<

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('create_project_role', call_args({}, {'body': {'description': description, 'name': name}})))

    def get_by_id(self, *, id: int) -> _t.ProjectRole:
        """
        Get project role by ID

        Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('get_project_role_by_id', call_args({'id': id})))

    def fully(self, *, id: int, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.ProjectRole:
        """
        Fully update project role

        Updates the project role's name and description. You must include both a name and a description in the request.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('fully_update_project_role', call_args({'id': id}, {'body': {'description': description, 'name': name}})))

    def partial(self, *, id: int, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.ProjectRole:
        """
        Partial update project role

        Updates either the project role's name or its description.

        You cannot update both the name and description at the same time using this operation. If you send a request with a name and a description only the name is updated.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectRole', self._runtime.call('partial_update_project_role', call_args({'id': id}, {'body': {'description': description, 'name': name}})))

    def delete(self, *, id: int, swap: int | Unset = UNSET) -> None:
        """
        Delete project role

        Deletes a project role. You must specify a replacement project role if you wish to delete a project role that is in use.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_project_role', call_args({'id': id, 'swap': swap}))

class _ProjectTemplatesResource:
    """Operations under ``project_templates``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create_project_with_custom_template(self, *, details: _t.CustomTemplatesProjectDetails | Unset = UNSET, template: _t.CustomTemplateRequestDto | Unset = UNSET) -> None:
        """
        Create custom project

        Creates a project based on a custom template provided in the request.

        The request body should contain the project details and the capabilities that comprise the project:

         *  `details` \\- represents the project details settings
         *  `template` \\- represents a list of capabilities responsible for creating specific parts of a project

        A capability is defined as a unit of configuration for the project you want to create.

        This operation is:

         *  [asynchronous](#async). Follow the `Location` link in the response header to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        ***Note: This API is only supported for Jira Enterprise edition.***

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('create_project_with_custom_template', call_args({}, {'body': {'details': details, 'template': template}}))

    def edit_template(self, *, template_description: str | Unset = UNSET, template_generation_options: _t.CustomTemplateOptions | Unset = UNSET, template_key: str | Unset = UNSET, template_name: str | Unset = UNSET) -> Any:
        """
        Edit a custom project template

        Edit custom template

        This API endpoint allows you to edit an existing customised template.

        ***Note: Custom Templates are only supported for Jira Enterprise edition.***
        """
        return cast('Any', self._runtime.call('edit_template', call_args({}, {'body': {'template_description': template_description, 'template_generation_options': template_generation_options, 'template_key': template_key, 'template_name': template_name}})))

    def live_template(self, *, project_id: str | Unset = UNSET, template_key: str | Unset = UNSET) -> _t.ProjectTemplateModel:
        """
        Gets a custom project template

        Get custom template

        This API endpoint allows you to get a live custom project template details by either templateKey or projectId

        ***Note: Custom Templates are only supported for Jira Enterprise edition.***
        """
        return cast('_t.ProjectTemplateModel', self._runtime.call('live_template', call_args({'project_id': project_id, 'template_key': template_key})))

    def remove_template(self, *, template_key: str) -> Any:
        """
        Deletes a custom project template

        Remove custom template

        This API endpoint allows you to remove a specified customised template

        ***Note: Custom Templates are only supported for Jira Enterprise edition.***
        """
        return cast('Any', self._runtime.call('remove_template', call_args({'template_key': template_key})))

    def save_template(self, *, template_description: str | Unset = UNSET, template_from_project_request: _t.SaveProjectTemplateRequest | Unset = UNSET, template_name: str | Unset = UNSET) -> _t.SaveTemplateResponse:
        """
        Save a custom project template

        Save custom template

        This API endpoint allows you to save a customised template

        ***Note: Custom Templates are only supported for Jira Enterprise edition.***
        """
        return cast('_t.SaveTemplateResponse', self._runtime.call('save_template', call_args({}, {'body': {'template_description': template_description, 'template_from_project_request': template_from_project_request, 'template_name': template_name}})))

class _ProjectTypesResource:
    """Operations under ``project_types``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_all(self) -> builtins.list[_t.ProjectType]:
        """
        Get all project types

        Returns all [project types](https://confluence.atlassian.com/x/Var1Nw), whether or not the instance has a valid license for each type.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('builtins.list[_t.ProjectType]', self._runtime.call('get_all_project_types', call_args({})))

    def list_all_accessible(self) -> builtins.list[_t.ProjectType]:
        """
        Get licensed project types

        Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.
        """
        return cast('builtins.list[_t.ProjectType]', self._runtime.call('get_all_accessible_project_types', call_args({})))

    def get_by_key(self, *, project_type_key: _t.GetProjectTypeByKeyProjectTypeKey) -> _t.ProjectType:
        """
        Get project type by key

        Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.ProjectType', self._runtime.call('get_project_type_by_key', call_args({'project_type_key': project_type_key})))

    def get_accessible_by_key(self, *, project_type_key: _t.GetAccessibleProjectTypeByKeyProjectTypeKey) -> _t.ProjectType:
        """
        Get accessible project type by key

        Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.ProjectType', self._runtime.call('get_accessible_project_type_by_key', call_args({'project_type_key': project_type_key})))

class _ProjectVersionsResource:
    """Operations under ``project_versions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_paginated(self, *, project_id_or_key: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: _t.GetProjectVersionsPaginatedOrderBy | Unset = UNSET, query: str | Unset = UNSET, status: str | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanVersion:
        """
        Get project versions paginated

        Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.PageBeanVersion', self._runtime.call('get_project_versions_paginated', call_args({'project_id_or_key': project_id_or_key, 'start_at': start_at, 'max_results': max_results, 'order_by': order_by, 'query': query, 'status': status, 'expand': expand})))

    def list(self, *, project_id_or_key: str, expand: str | Unset = UNSET) -> builtins.list[_t.Version]:
        """
        Get project versions

        Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('builtins.list[_t.Version]', self._runtime.call('get_project_versions', call_args({'project_id_or_key': project_id_or_key, 'expand': expand})))

    def create_version(self, *, approvers: builtins.list[_t.VersionApprover] | Unset = UNSET, archived: bool | Unset = UNSET, description: str | Unset = UNSET, driver: str | Unset = UNSET, expand: str | Unset = UNSET, id: str | Unset = UNSET, issues_status_for_fix_version: _t.VersionIssuesStatus | Unset = UNSET, move_unfixed_issues_to: str | Unset = UNSET, name: str | Unset = UNSET, operations: builtins.list[_t.SimpleLink] | Unset = UNSET, overdue: bool | Unset = UNSET, project: str | Unset = UNSET, project_id: int | Unset = UNSET, release_date: str | Unset = UNSET, released: bool | Unset = UNSET, self_: str | Unset = UNSET, start_date: str | Unset = UNSET, user_release_date: str | Unset = UNSET, user_start_date: str | Unset = UNSET) -> _t.Version:
        """
        Create version

        Creates a project version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the version is added to.
        """
        return cast('_t.Version', self._runtime.call('create_version', call_args({}, {'body': {'approvers': approvers, 'archived': archived, 'description': description, 'driver': driver, 'expand': expand, 'id': id, 'issues_status_for_fix_version': issues_status_for_fix_version, 'move_unfixed_issues_to': move_unfixed_issues_to, 'name': name, 'operations': operations, 'overdue': overdue, 'project': project, 'project_id': project_id, 'release_date': release_date, 'released': released, 'self': self_, 'start_date': start_date, 'user_release_date': user_release_date, 'user_start_date': user_start_date}})))

    def get_version(self, *, id: str, expand: str | Unset = UNSET) -> _t.Version:
        """
        Get version

        Returns a project version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
        """
        return cast('_t.Version', self._runtime.call('get_version', call_args({'id': id, 'expand': expand})))

    def update_version(self, *, id: str, body: _t.Version) -> _t.Version:
        """
        Update version

        Updates a project version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.
        """
        return cast('_t.Version', self._runtime.call('update_version', call_args({'id': id, 'body': body})))

    def delete_version(self, *, id: str, move_fix_issues_to: str | Unset = UNSET, move_affected_issues_to: str | Unset = UNSET) -> None:
        """
        Delete version

        Deletes a project version.

        Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that supports swapping version values in custom fields, in addition to the swapping for `fixVersion` and `affectedVersion` provided in this resource.

        Alternative versions can be provided to update issues that use the deleted version in `fixVersion` or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and `affectedVersion` that contain the deleted version are cleared.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

        Deprecated.
        """
        self._runtime.call('delete_version', call_args({'id': id, 'move_fix_issues_to': move_fix_issues_to, 'move_affected_issues_to': move_affected_issues_to}))

    def merge_versions(self, *, id: str, move_issues_to: str) -> Any:
        """
        Merge versions

        Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

        Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom fields.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.
        """
        return cast('Any', self._runtime.call('merge_versions', call_args({'id': id, 'move_issues_to': move_issues_to})))

    def move_version(self, *, id: str, after: str | Unset = UNSET, position: _t.VersionMoveBeanPosition | Unset = UNSET) -> _t.Version:
        """
        Move version

        Modifies the version's sequence within the project, which affects the display order of the versions in Jira.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
        """
        return cast('_t.Version', self._runtime.call('move_version', call_args({'id': id}, {'body': {'after': after, 'position': position}})))

    def list_version_related_issues(self, *, id: str) -> _t.VersionIssueCounts:
        """
        Get version's related issues count

        Returns the following counts for a version:

         *  Number of issues where the `fixVersion` is set to the version.
         *  Number of issues where the `affectedVersion` is set to the version.
         *  Number of issues where a version custom field is set to the version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
        """
        return cast('_t.VersionIssueCounts', self._runtime.call('get_version_related_issues', call_args({'id': id})))

    def get_related_work(self, *, id: str) -> builtins.list[_t.VersionRelatedWork]:
        """
        Get related work

        Returns related work items for the given version id.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
        """
        return cast('builtins.list[_t.VersionRelatedWork]', self._runtime.call('get_related_work', call_args({'id': id})))

    def update_related_work(self, *, id: str, category: str, issue_id: int | Unset = UNSET, related_work_id: str | Unset = UNSET, title: str | Unset = UNSET, url: str | Unset = UNSET) -> _t.VersionRelatedWork:
        """
        Update related work

        Updates the given related work. You can only update generic link related works via Rest APIs. Any archived version related works can't be edited.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
        """
        return cast('_t.VersionRelatedWork', self._runtime.call('update_related_work', call_args({'id': id}, {'body': {'category': category, 'issue_id': issue_id, 'related_work_id': related_work_id, 'title': title, 'url': url}}, required=frozenset({'body'}))))

    def create_related_work(self, *, id: str, category: str, issue_id: int | Unset = UNSET, related_work_id: str | Unset = UNSET, title: str | Unset = UNSET, url: str | Unset = UNSET) -> _t.VersionRelatedWork:
        """
        Create related work

        Creates a related work for the given version. You can only create a generic link type of related works via this API. relatedWorkId will be auto-generated UUID, that does not need to be provided.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
        """
        return cast('_t.VersionRelatedWork', self._runtime.call('create_related_work', call_args({'id': id}, {'body': {'category': category, 'issue_id': issue_id, 'related_work_id': related_work_id, 'title': title, 'url': url}}, required=frozenset({'body'}))))

    def delete_and_replace_version(self, *, id: str, custom_field_replacement_list: builtins.list[_t.CustomFieldReplacement] | Unset = UNSET, move_affected_issues_to: int | Unset = UNSET, move_fix_issues_to: int | Unset = UNSET) -> Any:
        """
        Delete and replace version

        Deletes a project version.

        Alternative versions can be provided to update issues that use the deleted version in `fixVersion`, `affectedVersion`, or any version picker custom fields. If alternatives are not provided, occurrences of `fixVersion`, `affectedVersion`, and any version picker custom field, that contain the deleted version, are cleared. Any replacement version must be in the same project as the version being deleted and cannot be the version being deleted.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.
        """
        return cast('Any', self._runtime.call('delete_and_replace_version', call_args({'id': id}, {'body': {'custom_field_replacement_list': custom_field_replacement_list, 'move_affected_issues_to': move_affected_issues_to, 'move_fix_issues_to': move_fix_issues_to}})))

    def list_version_unresolved_issues(self, *, id: str) -> _t.VersionUnresolvedIssuesCount:
        """
        Get version's unresolved issues count

        Returns counts of the issues and unresolved issues for the project version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
        """
        return cast('_t.VersionUnresolvedIssuesCount', self._runtime.call('get_version_unresolved_issues', call_args({'id': id})))

    def delete_related_work(self, *, version_id: str, related_work_id: str) -> None:
        """
        Delete related work

        Deletes the given related work for the given version.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
        """
        self._runtime.call('delete_related_work', call_args({'version_id': version_id, 'related_work_id': related_work_id}))

class _ProjectsResource:
    """Operations under ``projects``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, expand: str | Unset = UNSET, recent: int | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET) -> builtins.list[_t.Project]:
        """
        Get all projects

        Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

        Deprecated.
        """
        return cast('builtins.list[_t.Project]', self._runtime.call('get_all_projects', call_args({'expand': expand, 'recent': recent, 'properties': properties})))

    def create(self, *, key: str, name: str, assignee_type: _t.CreateProjectDetailsAssigneeType | Unset = UNSET, avatar_id: int | Unset = UNSET, category_id: int | Unset = UNSET, description: str | Unset = UNSET, field_configuration_scheme: int | Unset = UNSET, field_scheme: int | Unset = UNSET, issue_security_scheme: int | Unset = UNSET, issue_type_scheme: int | Unset = UNSET, issue_type_screen_scheme: int | Unset = UNSET, lead: str | Unset = UNSET, lead_account_id: str | Unset = UNSET, notification_scheme: int | Unset = UNSET, permission_scheme: int | Unset = UNSET, project_template_key: _t.CreateProjectDetailsProjectTemplateKey | Unset = UNSET, project_type_key: _t.CreateProjectDetailsProjectTypeKey | Unset = UNSET, url: str | Unset = UNSET, workflow_scheme: int | Unset = UNSET) -> _t.ProjectIdentifiers:
        """
        Create project

        Creates a project based on a project type template, as shown in the following table:

        | Project Type Key | Project Template Key |  
        |--|--|  
        | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`, `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |  
        | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`, `com.atlassian.servicedesk:simplified-external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`, `com.atlassian.servicedesk:simplified-facilities-service-desk`, `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`, `com.atlassian.servicedesk:simplified-design-service-desk`, `com.atlassian.servicedesk:simplified-sales-service-desk`, `com.atlassian.servicedesk:simplified-finance-service-desk`, `com.atlassian.servicedesk:company-managed-blank-service-project`, `com.atlassian.servicedesk:company-managed-general-service-project`, `com.atlassian.servicedesk:team-managed-general-service-project`, `com.atlassian.servicedesk:next-gen-it-service-desk`, `com.atlassian.servicedesk:next-gen-hr-service-desk`, `com.atlassian.servicedesk:next-gen-legal-service-desk`, `com.atlassian.servicedesk:next-gen-marketing-service-desk`, `com.atlassian.servicedesk:next-gen-facilities-service-desk`, `com.atlassian.servicedesk:next-gen-analytics-service-desk`, `com.atlassian.servicedesk:next-gen-finance-service-desk`, `com.atlassian.servicedesk:next-gen-design-service-desk`, `com.atlassian.servicedesk:next-gen-sales-service-desk` |  
        | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`, `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-simplified-scrum-classic` |  
        | `customer_service` | `com.atlassian.jcs:customer-service-management` |  
        The project types are available according to the installed Jira features as follows:

         *  Jira Core, the default, enables `business` projects.
         *  Jira Service Management enables `service_desk` projects.
         *  Jira Software enables `software` projects.
         *  Jira Customer Service enables `customer_service` projects.

        To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ProjectIdentifiers', self._runtime.call('create_project', call_args({}, {'body': {'assignee_type': assignee_type, 'avatar_id': avatar_id, 'category_id': category_id, 'description': description, 'field_configuration_scheme': field_configuration_scheme, 'field_scheme': field_scheme, 'issue_security_scheme': issue_security_scheme, 'issue_type_scheme': issue_type_scheme, 'issue_type_screen_scheme': issue_type_screen_scheme, 'key': key, 'lead': lead, 'lead_account_id': lead_account_id, 'name': name, 'notification_scheme': notification_scheme, 'permission_scheme': permission_scheme, 'project_template_key': project_template_key, 'project_type_key': project_type_key, 'url': url, 'workflow_scheme': workflow_scheme}}, required=frozenset({'body'}))))

    def get_recent(self, *, expand: str | Unset = UNSET, properties: builtins.list[_t.StringList] | Unset = UNSET) -> builtins.list[_t.Project]:
        """
        Get recent projects

        Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

         *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.Project]', self._runtime.call('get_recent', call_args({'expand': expand, 'properties': properties})))

    def search(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, order_by: _t.SearchProjectsOrderBy | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, keys: builtins.list[str] | Unset = UNSET, query: str | Unset = UNSET, type_key: str | Unset = UNSET, category_id: int | Unset = UNSET, action: _t.SearchProjectsAction | Unset = UNSET, expand: str | Unset = UNSET, status: builtins.list[_t.SearchProjectsStatusItem] | Unset = UNSET, properties: builtins.list[_t.StringList] | Unset = UNSET, property_query: str | Unset = UNSET) -> _t.PageBeanProject:
        """
        Get projects paginated

        Returns a [paginated](#pagination) list of projects visible to the user.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

         *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanProject', self._runtime.call('search_projects', call_args({'start_at': start_at, 'max_results': max_results, 'order_by': order_by, 'id': id, 'keys': keys, 'query': query, 'type_key': type_key, 'category_id': category_id, 'action': action, 'expand': expand, 'status': status, 'properties': properties, 'property_query': property_query})))

    def get(self, *, project_id_or_key: str, expand: str | Unset = UNSET, properties: builtins.list[str] | Unset = UNSET) -> _t.Project:
        """
        Get project

        Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.Project', self._runtime.call('get_project', call_args({'project_id_or_key': project_id_or_key, 'expand': expand, 'properties': properties})))

    def update(self, *, project_id_or_key: str, expand: str | Unset = UNSET, assignee_type: _t.UpdateProjectDetailsAssigneeType | Unset = UNSET, avatar_id: int | Unset = UNSET, category_id: int | Unset = UNSET, description: str | Unset = UNSET, issue_security_scheme: int | Unset = UNSET, key: str | Unset = UNSET, lead: str | Unset = UNSET, lead_account_id: str | Unset = UNSET, name: str | Unset = UNSET, notification_scheme: int | Unset = UNSET, permission_scheme: int | Unset = UNSET, released_project_keys: builtins.list[str] | Unset = UNSET, url: str | Unset = UNSET) -> _t.Project:
        """
        Update project

        Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project.

        All parameters are optional in the body of the request. Schemes will only be updated if they are included in the request, any omitted schemes will be left unchanged.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). is only needed when changing the schemes or project key. Otherwise you will only need *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('_t.Project', self._runtime.call('update_project', call_args({'project_id_or_key': project_id_or_key, 'expand': expand}, {'body': {'assignee_type': assignee_type, 'avatar_id': avatar_id, 'category_id': category_id, 'description': description, 'issue_security_scheme': issue_security_scheme, 'key': key, 'lead': lead, 'lead_account_id': lead_account_id, 'name': name, 'notification_scheme': notification_scheme, 'permission_scheme': permission_scheme, 'released_project_keys': released_project_keys, 'url': url}})))

    def delete(self, *, project_id_or_key: str, enable_undo: bool | Unset = UNSET) -> None:
        """
        Delete project

        Deletes a project.

        You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_project', call_args({'project_id_or_key': project_id_or_key, 'enable_undo': enable_undo}))

    def archive(self, *, project_id_or_key: str) -> Any:
        """
        Archive project

        Archives a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('archive_project', call_args({'project_id_or_key': project_id_or_key})))

    def delete_asynchronously(self, *, project_id_or_key: str) -> None:
        """
        Delete project asynchronously

        Deletes a project asynchronously.

        This operation is:

         *  transactional, that is, if part of the delete fails the project is not deleted.
         *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_project_asynchronously', call_args({'project_id_or_key': project_id_or_key}))

    def restore(self, *, project_id_or_key: str) -> _t.Project:
        """
        Restore deleted or archived project

        Restores a project that has been archived or placed in the Jira recycle bin.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)for Company managed projects.
         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project for Team managed projects.
        """
        return cast('_t.Project', self._runtime.call('restore', call_args({'project_id_or_key': project_id_or_key})))

    def list_all_statuses(self, *, project_id_or_key: str) -> builtins.list[_t.IssueTypeWithStatus]:
        """
        Get all statuses for project

        Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('builtins.list[_t.IssueTypeWithStatus]', self._runtime.call('get_all_statuses', call_args({'project_id_or_key': project_id_or_key})))

    def get_hierarchy(self, *, project_id: int) -> _t.ProjectIssueTypeHierarchy:
        """
        Get project issue type hierarchy

        Get the issue type hierarchy for a next-gen project.

        The issue type hierarchy for a project consists of:

         *  *Epic* at level 1 (optional).
         *  One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic.
         *  *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.

        **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
        """
        return cast('_t.ProjectIssueTypeHierarchy', self._runtime.call('get_hierarchy', call_args({'project_id': project_id})))

    def get_notification_scheme_for(self, *, project_key_or_id: str, expand: str | Unset = UNSET) -> _t.NotificationScheme:
        """
        Get project notification scheme

        Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
        """
        return cast('_t.NotificationScheme', self._runtime.call('get_notification_scheme_for_project', call_args({'project_key_or_id': project_key_or_id, 'expand': expand})))

class _ScreenSchemesResource:
    """Operations under ``screen_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, expand: str | Unset = UNSET, query_string: str | Unset = UNSET, order_by: _t.GetScreenSchemesOrderBy | Unset = UNSET) -> _t.PageBeanScreenScheme:
        """
        Get screen schemes

        Returns a [paginated](#pagination) list of screen schemes.

        Only screen schemes used in classic projects are returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanScreenScheme', self._runtime.call('get_screen_schemes', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'expand': expand, 'query_string': query_string, 'order_by': order_by})))

    def create(self, *, name: str, screens: _t.ScreenTypes, description: str | Unset = UNSET) -> _t.ScreenSchemeId:
        """
        Create screen scheme

        Creates a screen scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ScreenSchemeId', self._runtime.call('create_screen_scheme', call_args({}, {'body': {'description': description, 'name': name, 'screens': screens}}, required=frozenset({'body'}))))

    def update(self, *, screen_scheme_id: str, description: str | Unset = UNSET, name: str | Unset = UNSET, screens: _t.UpdateScreenTypes | Unset = UNSET) -> Any:
        """
        Update screen scheme

        Updates a screen scheme. Only screen schemes used in classic projects can be updated.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('update_screen_scheme', call_args({'screen_scheme_id': screen_scheme_id}, {'body': {'description': description, 'name': name, 'screens': screens}})))

    def delete(self, *, screen_scheme_id: str) -> None:
        """
        Delete screen scheme

        Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme.

        Only screens schemes used in classic projects can be deleted.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_screen_scheme', call_args({'screen_scheme_id': screen_scheme_id}))

class _ScreenTabFieldsResource:
    """Operations under ``screen_tab_fields``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, screen_id: int, tab_id: int, project_key: str | Unset = UNSET) -> builtins.list[_t.ScreenableField]:
        """
        Get all screen tab fields

        Returns all fields for a screen tab.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.
        """
        return cast('builtins.list[_t.ScreenableField]', self._runtime.call('get_all_screen_tab_fields', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'project_key': project_key})))

    def add(self, *, screen_id: int, tab_id: int, field_id: str, skip_field_association: bool | Unset = UNSET) -> _t.ScreenableField:
        """
        Add screen tab field

        Adds a field to a screen tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ScreenableField', self._runtime.call('add_screen_tab_field', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'skip_field_association': skip_field_association}, {'body': {'field_id': field_id}}, required=frozenset({'body'}))))

    def remove(self, *, screen_id: int, tab_id: int, id: str) -> None:
        """
        Remove screen tab field

        Removes a field from a screen tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('remove_screen_tab_field', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'id': id}))

    def move(self, *, screen_id: int, tab_id: int, id: str, after: str | Unset = UNSET, position: _t.MoveFieldBeanPosition | Unset = UNSET) -> Any:
        """
        Move screen tab field

        Moves a screen tab field.

        If `after` and `position` are provided in the request, `position` is ignored.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('move_screen_tab_field', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'id': id}, {'body': {'after': after, 'position': position}})))

class _ScreenTabsResource:
    """Operations under ``screen_tabs``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_bulk(self, *, screen_id: builtins.list[int] | Unset = UNSET, tab_id: builtins.list[int] | Unset = UNSET, start_at: int | Unset = UNSET, max_result: int | Unset = UNSET) -> Any:
        """
        Get bulk screen tabs

        Returns the list of tabs for a bulk of screens.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('get_bulk_screen_tabs', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'start_at': start_at, 'max_result': max_result})))

    def list_all(self, *, screen_id: int, project_key: str | Unset = UNSET) -> builtins.list[_t.ScreenableTab]:
        """
        Get all screen tabs

        Returns the list of tabs for a screen.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.
        """
        return cast('builtins.list[_t.ScreenableTab]', self._runtime.call('get_all_screen_tabs', call_args({'screen_id': screen_id, 'project_key': project_key})))

    def add(self, *, screen_id: int, name: str, id: int | Unset = UNSET) -> _t.ScreenableTab:
        """
        Create screen tab

        Creates a tab for a screen.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ScreenableTab', self._runtime.call('add_screen_tab', call_args({'screen_id': screen_id}, {'body': {'id': id, 'name': name}}, required=frozenset({'body'}))))

    def rename(self, *, screen_id: int, tab_id: int, name: str, id: int | Unset = UNSET) -> _t.ScreenableTab:
        """
        Update screen tab

        Updates the name of a screen tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ScreenableTab', self._runtime.call('rename_screen_tab', call_args({'screen_id': screen_id, 'tab_id': tab_id}, {'body': {'id': id, 'name': name}}, required=frozenset({'body'}))))

    def delete(self, *, screen_id: int, tab_id: int) -> None:
        """
        Delete screen tab

        Deletes a screen tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_screen_tab', call_args({'screen_id': screen_id, 'tab_id': tab_id}))

    def move(self, *, screen_id: int, tab_id: int, pos: int) -> Any:
        """
        Move screen tab

        Moves a screen tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('move_screen_tab', call_args({'screen_id': screen_id, 'tab_id': tab_id, 'pos': pos})))

class _ScreensResource:
    """Operations under ``screens``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_for_field(self, *, field_id: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanScreenWithTab:
        """
        Get screens for a field

        Returns a [paginated](#pagination) list of the screens a field is used in.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanScreenWithTab', self._runtime.call('get_screens_for_field', call_args({'field_id': field_id, 'start_at': start_at, 'max_results': max_results, 'expand': expand})))

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, id: builtins.list[int] | Unset = UNSET, query_string: str | Unset = UNSET, scope: builtins.list[_t.GetScreensScopeItem] | Unset = UNSET, order_by: _t.GetScreensOrderBy | Unset = UNSET) -> _t.PageBeanScreen:
        """
        Get screens

        Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanScreen', self._runtime.call('get_screens', call_args({'start_at': start_at, 'max_results': max_results, 'id': id, 'query_string': query_string, 'scope': scope, 'order_by': order_by})))

    def create(self, *, name: str, description: str | Unset = UNSET) -> _t.Screen:
        """
        Create screen

        Creates a screen with a default field tab.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.Screen', self._runtime.call('create_screen', call_args({}, {'body': {'description': description, 'name': name}}, required=frozenset({'body'}))))

    def add(self, *, field_id: str) -> Any:
        """
        Add field to default screen

        Adds a field to the default tab of the default screen.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_field_to_default_screen', call_args({'field_id': field_id})))

    def update(self, *, screen_id: int, description: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.Screen:
        """
        Update screen

        Updates a screen. Only screens used in classic projects can be updated.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.Screen', self._runtime.call('update_screen', call_args({'screen_id': screen_id}, {'body': {'description': description, 'name': name}})))

    def delete(self, *, screen_id: int) -> None:
        """
        Delete screen

        Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft.

        Only screens used in classic projects can be deleted.
        """
        self._runtime.call('delete_screen', call_args({'screen_id': screen_id}))

    def list_available_fields(self, *, screen_id: int) -> builtins.list[_t.ScreenableField]:
        """
        Get available screen fields

        Returns the fields that can be added to a tab on a screen.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.ScreenableField]', self._runtime.call('get_available_screen_fields', call_args({'screen_id': screen_id})))

class _ServerInfoResource:
    """Operations under ``server_info``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self) -> _t.ServerInformation:
        """
        Get Jira instance info

        Returns information about the Jira instance.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** None.
        """
        return cast('_t.ServerInformation', self._runtime.call('get_server_info', call_args({})))

class _ServiceRegistryResource:
    """Operations under ``service_registry``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def resource_services_get(self, *, service_ids: builtins.list[str]) -> builtins.list[_t.ServiceRegistry]:
        """
        Retrieve the attributes of service registries

        Retrieve the attributes of given service registries.

        **[Permissions](#permissions) required:** Only Connect apps can make this request and the servicesIds belong to the tenant you are requesting
        """
        return cast('builtins.list[_t.ServiceRegistry]', self._runtime.call('service_registry_resource_services_get', call_args({'service_ids': service_ids})))

class _StatusResource:
    """Operations under ``status``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_statuses(self, *, id: builtins.list[str]) -> builtins.list[_t.JiraStatus]:
        """
        Bulk get statuses

        Returns a list of the statuses specified by one or more status IDs.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('builtins.list[_t.JiraStatus]', self._runtime.call('get_statuses_by_id', call_args({'id': id})))

    def update_statuses(self, *, statuses: builtins.list[_t.StatusUpdate]) -> Any:
        """
        Bulk update statuses

        Updates statuses by ID.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('Any', self._runtime.call('update_statuses', call_args({}, {'body': {'statuses': statuses}}, required=frozenset({'body'}))))

    def create_statuses(self, *, scope: _t.StatusScope, statuses: builtins.list[_t.StatusCreate]) -> builtins.list[_t.JiraStatus]:
        """
        Bulk create statuses

        Creates statuses for a global or project scope.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('builtins.list[_t.JiraStatus]', self._runtime.call('create_statuses', call_args({}, {'body': {'scope': scope, 'statuses': statuses}}, required=frozenset({'body'}))))

    def delete_statuses(self, *, id: builtins.list[str]) -> Any:
        """
        Bulk delete Statuses

        Deletes statuses by ID.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('Any', self._runtime.call('delete_statuses_by_id', call_args({'id': id})))

    def list_statuses_by_name(self, *, name: builtins.list[str], project_id: str | Unset = UNSET) -> builtins.list[_t.JiraStatus]:
        """
        Bulk get statuses by name

        Returns a list of the statuses specified by one or more status names.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Browse projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('builtins.list[_t.JiraStatus]', self._runtime.call('get_statuses_by_name', call_args({'name': name, 'project_id': project_id})))

    def search(self, *, project_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, search_string: str | Unset = UNSET, status_category: str | Unset = UNSET, include_global_statuses: bool | Unset = UNSET) -> _t.PageOfStatuses:
        """
        Search statuses paginated

        Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.

        **[Permissions](#permissions) required:**

         *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
         *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('_t.PageOfStatuses', self._runtime.call('search', call_args({'project_id': project_id, 'start_at': start_at, 'max_results': max_results, 'search_string': search_string, 'status_category': status_category, 'include_global_statuses': include_global_statuses})))

    def get_project_issue_type_usages_for(self, *, status_id: str, project_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.StatusProjectIssueTypeUsageDto:
        """
        Get issue type usages by status and project

        Returns a page of issue types in a project using a given status.
        """
        return cast('_t.StatusProjectIssueTypeUsageDto', self._runtime.call('get_project_issue_type_usages_for_status', call_args({'status_id': status_id, 'project_id': project_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def get_project_usages_for(self, *, status_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.StatusProjectUsageDto:
        """
        Get project usages by status

        Returns a page of projects using a given status.
        """
        return cast('_t.StatusProjectUsageDto', self._runtime.call('get_project_usages_for_status', call_args({'status_id': status_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def get_workflow_usages_for(self, *, status_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.StatusWorkflowUsageDto:
        """
        Get workflow usages by status

        Returns a page of workflows using a given status.
        """
        return cast('_t.StatusWorkflowUsageDto', self._runtime.call('get_workflow_usages_for_status', call_args({'status_id': status_id, 'next_page_token': next_page_token, 'max_results': max_results})))

class _TasksResource:
    """Operations under ``tasks``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self, *, task_id: str) -> _t.TaskProgressBeanObject:
        """
        Get task

        Returns the status of a [long-running asynchronous task](#async).

        When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.

        **Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

         *  `read:jira-work`

        **[Permissions](#permissions) required:** either of:

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  Creator of the task.
        """
        return cast('_t.TaskProgressBeanObject', self._runtime.call('get_task', call_args({'task_id': task_id})))

    def cancel(self, *, task_id: str) -> Any:
        """
        Cancel task

        Cancels a task.

        **[Permissions](#permissions) required:** either of:

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
         *  Creator of the task.
        """
        return cast('Any', self._runtime.call('cancel_task', call_args({'task_id': task_id})))

class _TeamsInPlanResource:
    """Operations under ``teams_in_plan``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_teams(self, *, plan_id: int, cursor: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageWithCursorGetTeamResponseForPage:
        """
        Get teams in plan paginated

        Returns a [paginated](#pagination) list of plan-only and Atlassian teams in a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageWithCursorGetTeamResponseForPage', self._runtime.call('get_teams', call_args({'plan_id': plan_id, 'cursor': cursor, 'max_results': max_results})))

    def add_atlassian_team(self, *, plan_id: int, id: str, planning_style: _t.AddAtlassianTeamRequestPlanningStyle, capacity: float | Unset = UNSET, issue_source_id: int | Unset = UNSET, sprint_length: int | Unset = UNSET) -> Any:
        """
        Add Atlassian team to plan

        Adds an existing Atlassian team to a plan and configures their plannning settings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('add_atlassian_team', call_args({'plan_id': plan_id}, {'body': {'capacity': capacity, 'id': id, 'issue_source_id': issue_source_id, 'planning_style': planning_style, 'sprint_length': sprint_length}}, required=frozenset({'body'}))))

    def get_atlassian_team(self, *, plan_id: int, atlassian_team_id: str) -> _t.GetAtlassianTeamResponse:
        """
        Get Atlassian team in plan

        Returns planning settings for an Atlassian team in a plan.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.GetAtlassianTeamResponse', self._runtime.call('get_atlassian_team', call_args({'plan_id': plan_id, 'atlassian_team_id': atlassian_team_id})))

    def update_atlassian_team(self, *, plan_id: int, atlassian_team_id: str, body: builtins.dict[str, Any]) -> Any:
        """
        Update Atlassian team in plan

        Updates any of the following planning settings of an Atlassian team in a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

         *  planningStyle
         *  issueSourceId
         *  sprintLength
         *  capacity

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        *Note that "add" operations do not respect array indexes in target locations. Call the "Get Atlassian team in plan" endpoint to find out the order of array elements.*
        """
        return cast('Any', self._runtime.call('update_atlassian_team', call_args({'plan_id': plan_id, 'atlassian_team_id': atlassian_team_id, 'body': body})))

    def remove_atlassian_team(self, *, plan_id: int, atlassian_team_id: str) -> Any:
        """
        Remove Atlassian team from plan

        Removes an Atlassian team from a plan and deletes their planning settings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('remove_atlassian_team', call_args({'plan_id': plan_id, 'atlassian_team_id': atlassian_team_id})))

    def create_plan_only_team(self, *, plan_id: int, name: str, planning_style: _t.CreatePlanOnlyTeamRequestPlanningStyle, capacity: float | Unset = UNSET, issue_source_id: int | Unset = UNSET, member_account_ids: builtins.list[str] | Unset = UNSET, sprint_length: int | Unset = UNSET) -> int:
        """
        Create plan-only team

        Creates a plan-only team and configures their planning settings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('int', self._runtime.call('create_plan_only_team', call_args({'plan_id': plan_id}, {'body': {'capacity': capacity, 'issue_source_id': issue_source_id, 'member_account_ids': member_account_ids, 'name': name, 'planning_style': planning_style, 'sprint_length': sprint_length}}, required=frozenset({'body'}))))

    def get_plan_only_team(self, *, plan_id: int, plan_only_team_id: int) -> _t.GetPlanOnlyTeamResponse:
        """
        Get plan-only team

        Returns planning settings for a plan-only team.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.GetPlanOnlyTeamResponse', self._runtime.call('get_plan_only_team', call_args({'plan_id': plan_id, 'plan_only_team_id': plan_only_team_id})))

    def update_plan_only_team(self, *, plan_id: int, plan_only_team_id: int, body: builtins.dict[str, Any]) -> Any:
        """
        Update plan-only team

        Updates any of the following planning settings of a plan-only team using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

         *  name
         *  planningStyle
         *  issueSourceId
         *  sprintLength
         *  capacity
         *  memberAccountIds

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        *Note that "add" operations do not respect array indexes in target locations. Call the "Get plan-only team" endpoint to find out the order of array elements.*
        """
        return cast('Any', self._runtime.call('update_plan_only_team', call_args({'plan_id': plan_id, 'plan_only_team_id': plan_only_team_id, 'body': body})))

    def delete_plan_only_team(self, *, plan_id: int, plan_only_team_id: int) -> Any:
        """
        Delete plan-only team

        Deletes a plan-only team and their planning settings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_plan_only_team', call_args({'plan_id': plan_id, 'plan_only_team_id': plan_only_team_id})))

class _TimeTrackingResource:
    """Operations under ``time_tracking``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_selected_implementation(self) -> _t.TimeTrackingProvider:
        """
        Get selected time tracking provider

        Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.TimeTrackingProvider', self._runtime.call('get_selected_time_tracking_implementation', call_args({})))

    def select_implementation(self, *, key: str, name: str | Unset = UNSET, url: str | Unset = UNSET) -> Any:
        """
        Select time tracking provider

        Selects a time tracking provider.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('select_time_tracking_implementation', call_args({}, {'body': {'key': key, 'name': name, 'url': url}}, required=frozenset({'body'}))))

    def list_available_implementations(self) -> builtins.list[_t.TimeTrackingProvider]:
        """
        Get all time tracking providers

        Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.TimeTrackingProvider]', self._runtime.call('get_available_time_tracking_implementations', call_args({})))

    def get_shared_configuration(self) -> _t.TimeTrackingConfiguration:
        """
        Get time tracking settings

        Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.TimeTrackingConfiguration', self._runtime.call('get_shared_time_tracking_configuration', call_args({})))

    def set_shared_configuration(self, *, default_unit: _t.TimeTrackingConfigurationDefaultUnit, time_format: _t.TimeTrackingConfigurationTimeFormat, working_days_per_week: float, working_hours_per_day: float) -> _t.TimeTrackingConfiguration:
        """
        Set time tracking settings

        Sets the time tracking settings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.TimeTrackingConfiguration', self._runtime.call('set_shared_time_tracking_configuration', call_args({}, {'body': {'default_unit': default_unit, 'time_format': time_format, 'working_days_per_week': working_days_per_week, 'working_hours_per_day': working_hours_per_day}}, required=frozenset({'body'}))))

class _UiModificationsAppsResource:
    """Operations under ``ui_modifications_apps``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_ui_modifications(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanUiModificationDetails:
        """
        Get UI modifications

        Gets UI modifications. UI modifications can only be retrieved by Forge apps.

        **[Permissions](#permissions) required:** None.

        The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.PageBeanUiModificationDetails', self._runtime.call('get_ui_modifications', call_args({'start_at': start_at, 'max_results': max_results, 'expand': expand})))

    def create_ui_modification(self, *, name: str, contexts: builtins.list[_t.UiModificationContextDetails] | Unset = UNSET, data: str | Unset = UNSET, description: str | Unset = UNSET) -> _t.UiModificationIdentifiers:
        """
        Create UI modification

        Creates a UI modification. UI modification can only be created by Forge apps.

        Each app can define up to 3000 UI modifications. Each UI modification can define up to 1000 contexts. The same context can be assigned to maximum 100 UI modifications.

        **Context types:**

         *  **Jira contexts:** For Jira view types, use `projectId` and `issueTypeId`. One field can act as a wildcard. Supported Jira views:
            
             *  `GIC` \\- Jira global issue create
             *  `IssueView` \\- Jira issue view
             *  `IssueTransition` \\- Jira issue transition
         *  **Jira Service Management contexts:** For Jira Service Management view types, use `portalId` and `requestTypeId`. Wildcards are not supported. Supported JSM views:
            
             *  `JSMRequestCreate` \\- Jira Service Management request create portal view
         *  **Agent view contexts:** For Agent view types, use `projectId` and `issueTypeId` like Jira contexts, and optionally set `requestTypeId`. `portalId` must not be set. One of `projectId`, `issueTypeId`, or `viewType` can act as a wildcard. Supported Agent views:
            
             *  `GICAgentView` \\- Agent view variant of Jira global issue create
             *  `IssueViewAgentView` \\- Agent view variant of Jira issue view
             *  `IssueTransitionAgentView` \\- Agent view variant of Jira issue transition

        **[Permissions](#permissions) required:**

         *  *None* if the UI modification is created without contexts.
         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('_t.UiModificationIdentifiers', self._runtime.call('create_ui_modification', call_args({}, {'body': {'contexts': contexts, 'data': data, 'description': description, 'name': name}}, required=frozenset({'body'}))))

    def update_ui_modification(self, *, ui_modification_id: str, contexts: builtins.list[_t.UiModificationContextDetails] | Unset = UNSET, data: str | Unset = UNSET, description: str | Unset = UNSET, name: str | Unset = UNSET) -> Any:
        """
        Update UI modification

        Updates a UI modification. UI modification can only be updated by Forge apps.

        Each UI modification can define up to 1000 contexts. The same context can be assigned to maximum 100 UI modifications.

        **Context types:**

         *  **Jira contexts:** For Jira view types, use `projectId` and `issueTypeId`. One field can act as a wildcard. Supported Jira views:
            
             *  `GIC` \\- Jira global issue create
             *  `IssueView` \\- Jira issue view
             *  `IssueTransition` \\- Jira issue transition
         *  **Jira Service Management contexts:** For Jira Service Management view types, use `portalId` and `requestTypeId`. Wildcards are not supported. Supported JSM views:
            
             *  `JSMRequestCreate` \\- Jira Service Management request create portal view
         *  **Agent view contexts:** For Agent view types, use `projectId` and `issueTypeId` like Jira contexts, and optionally set `requestTypeId`. `portalId` must not be set. One of `projectId`, `issueTypeId`, or `viewType` can act as a wildcard. Supported Agent views:
            
             *  `GICAgentView` \\- Agent view variant of Jira global issue create
             *  `IssueViewAgentView` \\- Agent view variant of Jira issue view
             *  `IssueTransitionAgentView` \\- Agent view variant of Jira issue transition

        **[Permissions](#permissions) required:**

         *  *None* if the UI modification is created without contexts.
         *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('Any', self._runtime.call('update_ui_modification', call_args({'ui_modification_id': ui_modification_id}, {'body': {'contexts': contexts, 'data': data, 'description': description, 'name': name}})))

    def delete_ui_modification(self, *, ui_modification_id: str) -> Any:
        """
        Delete UI modification

        Deletes a UI modification. All the contexts that belong to the UI modification are deleted too. UI modification can only be deleted by Forge apps.

        **[Permissions](#permissions) required:** None.

        The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
        """
        return cast('Any', self._runtime.call('delete_ui_modification', call_args({'ui_modification_id': ui_modification_id})))

class _UserPropertiesResource:
    """Operations under ``user_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_keys(self, *, account_id: str | Unset = UNSET, user_key: str | Unset = UNSET, username: str | Unset = UNSET) -> _t.PropertyKeys:
        """
        Get user property keys

        Returns the keys of all properties for a user.

        Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user.
         *  Access to Jira, to access the calling user's property keys.
        """
        return cast('_t.PropertyKeys', self._runtime.call('get_user_property_keys', call_args({'account_id': account_id, 'user_key': user_key, 'username': username})))

    def get(self, *, property_key: str, account_id: str | Unset = UNSET, user_key: str | Unset = UNSET, username: str | Unset = UNSET) -> _t.EntityProperty:
        """
        Get user property

        Returns the value of a user's property. If no property key is provided [Get user property keys](#api-rest-api-3-user-properties-get) is called.

        Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a property from any user.
         *  Access to Jira, to get a property from the calling user's record.
        """
        return cast('_t.EntityProperty', self._runtime.call('get_user_property', call_args({'account_id': account_id, 'user_key': user_key, 'username': username, 'property_key': property_key})))

    def set(self, *, property_key: str, body: Any, account_id: str | Unset = UNSET, user_key: str | Unset = UNSET, username: str | Unset = UNSET) -> Any:
        """
        Set user property

        Sets the value of a user's property. Use this resource to store custom data against a user.

        Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a property on any user.
         *  Access to Jira, to set a property on the calling user's record.
        """
        return cast('Any', self._runtime.call('set_user_property', call_args({'account_id': account_id, 'user_key': user_key, 'username': username, 'property_key': property_key, 'body': body})))

    def delete(self, *, property_key: str, account_id: str | Unset = UNSET, user_key: str | Unset = UNSET, username: str | Unset = UNSET) -> None:
        """
        Delete user property

        Deletes a property from a user.

        Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to delete a property from any user.
         *  Access to Jira, to delete a property from the calling user's record.
        """
        self._runtime.call('delete_user_property', call_args({'account_id': account_id, 'user_key': user_key, 'username': username, 'property_key': property_key}))

class _UserSearchResource:
    """Operations under ``user_search``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def find_bulk_assignable_users(self, *, project_keys: str, query: str | Unset = UNSET, username: str | Unset = UNSET, account_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Find users assignable to projects

        Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned issues in the projects, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each project specified in `projectKeys`.
        """
        return cast('builtins.list[_t.User]', self._runtime.call('find_bulk_assignable_users', call_args({'query': query, 'username': username, 'account_id': account_id, 'project_keys': project_keys, 'start_at': start_at, 'max_results': max_results})))

    def find_assignable_users(self, *, query: str | Unset = UNSET, session_id: str | Unset = UNSET, username: str | Unset = UNSET, account_id: str | Unset = UNSET, project: str | Unset = UNSET, issue_key: str | Unset = UNSET, issue_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, action_descriptor_id: int | Unset = UNSET, recommend: bool | Unset = UNSET, account_type: builtins.list[str] | Unset = UNSET, app_type: builtins.list[str] | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Find users assignable to issues

        Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:

         *  a new issue, by providing the `projectKeyOrId`.
         *  an updated issue, by providing the `issueKey` or `issueId`.
         *  to an issue during a transition (workflow action), by providing the `issueKey` or `issueId` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-issueIdOrKey-get).

        In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Assign issues* [project permission](https://confluence.atlassian.com/x/yodKLg)
        """
        return cast('builtins.list[_t.User]', self._runtime.call('find_assignable_users', call_args({'query': query, 'session_id': session_id, 'username': username, 'account_id': account_id, 'project': project, 'issue_key': issue_key, 'issue_id': issue_id, 'start_at': start_at, 'max_results': max_results, 'action_descriptor_id': action_descriptor_id, 'recommend': recommend, 'account_type': account_type, 'app_type': app_type})))

    def find_users_with_all_permissions(self, *, permissions: str, query: str | Unset = UNSET, username: str | Unset = UNSET, account_id: str | Unset = UNSET, issue_key: str | Unset = UNSET, project_key: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Find users with permissions

        Returns a list of users who fulfill these criteria:

         *  their user attributes match a search string.
         *  they have a set of permissions for a project or issue.

        If no search string is provided, a list of all users with the permissions is returned.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.
         *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.
        """
        return cast('builtins.list[_t.User]', self._runtime.call('find_users_with_all_permissions', call_args({'query': query, 'username': username, 'account_id': account_id, 'permissions': permissions, 'issue_key': issue_key, 'project_key': project_key, 'start_at': start_at, 'max_results': max_results})))

    def find_users_for_picker(self, *, query: str, max_results: int | Unset = UNSET, show_avatar: bool | Unset = UNSET, exclude: builtins.list[str] | Unset = UNSET, exclude_account_ids: builtins.list[str] | Unset = UNSET, avatar_size: str | Unset = UNSET, exclude_connect_users: bool | Unset = UNSET) -> _t.FoundUsers:
        """
        Find users for picker

        Returns a list of users whose attributes match the query term. The returned object includes the `html` field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results.

        This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the query term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.
        """
        return cast('_t.FoundUsers', self._runtime.call('find_users_for_picker', call_args({'query': query, 'max_results': max_results, 'show_avatar': show_avatar, 'exclude': exclude, 'exclude_account_ids': exclude_account_ids, 'avatar_size': avatar_size, 'exclude_connect_users': exclude_connect_users})))

    def find_users(self, *, query: str | Unset = UNSET, username: str | Unset = UNSET, account_id: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, property: str | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Find users

        Returns a list of active users that match the search string and property.

        This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        This operation can be accessed anonymously.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.
        """
        return cast('builtins.list[_t.User]', self._runtime.call('find_users', call_args({'query': query, 'username': username, 'account_id': account_id, 'start_at': start_at, 'max_results': max_results, 'property': property})))

    def find_users_by_query(self, *, query: str, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanUser:
        """
        Find users by query

        Finds users with a structured query and returns a [paginated](#pagination) list of user details.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        The query statements are:

         *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project *PROJ*.
         *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.
         *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.
         *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.
         *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
         *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.
         *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.
         *  `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value. For example, if user property `location` is set to value `{"office": {"country": "AU", "city": "Sydney"}}`, then it's possible to use `[location].office.city is "Sydney"` to match the user.

        The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:

        `is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`
        """
        return cast('_t.PageBeanUser', self._runtime.call('find_users_by_query', call_args({'query': query, 'start_at': start_at, 'max_results': max_results})))

    def find_user_keys_by_query(self, *, query: str, start_at: int | Unset = UNSET, max_result: int | Unset = UNSET) -> _t.PageBeanUserKey:
        """
        Find user keys by query

        Finds users with a structured query and returns a [paginated](#pagination) list of user keys.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        The query statements are:

         *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project *PROJ*.
         *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.
         *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.
         *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.
         *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
         *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.
         *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.
         *  `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value. For example, if user property `location` is set to value `{"office": {"country": "AU", "city": "Sydney"}}`, then it's possible to use `[location].office.city is "Sydney"` to match the user.

        The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:

        `is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`
        """
        return cast('_t.PageBeanUserKey', self._runtime.call('find_user_keys_by_query', call_args({'query': query, 'start_at': start_at, 'max_result': max_result})))

    def find_users_with_browse_permission(self, *, query: str | Unset = UNSET, username: str | Unset = UNSET, account_id: str | Unset = UNSET, issue_key: str | Unset = UNSET, project_key: str | Unset = UNSET, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Find users with browse permission

        Returns a list of users who fulfill these criteria:

         *  their user attributes match a search string.
         *  they have permission to browse issues.

        Use this resource to find users who can browse:

         *  an issue, by providing the `issueKey`.
         *  any issue in a project, by providing the `projectKey`.

        This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission to browse issues, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        This operation can be accessed anonymously.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.
        """
        return cast('builtins.list[_t.User]', self._runtime.call('find_users_with_browse_permission', call_args({'query': query, 'username': username, 'account_id': account_id, 'issue_key': issue_key, 'project_key': project_key, 'start_at': start_at, 'max_results': max_results})))

class _UsersResource:
    """Operations under ``users``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self, *, account_id: str | Unset = UNSET, username: str | Unset = UNSET, key: str | Unset = UNSET, expand: str | Unset = UNSET) -> _t.User:
        """
        Get user

        Returns a user.

        Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.User', self._runtime.call('get_user', call_args({'account_id': account_id, 'username': username, 'key': key, 'expand': expand})))

    def create(self, *, email_address: str, products: builtins.list[str], application_keys: builtins.list[str] | Unset = UNSET, display_name: str | Unset = UNSET, key: str | Unset = UNSET, name: str | Unset = UNSET, password: str | Unset = UNSET, self_: str | Unset = UNSET) -> _t.User:
        """
        Create user

        Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable alternative is available this resource will be deprecated.

        **Note:** This API does not support Forge apps.

        If the user exists and has access to Jira, the operation returns a 201 status. If the user exists but does not have access to Jira & no new jira-products are requested, the operation returns a 400 status.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). The caller has to be an **organization admin**.
        """
        return cast('_t.User', self._runtime.call('create_user', call_args({}, {'body': {'application_keys': application_keys, 'display_name': display_name, 'email_address': email_address, 'key': key, 'name': name, 'password': password, 'products': products, 'self': self_}}, required=frozenset({'body'}))))

    def remove(self, *, account_id: str, username: str | Unset = UNSET, key: str | Unset = UNSET) -> None:
        """
        Delete user

        Deletes a user. If the operation completes successfully then the user is removed from Jira's user base. This operation does not delete the user's Atlassian account.

        **[Permissions](#permissions) required:** Site administration (that is, membership of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
        """
        self._runtime.call('remove_user', call_args({'account_id': account_id, 'username': username, 'key': key}))

    def bulk(self, *, account_id: builtins.list[str], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, username: builtins.list[str] | Unset = UNSET, key: builtins.list[str] | Unset = UNSET) -> _t.PageBeanUser:
        """
        Bulk get users

        Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.PageBeanUser', self._runtime.call('bulk_get_users', call_args({'start_at': start_at, 'max_results': max_results, 'username': username, 'key': key, 'account_id': account_id})))

    def bulk_get_migration(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, username: builtins.list[str] | Unset = UNSET, key: builtins.list[str] | Unset = UNSET) -> builtins.list[_t.UserMigrationBean]:
        """
        Get account IDs for users

        Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('builtins.list[_t.UserMigrationBean]', self._runtime.call('bulk_get_users_migration', call_args({'start_at': start_at, 'max_results': max_results, 'username': username, 'key': key})))

    def list_default_columns(self, *, account_id: str | Unset = UNSET, username: str | Unset = UNSET) -> builtins.list[_t.ColumnItem]:
        """
        Get user default columns

        Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If `accountId` is not passed in the request, the calling user's details are returned.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user.
         *  Permission to access Jira, to get the calling user's column details.
        """
        return cast('builtins.list[_t.ColumnItem]', self._runtime.call('get_user_default_columns', call_args({'account_id': account_id, 'username': username})))

    def set_columns(self, *, account_id: str | Unset = UNSET, columns: builtins.list[str] | Unset = UNSET) -> Any:
        """
        Set user default columns

        Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user's default columns are set. If no column details are sent, then all default columns are removed.

        The parameters for this resource are expressed as HTML form data. For example, in curl:

        `curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'`

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
         *  Permission to access Jira, to set the calling user's columns.
        """
        return cast('Any', self._runtime.call('set_user_columns', call_args({'account_id': account_id}, {'body': {'columns': columns}})))

    def reset_columns(self, *, account_id: str | Unset = UNSET, username: str | Unset = UNSET) -> None:
        """
        Reset user default columns

        Resets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user to the system default. If `accountId` is not passed, the calling user's default columns are reset.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
         *  Permission to access Jira, to set the calling user's columns.
        """
        self._runtime.call('reset_user_columns', call_args({'account_id': account_id, 'username': username}))

    def get_email(self, *, account_id: str) -> _t.UnrestrictedUserEmail:
        """
        Get user email

        Returns a user's email address regardless of the user's profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.
        """
        return cast('_t.UnrestrictedUserEmail', self._runtime.call('get_user_email', call_args({'account_id': account_id})))

    def get_email_bulk(self, *, account_id: builtins.list[str]) -> _t.UnrestrictedUserEmail:
        """
        Get user email bulk

        Returns a user's email address regardless of the user's profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.
        """
        return cast('_t.UnrestrictedUserEmail', self._runtime.call('get_user_email_bulk', call_args({'account_id': account_id})))

    def list_groups(self, *, account_id: str, username: str | Unset = UNSET, key: str | Unset = UNSET) -> builtins.list[_t.GroupName]:
        """
        Get user groups

        Returns the groups to which a user belongs.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.GroupName]', self._runtime.call('get_user_groups', call_args({'account_id': account_id, 'username': username, 'key': key})))

    def get_all_default(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Get all users default

        Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.User]', self._runtime.call('get_all_users_default', call_args({'start_at': start_at, 'max_results': max_results, 'expand': expand})))

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET) -> builtins.list[_t.User]:
        """
        Get all users

        Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.

        Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

        **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('builtins.list[_t.User]', self._runtime.call('get_all_users', call_args({'start_at': start_at, 'max_results': max_results, 'expand': expand})))

class _WebhooksResource:
    """Operations under ``webhooks``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_dynamic_for_app(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanWebhook:
        """
        Get dynamic webhooks for app

        Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
        """
        return cast('_t.PageBeanWebhook', self._runtime.call('get_dynamic_webhooks_for_app', call_args({'start_at': start_at, 'max_results': max_results})))

    def register(self, *, url: str, webhooks: builtins.list[_t.WebhookDetails]) -> _t.ContainerForRegisteredWebhooks:
        """
        Register dynamic webhooks

        Registers webhooks.

        **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook.

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
        """
        return cast('_t.ContainerForRegisteredWebhooks', self._runtime.call('register_dynamic_webhooks', call_args({}, {'body': {'url': url, 'webhooks': webhooks}}, required=frozenset({'body'}))))

    def delete(self, *, webhook_ids: builtins.list[int]) -> None:
        """
        Delete webhooks by ID

        Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored.

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
        """
        self._runtime.call('delete_webhook_by_id', call_args({}, {'body': {'webhook_ids': webhook_ids}}, required=frozenset({'body'})))

    def list(self, *, max_results: int | Unset = UNSET, after: int | Unset = UNSET) -> _t.FailedWebhooks:
        """
        Get failed webhooks

        Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.

        After 72 hours the failure may no longer be returned by this operation.

        The oldest failure is returned first.

        This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

        **[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.
        """
        return cast('_t.FailedWebhooks', self._runtime.call('get_failed_webhooks', call_args({'max_results': max_results, 'after': after})))

    def refresh(self, *, webhook_ids: builtins.list[int]) -> _t.WebhooksExpirationDate:
        """
        Extend webhook life

        Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive.

        Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored.

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
        """
        return cast('_t.WebhooksExpirationDate', self._runtime.call('refresh_webhooks', call_args({}, {'body': {'webhook_ids': webhook_ids}}, required=frozenset({'body'}))))

class _WorkflowSchemeDraftsResource:
    """Operations under ``workflow_scheme_drafts``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create_from_parent(self, *, id: int) -> _t.WorkflowScheme:
        """
        Create draft workflow scheme

        Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('create_workflow_scheme_draft_from_parent', call_args({'id': id})))

    def get(self, *, id: int) -> _t.WorkflowScheme:
        """
        Get draft workflow scheme

        Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.  
        Note that:

         *  Only active workflow schemes can have draft workflow schemes.
         *  An active workflow scheme can only have one draft workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('get_workflow_scheme_draft', call_args({'id': id})))

    def update(self, *, id: int, body: _t.WorkflowScheme) -> _t.WorkflowScheme:
        """
        Update draft workflow scheme

        Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_workflow_scheme_draft', call_args({'id': id, 'body': body})))

    def delete(self, *, id: int) -> None:
        """
        Delete draft workflow scheme

        Deletes a draft workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_workflow_scheme_draft', call_args({'id': id}))

    def get_draft_default_workflow(self, *, id: int) -> _t.DefaultWorkflow:
        """
        Get draft default workflow

        Returns the default workflow for a workflow scheme's draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.DefaultWorkflow', self._runtime.call('get_draft_default_workflow', call_args({'id': id})))

    def update_draft_default_workflow(self, *, id: int, workflow: str, update_draft_if_needed: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Update draft default workflow

        Sets the default workflow for a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_draft_default_workflow', call_args({'id': id}, {'body': {'update_draft_if_needed': update_draft_if_needed, 'workflow': workflow}}, required=frozenset({'body'}))))

    def delete_draft_default_workflow(self, *, id: int) -> _t.WorkflowScheme:
        """
        Delete draft default workflow

        Resets the default workflow for a workflow scheme's draft. That is, the default workflow is set to Jira's system workflow (the *jira* workflow).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('delete_draft_default_workflow', call_args({'id': id})))

    def get_issue_type(self, *, id: int, issue_type: str) -> _t.IssueTypeWorkflowMapping:
        """
        Get workflow for issue type in draft workflow scheme

        Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeWorkflowMapping', self._runtime.call('get_workflow_scheme_draft_issue_type', call_args({'id': id, 'issue_type': issue_type})))

    def set_issue_type(self, *, id: int, issue_type: str, body: _t.IssueTypeWorkflowMapping) -> _t.WorkflowScheme:
        """
        Set workflow for issue type in draft workflow scheme

        Sets the workflow for an issue type in a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('set_workflow_scheme_draft_issue_type', call_args({'id': id, 'issue_type': issue_type, 'body': body})))

    def delete_issue_type(self, *, id: int, issue_type: str) -> _t.WorkflowScheme:
        """
        Delete workflow for issue type in draft workflow scheme

        Deletes the issue type-workflow mapping for an issue type in a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('delete_workflow_scheme_draft_issue_type', call_args({'id': id, 'issue_type': issue_type})))

    def publish_draft_workflow_scheme(self, *, id: int, validate_only: bool | Unset = UNSET, status_mappings: builtins.list[_t.StatusMapping] | Unset = UNSET) -> None:
        """
        Publish draft workflow scheme

        Publishes a draft workflow scheme.

        Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.

        This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('publish_draft_workflow_scheme', call_args({'id': id, 'validate_only': validate_only}, {'body': {'status_mappings': status_mappings}}))

    def get_draft_workflow(self, *, id: int, workflow_name: str | Unset = UNSET) -> _t.IssueTypesWorkflowMapping:
        """
        Get issue types for workflows in draft workflow scheme

        Returns the workflow-issue type mappings for a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypesWorkflowMapping', self._runtime.call('get_draft_workflow', call_args({'id': id, 'workflow_name': workflow_name})))

    def update_draft_workflow_mapping(self, *, id: int, workflow_name: str, default_mapping: bool | Unset = UNSET, issue_types: builtins.list[str] | Unset = UNSET, update_draft_if_needed: bool | Unset = UNSET, workflow: str | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Set issue types for workflow in workflow scheme

        Sets the issue types for a workflow in a workflow scheme's draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_draft_workflow_mapping', call_args({'id': id, 'workflow_name': workflow_name}, {'body': {'default_mapping': default_mapping, 'issue_types': issue_types, 'update_draft_if_needed': update_draft_if_needed, 'workflow': workflow}})))

    def delete_draft_workflow_mapping(self, *, id: int, workflow_name: str) -> None:
        """
        Delete issue types for workflow in draft workflow scheme

        Deletes the workflow-issue type mapping for a workflow in a workflow scheme's draft.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_draft_workflow_mapping', call_args({'id': id, 'workflow_name': workflow_name}))

class _WorkflowSchemeProjectAssociationsResource:
    """Operations under ``workflow_scheme_project_associations``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, project_id: builtins.list[int]) -> _t.ContainerOfWorkflowSchemeAssociations:
        """
        Get workflow scheme project associations

        Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.

        If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because the way the `Default Workflow Scheme` is stored means it has no ID.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.ContainerOfWorkflowSchemeAssociations', self._runtime.call('get_workflow_scheme_project_associations', call_args({'project_id': project_id})))

    def assign_scheme_to_project(self, *, project_id: str, workflow_scheme_id: str | Unset = UNSET) -> Any:
        """
        Assign workflow scheme to project

        Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.

        Workflow schemes can only be assigned to classic projects.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('assign_scheme_to_project', call_args({}, {'body': {'project_id': project_id, 'workflow_scheme_id': workflow_scheme_id}}, required=frozenset({'body'}))))

class _WorkflowSchemesResource:
    """Operations under ``workflow_schemes``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.PageBeanWorkflowScheme:
        """
        Get all workflow schemes

        Returns a [paginated](#pagination) list of all workflow schemes, not including draft workflow schemes.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.PageBeanWorkflowScheme', self._runtime.call('get_all_workflow_schemes', call_args({'start_at': start_at, 'max_results': max_results})))

    def create(self, *, default_workflow: str | Unset = UNSET, description: str | Unset = UNSET, draft: bool | Unset = UNSET, id: int | Unset = UNSET, issue_type_mappings: builtins.dict[str, str] | Unset = UNSET, issue_types: builtins.dict[str, _t.IssueTypeDetails] | Unset = UNSET, last_modified: str | Unset = UNSET, last_modified_user: _t.User | Unset = UNSET, name: str | Unset = UNSET, original_default_workflow: str | Unset = UNSET, original_issue_type_mappings: builtins.dict[str, str] | Unset = UNSET, self_: str | Unset = UNSET, update_draft_if_needed: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Create workflow scheme

        Creates a workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('create_workflow_scheme', call_args({}, {'body': {'default_workflow': default_workflow, 'description': description, 'draft': draft, 'id': id, 'issue_type_mappings': issue_type_mappings, 'issue_types': issue_types, 'last_modified': last_modified, 'last_modified_user': last_modified_user, 'name': name, 'original_default_workflow': original_default_workflow, 'original_issue_type_mappings': original_issue_type_mappings, 'self': self_, 'update_draft_if_needed': update_draft_if_needed}})))

    def switch_for_project(self, *, mappings_by_issue_type_override: builtins.list[_t.MappingsByIssueTypeOverride] | Unset = UNSET, project_id: str | Unset = UNSET, target_scheme_id: str | Unset = UNSET) -> None:
        """
        Switch workflow scheme for project

        Switches a workflow scheme for a project.

        Workflow schemes can only be assigned to classic projects.

        **Calculating required mappings:** If statuses from the current workflow scheme won't exist in the target workflow scheme, you must provide `mappingsByIssueTypeOverride` to specify how issues with those statuses should be migrated. Use [the required workflow scheme mappings API](#api-rest-api-3-workflowscheme-update-mappings-post) to determine which statuses and issue types require mappings.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('switch_workflow_scheme_for_project', call_args({}, {'body': {'mappings_by_issue_type_override': mappings_by_issue_type_override, 'project_id': project_id, 'target_scheme_id': target_scheme_id}}))

    def read(self, *, project_ids: builtins.list[str | None] | None | Unset = UNSET, workflow_scheme_ids: builtins.list[str | None] | None | Unset = UNSET) -> builtins.list[_t.WorkflowSchemeReadResponse]:
        """
        Bulk get workflow schemes

        Returns a list of workflow schemes by providing workflow scheme IDs or project IDs.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to access all, including project-scoped, workflow schemes
         *  *Administer projects* project permissions to access project-scoped workflow schemes
        """
        return cast('builtins.list[_t.WorkflowSchemeReadResponse]', self._runtime.call('read_workflow_schemes', call_args({}, {'body': {'project_ids': project_ids, 'workflow_scheme_ids': workflow_scheme_ids}})))

    def update_schemes(self, *, description: str, id: str, name: str, version: _t.DocumentVersion, default_workflow_id: str | Unset = UNSET, status_mappings_by_issue_type_override: builtins.list[_t.MappingsByIssueTypeOverride] | Unset = UNSET, status_mappings_by_workflows: builtins.list[_t.MappingsByWorkflow] | Unset = UNSET, workflows_for_issue_types: builtins.list[_t.WorkflowSchemeAssociation] | Unset = UNSET) -> Any:
        """
        Update workflow scheme

        Updates company-managed and team-managed project workflow schemes. This API doesn't have a concept of draft, so any changes made to a workflow scheme are immediately available. When changing the available statuses for issue types, an [asynchronous task](#async) migrates the issues as defined in the provided mappings.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to update all, including global-scoped, workflow schemes.
         *  *Administer projects* project permission to update project-scoped workflow schemes.
        """
        return cast('Any', self._runtime.call('update_schemes', call_args({}, {'body': {'default_workflow_id': default_workflow_id, 'description': description, 'id': id, 'name': name, 'status_mappings_by_issue_type_override': status_mappings_by_issue_type_override, 'status_mappings_by_workflows': status_mappings_by_workflows, 'version': version, 'workflows_for_issue_types': workflows_for_issue_types}}, required=frozenset({'body'}))))

    def list_required_mappings(self, *, id: str, workflows_for_issue_types: builtins.list[_t.WorkflowSchemeAssociation], default_workflow_id: str | None | Unset = UNSET) -> _t.WorkflowSchemeUpdateRequiredMappingsResponse:
        """
        Get required status mappings for workflow scheme update

        Gets the required status mappings for the desired changes to a workflow scheme. The results are provided per issue type and workflow. When updating a workflow scheme, status mappings can be provided per issue type, per workflow, or both.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* permission to update all, including global-scoped, workflow schemes.
         *  *Administer projects* project permission to update project-scoped workflow schemes.
        """
        return cast('_t.WorkflowSchemeUpdateRequiredMappingsResponse', self._runtime.call('get_required_workflow_scheme_mappings', call_args({}, {'body': {'default_workflow_id': default_workflow_id, 'id': id, 'workflows_for_issue_types': workflows_for_issue_types}}, required=frozenset({'body'}))))

    def get(self, *, id: int, return_draft_if_exists: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Get workflow scheme

        Returns a workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('get_workflow_scheme', call_args({'id': id, 'return_draft_if_exists': return_draft_if_exists})))

    def update(self, *, id: int, body: _t.WorkflowScheme) -> _t.WorkflowScheme:
        """
        Classic update workflow scheme

        Updates a company-manged project workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead, provided that `updateDraftIfNeeded` is set to `true`.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_workflow_scheme', call_args({'id': id, 'body': body})))

    def delete(self, *, id: int) -> Any:
        """
        Delete workflow scheme

        Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project).

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('Any', self._runtime.call('delete_workflow_scheme', call_args({'id': id})))

    def get_default_workflow(self, *, id: int, return_draft_if_exists: bool | Unset = UNSET) -> _t.DefaultWorkflow:
        """
        Get default workflow

        Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.DefaultWorkflow', self._runtime.call('get_default_workflow', call_args({'id': id, 'return_draft_if_exists': return_draft_if_exists})))

    def update_default_workflow(self, *, id: int, workflow: str, update_draft_if_needed: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Update default workflow

        Sets the default workflow for a workflow scheme.

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request object and a draft workflow scheme is created or updated with the new default workflow. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_default_workflow', call_args({'id': id}, {'body': {'update_draft_if_needed': update_draft_if_needed, 'workflow': workflow}}, required=frozenset({'body'}))))

    def delete_default_workflow(self, *, id: int, update_draft_if_needed: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Delete default workflow

        Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's system workflow (the *jira* workflow).

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default workflow reset. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('delete_default_workflow', call_args({'id': id, 'update_draft_if_needed': update_draft_if_needed})))

    def get_issue_type(self, *, id: int, issue_type: str, return_draft_if_exists: bool | Unset = UNSET) -> _t.IssueTypeWorkflowMapping:
        """
        Get workflow for issue type in workflow scheme

        Returns the issue type-workflow mapping for an issue type in a workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypeWorkflowMapping', self._runtime.call('get_workflow_scheme_issue_type', call_args({'id': id, 'issue_type': issue_type, 'return_draft_if_exists': return_draft_if_exists})))

    def set_issue_type(self, *, id: int, issue_type: str, body: _t.IssueTypeWorkflowMapping) -> _t.WorkflowScheme:
        """
        Set workflow for issue type in workflow scheme

        Sets the workflow for an issue type in a workflow scheme.

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('set_workflow_scheme_issue_type', call_args({'id': id, 'issue_type': issue_type, 'body': body})))

    def delete_issue_type(self, *, id: int, issue_type: str, update_draft_if_needed: bool | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Delete workflow for issue type in workflow scheme

        Deletes the issue type-workflow mapping for an issue type in a workflow scheme.

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the issue type-workflow mapping deleted. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('delete_workflow_scheme_issue_type', call_args({'id': id, 'issue_type': issue_type, 'update_draft_if_needed': update_draft_if_needed})))

    def get_workflow(self, *, id: int, workflow_name: str | Unset = UNSET, return_draft_if_exists: bool | Unset = UNSET) -> _t.IssueTypesWorkflowMapping:
        """
        Get issue types for workflows in workflow scheme

        Returns the workflow-issue type mappings for a workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.IssueTypesWorkflowMapping', self._runtime.call('get_workflow', call_args({'id': id, 'workflow_name': workflow_name, 'return_draft_if_exists': return_draft_if_exists})))

    def update_workflow_mapping(self, *, id: int, workflow_name: str, default_mapping: bool | Unset = UNSET, issue_types: builtins.list[str] | Unset = UNSET, update_draft_if_needed: bool | Unset = UNSET, workflow: str | Unset = UNSET) -> _t.WorkflowScheme:
        """
        Set issue types for workflow in workflow scheme

        Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new workflow-issue types mappings. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        return cast('_t.WorkflowScheme', self._runtime.call('update_workflow_mapping', call_args({'id': id, 'workflow_name': workflow_name}, {'body': {'default_mapping': default_mapping, 'issue_types': issue_types, 'update_draft_if_needed': update_draft_if_needed, 'workflow': workflow}})))

    def delete_workflow_mapping(self, *, id: int, workflow_name: str, update_draft_if_needed: bool | Unset = UNSET) -> None:
        """
        Delete issue types for workflow in workflow scheme

        Deletes the workflow-issue type mapping for a workflow in a workflow scheme.

        Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the workflow-issue type mapping deleted. The draft workflow scheme can be published in Jira.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_workflow_mapping', call_args({'id': id, 'workflow_name': workflow_name, 'update_draft_if_needed': update_draft_if_needed}))

    def get_project_usages_for(self, *, workflow_scheme_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.WorkflowSchemeProjectUsageDto:
        """
        Get projects which are using a given workflow scheme

        Returns a page of projects using a given workflow scheme.
        """
        return cast('_t.WorkflowSchemeProjectUsageDto', self._runtime.call('get_project_usages_for_workflow_scheme', call_args({'workflow_scheme_id': workflow_scheme_id, 'next_page_token': next_page_token, 'max_results': max_results})))

class _WorkflowStatusCategoriesResource:
    """Operations under ``workflow_status_categories``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_status_categories(self) -> builtins.list[_t.StatusCategory]:
        """
        Get all status categories

        Returns a list of all status categories.

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('builtins.list[_t.StatusCategory]', self._runtime.call('get_status_categories', call_args({})))

    def get_status_category(self, *, id_or_key: str) -> _t.StatusCategory:
        """
        Get status category

        Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get).

        **[Permissions](#permissions) required:** Permission to access Jira.
        """
        return cast('_t.StatusCategory', self._runtime.call('get_status_category', call_args({'id_or_key': id_or_key})))

class _WorkflowStatusesResource:
    """Operations under ``workflow_statuses``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_statuses(self) -> builtins.list[_t.StatusDetails]:
        """
        Get all statuses

        Returns a list of all statuses associated with active workflows.

        This operation can be accessed anonymously.

        [Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.
        """
        return cast('builtins.list[_t.StatusDetails]', self._runtime.call('get_statuses', call_args({})))

    def get_status(self, *, id_or_name: str) -> _t.StatusDetails:
        """
        Get status

        Returns a status. The status must be associated with an active workflow to be returned.

        If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.

        This operation can be accessed anonymously.

        [Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.
        """
        return cast('_t.StatusDetails', self._runtime.call('get_status', call_args({'id_or_name': id_or_name})))

class _WorkflowTransitionRulesResource:
    """Operations under ``workflow_transition_rules``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_configurations(self, *, types: builtins.list[_t.GetWorkflowTransitionRuleConfigurationsTypesItem], start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, keys: builtins.list[str] | Unset = UNSET, workflow_names: builtins.list[str] | Unset = UNSET, with_tags: builtins.list[str] | Unset = UNSET, draft: bool | Unset = UNSET, expand: str | Unset = UNSET) -> _t.PageBeanWorkflowTransitionRules:
        """
        Get workflow transition rule configurations

        Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:

         *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
         *  matching one or more transition rule keys.

        Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.

        Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.
        """
        return cast('_t.PageBeanWorkflowTransitionRules', self._runtime.call('get_workflow_transition_rule_configurations', call_args({'start_at': start_at, 'max_results': max_results, 'types': types, 'keys': keys, 'workflow_names': workflow_names, 'with_tags': with_tags, 'draft': draft, 'expand': expand})))

    def update_configurations(self, *, workflows: builtins.list[_t.WorkflowTransitionRules]) -> _t.WorkflowTransitionRulesUpdateErrors:
        """
        Update workflow transition rule configurations

        Updates configuration of workflow transition rules. The following rule types are supported:

         *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
         *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
         *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

        Only rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app can be updated.

        To assist with app migration, this operation can be used to:

         *  Disable a rule.
         *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).

        Rules are enabled if the `disabled` parameter is not provided.

        **Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

        **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.
        """
        return cast('_t.WorkflowTransitionRulesUpdateErrors', self._runtime.call('update_workflow_transition_rule_configurations', call_args({}, {'body': {'workflows': workflows}}, required=frozenset({'body'}))))

    def delete_configurations(self, *, workflows: builtins.list[_t.WorkflowTransitionRulesDetails]) -> _t.WorkflowTransitionRulesUpdateErrors:
        """
        Delete workflow transition rule configurations

        Deletes workflow transition rules from one or more workflows. These rule types are supported:

         *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
         *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
         *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

        Only rules created by the calling Connect app can be deleted.

        **Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

        **[Permissions](#permissions) required:** Only Connect apps can use this operation.
        """
        return cast('_t.WorkflowTransitionRulesUpdateErrors', self._runtime.call('delete_workflow_transition_rule_configurations', call_args({}, {'body': {'workflows': workflows}}, required=frozenset({'body'}))))

class _WorkflowsResource:
    """Operations under ``workflows``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def read_from_history(self, *, version: int | Unset = UNSET, workflow_id: str | Unset = UNSET) -> _t.WorkflowHistoryReadResponseDto:
        """
        Read workflow version from history

        Returns a workflow and related statuses for a specified workflow id and version number.

        **Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to access all, including project-scoped, workflows
         *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
        """
        return cast('_t.WorkflowHistoryReadResponseDto', self._runtime.call('read_workflow_from_history', call_args({}, {'body': {'version': version, 'workflow_id': workflow_id}})))

    def list_history(self, *, expand: str | Unset = UNSET, workflow_id: str | Unset = UNSET) -> _t.WorkflowHistoryListResponseDto:
        """
        List workflow history entries

        Returns a list of workflow history entries for a specified workflow id.

        **Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to access all, including project-scoped, workflows
         *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
        """
        return cast('_t.WorkflowHistoryListResponseDto', self._runtime.call('list_workflow_history', call_args({'expand': expand}, {'body': {'workflow_id': workflow_id}})))

    def get_paginated(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, workflow_name: builtins.list[str] | Unset = UNSET, expand: str | Unset = UNSET, query_string: str | Unset = UNSET, order_by: _t.GetWorkflowsPaginatedOrderBy | Unset = UNSET, is_active: bool | Unset = UNSET) -> _t.PageBeanWorkflow:
        """
        Get workflows paginated

        This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2569); use [Search workflows](#api-rest-api-3-workflows-search-get) instead.

        Returns a [paginated](#pagination) list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned.

        This operation does not return next-gen workflows.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

        Deprecated.
        """
        return cast('_t.PageBeanWorkflow', self._runtime.call('get_workflows_paginated', call_args({'start_at': start_at, 'max_results': max_results, 'workflow_name': workflow_name, 'expand': expand, 'query_string': query_string, 'order_by': order_by, 'is_active': is_active})))

    def delete(self, *, entity_id: str) -> None:
        """
        Delete inactive workflow

        Deletes a workflow.

        The workflow cannot be deleted if it is:

         *  an active workflow.
         *  a system workflow.
         *  associated with any workflow scheme.
         *  associated with any draft workflow scheme.

        **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
        """
        self._runtime.call('delete_inactive_workflow', call_args({'entity_id': entity_id}))

    def list_project_issue_type_usages(self, *, workflow_id: str, project_id: int, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.WorkflowProjectIssueTypeUsageDto:
        """
        Get issue types in a project that are using a given workflow

        Returns a page of issue types using a given workflow within a project.
        """
        return cast('_t.WorkflowProjectIssueTypeUsageDto', self._runtime.call('get_workflow_project_issue_type_usages', call_args({'workflow_id': workflow_id, 'project_id': project_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def get(self, *, workflow_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.WorkflowProjectUsageDto:
        """
        Get projects using a given workflow

        Returns a page of projects using a given workflow.
        """
        return cast('_t.WorkflowProjectUsageDto', self._runtime.call('get_project_usages_for_workflow', call_args({'workflow_id': workflow_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def get_scheme_usages_for_workflow(self, *, workflow_id: str, next_page_token: str | Unset = UNSET, max_results: int | Unset = UNSET) -> _t.WorkflowSchemeUsageDto:
        """
        Get workflow schemes which are using a given workflow

        Returns a page of workflow schemes using a given workflow.
        """
        return cast('_t.WorkflowSchemeUsageDto', self._runtime.call('get_workflow_scheme_usages_for_workflow', call_args({'workflow_id': workflow_id, 'next_page_token': next_page_token, 'max_results': max_results})))

    def read(self, *, project_and_issue_types: builtins.list[_t.ProjectAndIssueTypePair] | Unset = UNSET, workflow_ids: builtins.list[str] | Unset = UNSET, workflow_names: builtins.list[str] | Unset = UNSET) -> _t.WorkflowReadResponse:
        """
        Bulk get workflows

        Returns a list of workflows and related statuses by providing workflow names, workflow IDs, or project and issue types.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to access all, including project-scoped, workflows
         *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
        """
        return cast('_t.WorkflowReadResponse', self._runtime.call('read_workflows', call_args({}, {'body': {'project_and_issue_types': project_and_issue_types, 'workflow_ids': workflow_ids, 'workflow_names': workflow_names}})))

    def capabilities(self, *, workflow_id: str | Unset = UNSET, project_id: str | Unset = UNSET, issue_type_id: str | Unset = UNSET) -> _t.WorkflowCapabilities:
        """
        Get available workflow capabilities

        Get the list of workflow capabilities for a specific workflow using either the workflow ID, or the project and issue type ID pair. The response includes the scope of the workflow, defined as global/project-based, and a list of project types that the workflow is scoped to. It also includes all rules organised into their broad categories (conditions, validators, actions, triggers, screens) as well as the source location (Atlassian-provided, Connect, Forge).

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to access all, including global-scoped, workflows
         *  *Administer projects* project permissions to access project-scoped workflows

        The current list of Atlassian-provided rules:

        #### Validators ####

        A validator rule that checks if a user has the required permissions to execute the transition in the workflow.

        ##### Permission validator #####

        A validator rule that checks if a user has the required permissions to execute the transition in the workflow.

            {
               "ruleKey": "system:check-permission-validator",
               "parameters": {
                 "permissionKey": "ADMINISTER_PROJECTS"
               }
             }

        Parameters:

         *  `permissionKey` The permission required to perform the transition. Allowed values: [built-in Jira permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/#built-in-permissions).

        ##### Parent or child blocking validator #####

        A validator to block the child issue's transition depending on the parent issue's status.

            {
               "ruleKey" : "system:parent-or-child-blocking-validator"
               "parameters" : {
                 "blocker" : "PARENT"
                 "statusIds" : "1,2,3"
               }
             }

        Parameters:

         *  `blocker` currently only supports `PARENT`.
         *  `statusIds` a comma-separated list of status IDs.

        ##### Previous status validator #####

        A validator that checks if an issue has transitioned through specified previous status(es) before allowing the current transition to occur.

            {
               "ruleKey": "system:previous-status-validator",
               "parameters": {
                 "previousStatusIds": "10014",
                 "mostRecentStatusOnly": "true"
               }
             }

        Parameters:

         *  `previousStatusIds` a comma-separated list of status IDs, currently only support one ID.
         *  `mostRecentStatusOnly` when `true` only considers the most recent status for the condition evaluation. Allowed values: `true`, `false`.

        ##### Validate a field value #####

        A validation that ensures a specific field's value meets the defined criteria before allowing an issue to transition in the workflow.

        Depending on the rule type, the result will vary:

        ###### Field required ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "fieldRequired",
                 "fieldsRequired": "assignee",
                 "ignoreContext": "true",
                 "errorMessage": "An assignee must be set!"
               }
             }

        Parameters:

         *  `fieldsRequired` the ID of the field that is required. For a custom field, it would look like `customfield_123`.
         *  `ignoreContext` controls the impact of context settings on field validation. When set to `true`, the validator doesn't check a required field if its context isn't configured for the current issue. When set to `false`, the validator requires a field even if its context is invalid. Allowed values: `true`, `false`.
         *  `errorMessage` is the error message to display if the user does not provide a value during the transition. A default error message will be shown if you don't provide one (Optional).

        ###### Field changed ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "fieldChanged",
                 "groupsExemptFromValidation": "6862ac20-8672-4f68-896d-4854f5efb79e",
                 "fieldKey": "versions",
                 "errorMessage": "Affect versions must be modified before transition"
               }
             }

        Parameters:

         *  `groupsExemptFromValidation` a comma-separated list of group IDs to be exempt from the validation.
         *  `fieldKey` the ID of the field that has changed. For a custom field, it would look like `customfield_123`.
         *  `errorMessage` the error message to display if the user does not provide a value during the transition. A default error message will be shown if you don't provide one (Optional).

        ###### Field has a single value ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "fieldHasSingleValue",
                 "fieldKey": "created",
                 "excludeSubtasks": "true"
               }
             }

        Parameters:

         *  `fieldKey` the ID of the field to validate. For a custom field, it would look like `customfield_123`.
         *  `excludeSubtasks` Option to exclude values copied from sub-tasks. Allowed values: `true`, `false`.

        ###### Field matches regular expression ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "fieldMatchesRegularExpression",
                 "regexp": "[0-9]{4}",
                 "fieldKey": "description",
                 "errorMessage": "Description must contain a 4-digit year"
               }
             }

        Parameters:

         *  `regexp` the regular expression used to validate the field's content.
         *  `fieldKey` the ID of the field to validate. For a custom field, it would look like `customfield_123`.
         *  `errorMessage` the error message to display if the field value does not match the regular expression. A default error message will be shown if you don't provide one (Optional).

        ###### Date field comparison ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "dateFieldComparison",
                 "date1FieldKey": "duedate",
                 "date2FieldKey": "customfield_10054",
                 "includeTime": "true",
                 "conditionSelected": ">="
               }
             }

        Parameters:

         *  `date1FieldKey` the ID of the first field to compare. For a custom field, it would look like `customfield_123`.
         *  `date2FieldKey` the ID of the second field to compare. For a custom field, it would look like `customfield_123`.
         *  `includeTime` if `true`, compares both date and time. Allowed values: `true`, `false`.
         *  `conditionSelected` the condition to compare with. Allowed values: `>`, `>=`, `=`, `<=`, `<`, `!=`.

        ###### Date range comparison ######

            {
               "ruleKey": "system:validate-field-value",
               "parameters": {
                 "ruleType": "windowDateComparison",
                 "date1FieldKey": "customfield_10009",
                 "date2FieldKey": "customfield_10054",
                 "numberOfDays": "3"
               }
             }

        Parameters:

         *  `date1FieldKey` the ID of the first field to compare. For a custom field, it would look like `customfield_123`.
         *  `date2FieldKey` the ID of the second field to compare. For a custom field, it would look like `customfield_123`.
         *  `numberOfDays` maximum number of days past the reference date (`date2FieldKey`) to pass validation.

        This rule is composed by aggregating the following legacy rules:

         *  FieldRequiredValidator
         *  FieldChangedValidator
         *  FieldHasSingleValueValidator
         *  RegexpFieldValidator
         *  DateFieldValidator
         *  WindowsDateValidator

        ##### Pro forma: Forms attached validator #####

        Validates that one or more forms are attached to the issue.

            {
               "ruleKey" : "system:proforma-forms-attached"
               "parameters" : {}
             }

        ##### Proforma: Forms submitted validator #####

        Validates that all forms attached to the issue have been submitted.

            {
               "ruleKey" : "system:proforma-forms-submitted"
               "parameters" : {}
             }

        #### Conditions ####

        Conditions enable workflow rules that govern whether a transition can execute.

        ##### Check field value #####

        A condition rule evaluates as true if a specific field's value meets the defined criteria. This rule ensures that an issue can only transition to the next step in the workflow if the field's value matches the desired condition.

            {
               "ruleKey": "system:check-field-value",
               "parameters": {
                 "fieldId": "description",
                 "fieldValue": "[\\"Done\\"]",
                 "comparator": "=",
                 "comparisonType": "STRING"
               }
             }

        Parameters:

         *  `fieldId` The ID of the field to check the value of. For non-system fields, it will look like `customfield_123`. Note: `fieldId` is used interchangeably with the idea of `fieldKey` here, they refer to the same field.
         *  `fieldValue` the list of values to check against the field\\\\u2019s value.
         *  `comparator` The comparison logic. Allowed values: `>`, `>=`, `=`, `<=`, `<`, `!=`.
         *  `comparisonType` The type of data being compared. Allowed values: `STRING`, `NUMBER`, `DATE`, `DATE_WITHOUT_TIME`, `OPTIONID`.

        ##### Restrict issue transition #####

        This rule ensures that issue transitions are restricted based on user accounts, roles, group memberships, and permissions, maintaining control over who can transition an issue. This condition evaluates as `true` if any of the following criteria is met.

            {
               "ruleKey": "system:restrict-issue-transition",
               "parameters": {
                 "accountIds": "allow-reporter,5e68ac137d64450d01a77fa0",
                 "roleIds": "10002,10004",
                 "groupIds": "703ff44a-7dc8-4f4b-9aa6-a65bf3574fa4",
                 "permissionKeys": "ADMINISTER_PROJECTS",
                 "groupCustomFields": "customfield_10028",
                 "allowUserCustomFields": "customfield_10072,customfield_10144,customfield_10007",
                 "denyUserCustomFields": "customfield_10107"
               }
             }

        Parameters:

         *  `accountIds` a comma-separated list of the user account IDs. It also allows generic values like: `allow-assignee`, `allow-reporter`, and `accountIds` Note: This is only supported in team-managed projects
         *  `roleIds` a comma-separated list of role IDs.
         *  `groupIds` a comma-separated list of group IDs.
         *  `permissionKeys` a comma-separated list of permission keys. Allowed values: [built-in Jira permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/#built-in-permissions).
         *  `groupCustomFields` a comma-separated list of group custom field IDs.
         *  `allowUserCustomFields` a comma-separated list of user custom field IDs to allow for issue transition.
         *  `denyUserCustomFields` a comma-separated list of user custom field IDs to deny for issue transition.

        This rule is composed by aggregating the following legacy rules:

         *  AllowOnlyAssignee
         *  AllowOnlyReporter
         *  InAnyProjectRoleCondition
         *  InProjectRoleCondition
         *  UserInAnyGroupCondition
         *  UserInGroupCondition
         *  PermissionCondtion
         *  InGroupCFCondition
         *  UserIsInCustomFieldCondition

        ##### Previous status condition #####

        A condition that evaluates based on an issue's previous status(es) and specific criteria.

            {
               "ruleKey" : "system:previous-status-condition"
               "parameters" : {
                 "previousStatusIds" : "10004",
                 "not": "true",
                 "mostRecentStatusOnly" : "true",
                 "includeCurrentStatus": "true",
                 "ignoreLoopTransitions": "true"
               }
             }

        Parameters:

         *  `previousStatusIds` a comma-separated list of status IDs, current only support one ID.
         *  `not` indicates if the condition should be reversed. When `true` it checks that the issue has not been in the selected statuses. Allowed values: `true`, `false`.
         *  `mostRecentStatusOnly` when true only considers the most recent status for the condition evaluation. Allowed values: `true`, `false`.
         *  `includeCurrentStatus` includes the current status when evaluating if the issue has been through the selected statuses. Allowed values: `true`, `false`.
         *  `ignoreLoopTransitions` ignore loop transitions. Allowed values: `true`, `false`.

        ##### Parent or child blocking condition #####

        A condition to block the parent\\\\u2019s issue transition depending on the child\\\\u2019s issue status.

            {
               "ruleKey" : "system:parent-or-child-blocking-condition"
               "parameters" : {
                 "blocker" : "CHILD",
                 "statusIds" : "1,2,3"
               }
             }

        Parameters:

         *  `blocker` currently only supports `CHILD`.
         *  `statusIds` a comma-separated list of status IDs.

        ##### Separation of duties #####

        A condition preventing the user from performing, if the user has already performed a transition on the issue.

            {
               "ruleKey": "system:separation-of-duties",
               "parameters": {
                 "fromStatusId": "10161",
                 "toStatusId": "10160"
               }
             }

        Parameters:

         *  `fromStatusId` represents the status ID from which the issue is transitioning. It ensures that the user performing the current transition has not performed any actions when the issue was in the specified status.
         *  `toStatusId` represents the status ID to which the issue is transitioning. It ensures that the user performing the current transition is not the same user who has previously transitioned the issue.

        ##### Restrict transitions #####

        A condition preventing all users from transitioning the issue can also optionally include APIs as well.

            {
               "ruleKey": "system:restrict-from-all-users",
               "parameters": {
                 "restrictMode": "users"
               }
             }

        Parameters:

         *  `restrictMode` restricts the issue transition including/excluding APIs. Allowed values: `"users"`, `"usersAndAPI"`.

        ##### Jira Service Management block until approved #####

        Block an issue transition until approval. Note: This is only supported in team-managed projects.

            {
               "ruleKey": "system:jsd-approvals-block-until-approved",
               "parameters": {
                 "approvalConfigurationJson": "{"statusExternalUuid...}"
               }
             }

        Parameters:

         *  `approvalConfigurationJson` a stringified JSON holding the Jira Service Management approval configuration.

        ##### Jira Service Management block until rejected #####

        Block an issue transition until rejected. Note: This is only supported in team-managed projects.

            {
               "ruleKey": "system:jsd-approvals-block-until-rejected",
               "parameters": {
                 "approvalConfigurationJson": "{"statusExternalUuid...}"
               }
             }

        Parameters:

         *  `approvalConfigurationJson` a stringified JSON holding the Jira Service Management approval configuration.

        ##### Block in progress approval #####

        Condition to block issue transition if there is pending approval. Note: This is only supported in company-managed projects.

            {
               "ruleKey": "system:block-in-progress-approval",
               "parameters": {}
             }

        #### Post functions ####

        Post functions carry out any additional processing required after a workflow transition is executed.

        ##### Change assignee #####

        A post function rule that changes the assignee of an issue after a transition.

            {
               "ruleKey": "system:change-assignee",
               "parameters": {
                 "type": "to-selected-user",
                 "accountId": "example-account-id"
               }
             }

        Parameters:

         *  `type` the parameter used to determine the new assignee. Allowed values: `to-selected-user`, `to-unassigned`, `to-current-user`, `to-current-user`, `to-default-user`, `to-default-user`
         *  `accountId` the account ID of the user to assign the issue to. This parameter is required only when the type is `"to-selected-user"`.

        ##### Copy field value #####

        A post function that automates the process of copying values between fields during a specific transition, ensuring data consistency and reducing manual effort.

            {
               "ruleKey": "system:copy-value-from-other-field",
               "parameters": {
                 "sourceFieldKey": "description",
                 "targetFieldKey": "components",
                 "issueSource": "SAME"
               }
             }

        Parameters:

         *  `sourceFieldKey` the field key to copy from. For a custom field, it would look like `customfield_123`
         *  `targetFieldKey` the field key to copy to. For a custom field, it would look like `customfield_123`
         *  `issueSource` `SAME` or `PARENT`. Defaults to `SAME` if no value is provided.

        ##### Update field #####

        A post function that updates or appends a specific field with the given value.

            {
               "ruleKey": "system:update-field",
               "parameters": {
                 "field": "customfield_10056",
                 "value": "asdf",
                 "mode": "append"
               }
             }

        Parameters:

         *  `field` the ID of the field to update. For a custom field, it would look like `customfield_123`
         *  `value` the value to update the field with.
         *  `mode` `append` or `replace`. Determines if a value will be appended to the current value, or if the current value will be replaced.

        ##### Trigger webhook #####

        A post function that automatically triggers a predefined webhook when a transition occurs in the workflow.

            {
               "ruleKey": "system:trigger-webhook",
               "parameters": {
                 "webhookId": "1"
               }
             }

        Parameters:

         *  `webhookId` the ID of the webhook.

        ##### Trigger agent #####

        A post function that triggers a Jira AI agent for the issue after the transition runs, using the configured agent and an optional prompt. The agent run is asynchronous: it is scheduled after the transition finishes and does not block the transition.

            {
               "ruleKey": "system:trigger-agent",
               "parameters": {
                 "agentId": "712020:3c6d3f05-331a-4488-932e-37c34b704720",
                 "promptValue": ""
               }
             }

        Parameters:

         *  `agentId` the identifier of the agent to trigger (the Atlassian account ID of the agent).
         *  `promptValue` optional text passed to the agent as a user prompt after the transition runs; use an empty string if no extra prompt is needed.

        #### Screen ####

        ##### Remind people to update fields #####

        A screen rule that prompts users to update a specific field when they interact with an issue screen during a transition. This rule is useful for ensuring that users provide or modify necessary information before moving an issue to the next step in the workflow.

            {
               "ruleKey": "system:remind-people-to-update-fields",
               "params": {
                 "remindingFieldIds": "assignee,customfield_10025",
                 "remindingMessage": "The message",
                 "remindingAlwaysAsk": "true"
               }
             }

        Parameters:

         *  `remindingFieldIds` a comma-separated list of field IDs. Note: `fieldId` is used interchangeably with the idea of `fieldKey` here, they refer to the same field.
         *  `remindingMessage` the message to display when prompting the users to update the fields.
         *  `remindingAlwaysAsk` always remind to update fields. Allowed values: `true`, `false`.

        ##### Shared transition screen #####

        A common screen that is shared between transitions in a workflow.

            {
               "ruleKey": "system:transition-screen",
               "params": {
                 "screenId": "3"
               }
             }

        Parameters:

         *  `screenId` the ID of the screen.

        #### Connect & Forge ####

        ##### Connect rules #####

        Validator/Condition/Post function for Connect app.

            {
               "ruleKey": "connect:expression-validator",
               "parameters": {
                 "appKey": "com.atlassian.app",
                 "config": "",
                 "id": "90ce590f-e90c-4cd3-8281-165ce41f2ac3",
                 "disabled": "false",
                 "tag": ""
               }
             }

        Parameters:

         *  `ruleKey` Validator: `connect:expression-validator`, Condition: `connect:expression-condition`, and Post function: `connect:remote-workflow-function`
         *  `appKey` the reference to the Connect app
         *  `config` a JSON payload string describing the configuration
         *  `id` the ID of the rule
         *  `disabled` determine if the Connect app is disabled. Allowed values: `true`, `false`.
         *  `tag` additional tags for the Connect app

        ##### Forge rules #####

        Validator/Condition/Post function for Forge app.

            {
               "ruleKey": "forge:expression-validator",
               "parameters": {
                 "key": "ari:cloud:ecosystem::extension/{appId}/{environmentId}/static/{moduleKey}",
                 "config": "{"searchString":"workflow validator"}",
                 "id": "a865ddf6-bb3f-4a7b-9540-c2f8b3f9f6c2",
                 "disabled": "false",
                 "tag": ""
               }
             }

        Parameters:

         *  `ruleKey` Validator: `forge:expression-validator`, Condition: `forge:expression-condition`, and Post function: `forge:workflow-post-function`
         *  `key` the identifier for the Forge app
         *  `config` the persistent stringified JSON configuration for the Forge rule
         *  `id` the ID of the Forge rule
         *  `disabled` determine if the Forge app is disabled. Allowed values: `true`, `false`.
         *  `tag` additional tags for the Forge app
        """
        return cast('_t.WorkflowCapabilities', self._runtime.call('workflow_capabilities', call_args({'workflow_id': workflow_id, 'project_id': project_id, 'issue_type_id': issue_type_id})))

    def copy(self, *, workflow_id: str, workflow_name: str, description: str | Unset = UNSET) -> _t.WorkflowCreateResponse:
        """
        Copy workflow

        Copies an existing workflow, and the statuses it uses, into a new workflow with the given name. The copy is created in the same scope as the workflow it is copied from. If no description is provided, the copy is created with an empty description.

        Copying a workflow requires permission both to read the workflow being copied and to create the copy, which is created in the same scope as its source.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to copy all, including project-scoped, workflows
         *  To copy a project-scoped workflow, either the *Edit workflows* project permission, or both the *View (read-only) workflow* and *Administer projects* project permissions
        """
        return cast('_t.WorkflowCreateResponse', self._runtime.call('copy_workflow', call_args({}, {'body': {'description': description, 'workflow_id': workflow_id, 'workflow_name': workflow_name}}, required=frozenset({'body'}))))

    def create(self, *, scope: _t.WorkflowScope | Unset = UNSET, statuses: builtins.list[_t.WorkflowStatusUpdate] | Unset = UNSET, workflows: builtins.list[_t.WorkflowCreate] | Unset = UNSET) -> _t.WorkflowCreateResponse:
        """
        Bulk create workflows

        Create workflows and related statuses.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to create all, including global-scoped, workflows
         *  *Administer projects* project permissions to create project-scoped workflows
        """
        return cast('_t.WorkflowCreateResponse', self._runtime.call('create_workflows', call_args({}, {'body': {'scope': scope, 'statuses': statuses, 'workflows': workflows}})))

    def validate_create(self, *, payload: _t.WorkflowCreateRequest, validation_options: _t.ValidationOptionsForCreate | Unset = UNSET) -> _t.WorkflowValidationErrorList:
        """
        Validate create workflows

        Validate the payload for bulk create workflows.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to create all, including global-scoped, workflows
         *  *Administer projects* project permissions to create project-scoped workflows
        """
        return cast('_t.WorkflowValidationErrorList', self._runtime.call('validate_create_workflows', call_args({}, {'body': {'payload': payload, 'validation_options': validation_options}}, required=frozenset({'body'}))))

    def get_default_editor(self) -> _t.DefaultWorkflowEditorResponse:
        """
        Get the user's default workflow editor

        Get the user's default workflow editor. This can be either the new editor or the legacy editor.
        """
        return cast('_t.DefaultWorkflowEditorResponse', self._runtime.call('get_default_editor', call_args({})))

    def read_previews(self, *, project_id: str, issue_type_ids: builtins.list[str] | Unset = UNSET, workflow_ids: builtins.list[str] | Unset = UNSET, workflow_names: builtins.list[str] | Unset = UNSET) -> _t.WorkflowPreviewResponse:
        """
        Preview workflow

        Returns a requested workflow within a given project. The response provides a read-only preview of the workflow, omitting full configuration details.

        **[Permissions](#permissions) required:**

         *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions
        """
        return cast('_t.WorkflowPreviewResponse', self._runtime.call('read_workflow_previews', call_args({}, {'body': {'issue_type_ids': issue_type_ids, 'project_id': project_id, 'workflow_ids': workflow_ids, 'workflow_names': workflow_names}}, required=frozenset({'body'}))))

    def search(self, *, start_at: int | Unset = UNSET, max_results: int | Unset = UNSET, expand: str | Unset = UNSET, query_string: str | Unset = UNSET, order_by: str | Unset = UNSET, scope: str | Unset = UNSET, is_active: bool | Unset = UNSET, project_id: int | Unset = UNSET) -> _t.WorkflowSearchResponse:
        """
        Search workflows

        Returns a [paginated](#pagination) list of global and project workflows. If workflow names are specified in the query string, details of those workflows are returned. Otherwise, all workflows are returned.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* global permission to access all, including project-scoped, workflows
         *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
        """
        return cast('_t.WorkflowSearchResponse', self._runtime.call('search_workflows', call_args({'start_at': start_at, 'max_results': max_results, 'expand': expand, 'query_string': query_string, 'order_by': order_by, 'scope': scope, 'is_active': is_active, 'project_id': project_id})))

    def update(self, *, statuses: builtins.list[_t.WorkflowStatusUpdate] | Unset = UNSET, workflows: builtins.list[_t.WorkflowUpdate] | Unset = UNSET) -> _t.WorkflowUpdateResponse:
        """
        Bulk update workflows

        Update workflows and related statuses.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to create all, including global-scoped, workflows
         *  *Administer projects* project permissions to create project-scoped workflows
        """
        return cast('_t.WorkflowUpdateResponse', self._runtime.call('update_workflows', call_args({}, {'body': {'statuses': statuses, 'workflows': workflows}})))

    def validate_update(self, *, payload: _t.WorkflowUpdateRequest, validation_options: _t.ValidationOptionsForUpdate | Unset = UNSET) -> _t.WorkflowValidationErrorList:
        """
        Validate update workflows

        Validate the payload for bulk update workflows.

        **[Permissions](#permissions) required:**

         *  *Administer Jira* project permission to create all, including global-scoped, workflows
         *  *Administer projects* project permissions to create project-scoped workflows
        """
        return cast('_t.WorkflowValidationErrorList', self._runtime.call('validate_update_workflows', call_args({}, {'body': {'payload': payload, 'validation_options': validation_options}}, required=frozenset({'body'}))))


class Client:
    """
    The Jira Cloud platform REST API client.

    Default base URL: https://your-domain.atlassian.net
    """

    def __init__(
        self,
        *,
        base_url: str | None = None,
        auth: AuthProvider | None = None,
        transport: Transport | None = None,
        middleware: Sequence[Middleware] | None = None,
        validate: bool = True,
        timeout: float = 30.0,
        allow_private: bool = False,
        response_validation: str = "strict",
        proxy: str | None = None,
        protocols: Mapping[str, Any] | None = None,
        hooks: Sequence[Any] = (),
    ) -> None:
        self._runtime = RuntimeClient(
            _model(),
            base_url=base_url,
            auth=auth,
            transport=transport,
            middleware=middleware,
            validate=validate,
            timeout=timeout,
            allow_private=allow_private,
            response_validation=response_validation,
            proxy=proxy,
            protocols={**PROTOCOLS, **(protocols or {})},
            hooks=hooks,
        )
        self.agents = _AgentsResource(self._runtime)
        self.announcement_banner = _AnnouncementBannerResource(self._runtime)
        self.app_data_policies = _AppDataPoliciesResource(self._runtime)
        self.app_migration = _AppMigrationResource(self._runtime)
        self.app_properties = _AppPropertiesResource(self._runtime)
        self.application_roles = _ApplicationRolesResource(self._runtime)
        self.audit_records = _AuditRecordsResource(self._runtime)
        self.avatars = _AvatarsResource(self._runtime)
        self.classification_levels = _ClassificationLevelsResource(self._runtime)
        self.dashboards = _DashboardsResource(self._runtime)
        self.dynamic_modules = _DynamicModulesResource(self._runtime)
        self.field_schemes = _FieldSchemesResource(self._runtime)
        self.filter_sharing = _FilterSharingResource(self._runtime)
        self.filters = _FiltersResource(self._runtime)
        self.group_and_user_picker = _GroupAndUserPickerResource(self._runtime)
        self.groups = _GroupsResource(self._runtime)
        self.issue_attachments = _IssueAttachmentsResource(self._runtime)
        self.issue_bulk_operations = _IssueBulkOperationsResource(self._runtime)
        self.issue_comment_properties = _IssueCommentPropertiesResource(self._runtime)
        self.issue_comments = _IssueCommentsResource(self._runtime)
        self.issue_custom_field_associations = _IssueCustomFieldAssociationsResource(self._runtime)
        self.issue_custom_field_configuration_apps = _IssueCustomFieldConfigurationAppsResource(self._runtime)
        self.issue_custom_field_contexts = _IssueCustomFieldContextsResource(self._runtime)
        self.issue_custom_field_options = _IssueCustomFieldOptionsResource(self._runtime)
        self.issue_custom_field_options_apps = _IssueCustomFieldOptionsAppsResource(self._runtime)
        self.issue_custom_field_values_apps = _IssueCustomFieldValuesAppsResource(self._runtime)
        self.issue_field_configurations = _IssueFieldConfigurationsResource(self._runtime)
        self.issue_fields = _IssueFieldsResource(self._runtime)
        self.issue_link_types = _IssueLinkTypesResource(self._runtime)
        self.issue_links = _IssueLinksResource(self._runtime)
        self.issue_navigator_settings = _IssueNavigatorSettingsResource(self._runtime)
        self.issue_notification_schemes = _IssueNotificationSchemesResource(self._runtime)
        self.issue_panels = _IssuePanelsResource(self._runtime)
        self.issue_priorities = _IssuePrioritiesResource(self._runtime)
        self.issue_properties = _IssuePropertiesResource(self._runtime)
        self.issue_redaction = _IssueRedactionResource(self._runtime)
        self.issue_remote_links = _IssueRemoteLinksResource(self._runtime)
        self.issue_resolutions = _IssueResolutionsResource(self._runtime)
        self.issue_search = _IssueSearchResource(self._runtime)
        self.issue_security_level = _IssueSecurityLevelResource(self._runtime)
        self.issue_security_schemes = _IssueSecuritySchemesResource(self._runtime)
        self.issue_type_properties = _IssueTypePropertiesResource(self._runtime)
        self.issue_type_schemes = _IssueTypeSchemesResource(self._runtime)
        self.issue_type_screen_schemes = _IssueTypeScreenSchemesResource(self._runtime)
        self.issue_types = _IssueTypesResource(self._runtime)
        self.issue_votes = _IssueVotesResource(self._runtime)
        self.issue_watchers = _IssueWatchersResource(self._runtime)
        self.issue_worklog_properties = _IssueWorklogPropertiesResource(self._runtime)
        self.issue_worklogs = _IssueWorklogsResource(self._runtime)
        self.issues = _IssuesResource(self._runtime)
        self.jira_expressions = _JiraExpressionsResource(self._runtime)
        self.jira_settings = _JiraSettingsResource(self._runtime)
        self.jql = _JqlResource(self._runtime)
        self.jql_functions_apps = _JqlFunctionsAppsResource(self._runtime)
        self.labels = _LabelsResource(self._runtime)
        self.license_metrics = _LicenseMetricsResource(self._runtime)
        self.migration_of_connect_modules_to_forge = _MigrationOfConnectModulesToForgeResource(self._runtime)
        self.myself = _MyselfResource(self._runtime)
        self.permission_schemes = _PermissionSchemesResource(self._runtime)
        self.permissions = _PermissionsResource(self._runtime)
        self.plans = _PlansResource(self._runtime)
        self.policies = _PoliciesResource(self._runtime)
        self.priority_schemes = _PrioritySchemesResource(self._runtime)
        self.project_avatars = _ProjectAvatarsResource(self._runtime)
        self.project_categories = _ProjectCategoriesResource(self._runtime)
        self.project_classification_levels = _ProjectClassificationLevelsResource(self._runtime)
        self.project_components = _ProjectComponentsResource(self._runtime)
        self.project_email = _ProjectEmailResource(self._runtime)
        self.project_features = _ProjectFeaturesResource(self._runtime)
        self.project_key_and_name_validation = _ProjectKeyAndNameValidationResource(self._runtime)
        self.project_permission_schemes = _ProjectPermissionSchemesResource(self._runtime)
        self.project_properties = _ProjectPropertiesResource(self._runtime)
        self.project_role_actors = _ProjectRoleActorsResource(self._runtime)
        self.project_roles = _ProjectRolesResource(self._runtime)
        self.project_templates = _ProjectTemplatesResource(self._runtime)
        self.project_types = _ProjectTypesResource(self._runtime)
        self.project_versions = _ProjectVersionsResource(self._runtime)
        self.projects = _ProjectsResource(self._runtime)
        self.screen_schemes = _ScreenSchemesResource(self._runtime)
        self.screen_tab_fields = _ScreenTabFieldsResource(self._runtime)
        self.screen_tabs = _ScreenTabsResource(self._runtime)
        self.screens = _ScreensResource(self._runtime)
        self.server_info = _ServerInfoResource(self._runtime)
        self.service_registry = _ServiceRegistryResource(self._runtime)
        self.status = _StatusResource(self._runtime)
        self.tasks = _TasksResource(self._runtime)
        self.teams_in_plan = _TeamsInPlanResource(self._runtime)
        self.time_tracking = _TimeTrackingResource(self._runtime)
        self.ui_modifications_apps = _UiModificationsAppsResource(self._runtime)
        self.user_properties = _UserPropertiesResource(self._runtime)
        self.user_search = _UserSearchResource(self._runtime)
        self.users = _UsersResource(self._runtime)
        self.webhooks = _WebhooksResource(self._runtime)
        self.workflow_scheme_drafts = _WorkflowSchemeDraftsResource(self._runtime)
        self.workflow_scheme_project_associations = _WorkflowSchemeProjectAssociationsResource(self._runtime)
        self.workflow_schemes = _WorkflowSchemesResource(self._runtime)
        self.workflow_status_categories = _WorkflowStatusCategoriesResource(self._runtime)
        self.workflow_statuses = _WorkflowStatusesResource(self._runtime)
        self.workflow_transition_rules = _WorkflowTransitionRulesResource(self._runtime)
        self.workflows = _WorkflowsResource(self._runtime)

    def list_worklogs_by_issue_id_and_worklog_id(self, *, requests: builtins.list[_t.WorklogCompositeKey] | Unset = UNSET) -> _t.BulkWorklogKeyResponseBean:
        """
        Get worklogs by issue id and worklog id

        Returns worklog details for a list of issue ID and worklog ID pairs.

        This is an internal API for bulk fetching worklogs by their issue and worklog IDs. Worklogs that don't exist will be filtered out from the response.

        The returned list of worklogs is limited to 1000 items.

        **[Permissions](#permissions) required:** This is an internal service-to-service API that requires ASAP authentication. No user permission checks are performed as this bypasses normal user context.
        """
        return cast('_t.BulkWorklogKeyResponseBean', self._runtime.call('get_worklogs_by_issue_id_and_worklog_id', call_args({}, {'body': {'requests': requests}})))
