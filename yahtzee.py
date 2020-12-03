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
    """
    pass


def roll_dice(number_of_rolls: int) -> tuple:
    """
    Simulate rolling a die 5 times.

    Return a tuple of random integers between 1 and 6 inclusively.


    :param number_of_rolls: an integer that specifies the number of integers to be added to the tuple.
    :return: a tuple of integers
    """
    pass


def validate_upper(current_hand: tuple) -> list:
    """
    Return a list of all valid upper section hands that can be formed from the player's current hand.

    Examine current 5-dice hand for the presence of numbers 1-6.

    :param current_hand: a tuple representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the tuple should appear in ascending order.
    :postcondition: Determines if the hand contains any hands that can be scored in the upper section of Yahtzee.
    :return: a list of strings
    """
    pass


def validate_lower(current_hand: tuple) -> list:
    """
    Return a list of all valid lower section hands that can be formed from the player's current hand.

    Examine current 5-dice hand for presence of three of a kind, four of a kind, full house, small straight,
    large straight, five of a kind (YAHTZEE), and chance.

    :param current_hand: a tuple representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the tuple should appear in ascending order.
    :postcondition: Determines if the hand contains any hands that can be scored in the lower section of Yahtzee.
    :return: a list of strings
    """
    pass


def re_roll(current_hand: tuple) -> tuple:
    """
    Simulate rolling X number of dice depending on player input.

    Player will be prompted to select which values in the tuple they wish to keep. These values will be added to a list.
    If the list length is 5, the player has indicated they wish to commit a score. Return "commit".
    If the list length is less than 5, roll dice and append each new face value to the list such that the length is 5.

    :param current_hand: a tuple representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the tuple should appear in ascending order.
    :postcondition: Determines if the hand contains any hands that can be scored in the lower section of Yahtzee.
    :return: either a string or a tuple of integers
    """
    pass


def commit_score(current_hand: tuple, valid_hands: list, scorecard: dict):
    """
    Prompt player to commit their current hand as a value on their Yahtzee scorecard.

    Prompt player to input the type of hand they would like to score. E.g. 'aces'
    If the input is in valid_hands, calculate the point value of that hand and log it on the scorecard.

    :param current_hand: a tuple representing face values of rolled dice.
    :param valid_hands: a list of strings representing valid hands which can be formed from the current player's hand.
    :param scorecard: a dictionary representing current player's scorecard.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in current hand should appear in ascending order.
                    Valid hands list should not be empty.
                    Scorecard should contain at least one value that is None.
    :postcondition: Calculates and appends point value into current player's scorecard.
    """
    pass


def main():
    """
    Drives the program.
    """
    pass


if __name__ == "__main__":
    main()
