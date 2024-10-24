import unittest

from educabiz.client import Client


class Test(unittest.TestCase):
    def test_client(self):
        c = Client()
        self.assertEqual(c, c)
