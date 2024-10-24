#!/usr/bin/env -S python3 -u

import os

import dotenv

from educabiz.client import Client
from datetime import datetime


def cli():
    dotenv.load_dotenv()
    c = Client()
    c.login(os.getenv('EDUCA_USERNAME'), os.getenv('EDUCA_PASSWORD'))
    data = c.home()
    print(f'School: {data["schoolname"]}')
    for child_id, child in data['children'].items():
        print(f'{child_id}:')
        print(f'* Name: {child["name"]}')
    children = c.school_qrcodeinfo()['child']
    for child in children.values():
        print(child)
        assert len(child['presence']) == 1
        assert child['presence'][0]['id'] == 'undefined'
        # after check-in!
        # [{'id': '42039492', 'hourIn': '11:57', 'hourOut': '--:--', 'notes': '', 'date': '2024-10-24 00:00:00.0', 'absent': False, 'presenceNumber': '1'}]
        # after absent
        # [{'id': '42039680', 'hourIn': '--:--', 'hourOut': '--:--', 'notes': 'Doente', 'date': '2024-10-24 00:00:00.0', 'absent': True, 'presenceNumber': '1'}]}
        # print(c.child_check_in(child['id']))
        # print(c.child_absent(child['id'], 'Doente'))


if __name__ == '__main__':
    cli()
