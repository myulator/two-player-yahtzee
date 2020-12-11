from unittest import TestCase
from yahtzee import re_roll
from unittest.mock import patch


class TestReRoll(TestCase):
    @patch('builtins.input', side_effect=['12345'])
    def test_re_roll_keep_all(self, mock_input):
        actual_return = re_roll([6, 6, 6, 6, 6])
        expected_return = [6, 6, 6, 6, 6]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep their whole hand.")

    @patch('builtins.input', side_effect=['1'])
    def test_re_roll_keep_die_1(self, mock_input):
        actual_return = re_roll([6, 6, 6, 6, 6])
        expected_return = [6]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the first die in their hand.")

    @patch('builtins.input', side_effect=['12'])
    def test_re_roll_keep_die_1_and_2(self, mock_input):
        actual_return = re_roll([4, 5, 6, 6, 6])
        expected_return = [4, 5]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the first 2 dice in their hand.")

    @patch('builtins.input', side_effect=['5'])
    def test_re_roll_keep_die_last(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [6]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the last die in their hand.")

    @patch('builtins.input', side_effect=['45'])
    def test_re_roll_keep_die_last_2(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [4, 6]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the last two dice in their hand.")

    @patch('builtins.input', side_effect=['345'])
    def test_re_roll_keep_die_last_3(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [4, 4, 6]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the last three dice in their hand.")

    @patch('builtins.input', side_effect=['123'])
    def test_re_roll_keep_die_first_3(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [1, 3, 4]
        self.assertEqual(expected_return, actual_return, "Player wishes to keep the first three dice in their hand.")

    @patch('builtins.input', side_effect=['1234'])
    def test_re_roll_keep_die_first_4(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [1, 3, 4, 4]
        self.assertEqual(expected_return, actual_return, "Player wishes to discard the last die in their hand.")

    @patch('builtins.input', side_effect=['2345'])
    def test_re_roll_keep_die_last_4(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = [3, 4, 4, 6]
        self.assertEqual(expected_return, actual_return, "Player wishes to discard the first die in their hand.")

    @patch('builtins.input', side_effect=[''])
    def test_re_roll_all(self, mock_input):
        actual_return = re_roll([1, 3, 4, 4, 6])
        expected_return = []
        self.assertEqual(expected_return, actual_return, "Player wishes to re-roll their entire hand.")
