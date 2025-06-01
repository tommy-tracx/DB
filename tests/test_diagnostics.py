import unittest
from autoshop.diagnostics import interpret_codes
from autoshop.config import AppConfig


class TestDiagnostics(unittest.TestCase):
    def setUp(self):
        self.config = AppConfig(dtc_path='data/dtc_codes.json')

    def test_known_code(self):
        result = interpret_codes(['P0001'], self.config)
        self.assertEqual(result[0]['description'], 'Fuel Volume Regulator Control Circuit/Open')

    def test_unknown_code(self):
        result = interpret_codes(['XYZ'], self.config)
        self.assertEqual(result[0]['description'], 'Unknown code')


if __name__ == '__main__':
    unittest.main()
