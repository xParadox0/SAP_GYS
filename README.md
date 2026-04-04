# SAP_GYS

Repository prepared for GitHub ↔ Postman integration.

This repo is structured to store and manage:
- Postman collections
- Postman environments
- exported documentation assets
- validation scripts
- GitHub Actions checks for Postman files

## Repository structure

- `postman/collections/`
  - Store exported Postman collection JSON files
- `postman/environments/`
  - Store environment JSON files or templates
- `docs/`
  - Human-readable API and integration documentation
- `scripts/`
  - Utility scripts for validation and automation
- `.github/workflows/`
  - CI checks for collection/environment quality

## Recommended workflow

1. Export your Postman collection into `postman/collections/`
2. Export a safe environment template into `postman/environments/`
3. Keep real secrets out of GitHub
4. Use GitHub commits to version API changes
5. Let GitHub Actions validate JSON structure on every push

## Security guidance

Do not commit:
- live bearer tokens
- passwords
- API keys
- production secrets

Commit only:
- collection files
- environment templates with placeholders
- documentation
- test examples with masked values

## Next suggested files to add

- `postman/collections/SAP_GYS.postman_collection.json`
- `postman/environments/dev.template.postman_environment.json`
- generated PDF/API docs under `docs/`

## CI behavior

The included workflow validates:
- JSON syntax for Postman collection/environment files
- basic Postman file shape checks
- template environment safety checks
