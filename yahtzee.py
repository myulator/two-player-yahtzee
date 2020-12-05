"""
COMP 1510 A3
Michael Yu
A00962260
Date: December 4, 2020
"""


def roll_initiative():
    """
    Simulate rolling a die for both players to determine who goes first.

    Both players will press enter to roll a die, and their numbers will be printed to the screen.
    If both players roll the same number, re-roll. Otherwise, the player with the higher roll goes first.

    :return: an integer
    """
    pass


def create_scorecard():
    """
    Create a dictionary data structure to track a player's score.

    Each hand in Yahtzee will be a key in the dictionary, and the default value for each key will be None.
    Logic: As long as there is a None value in either player's scorecard dictionary, the game will continue.

    :return: a dictionary

    >>> create_scorecard()
    {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, '3 of a kind': None,
'4 of a kind': None, 'full house': None, 'small straight': None, 'large straight': None, 'yahtzee': None,
'chance': None, 'yahtzee bonus': 0}
    """
    pass


def roll_dice(current_hand: list) -> list:
    """
    Roll dice to create a 5-dice hand.

    Return a list of 5 random integers between 1 and 6 inclusively.

    :param current_hand: a potentially empty list representing face values of rolled dice.
    :return: a list of integers in ascending order

    >>> roll_dice([])
    [1, 2, 3, 5, 6]
    >>> roll_dice([1, 3, 5])
    [1, 3, 5, 6, 6]
    >>> roll_dice([1, 1, 1, 1, 2])
    [1, 1, 1, 1, 2]
    """
    pass


def re_roll(current_hand: list) -> list:
    """
    Simulate rolling X number of dice depending on player input.

    Player will be prompted to select which values in the list they wish to keep. These values will be added to a list.
    If the list length is 5, the player has indicated they wish to commit a score. Return "commit".
    If the list length is less than 5, return the list.

    :param current_hand: a list representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the list should appear in ascending order.
    :postcondition: Direct player to commit their score or returns their new hand after re-rolling dice.
    :return: either a string or a list of integers
    """
    pass


def commit_score(current_hand: list, scorecard: dict):
    """
    Prompt player to commit their current hand as a value on their Yahtzee scorecard.

    Prompt player to input the type of hand they would like to score. E.g. 'aces'
    If the inputted hand already has points assigned in the scorecard, display an error message and re-prompt player.
    Otherwise, call the point calculator and append the returned value into the scorecard.

    :param current_hand: a list representing face values of rolled dice.
    :param scorecard: a dictionary representing current player's scorecard.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in current hand should appear in ascending order.
                    Scorecard should contain at least one value that is None.
    :postcondition: Calculates and appends point value into current player's scorecard.
    :return: scorecard dictionary with updated point values.
    """
    pass


def point_calculator(current_hand: list, hand: str) -> int:
    """
    Calculate point value that can be scored with current hand.

    :param current_hand: a list representing face values of rolled dice.
    :param hand: a string representing the hand value to be calculated.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in current hand should appear in ascending order.
                    The hand string should contain a valid type of hand in yahtzee.
    :postcondition: Calculates and appends point value into current player's scorecard.
    :return: an integer

    >>> point_calculator([1, 1, 1, 2, 2], 'aces')
    3
    >>> point_calculator([1, 1, 1, 2, 2], 'twos')
    4
    >>> point_calculator([1, 1, 1, 2, 2], 'full house')
    25
    >>> point_calculator([5, 5, 5, 5, 6], '4 of a kind')
    26
    >>> point_calculator([5, 5, 5, 5, 6], '3 of a kind')
    26
    >>> point_calculator([1, 1, 1, 1, 1], 'yahtzee')
    50
    >>> point_calculator([1, 2, 3, 4, 5], 'yahtzee')
    0
    """
    pass


def calculate_winner(scorecard1: dict, scorecard2: dict):
    """
    Calculate the final score of both players and declare the winner.

    :param scorecard1: a dictionary representing player 1's scorecard.
    :param scorecard2: a dictionary representing player 2's scorecard.
    :precondition: both dictionaries must contain only integer values assigned to string keys.
    :postcondition: correctly calculates total scores including any bonuses.

    >>> p1_scorecard = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
    '4 of a kind': 30, 'full house': 25, 'small straight': 30,'large straight': 40, 'yahtzee': 50, 'chance': 24,
    'yahtzee bonus': 0}
    >>> p2_scorecard = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
    '4 of a kind': 30, 'full house': 25, 'small straight': 30,'large straight': 40, 'yahtzee': 50, 'chance': 24,
    'yahtzee bonus': 0}
    >>> calculate_winner(p1_scorecard, p2_scorecard)
    Player 1 scored: 279 points
    Player 2 scored: 261 points
    Player 1 wins!
    """
    pass


def main():
    """
    Drives the program.
    """
    pass


if __name__ == "__main__":
    main()
