from unittest import TestCase
from yahtzee import announce_winner
import io
from unittest.mock import patch


class TestAnnounceWinner(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_announce_winner_p1(self, mock_print):
        argument1 = 279
        argument2 = 261
        announce_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 279 points\nPlayer 2 scored: 261 points\nPlayer 1 wins!\n'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player 1 wins.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_announce_winner_p2(self, mock_print):
        argument1 = 279
        argument2 = 479
        announce_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 279 points\nPlayer 2 scored: 479 points\nPlayer 2 wins!\n'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player 2 wins.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_announce_winner_tie(self, mock_print):
        argument1 = 300
        argument2 = 300
        announce_winner(argument1, argument2)
        expected_print = 'Player 1 scored: 300 points\nPlayer 2 scored: 300 points\nTie game!\n'
        self.assertEqual(expected_print, mock_print.getvalue(), "Tie game.")

