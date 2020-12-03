from unittest import TestCase
from yahtzee import roll_initiative
from unittest.mock import patch


class TestRollInitiative(TestCase):
    @patch('roll1', side_effect=[1])
    @patch('roll2', side_effect=[6])
    def test_roll_initiative_p2(self, mock_roll2, mock_roll1):
        actual_return = roll_initiative()
        expected_return = 2
        self.assertEqual(expected_return, actual_return, "Player 2 rolls higher than Player 1.")

    @patch('roll1', side_effect=[4])
    @patch('roll2', side_effect=[2])
    def test_roll_initiative_p1(self, mock_roll2, mock_roll1):
        actual_return = roll_initiative()
        expected_return = 1
        self.assertEqual(expected_return, actual_return, "Player 1 rolls higher than Player 2.")
