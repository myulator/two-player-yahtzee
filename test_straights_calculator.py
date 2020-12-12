from unittest import TestCase
from yahtzee import straights_calculator


class TestStraightsCalculator(TestCase):
    def test_straights_calculator_small(self):
        actual_return = straights_calculator([3, 4, 5, 5, 6], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a small straight.")

    def test_straights_calculator_small_middle_front(self):
        actual_return = straights_calculator([1, 2, 2, 3, 4], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a small straight with duplicate in the middle.")

    def test_straights_calculator_small_middle_end(self):
        actual_return = straights_calculator([2, 3, 4, 4, 5], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a small straight with duplicate in the middle.")

    def test_straights_calculator_small_middle_alternative(self):
        actual_return = straights_calculator([1, 2, 3, 3, 4], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a small straight with duplicate in the middle.")

    def test_straights_calculator_small_large(self):
        actual_return = straights_calculator([2, 3, 4, 5, 6], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a large straight.")

    def test_straights_calculator_small_none(self):
        actual_return = straights_calculator([1, 1, 2, 2, 2], 'small straight')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "Player has no small straight.")

    def test_straights_calculator_large_small(self):
        actual_return = straights_calculator([1, 2, 3, 3, 4], 'large straight')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "Player has a small straight.")

    def test_straights_calculator_large_low(self):
        actual_return = straights_calculator([2, 3, 4, 5, 6], 'large straight')
        expected_return = 40
        self.assertEqual(expected_return, actual_return, "Player has a low large straight.")

    def test_straights_calculator_large_high(self):
        actual_return = straights_calculator([1, 2, 3, 4, 5], 'large straight')
        expected_return = 40
        self.assertEqual(expected_return, actual_return, "Player has a high large straight.")

    def test_straights_calculator_large_none(self):
        actual_return = straights_calculator([2, 2, 3, 3, 4], 'large straight')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "Player has no large straight.")
