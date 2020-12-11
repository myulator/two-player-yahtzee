"""
COMP 1510 Final Exam
Michael Yu
A00962260
Date: December 11, 2020
"""
import random
import re
from collections import Counter


def FULL_HOUSE():
    return 25


def SM_STRAIGHT():
    return 30


def LG_STRAIGHT():
    return 40


def YAHTZEE():
    return 50


def YAHTZEE_BONUS():
    return 100


def UPPER_BONUS():
    return 35


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


def roll_dice(current_hand: list):
    """
    Roll dice to create a 5-dice hand.

    Modify the list such that it contains 5 random integers between 1 and 6 inclusively.

    :param current_hand: a potentially empty list representing face values of rolled dice.
    :precondition: current_hand length should be between 0 and 5.
    :postcondition: modifies the list to make a 5-dice hand.

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
    Simulate keeping any number of dice from the player's current hand.

    Player will be prompted to select which values in the list they wish to keep.
    If the input length is 5, the player has indicated they wish to commit a score. Return the list.
    If the input length is less than 5, add the desired dice to a new list. Return the list.

    :param current_hand: a list representing face values of rolled dice.
    :precondition: Hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in the list should appear in ascending order.
    :postcondition: Returns the player's hand after re-rolling/keeping all dice.
    :return: a list of integers
    """
    # This does not need to return the list: can just modify the list. Unittests will need to be edited.
    # Ask player to input the dice they wish to keep e.g "12345" would mean they wish to keep all dice.
    print('----------------------------How to select which dice to keep------------------------------')
    print('E.g. If you would like to keep your entire hand, input 12345')
    print('E.g. If you would like to keep the only the 1st, 3rd, and 5th dice in your hand, input 135')
    print('E.g. If you would like to re-roll your entire hand, press enter.')
    print('------------------------------------------------------------------------------------------')
    kept_dice = input('Please enter which dice in your hand you would like to keep: ')

    if len(kept_dice) == 5:
        return current_hand
    else:
        kept_dice_list = []
        for die in kept_dice:
            kept_dice_list.append(current_hand[int(die) - 1])
        print(f'You chose to keep {kept_dice_list}')
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
    # This does not need to return the dict: can just modify. Unittests will need to be edited.
    # Will probably use a try except here in case player input is invalid
    committed = 0
    # While loop: need a condition to break loop once a valid entry has been made in the scorecard dictionary.
    while committed < 1:
        try:
            score_section = (input('In which section would you like to enter your score?: ')).strip().lower()
            if scorecard[score_section] == -1:
                scorecard[score_section] = point_calculator(current_hand, score_section)
                committed += 1
            elif score_section == 'yahtzee':
                if yahtzee_validator(current_hand):
                    scorecard['yahtzee bonus'] += YAHTZEE_BONUS()
                else:
                    print('Error: You have already recorded a score in the yahtzee section and your current hand does\
                          not contain a yahtzee.')
        except KeyError:
            print('That is not a valid section in the Yahtzee scorecard. Please try again.')
    # Ask player what section they want to score (strip and lowercase the input)
    # Check if that key in the scorecard contains -1 value
    # if it does, pass to point calculator -> commit the points returned from it to the scorecard
    # else if the input is yahtzee, pass to bonus yahtzee validator.
    # if the return value from yahtzee validator is true, add 100 points to the yahtzee bonus value in scorecard
    # if the return value from yahtzee validator is false, error message: you don't have another yahtzee to score.

    # else if the input is not yahtzee, print error message.
    # except key error, print error message: the input is not valid


def yahtzee_validator(current_hand: list) -> bool:
    """
    Validate the current hand for the presence of 5 of a kind (yahtzee).

    :param current_hand: a list representing face values of rolled dice.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
    :postcondition: Determines whether the hand contains 5 of the same number.
    :return: a boolean

    >>> print(yahtzee_validator([1, 1, 1, 1, 1]))
    True
    >>> print(yahtzee_validator([1, 1, 1, 1, 2]))
    False
    """
    # use Counter function from collections module, length of the returned list needs to be 1.
    if len(Counter(current_hand).values()) == 1:
        return True
    else:
        return False


def straights_calculator(current_hand: list, hand: str) -> int:
    """
    Calculate point value that can be scored with current hand.

    :param current_hand: a list representing face values of rolled dice.
    :param hand: a string representing the hand value to be calculated.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in current hand should appear in ascending order.
                    The hand string should contain a valid type of hand in yahtzee.
    :postcondition: Calculates the point value to be recorded in the upper section of a player's scorecard.
    :return: an integer
    """
    str_hand = "".join(map(str, current_hand))
    sm_straight_regex = re.compile(r'1234|2345|3456')
    lg_straight_regex = re.compile(r'12345|23456')
    if hand == 'small straight':
        if sm_straight_regex.search(str_hand):
            return SM_STRAIGHT()
        else:
            return 0
    elif hand == 'large straight':
        if lg_straight_regex.search(str_hand):
            return LG_STRAIGHT()
        else:
            return 0


