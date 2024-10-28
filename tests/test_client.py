import unittest

from educabiz.client import Client


class Test(unittest.TestCase):
    def test_client(self):
        c = Client('x', 'y')
        c.login()
