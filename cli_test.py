#!/usr/bin/env -S python3 -u

import html
import os

import dotenv

from educabiz.client import Client


def cli():
    dotenv.load_dotenv()
    c = Client(os.getenv('EDUCA_USERNAME'), os.getenv('EDUCA_PASSWORD'), login_if_required=True)
    data = c.home()
    print(f'School: {data.schoolname}')
    children = c.school_qrcodeinfo()['child']
    for child in children.values():
        child_id = child['id']
        home_data = data.children[child_id]
        print(f'{child_id}:')
        print(f'* Name: {html.unescape(child["name"])}')
        print(f'* Photo URL: {home_data.photo}')
        presence = child['presence'][0]
        if presence['id'] == 'undefined':
            presence_str = '(none)'
        elif presence['absent']:
            presence_str = f'absent ({presence["notes"]})'
        elif presence['hourOut'] == '--:--':
            presence_str = f'checked in at {presence["hourIn"]}'
        else:
            presence_str = f'checked in at {presence["hourIn"]} and out at {presence["hourOut"]}'
        print(f'* Presence: {presence_str}')


if __name__ == '__main__':
    cli()
