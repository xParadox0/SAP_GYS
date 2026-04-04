#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTMAN_DIR = ROOT / 'postman'


def fail(msg):
    print(f'ERROR: {msg}')
    sys.exit(1)


def check_json_file(path: Path):
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        fail(f'{path}: invalid JSON: {e}')
    return data


def validate_collection(path: Path):
    data = check_json_file(path)
    if 'info' not in data:
        fail(f'{path}: missing top-level info object')
    if 'item' not in data:
        fail(f'{path}: missing top-level item array')
    print(f'OK collection: {path}')


def validate_environment(path: Path):
    data = check_json_file(path)
    if data.get('_postman_variable_scope') != 'environment':
        fail(f'{path}: not a Postman environment export')
    values = data.get('values', [])
    for entry in values:
        key = str(entry.get('key', '')).lower()
        value = str(entry.get('value', ''))
        if key in {'password', 'token', 'apikey', 'api_key', 'secret'}:
            if value and 'SET_IN_POSTMAN_ONLY' not in value and 'example' not in value.lower() and 'placeholder' not in value.lower() and '{{' not in value:
                fail(f'{path}: sensitive-looking value committed for key {entry.get("key")}')
    print(f'OK environment: {path}')


def main():
    if not POSTMAN_DIR.exists():
        print('No postman directory found; nothing to validate.')
        return

    collection_files = sorted((POSTMAN_DIR / 'collections').glob('*.json')) if (POSTMAN_DIR / 'collections').exists() else []
    environment_files = sorted((POSTMAN_DIR / 'environments').glob('*.json')) if (POSTMAN_DIR / 'environments').exists() else []

    for path in collection_files:
        validate_collection(path)

    for path in environment_files:
        validate_environment(path)

    print('Validation complete.')


if __name__ == '__main__':
    main()
