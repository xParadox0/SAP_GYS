# GitHub ↔ Postman Integration Guide

## Goal

Use GitHub as the source-controlled home for your Postman assets.

## What should live in GitHub

- Postman collections
- safe environment templates
- generated documentation
- validation scripts
- workflow automation

## What should not live in GitHub

- passwords
- bearer tokens
- personal access tokens
- production-only secrets
- unmasked credential examples

## Recommended repository flow

1. Maintain the main collection in Postman
2. Export the collection JSON into `postman/collections/`
3. Export a sanitized environment template into `postman/environments/`
4. Commit changes to GitHub
5. Let CI validate file structure
6. Optionally generate docs or PDF exports from those committed assets

## Suggested naming convention

### Collections
- `SAP_GYS.postman_collection.json`

### Environments
- `dev.template.postman_environment.json`
- `uat.template.postman_environment.json`
- `prod.template.postman_environment.json`

## Practical next step for this repo

Add your exported Postman collection file here:

`postman/collections/SAP_GYS.postman_collection.json`

Then I can:
- validate it
- summarize endpoints
- generate docs
- export polished PDF documentation from the committed collection
