# Risk Dice Roller - Game

# Intro

Game simulator, based on the board game "Risk".

1. There is an attacker who rolls up to 3 dice and a defender who rolls up to 2. 
2. Then, based on these results, the attacker and defender lose up to 2 units. 
3. They then repeat this process until either side has no units left, or the attacker gives up.

Combat Rules

* There is an attacker and a defender.
* The attacker rolls 3 dice if they have 3 or more units, 2 dice if they have 2 units, and 1 die if they only have 1 unit.
* The defender rolls 2 dice if they have 2 or more units, and 1 die if they only have 1 unit.
* All dice are standard 6-sided dice with an equal chance of rolling any number between 1 and 6, inclusive.
* The attacker can choose to stop the battle at any time.
* Match the highest attacking die to the highest defending die - the side with the lower number loses a unit. The defender always wins ties.
* If both sides rolled a second die, match the second-highest attacking die to the second-highest defending die - the side with the lower number loses a unit. The defender always wins ties.

`Risk_Dice_Roller.py` simulates the dice rolling results and thus, the result of the game.

# Usage 

Input:
* The number of attacking units
* The number of defending units
* The number of units the attacker is willing to lose before they call off the attack (this can be equal to or less than the number of units they are attacking with)

Output:
* Final result of the game
