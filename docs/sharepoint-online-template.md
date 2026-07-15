# SharePoint Online Template

## Files

- `postman/collections/SharePointOnline.postman_collection.json` — request collection covering Auth, Sites, Lists, List Items, Files, and Users
- `postman/environments/sharepoint-online.template.postman_environment.json` — matching environment template with placeholder values

## Authentication

The collection uses Azure AD app-only auth (client credentials flow):

1. Register an app in Azure AD (Entra ID).
2. Grant it an application permission such as `Sites.Read.All` or `Sites.ReadWrite.All` (Microsoft Graph) and get admin consent.
3. Create a client secret for the app.
4. In Postman, fill in `tenant_id`, `client_id`, and `client_secret` on the environment (never commit real values — keep them in Postman only, matching the pattern used for `token` in `dev.template.postman_environment.json`).
5. Run **Auth → Get Access Token (Client Credentials)**. Its test script stores the result in the `access_token` environment variable, which the rest of the collection uses via the collection-level Bearer auth.

## Two API surfaces

- **Microsoft Graph** (`{{graph_base}}`, `https://graph.microsoft.com/v1.0`) — recommended for new integrations. Requires `site_id`, obtained from **Sites → Get Site (Graph, by server-relative path)**.
- **Classic SharePoint REST API** (`{{site_url}}/_api/...`) — useful when you need list/library operations not yet covered by Graph, or when working with older tenants.

## Filling in variables

Update the environment template (or your local Postman-only copy) with:

- `tenant_name`, `site_name`, `site_url` — your tenant and target site
- `list_title`, `list_id`, `list_item_entity_type` — target list details (`list_item_entity_type` is the list's `ListItemEntityTypeFullName`, e.g. `SP.Data.MyListListItem`)
- `folder_relative_url`, `file_relative_url`, `upload_file_name` — for the Files requests

## Validation

`scripts/validate_postman_assets.py` runs against everything in `postman/collections/` and `postman/environments/`, so this template is checked by the same CI workflow (`.github/workflows/validate-postman.yml`) as the existing SAP collection.
