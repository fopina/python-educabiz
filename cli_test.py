#!/usr/bin/env -S python3 -u

import os

import dotenv

from educabiz.client import Client


def cli():
    dotenv.load_dotenv()
    c = Client()
    c.login(os.getenv('EDUCA_USERNAME'), os.getenv('EDUCA_PASSWORD'))
    data = c.home()
    print(f'School: {data["schoolname"]}')
    for child_id, child in data['children'].items():
        print(f'{child_id}:')
        print(f'* Name: {child["name"]}')


if __name__ == '__main__':
    cli()
