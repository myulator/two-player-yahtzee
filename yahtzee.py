"""
COMP 1510 Final Exam
Michael Yu
A00962260
Date: December 11, 2020
"""
import random


def create_scorecard():
    """
    Create a dictionary data structure to track a player's score.

    Each hand in Yahtzee will be a key in the dictionary, and the default value for each key will be None.
    Logic: As long as there is a None value in either player's scorecard dictionary, the game will continue.

    :return: a dictionary

    >>> create_scorecard()
    {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1, '3 of a kind': -1, '4 of a kind': -1,
    'full house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1, 'chance': -1, 'yahtzee bonus': 0}
    """
    scorecard = {'aces': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1, '3 of a kind': -1,
                 '4 of a kind': -1, 'full house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1,
                 'chance': -1, 'yahtzee bonus': 0}
    return scorecard


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
    # Note: This does not need to return the list: can just modify the list. Unittests will need to be edited.
    # While the current_hand list length is less than 5:
    # Append a random integer between 1 and 6 to the list
    # Sort the list in ascending order
    while len(current_hand) < 5:
        current_hand.append(random.randint(1, 6))
    current_hand.sort()


def re_roll(current_hand: list) -> list:
    """
    Simulate rolling X number of dice depending on player input.

    Player will be prompted to select which values in the list they wish to keep.
    If the input length is 5, the player has indicated they wish to commit a score. Return the list.
    If the input length is less than 5, add the desired dice to a new list. Return the list.

    :param current_hand: a list representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the list should appear in ascending order.
    :postcondition: Returns the player's hand after re-rolling/keeping all dice.
    :return: a list of integers
    """
    pass
    # This does not need to return the list: can just modify the list. Unittests will need to be edited.
    # Ask player to input the dice they wish to keep e.g "12345" would mean they wish to keep all dice.
    print('------------Selecting which dice to keep------------')
    print('E.g. If you would like to keep your entire hand, input 12345')
    print('E.g. If you would only like to keep the 1st, 3rd, and 5th dice in your hand, input 135')
    print('----------------------------------------------------')
    kept_dice = input('Please enter which dice in your hand you would like to keep.')
    # if the input is 12345, return "commit"
    if len(kept_dice) == 5:
        return current_hand
    else:
        kept_dice_list = []
        for die in range(0, len(kept_dice)):
            kept_dice_list.append(die)
        return kept_dice_list
    # otherwise, for loop over range from 0 to length of the input string
    # each character in the string points to an index in the current_hand list, append those dice to a new list
    # return the new list


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
                    Scorecard should contain at least one value that is -1.
    :postcondition: Calculates and appends point value into current player's scorecard.
    :return: scorecard dictionary with updated point values.
    """
    pass
    # This does not need to return the dict: can just modify. Unittests will need to be edited.
    # Will probably use a try except here in case player input is invalid

    # While loop: need a condition to break loop once a valid entry has been made in the scorecard dictionary.
    # Ask player what section they want to score (strip and lowercase the input)
    # Check if that key in the scorecard contains -1 value
    # if it does, pass to point calculator -> commit the points returned from it to the scorecard
    # else if the input is yahtzee, pass to bonus yahtzee validator.
    # if the return value from yahtzee validator is true, add 100 points to the yahtzee bonus value in scorecard
    # if the return value from yahtzee validator is false, error message: you don't have another yahtzee to score.

    # else if the input is not yahtzee, print error message.
    # except key error, print error message: the input is not valid


def bonus_yahtzee_validator(current_hand: list) -> bool:
    """
    Validate the current hand for the presence of 5 of a kind (yahtzee).

    :param current_hand: a list representing face values of rolled dice.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
    :postcondition: Determines whether the hand contains 5 of the same number.
    :return: a boolean

    >>> print(bonus_yahtzee_validator([1, 1, 1, 1, 1]))
    True
    >>> print(bonus_yahtzee_validator([1, 1, 1, 1, 2]))
    False
    """
    pass
    # could use regex here
    # or use Counter function from collections module, length of the returned list needs to be 1.


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
    # if the hand string is 'aces', count instances of 1 in the list, and multiply by that 1.
    # if the hand string is 'twos', count instances of 2 in the list, and multiply by that 2.
    # do the same for 3s, 4s, 5s, 6s.

    # if the hand string is 'full house', call the complex hand (full house, 4kind, 3kind) calculator (use regex?).
    # if hand string is yahtzee, validate yahtzee with function.
    # if hand string is chance, add all numbers in the list.
    # if hand string is sm straight, either pass to a straight calculator for just compare hand to preset lists.
    # e.g. sm straights can only be 1234, 2345, 3456.
    # e.g. lg straights can only be 12345, 23456.
    pass


def calculate_final_score(scorecard: dict) -> int:
    """
    Calculate the total points scored in a player's scorecard.

    :param scorecard: a dictionary representing a player's scorecard.
    :precondition: scorecard dictionary must contain only positive integer values assigned to string keys.
    :postcondition: correctly calculates total score including any bonuses.
    :return: an integer

    >>> p1_scorecard = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
    '4 of a kind': 30, 'full house': 25, 'small straight': 30,'large straight': 40, 'yahtzee': 50, 'chance': 24,
    'yahtzee bonus': 0}
    >>> p2_scorecard = {'aces': 5, 'twos': 10, 'threes': 15, 'fours': 20, 'fives': 25, 'sixes': 30, '3 of a kind': 30,
    '4 of a kind': 30, 'full house': 25, 'small straight': 30,'large straight': 40, 'yahtzee': 50, 'chance': 24,
    'yahtzee bonus': 0}
    >>> print(calculate_final_score(p1_scorecard))
    279
    >>> print(calculate_final_score(p2_scorecard))
    261
    """
    # for every value in scorecard, add it to a sum and return it.
    pass


def announce_winner(score1: int, score2: int):
    """
    Determine the player with higher points and announce them as the winner.

    :param score1: an integer representing player 1's final score
    :param score2: an integer representing player 2's final score

    >>> announce_winner(279, 261)
    Player 1 scored: 279 points
    Player 2 scored: 261 points
    Player 1 wins!

    >>> announce_winner(279, 300)
    Player 1 scored: 279 points
    Player 2 scored: 300 points
    Player 2 wins!

    >>> announce_winner(300, 300)
    Player 1 scored: 300 points
    Player 2 scored: 300 points
    Tie game!
    """
    # print both players' scores first
    # see which score is greater, and announce winner
    pass


def main():
    """
    Drives the program.
    """
    # NOTE: may need to use a game() function if 20 line limit is exceeded.
    # this game function would take ONE param: the current player's scorecard dictionary.

    # print welcome to yahtzee!

    # create p1 and p2's scorecards.

    # while loop: main program keeps game going as long as there is at least one -1 value in either player's scorecard.
    # set turn counter to 1.
    # if turn counter does not evenly divide by 2 AND there is a -1 in the scorecard, it is p1's turn
    # if turn counter evenly divides by 2 AND there is a -1 in the scorecard, it is p2's turn
    # end of turn, increment turn counter by 1

    # these conditions keep track of who's turn it is, and if one player finishes early,
    # they skip their turns until the game ends

    # when the program exits the main while loop, that means the player's have filled their scorecards
    # calculate final scores, then announce winner.
    pass


if __name__ == "__main__":
    main()
