#!/usr/bin/env -S python3 -u

import requests
import dotenv
import os
from datetime import datetime, date


class Client(requests.Session):
    URL = 'https://mobile.educabiz.com'

    def request(self, method, url, *a, **b):
        if url[0] == '/':
            url = f'{self.URL}{url}'
        return super().request(method, url, *a, **b)

    def login(self, username, password):
        r = self.post('/mobile/login', data={'username': username, 'password': password})
        r.raise_for_status()
        r = r.json()
        assert r['status'] == 'ok'
        return r

    def home(self):
        r = self.get('/educators/home')
        r.raise_for_status()
        return r.json()

    def notifications(self):
        r = self.get('/educators/notifications')
        r.raise_for_status()
        return r.json()

    def child_payments(self, child):
        r = self.get(f'/child/{child}/payments')
        r.raise_for_status()
        return r.json()

    def child_report(self, child, page=0, build_page=False):
        r = self.post(f'/child/{child}/report', data={'page': page, 'buildPage': build_page})
        r.raise_for_status()
        return r.json()

    def child_messages(self, child, page=1):
        r = self.get(f'/child/{child}/messages/income', params={'page': page})
        r.raise_for_status()
        return r.json()

    def child_services(self, child):
        r = self.get(f'/child/{child}/services')
        r.raise_for_status()
        return r.json()

    def child_timetable(self, child):
        r = self.get(f'/child/{child}/timetable')
        r.raise_for_status()
        return r.json()

    def child_gallery(self, child, page=1, build_page=False):
        r = self.get(
            f'/child/{child}/gallery',
            params={
                'page': page,
                'buildPage': build_page,
                'childId': child,
                'serviceId': '',
            },
        )
        r.raise_for_status()
        return r.json()

    def school_qrcodeinfo(self):
        r = self.get(
            '/school/qrcodeinfo',
        )
        r.raise_for_status()
        return r.json()

    def _bool(self, b):
        return 'true' if b else 'false'

    def _schoolctrl_save_presence(
        self,
        path: str,
        child_id: str,
        date: date,
        notes='',
        absent=False,
        is_checked=True,
        is_enter=False,
        number_day=1,
    ):
        r = self.post(
            f'/schoolctrl/{path}',
            data={
                'colabId': '',
                'date': date.strftime('%d-%m-%Y'),
                'notes': notes,
                'absent': self._bool(absent),
                'isChecked': self._bool(is_checked),
                'isEnter': self._bool(is_enter),
                'numberDay': number_day,
                'childId': child_id,
            },
        )
        r.raise_for_status()
        return r.json()

    def schoolctrl_save_presence_note(self, child_id: str, date: datetime.date, notes=''):
        return self._schoolctrl_save_presence('savepresencesinglenote', child_id, date, notes=notes, absent=True)

    def schoolctrl_save_presence_out(self, child_id: str, date: datetime.date):
        return self._schoolctrl_save_presence('savepresenceout', child_id, date)

    def schoolctrl_save_presence_in(self, child_id: str, date: datetime.date):
        return self._schoolctrl_save_presence('savepresencein', child_id, date, is_enter=True)


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
