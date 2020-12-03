from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScorecard(TestCase):
    def test_create_scorecard(self):
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = create_scorecard()
        self.assertEqual(expected_return, actual_return, "Creating an empty scorecard")
