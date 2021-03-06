from unittest import TestCase
from yahtzee import commit_score
from unittest.mock import patch


class TestCommitScore(TestCase):
    @patch('builtins.input', return_value='aces')
    def test_commit_score_ones(self, mock_input):
        argument1 = [1, 1, 1, 1, 1]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        expected_outcome = {'aces': 5, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        self.assertEqual(expected_outcome, argument2, "Player wishes to score aces.")

    @patch('builtins.input', return_value='twos')
    def test_commit_score_twos(self, mock_input):
        argument1 = [1, 1, 2, 2, 2]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        expected_outcome = {'aces': -1, 'twos': 6, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        self.assertEqual(expected_outcome, argument2, "Player wishes to score twos.")

    @patch('builtins.input', return_value='threes')
    def test_commit_score_threes(self, mock_input):
        argument1 = [2, 3, 3, 3, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': 9, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}

        self.assertEqual(expected_outcome, argument2, "Player wishes to score threes.")

    @patch('builtins.input', return_value='fours')
    def test_commit_score_fours(self, mock_input):
        argument1 = [4, 4, 4, 4, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': 16, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score fours.")

    @patch('builtins.input', return_value='fives')
    def test_commit_score_fives(self, mock_input):
        argument1 = [5, 5, 6, 6, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': 10, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score fives.")

    @patch('builtins.input', return_value='sixes')
    def test_commit_score_sixes(self, mock_input):
        argument1 = [5, 6, 6, 6, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': 24,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score fives.")

    @patch('builtins.input', return_value='3 of a kind')
    def test_commit_score_3_of_a_kind(self, mock_input):
        argument1 = [6, 6, 6, 6, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': 30, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score three of a kind.")

    @patch('builtins.input', return_value='4 of a kind')
    def test_commit_score_4_of_a_kind(self, mock_input):
        argument1 = [5, 5, 5, 5, 5]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': 25, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score four of a kind.")

    @patch('builtins.input', return_value='full house')
    def test_commit_score_full_house(self, mock_input):
        argument1 = [2, 2, 4, 4, 4]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': 25, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score full house.")

    @patch('builtins.input', return_value='small straight')
    def test_commit_score_sm_straight(self, mock_input):
        argument1 = [1, 3, 4, 5, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': 30,
                            'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score small straight.")

    @patch('builtins.input', return_value='large straight')
    def test_commit_score_lg_straight(self, mock_input):
        argument1 = [2, 3, 4, 5, 6]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': 40, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score large straight.")

    @patch('builtins.input', return_value='yahtzee')
    def test_commit_score_yahtzee(self, mock_input):
        argument1 = [3, 3, 3, 3, 3]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': 50, 'chance': -1, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score their first yahtzee.")

    @patch('builtins.input', return_value='yahtzee')
    def test_commit_score_2nd_yahtzee(self, mock_input):
        argument1 = [4, 4, 4, 4, 4]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': 50, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': 50, 'chance': -1, 'yahtzee bonus': 100}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to score their 2nd yahtzee.")

    @patch('builtins.input', return_value='chance')
    def test_commit_score_chance(self, mock_input):
        argument1 = [1, 1, 3, 4, 5]
        argument2 = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                     '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                     'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
        expected_outcome = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                            '3 of a kind': -1, '4 of a kind': -1, 'full house': -1, 'small straight': -1,
                            'large straight': -1, 'yahtzee': -1, 'chance': 14, 'yahtzee bonus': 0}
        commit_score(argument1, argument2)
        self.assertEqual(expected_outcome, argument2, "Player wishes to use their chance.")
