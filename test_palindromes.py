import palindromes

import unittest

class TestPalindrome(unittest.TestCase):
    
    def test_even_string_palindrome_true(self):
        self.assertTrue(palindromes.is_palindrome('barrab'))

    def test_even_string_palindrome_false(self):
        self.assertFalse(palindromes.is_palindrome('foobar'))

    def test_odd_string_palindrome_true(self):
        self.assertTrue(palindromes.is_palindrome('barab'))

    def test_odd_string_palindrome_false(self):
        self.assertFalse(palindromes.is_palindrome('fobar'))

    def test_even_list_palindrome_true(self):
        self.assertTrue(palindromes.is_palindrome([1,2,3,3,2,1]))

    def test_even_list_palindrome_false(self):
        self.assertFalse(palindromes.is_palindrome([1,2,3,4,5,6]))

    def test_odd_list_palindrome_true(self):
        self.assertTrue(palindromes.is_palindrome([1,2,3,2,1]))

    def test_odd_list_palindrome_false(self):
        self.assertFalse(palindromes.is_palindrome([1,2,3,4,5]))

    def test_empty_list_palindrome(self):
        self.assertTrue(palindromes.is_palindrome([]))

    def test_empty_string_palindrome(self):
        self.assertTrue(palindromes.is_palindrome(''))

    def test_list_of_one_palindrome(self):
        self.assertTrue(palindromes.is_palindrome([1]))

    def test_string_of_one_palindrome(self):
        self.assertTrue(palindromes.is_palindrome('f'))


    def test_change_base(self):
        self.assertEqual(palindromes.change_base(44,3), [1, 1, 2, 2])
        self.assertEqual(palindromes.change_base(885,19), [2, 8, 11])
        self.assertEqual(palindromes.change_base(19,2), [1, 0, 0, 1, 1])


    def test_find_lowest_palindrome_base(self):
        # The following cases are given in challenge description
        self.assertEqual(palindromes.find_lowest_palindrome_base(1), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(2), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(3), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(4), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(5), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(6), 5)
        self.assertEqual(palindromes.find_lowest_palindrome_base(7), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(8), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(9), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(10), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(11), 10)
        self.assertEqual(palindromes.find_lowest_palindrome_base(12), 5)
        self.assertEqual(palindromes.find_lowest_palindrome_base(13), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(14), 6)
        self.assertEqual(palindromes.find_lowest_palindrome_base(15), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(16), 3)
        self.assertEqual(palindromes.find_lowest_palindrome_base(17), 2)
        self.assertEqual(palindromes.find_lowest_palindrome_base(18), 5)
        self.assertEqual(palindromes.find_lowest_palindrome_base(19), 18)
        self.assertEqual(palindromes.find_lowest_palindrome_base(20), 3)
