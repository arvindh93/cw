import unittest
from isbn10validation import valid_ISBN10_opt as valid_ISBN10

class TestValidISBN(unittest.TestCase):
    def tests(self):
        self.assertEqual(valid_ISBN10('1112223339'), True)
        self.assertEqual(valid_ISBN10('048665088X'), True)
        self.assertEqual(valid_ISBN10('1293000000'), True)
        self.assertEqual(valid_ISBN10('1234554321'), True)
        self.assertEqual(valid_ISBN10('1234512345'), False)
        self.assertEqual(valid_ISBN10('1293'), False)
        self.assertEqual(valid_ISBN10('X123456788'), False)
        self.assertEqual(valid_ISBN10('ABCDEFGHIJ'), False)
        self.assertEqual(valid_ISBN10('XXXXXXXXXX'), False)
        self.assertEqual(valid_ISBN10('123456789T'), False)


if __name__ == '__main__':
    unittest.main()