def point_calculator(current_hand: list, hand: str) -> int:
    """
    Calculate point value that can be scored with current hand.

    :param current_hand: a list representing face values of rolled dice.
    :param hand: a string representing the hand value to be calculated.
    :precondition: Current hand must contain 5 integers between 1 and 6 inclusively.
                    Numbers in current hand should appear in ascending order.
                    The hand string should contain a valid type of hand in yahtzee.
    :postcondition: Calculates the point value to be recorded in current player's scorecard.
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
    upper_section = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes']
    if hand in upper_section:
        return current_hand.count(upper_section.index(hand) + 1) * (upper_section.index(hand) + 1)
    if hand == 'full house' and len(Counter(current_hand).values()) == 2:
        return FULL_HOUSE()
    if hand == '3 of a kind' and 3 in Counter(current_hand).values():
        return sum(current_hand)
    if hand == '4 of a kind' and 4 in Counter(current_hand).values():
        return sum(current_hand)
    if hand == 'yahtzee' and yahtzee_validator(current_hand):
        return YAHTZEE()
    if hand == 'chance':
        return sum(current_hand)
    if hand in ['small straight', 'large straight']:
        return straights_calculator(current_hand, hand)
    else:
        return 0

    # if the hand string is 'full house', call the complex hand (full house, 4kind, 3kind) calculator (use regex?).
    # if hand string is yahtzee, validate yahtzee with function.
    # if hand string is chance, add all numbers in the list.
    # if hand string is sm straight, either pass to a straight calculator for just compare hand to preset lists.
    # e.g. sm straights can only be 1234, 2345, 3456.
    # e.g. lg straights can only be 12345, 23456.


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
    total = 0
    for key, value in scorecard.items():
        total += value

    upper_bonus = 0
    for upper_score in ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes']:
        upper_bonus += scorecard[upper_score]

    if upper_bonus > 62:
        total += UPPER_BONUS()

    return total


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
    print(f'Player 1 scored: {score1} points')
    print(f'Player 2 scored: {score2} points')

    if score1 > score2:
        print('Player 1 wins!')
    elif score1 < score2:
        print('Player 2 wins!')
    else:
        print('Tie game!')


def game(scorecard: dict):
    """
    Drives the entire turn for the current player
    """
    rolls_left = 3
    hand = []
    while rolls_left > 1:
        input('\nPress enter to roll dice...')
        roll_dice(hand)
        rolls_left -= 1
        print(f'\nYour current hand is {hand}\n')
        hand = re_roll(hand)
        if len(hand) == 5:
            commit_score(hand, scorecard)
            return
        print(f'You have {rolls_left} roll(s) remaining this turn.')
    input('\nPress enter to roll dice...')
    roll_dice(hand)
    print(f'Your current hand is {hand}\n')
    commit_score(hand, scorecard)


def main():
    """
    Drives the program.
    """
    print('Welcome to two player Yahtzee!\n------------------------------')
    p1_scorecard = create_scorecard()
    p2_scorecard = create_scorecard()

    # while loop: main program keeps game going as long as there is at least one -1 value in either player's scorecard.
    turn_counter = 1
    while -1 in p1_scorecard.values() or -1 in p2_scorecard.values():
        # these conditions keep track of who's turn it is, and if a player finishes early, they stop taking turns.
        if turn_counter % 2 == 0:
            print('It is player 2\'s turn.')
            game(p2_scorecard)
            print(f'Player 2\'s current scores are: \n{p2_scorecard}\n------------------------------')
            turn_counter += 1
        elif turn_counter % 2 != 0:
            print('It is player 1\'s turn.')
            game(p1_scorecard)
            print(f'Player 1\'s current scores are: \n{p1_scorecard}\n------------------------------')
            turn_counter += 1

    # if turn counter does not evenly divide by 2 AND there is a -1 in the scorecard, it is p1's turn
    # if turn counter evenly divides by 2 AND there is a -1 in the scorecard, it is p2's turn
    # end of turn, increment turn counter by 1

    p1_total = calculate_final_score(p1_scorecard)
    p2_total = calculate_final_score(p2_scorecard)
    announce_winner(p1_total, p2_total)
    print('Thank you for playing!')


if __name__ == "__main__":
    main()
