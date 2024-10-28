import unittest
from unittest import mock

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
