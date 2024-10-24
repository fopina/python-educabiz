#!/usr/bin/env -S python3 -u
"""
dephell did this but no longer maintained??
"""

import argparse
import sys

# tomlkit over toml because it preserves format/comments :trophy:
from tomlkit import dumps, parse


def pipfile_to_pyproject(pipfile_path, pyproject_path, dry):
    with open(pipfile_path, 'r') as f:
        pipfile_content = f.read()
    with open(pyproject_path, 'r') as f:
        pyproject_content = f.read()

    pipfile_data = parse(pipfile_content)
    pyproject_data = parse(pyproject_content)

    if pyproject_data['project']['dependencies'] == pipfile_data.get('packages', {}):
        return False

    if not dry:
        pyproject_data['project']['dependencies'] = pipfile_data.get('packages', {})
        with open(pyproject_path, 'w') as f:
            f.write(dumps(pyproject_data))

    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fix', action='store_true', help='Apply required changes')
    args = p.parse_args()

    r = pipfile_to_pyproject('Pipfile', 'pyproject.toml', not args.fix)
    if r:
        if args.fix:
            print('pyproject.toml dependencies UPDATED!')
        else:
            print('pyproject.toml dependencies NEED UPDATE!')
            sys.exit(1)
    else:
        print('pyproject.toml dependecies are up to date')


if __name__ == '__main__':
    main()
