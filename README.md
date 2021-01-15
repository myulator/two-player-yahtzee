# 2 Player Yahtzee | BCIT CST COMP 1510 (Programming Methods) Final Hackathon		  
Name: Michael Yu    
Date: December 2020   

This program was developed during the 6-hour final hackathon for COMP 1510 at BCIT, supervised by Chris Thompson.

This program simulates a game of Yahtzee in command-line interface for two players.    
Player 1 always goes first.    Play rock, paper, scissors with your opponent to determine who will be player 1. 

# Yahtzee basic rules:
Every turn, a player has up to 3 rolls of a combination of between 1-5 dice.    
Objective is to rack up the best possible score by strategically creating 5-dice hands.    
View a demonstration on how to play Yahtzee here: https://www.youtube.com/watch?v=6kxYPfRoHlY (AwesomeByrd's Youtube Channel)    

# Notes:
After rolling dice, the game automatically sorts the player's hand in ascending order.    
Empty boxes in the scorecard are displayed with a value of -1.    
A winner cannot be decided until both players have recorded a value in every box of the scorecard, excluding the yahtzee bonus.    
Once a player completes their scorecard, the game will continue with the remaining player until their scorecard is completed.     
Players who qualify for the upper section bonus have 35 points automatically applied to their total score at the end of the game.    

# List of functions in this program: 
create_scorecard    
roll_dice    
re_roll    
commit_score    
print_valid_sections  
yahtzee_validator  
straights_calculator  
point_calculator  
calculate_final_score  
announce_winner  
print_scorecard  
game  
main  
