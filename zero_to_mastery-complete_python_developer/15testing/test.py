import unittest
import main


class TestMain(unittest.TestCase):
    def test_number_in_range(self):
        self.assertEqual(main.numberInRange(1, 10, 5), True)
        self.assertEqual(main.numberInRange(1, 10, 11), False)
        self.assertEqual(main.numberInRange(1, 10, 0), False)

    def test_exact_number(self):
        main.guess = 5
        self.assertEqual(main.exactNumber(5), True)
        self.assertEqual(main.exactNumber(4), False)
        self.assertEqual(main.exactNumber(6), False)
