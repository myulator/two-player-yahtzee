from unittest import TestCase
from yahtzee import commit_score
from unittest.mock import patch


class TestCommitScore(TestCase):
    @patch('builtins.input', side_effect=['aces'])
    def test_commit_score_ones(self, mock_input):
        argument1 = [1, 1, 1, 1, 1]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': 5, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score aces.")

    @patch('builtins.input', side_effect=['twos'])
    def test_commit_score_twos(self, mock_input):
        argument1 = [1, 1, 2, 2, 2]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': 6, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score twos.")

    @patch('builtins.input', side_effect=['threes'])
    def test_commit_score_threes(self, mock_input):
        argument1 = [2, 3, 3, 3, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': 9, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score threes.")

    @patch('builtins.input', side_effect=['fours'])
    def test_commit_score_fours(self, mock_input):
        argument1 = [4, 4, 4, 4, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': 16, 'fives': None, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score fours.")

    @patch('builtins.input', side_effect=['fives'])
    def test_commit_score_fives(self, mock_input):
        argument1 = [5, 5, 6, 6, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': 10, 'sixes': None,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score fives.")

    @patch('builtins.input', side_effect=['sixes'])
    def test_commit_score_sixes(self, mock_input):
        argument1 = [5, 6, 6, 6, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': 24,
                           '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score fives.")

    @patch('builtins.input', side_effect=['3 of a kind'])
    def test_commit_score_3_of_a_kind(self, mock_input):
        argument1 = [6, 6, 6, 6, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': None, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': None, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score three of a kind.")

    @patch('builtins.input', side_effect=['4 of a kind'])
    def test_commit_score_4_of_a_kind(self, mock_input):
        argument1 = [5, 5, 5, 5, 5]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': None, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': None, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score four of a kind.")

    @patch('builtins.input', side_effect=['full house'])
    def test_commit_score_full_house(self, mock_input):
        argument1 = [2, 2, 4, 4, 4]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': None, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': None,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score full house.")

    @patch('builtins.input', side_effect=['small straight'])
    def test_commit_score_sm_straight(self, mock_input):
        argument1 = [1, 3, 4, 5, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': None,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                           'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score small straight.")

    @patch('builtins.input', side_effect=['large straight'])
    def test_commit_score_lg_straight(self, mock_input):
        argument1 = [2, 3, 4, 5, 6]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                     'large straight': None, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                           'large straight': 40, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score large straight.")

    @patch('builtins.input', side_effect=['yahtzee'])
    def test_commit_score_yahtzee(self, mock_input):
        argument1 = [3, 3, 3, 3, 3]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': None, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                           'large straight': 40, 'yahtzee': 50, 'chance': None, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score their first yahtzee.")

    @patch('builtins.input', side_effect=['yahtzee'])
    def test_commit_score_2nd_yahtzee(self, mock_input):
        argument1 = [4, 4, 4, 4, 4]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 50, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                           'large straight': 40, 'yahtzee': 50, 'chance': None, 'yahtzee bonus': 100}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to score their 2nd yahtzee.")

    @patch('builtins.input', side_effect=['chance'])
    def test_commit_score_chance(self, mock_input):
        argument1 = [1, 1, 3, 4, 5]
        argument2 = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                     '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 50, 'chance': None, 'yahtzee bonus': 0}
        expected_return = {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None,
                           '3 of a kind': 30, '4 of a kind': 25, 'full house': 25, 'small straight': 30,
                           'large straight': 40, 'yahtzee': 50, 'chance': 14, 'yahtzee bonus': 0}
        actual_return = commit_score(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Player wishes to use their chance.")
