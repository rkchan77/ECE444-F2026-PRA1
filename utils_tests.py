import unittest

from utils import utils


class TestReversed(unittest.TestCase):
    def test_reversed_with_integer(self):
        self.assertEqual(utils.reversed(123), 321)

    def test_reversed_with_string(self):
        self.assertEqual(utils.reversed("123"), 321)

    def test_reversed_with_float(self):
        with self.assertRaises(ValueError):
            utils.reversed(123.45)


class TestFormatter(unittest.TestCase):
    def test_formatter_with_integer(self):
        self.assertEqual(utils.formatter(10), (bin(10), oct(10)))

    def test_formatter_with_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("10")

    def test_formatter_with_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(10.5)


if __name__ == "__main__":
    unittest.main()
