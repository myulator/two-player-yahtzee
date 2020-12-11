from unittest import TestCase
from yahtzee import bonus_yahtzee_validator


class TestBonusYahtzeeValidator(TestCase):
    def test_bonus_yahtzee_validator_valid(self):
        expected_return = True
        actual_return = bonus_yahtzee_validator([1, 1, 1, 1, 1])
        self.assertEqual(expected_return, actual_return, "Hand contains 5 of a kind.")

    def test_bonus_yahtzee_validator_4kind(self):
        expected_return = False
        actual_return = bonus_yahtzee_validator([6, 6, 6, 6, 5])
        self.assertEqual(expected_return, actual_return, "Hand contains 4 of a kind.")

    def test_bonus_yahtzee_validator_fh(self):
        expected_return = False
        actual_return = bonus_yahtzee_validator([5, 5, 6, 6, 6])
        self.assertEqual(expected_return, actual_return, "Hand contains full house.")
