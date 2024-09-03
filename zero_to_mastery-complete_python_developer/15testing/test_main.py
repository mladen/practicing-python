import unittest
import main


class TestMain(unittest.TestCase):
    """Testing the guessedNumberInRange function in main.py"""

    def test_number_in_range(self):
        self.assertEqual(main.guessedNumberInRange(5), True)
        self.assertEqual(main.guessedNumberInRange(0), False)

    """Testing the exactNumber function in main.py"""

    def test_entry_is_a_number(self):
        self.assertEqual(main.guessedNumberInRange(5), True)
        self.assertEqual(main.guessedNumberInRange("5"), False)

    """Testing the exactNumber function in main.py"""

    def test_exact_number(self):
        main.guess = 5
        self.assertEqual(main.exactNumber(5, 5), True)
        self.assertEqual(main.exactNumber(6, 5), False)
        self.assertEqual(main.exactNumber(4, 5), False)


if __name__ == "__main__":
    unittest.main()
