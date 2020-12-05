from unittest import TestCase
from yahtzee import calculate_winner
import io
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_winner_p1(self, mock_print):
        argument1 = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30,
                     '3 of a kind': 30, '4 of a kind': 30, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 50, 'chance': 24, 'yahtzee bonus': 0}
        argument2 = {'aces': 2, 'twos': 6, 'threes': 9, 'fours': 8, 'fives': 15, 'sixes': 30,
                     '3 of a kind': 30, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 10, 'yahtzee bonus': 0}
        calculate_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 279 points\nPlayer 2 scored: 261 points\nPlayer 1 wins!'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player 1 wins.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_winner_p2(self, mock_print):
        argument1 = {'aces': 2, 'twos': 6, 'threes': 9, 'fours': 8, 'fives': 15, 'sixes': 30,
                     '3 of a kind': 30, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 10, 'yahtzee bonus': 0}
        argument2 = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30,
                     '3 of a kind': 30, '4 of a kind': 30, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 50, 'chance': 24, 'yahtzee bonus': 200}
        calculate_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 261 points\nPlayer 2 scored: 479 points\nPlayer 2 wins!'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player 2 wins with 3 yahtzees!.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_winner_p2_wins_with_upper_bonus(self, mock_print):
        argument1 = {'aces': 2, 'twos': 4, 'threes': 9, 'fours': 8, 'fives': 15, 'sixes': 18,
                     '3 of a kind': 14, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 10, 'yahtzee bonus': 0}
        argument2 = {'aces': 5, 'twos': 6, 'threes': 1, 'fours': 20, 'fives': 10, 'sixes': 30,
                     '3 of a kind': 14, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 12, 'yahtzee bonus': 0}
        calculate_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 196 points\nPlayer 2 scored: 249 points\nPlayer 2 wins!'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player 2 wins, P1 did not reach the upper bonus.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_winner_tie(self, mock_print):
        argument1 = {'aces': 2, 'twos': 4, 'threes': 9, 'fours': 8, 'fives': 15, 'sixes': 18,
                     '3 of a kind': 14, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 10, 'yahtzee bonus': 0}
        argument2 = {'aces': 2, 'twos': 4, 'threes': 9, 'fours': 8, 'fives': 15, 'sixes': 18,
                     '3 of a kind': 14, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 10, 'yahtzee bonus': 0}
        calculate_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 196 points\nPlayer 2 scored: 196 points\nTie game!'
        self.assertEqual(expected_print, mock_print.getvalue(), "Incredible, both players have the same score.")
