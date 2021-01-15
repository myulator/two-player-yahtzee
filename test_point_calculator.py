from unittest import TestCase
from yahtzee import point_calculator


class TestPointCalculator(TestCase):
    def test_point_calculator_aces(self):
        actual_return = point_calculator([1, 1, 1, 2, 2], 'aces')
        expected_return = 3
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in aces.")

    def test_point_calculator_twos(self):
        actual_return = point_calculator([1, 1, 1, 2, 2], 'twos')
        expected_return = 4
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in twos.")

    def test_point_calculator_threes(self):
        actual_return = point_calculator([1, 3, 3, 3, 3], 'threes')
        expected_return = 12
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in threes.")

    def test_point_calculator_fours(self):
        actual_return = point_calculator([3, 4, 4, 4, 4], 'fours')
        expected_return = 16
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in fours.")

    def test_point_calculator_fives(self):
        actual_return = point_calculator([4, 5, 5, 6, 6], 'fives')
        expected_return = 10
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in fives.")

    def test_point_calculator_sixes(self):
        actual_return = point_calculator([1, 1, 1, 6, 6], 'sixes')
        expected_return = 12
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in sixes.")

    def test_point_calculator_3kind(self):
        actual_return = point_calculator([1, 1, 6, 6, 6], '3 of a kind')
        expected_return = 20
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in 3 of a kind.")

    def test_point_calculator_no_3kind(self):
        actual_return = point_calculator([1, 1, 5, 6, 6], '3 of a kind')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "No 3 of a kind in current hand.")

    def test_point_calculator_4kind(self):
        actual_return = point_calculator([1, 3, 3, 3, 3], '4 of a kind')
        expected_return = 13
        self.assertEqual(expected_return, actual_return, "Player wants to write their score in 4 of a kind.")

    def test_point_calculator_no_4kind(self):
        actual_return = point_calculator([1, 3, 3, 3, 5], '4 of a kind')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "No 4 of a kind in current hand.")

    def test_point_calculator_full_house_pair_triple(self):
        actual_return = point_calculator([2, 2, 5, 5, 5], 'full house')
        expected_return = 25
        self.assertEqual(expected_return, actual_return, "Player has a pair and a triple.")

    def test_point_calculator_no_full_house(self):
        actual_return = point_calculator([2, 3, 5, 5, 5], 'full house')
        expected_return = 0
        self.assertEqual(expected_return, actual_return, "No full house in current hand.")

    def test_point_calculator_full_house_triple_pair(self):
        actual_return = point_calculator([4, 4, 4, 5, 5], 'full house')
        expected_return = 25
        self.assertEqual(expected_return, actual_return, "Player has a triple and a pair.")

    def test_point_calculator_sm_straight_low(self):
        actual_return = point_calculator([1, 1, 2, 3, 4], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a low sm straight.")

    def test_point_calculator_sm_straight_mid(self):
        actual_return = point_calculator([2, 3, 3, 4, 5], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a middle sm straight.")

    def test_point_calculator_sm_straight_high(self):
        actual_return = point_calculator([3, 4, 5, 5, 6], 'small straight')
        expected_return = 30
        self.assertEqual(expected_return, actual_return, "Player has a high sm straight.")

    def test_point_calculator_lg_straight_low(self):
        actual_return = point_calculator([1, 2, 3, 4, 5], 'large straight')
        expected_return = 40
        self.assertEqual(expected_return, actual_return, "Player has a low large straight.")

    def test_point_calculator_lg_straight_high(self):
        actual_return = point_calculator([2, 3, 4, 5, 6], 'large straight')
        expected_return = 40
        self.assertEqual(expected_return, actual_return, "Player has a high large straight.")

    def test_point_calculator_yahtzee(self):
        actual_return = point_calculator([4, 4, 4, 4, 4], 'yahtzee')
        expected_return = 50
        self.assertEqual(expected_return, actual_return, "Player has 5 of a kind.")

    def test_point_calculator_chance(self):
        actual_return = point_calculator([1, 3, 4, 4, 6], 'chance')
        expected_return = 18
        self.assertEqual(expected_return, actual_return, "Player uses their chance.")
