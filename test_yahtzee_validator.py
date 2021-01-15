from unittest import TestCase
from yahtzee import yahtzee_validator


class TestYahtzeeValidator(TestCase):
    def test_yahtzee_validator_valid(self):
        expected_return = True
        actual_return = yahtzee_validator([1, 1, 1, 1, 1])
        self.assertEqual(expected_return, actual_return, "Hand contains 5 of a kind.")

    def test_yahtzee_validator_4kind(self):
        expected_return = False
        actual_return = yahtzee_validator([6, 6, 6, 6, 5])
        self.assertEqual(expected_return, actual_return, "Hand contains 4 of a kind.")

    def test_yahtzee_validator_fh(self):
        expected_return = False
        actual_return = yahtzee_validator([5, 5, 6, 6, 6])
        self.assertEqual(expected_return, actual_return, "Hand contains full house.")
