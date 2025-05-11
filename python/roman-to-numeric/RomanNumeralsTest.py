import unittest
from icecream import ic
from RomanNumerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):
    def do_test(self, input, expected):
        func = RomanNumerals.to_roman if type(input) is int else RomanNumerals.from_roman
        actual = func(input)
        self.assertEqual(actual, expected, f'testing {func.__name__}, for input {input}\n')

    def test_fixed_tests_to(self):
        self.do_test(1000, 'M')
        self.do_test(4, 'IV')
        self.do_test(1, 'I')
        self.do_test(2, 'II')
        self.do_test(3, 'III')
        self.do_test(4, 'IV')
        self.do_test(5, 'V')
        self.do_test(6, 'VI')
        self.do_test(7, 'VII')
        self.do_test(8, 'VIII')
        self.do_test(9, 'IX')
        self.do_test(10, 'X')
        self.do_test(11, 'XI')
        self.do_test(11, 'XI')
        self.do_test(20, 'XX')
        self.do_test(66, 'LXVI')
        self.do_test(89, 'LXXXIX')
        self.do_test(152, 'CLII')
        self.do_test(259, 'CCLIX')
        self.do_test(659, 'DCLIX')
        self.do_test(899, 'DCCCXCIX')
        self.do_test(1990, 'MCMXC')
        self.do_test(2008, 'MMVIII')

    def test_fixed_tests_from(self):
        self.do_test('XXI', 21)
        self.do_test('I', 1)
        self.do_test('IV', 4)
        self.do_test('MMVIII', 2008)
        self.do_test('MDCLXVI', 1666)
        self.do_test('MCMXCIV', 1994)

if __name__ == '__main__':
    unittest.main()