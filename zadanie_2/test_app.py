import unittest
from app import is_valid_email, calculate_area, filter_even_numbers, format_date, is_palindrome

class TestFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test@com"))
        self.assertFalse(is_valid_email("test.com"))

    def test_calculate_area(self):
        self.assertEqual(calculate_area("square", 4), 16)
        self.assertEqual(calculate_area("rectangle", 4, 5), 20)
        self.assertEqual(calculate_area("circle", 3), 28.27331)
        with self.assertRaises(ValueError):
            calculate_area("triangle", 3, 4)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([7, 9, 11]), [])
        self.assertEqual(filter_even_numbers([0, 8, 10]), [0, 8, 10])

    def test_format_date(self):
        self.assertEqual(format_date("2024-03-17"), "17/03/2024")
        self.assertEqual(format_date("2024/03/17", "%Y/%m/%d", "%d-%m-%Y"), "17-03-2024")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("Ala ma kota, a kot ma Alę"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()
