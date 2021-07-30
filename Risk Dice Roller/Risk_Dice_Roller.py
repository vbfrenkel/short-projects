import numpy as np

att_un = int(input("Number of attacking units: "))
def_un = int(input("Number of defending units: "))
max_loss = int(input("Number of units the attacker is willing to lose: "))
min_un = att_un-max_loss
while max_loss > att_un:
    print("The number of units to lose must be equal or less than the selected number of attaking units")
    max_loss = int(input("Number of units the attacker is willing to lose: "))


#Define dice number per player
def dices_in_game(att, defe):
    """
    Acording to the units in the game, defines the dices to roll for attacker and defender.

    input
    att_un: attack units that are in the game. int
    def_un: defence units that are in the game. int

    output
    att_dice: attacker dices to play. int
    def_dice: defender dices to play. int

    """
    if att >= 3:
        att_dice = 3
    elif att == 2:
        att_dice = 2
    else:
        att_dice =1


    if defe >= 2:
        def_dice = 2
    else:
        def_dice = 1

    return att_dice, def_dice


#Roll the dices in game
def roll (att_dice, def_dice):

    """
    Roll both dices, and asign them a random value

    input
    att_dice: number of dices of the attacker. int
    def_dice: number of dices of the deffender. int

    output
    list with
    att_dice_numbers: number of each dice after rolling, list(int)
    def_dice_numbers: number of each dice after rolling, list(int)

    """

    att_dice_numbers = []
    for n in range(att_dice):
        att_dice_numbers.append(np.random.randint(1,6))

    def_dice_numbers = []
    for n in range(def_dice):
        def_dice_numbers.append(np.random.randint(1,6))

    return att_dice_numbers, def_dice_numbers

#loop
play = True
while play == True:
    dices = dices_in_game(att_un, def_un)
    dice_rolled = roll (dices[0], dices[1])
    
    # Dice comparision
    dice_rolled[0].sort(reverse=True)
    dice_rolled[1].sort(reverse=True)
    attacker = dice_rolled[0]
    defender = dice_rolled[1]
    pairs = min(len(attacker), len(defender))

    for n in range(pairs):
        if attacker[n] > defender[n]:
            # Attacker wins
            def_un = def_un -1
            if def_un == 0:
                play = False
                winner = "Attacker Wins"
        else:
            # Defender wins
            att_un = att_un -1
            if att_un == 0:
                play = False
                winner = "Defender Wins"
            elif att_un == min_un:
                play = False
                winner = "Defender Wins, Attacker surrender"
                
print ("Attacker: " + str(att_un)+" / Defender: " + str(def_un))
print (winner)