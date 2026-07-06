import unittest
from unittest import mock

import requests

from educabiz import client


class Test(unittest.TestCase):
    @mock.patch('educabiz.client.requests.Session.request')
    def test_client_login(self, request_mock):
        request_mock.return_value.json.return_value = {'status': 'ok'}
        c = client.Client('x', 'y')
        c.login()

    @mock.patch('educabiz.client.requests.Session.request')
    def test_client_login_failed(self, request_mock):
        request_mock.return_value.json.return_value = {'status': 'fail'}
        c = client.Client('x', 'y')
        with self.assertRaises(client.LoginFailedError):
            c.login()

    @mock.patch('educabiz.client.requests.Session.request')
    def test_response_json_decodes_utf8_bom(self, request_mock):
        response = requests.Response()
        response._content = b'\xef\xbb\xbf{"status": "ok"}'
        request_mock.return_value = response

        c = client.Client('x', 'y')
        response = c.get('/test')

        self.assertEqual(response.json(), {'status': 'ok'})

    @mock.patch('educabiz.client.requests.Session.request')
    def test_relogin_response_json_decodes_utf8_bom(self, request_mock):
        login_required_response = requests.Response()
        login_required_response._content = b'{"formAction": "https://mobile.educabiz.com/authenticate"}'
        login_required_response.status_code = 200
        login_response = requests.Response()
        login_response._content = b'{"status": "ok"}'
        login_response.status_code = 200
        retried_response = requests.Response()
        retried_response._content = b'\xef\xbb\xbf{"status": "ok"}'
        retried_response.status_code = 200
        request_mock.side_effect = [login_required_response, login_response, retried_response]

        c = client.Client('x', 'y', login_if_required=True)
        response = c.get('/test')

        self.assertEqual(response.json(), {'status': 'ok'})
