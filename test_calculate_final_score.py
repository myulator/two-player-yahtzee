from unittest import TestCase
from yahtzee import calculate_final_score


class Test(TestCase):
    def test_calculate_final_score_p1(self):
        argument1 = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
                     '4 of a kind': 30, 'full house': 25, 'small straight': 30, 'large straight': 40, 'yahtzee': 50,
                     'chance': 24, 'yahtzee bonus': 0}
        actual_return = calculate_final_score(argument1)
        expected_return = 369
        self.assertEqual(expected_return, actual_return, "Player scores 369 points.")

    def test_calculate_final_score_p2(self):
        argument2 = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30,
                     '3 of a kind': 30, '4 of a kind': 30, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 50, 'chance': 24, 'yahtzee bonus': 200}
        actual_return = calculate_final_score(argument2)
        expected_return = 569
        self.assertEqual(expected_return, actual_return, "Player scores 479 points with 3 yahtzees.")

    def test_calculate_final_score_p2_with_upper_bonus(self):
        argument2 = {'aces': 5, 'twos': 6, 'threes': 1, 'fours': 20, 'fives': 10, 'sixes': 30,
                     '3 of a kind': 14, '4 of a kind': 21, 'full house': 25, 'small straight': 30,
                     'large straight': 40, 'yahtzee': 0, 'chance': 12, 'yahtzee bonus': 0}
        actual_return = calculate_final_score(argument2)
        expected_return = 249
        self.assertEqual(expected_return, actual_return, "Player achieves upper section bonus.")
