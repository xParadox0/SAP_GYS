# Postman Assets

This folder stores versioned Postman assets.

## Folders

- `collections/` — exported Postman collection JSON
- `environments/` — exported or templated Postman environment JSON

## Rules

1. Commit collections freely.
2. Commit only safe environment templates.
3. Do not commit secrets or live tokens.
4. Prefer filenames like:
   - `SAP_GYS.postman_collection.json`
   - `dev.template.postman_environment.json`
   - `uat.template.postman_environment.json`

## Suggested process

- Keep one canonical collection in GitHub
- Update it whenever endpoints or examples change
- Export environment templates with placeholder values only
- Keep sensitive values in Postman or GitHub Secrets, not in the repo
