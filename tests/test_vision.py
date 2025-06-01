import unittest
from autoshop.vision import analyze_image


class TestVision(unittest.TestCase):
    def test_empty_image(self):
        with self.assertRaises(ValueError):
            analyze_image(b'')

    def test_dummy_image(self):
        data = analyze_image(b'abc')
        self.assertIn('damage_detected', data)
        self.assertFalse(any(data.values()))


if __name__ == '__main__':
    unittest.main()
