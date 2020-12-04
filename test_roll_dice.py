from unittest import TestCase
from yahtzee import roll_dice
from unittest.mock import patch


class TestRollDice(TestCase):
    @patch('roll', side_effect=[6])
    def test_roll_dice_empty(self):
        actual_return = roll_dice([])
        expected_return = [6, 6, 6, 6, 6]
        self.assertEqual(expected_return, actual_return, "Initial hand is empty.")

    @patch('roll', side_effect=[6])
    def test_roll_dice_one(self):
        actual_return = roll_dice([1])
        expected_return = [1, 6, 6, 6, 6]
        self.assertEqual(expected_return, actual_return, "Initial hand has only 1 die.")

    @patch('roll', side_effect=[6])
    def test_roll_dice_two(self):
        actual_return = roll_dice([1, 2])
        expected_return = [1, 2, 6, 6, 6]
        self.assertEqual(expected_return, actual_return, "Initial hand has only 2 dice.")

    @patch('roll', side_effect=[6])
    def test_roll_dice_three(self):
        actual_return = roll_dice([1, 2, 2])
        expected_return = [1, 2, 2, 6, 6]
        self.assertEqual(expected_return, actual_return, "Initial hand has 3 dice.")

    @patch('roll', side_effect=[6])
    def test_roll_dice_four(self):
        actual_return = roll_dice([1, 4, 5, 5])
        expected_return = [1, 4, 5, 5, 6]
        self.assertEqual(expected_return, actual_return, "Initial hand has 4 dice.")

    @patch('roll', side_effect=[6])
    def test_roll_dice_five(self):
        actual_return = roll_dice([1, 4, 5, 5, 5])
        expected_return = [1, 4, 5, 5, 5]
        self.assertEqual(expected_return, actual_return, "Initial hand already has 5 dice.")
