import unittest

import example
import example.demo


class Test(unittest.TestCase):
    # TODO: update with your own unit tests and assertions
    def test_echo(self):
        self.assertEqual(example.demo.echo('hey'), 'HEY right back at ya!')
