from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScorecard(TestCase):
    def test_create_scorecard(self):
        expected_return = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                           '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                           'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        actual_return = create_scorecard()
        self.assertEqual(expected_return, actual_return, "Creating an empty scorecard")
