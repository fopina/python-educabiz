from datetime import date, datetime

import requests

from educabiz.exceptions import LoginFailedError


class Client(requests.Session):
    URL = 'https://mobile.educabiz.com'

    def __init__(self, username: str, password: str, login_if_required=False):
        super().__init__()
        self._username = username
        self._password = password
        self._relogin = login_if_required

    def request(self, method, url, *a, login_if_required=True, **b):
        if url[0] == '/':
            url = f'{self.URL}{url}'
        r = super().request(method, url, *a, **b)
        if login_if_required and self._relogin:
            try:
                data = r.json()
            except Exception:
                return r
            if data.get('formAction') == 'https://mobile.educabiz.com/authenticate':
                self.login()
                return super().request(method, url, *a, **b)

        return r

    def login(self):
        r = self.post(
            '/mobile/login', login_if_required=False, data={'username': self._username, 'password': self._password}
        )
        r.raise_for_status()
        r = r.json()
        if r['status'] != 'ok':
            raise LoginFailedError()
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
                'absent': _bool(absent),
                'isChecked': _bool(is_checked),
                'isEnter': _bool(is_enter),
                'numberDay': number_day,
                'childId': child_id,
            },
        )
        r.raise_for_status()
        return r.json()

    def schoolctrl_save_presence_note(self, child_id: str, date: date, notes=''):
        return self._schoolctrl_save_presence('savepresencesinglenote', child_id, date, notes=notes, absent=True)

    def schoolctrl_save_presence_out(self, child_id: str, date: date):
        return self._schoolctrl_save_presence('savepresenceout', child_id, date)

    def schoolctrl_save_presence_in(self, child_id: str, date: date):
        return self._schoolctrl_save_presence('savepresencein', child_id, date, is_enter=True)

    def child_check_in(self, child_id: str):
        """Check in kid in current day"""
        return self.schoolctrl_save_presence_in(child_id, datetime.now())

    def child_check_out(self, child_id: str):
        """Check out kid in current day"""
        return self.schoolctrl_save_presence_out(child_id, datetime.now())

    def child_absent(self, child_id: str, reason: str):
        """Leave note that kid is absent"""
        return self.schoolctrl_save_presence_note(child_id, datetime.now(), notes=reason)


def _bool(b):
    return 'true' if b else 'false'
