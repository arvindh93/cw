from Brackets import validate
import unittest

class TestBracketsValidation(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(validate('()'), True, "valid brackets")
        self.assertEqual(validate('(]'), False, "valid brackets")
        self.assertEqual(validate('([])'), True, "valid brackets")
        self.assertEqual(validate('([)]'), False, "valid brackets")
if __name__ == '__main__':
    unittest.main()