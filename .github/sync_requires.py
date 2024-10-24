#!/usr/bin/env -S python3 -u
"""
dephell did this but no longer maintained??
"""
import argparse

# tomlkit over toml because it preserves format/comments :trophy:
from tomlkit import dumps
from tomlkit import parse


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fix', action='store_true', help='Apply required changes')
    args = p.parse_args()

    def pipfile_to_pyproject(pipfile_path, pyproject_path):
        with open(pipfile_path, 'r') as f:
            pipfile_content = f.read()
        with open(pyproject_path, 'r') as f:
            pyproject_content = f.read()

        pipfile_data = parse(pipfile_content)
        pyproject_data = parse(pyproject_content)
        pyproject_data['project']['dependencies'] = pipfile_data.get('packages', {})

        # Write the pyproject.toml file
        with open(pyproject_path, 'w') as f:
            f.write(dumps(pyproject_data))

    # Convert Pipfile to pyproject.toml
    pipfile_to_pyproject('Pipfile', 'pyproject.toml')

    print('Conversion from Pipfile to pyproject.toml is complete.')


if __name__ == '__main__':
    main()
