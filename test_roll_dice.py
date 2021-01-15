from unittest import TestCase
from yahtzee import roll_dice
from unittest.mock import patch


class TestRollDice(TestCase):
    @patch('random.randint', return_value=6)
    def test_roll_dice_empty(self, mock_random):
        actual_hand = []
        roll_dice(actual_hand)
        expected_hand = [6, 6, 6, 6, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand is empty.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_one(self, mock_random):
        actual_hand = [1]
        roll_dice(actual_hand)
        expected_hand = [1, 6, 6, 6, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand has only 1 die.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_two(self, mock_random):
        actual_hand = [1, 2]
        roll_dice(actual_hand)
        expected_hand = [1, 2, 6, 6, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand has only 2 dice.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_three(self, mock_random):
        actual_hand = [1, 2, 2]
        roll_dice(actual_hand)
        expected_hand = [1, 2, 2, 6, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand has 3 dice.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_four(self, mock_random):
        actual_hand = [1, 4, 5, 5]
        roll_dice(actual_hand)
        expected_hand = [1, 4, 5, 5, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand has 4 dice.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_five(self, mock_random):
        actual_hand = [5, 5, 5, 5, 5]
        roll_dice(actual_hand)
        expected_hand = [5, 5, 5, 5, 5]
        self.assertEqual(expected_hand, actual_hand, "Initial hand already has 5 dice.")

    @patch('random.randint', return_value=6)
    def test_roll_dice_sixes(self, mock_random):
        actual_hand = [6, 6, 6]
        roll_dice(actual_hand)
        expected_hand = [6, 6, 6, 6, 6]
        self.assertEqual(expected_hand, actual_hand, "Initial hand already has sixes.")
