# python-educabiz

API client to interact with [educabiz.com](https://www.educabiz.com) portals.

## Install

```
pip install educabiz
```

## Usage

```python
from educabiz.client import Client

eb_client = Client(username, password, login_if_required=True)
data = eb_client.home()
print(f'School: {data["schoolname"]}')
children = eb_client.school_qrcodeinfo()['child']
for child in children.values():
    child_id = child['id']
    home_data = data['children'][child_id]
    print(f'{child_id}:')
    print(f'* Name: {html.unescape(child["name"])}')
    print(f'* Photo URL: {home_data["photo"]}')
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
```

## Build

Check out [CONTRIBUTING.md](CONTRIBUTING.md)
