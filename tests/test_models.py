import unittest


class Test(unittest.TestCase):
    def test_presence(self):
        from educabiz.models.school_qrcodeinfo import PresenceItem

        p = PresenceItem.model_validate({'id': '123123', 'notes': 'nice'})
        self.assertEqual(p.id, '123123')
        self.assertEqual(p.model_extra['notes'], 'nice')

    def test_child_name(self):
        from educabiz.models.school_qrcodeinfo import Child

        c = Child.model_validate({'id': '1', 'presence': [], 'name': 'S&atilde;o T&oacute;'})
        self.assertEqual(c.name, 'São Tó')
