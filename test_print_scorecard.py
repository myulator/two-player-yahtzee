from unittest import TestCase
from yahtzee import print_scorecard
import io
from unittest.mock import patch


class TestPrintScorecard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scorecard(self, mock_print):
        argument = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
                    '4 of a kind': 30, 'full house': 25, 'small straight': 30, 'large straight': 40, 'yahtzee': 50,
                    'chance': 24, 'yahtzee bonus': 0}
        print_scorecard(argument)
        expected_print = 'aces: 5\ntwos: 10\nthrees: 15\nfours: 20\nfives: 25\nsixes: 30\n3 of a kind: 30\n' \
                         '4 of a kind: 30\nfull house: 25\nsmall straight: 30\nlarge straight: 40\nyahtzee: 50\n' \
                         'chance: 24\nyahtzee bonus: 0\n------------------------------\n'
        self.assertEqual(expected_print, mock_print.getvalue(), "Player's scorecard has been filled.")
