import unittest


class Test(unittest.TestCase):
    def test_presence(self):
        from educabiz.models.school_qrcodeinfo import PresenceItem

        p = PresenceItem.model_validate({'id': '123123', 'notes': 'nice', 'random': 'z', 'hourIn': '--:--'})
        self.assertEqual(p.id, '123123')
        self.assertEqual(p.notes, 'nice')
        self.assertEqual(p.hourOut, '')
        self.assertEqual(p.hourIn, '')
        self.assertEqual(p.model_extra['random'], 'z')

    def test_child_name(self):
        from educabiz.models.school_qrcodeinfo import Child

        c = Child.model_validate({'id': '1', 'presence': [], 'name': 'S&atilde;o T&oacute;'})
        self.assertEqual(c.name, 'São Tó')
