import random
import gv_die



#Function to roll the dice and return dice total (STEP 1)
def roll_dice(first_die, second_die, credits, goal, round): 
    first_die.roll()
    second_die.roll()
    goal_set = False
    dice_total = first_die.get_value() + second_die.get_value()

    if dice_total == 7 or dice_total == 11:
        credits += 1
    elif dice_total == 2 or dice_total == 3 or dice_total ==12:
        credits -= 1
    else:
        credits = credits
        goal = dice_total
        goal_set = True
    
    round += 1
    
    return credits, dice_total, goal, goal_set, round

#STEP 2
def keep_rolling(first_die, second_die, credits, goal):

    round_in_session = True

    while round_in_session == True:
        first_die.roll()
        second_die.roll()
        dice_total = first_die.get_value() + second_die.get_value()

        if dice_total == 7:
            credits -= 1
            round_in_session = False
            print(f"Dice total: {dice_total}")
        elif dice_total == goal:
            credits += 1
            print(f"Dice total: {dice_total}")
            round_in_session = False
        else:
            print(f"Dice total: {dice_total}")
    goal = -1

    return credits, dice_total, goal

def main():
    # Create two GVDie objects
    die1 = gv_die.GVDie()
    die2 = gv_die.GVDie()

    # Read random seed to support testing (do not alter) and starting credits
    seed = int(input())
    # Set the seed for random
    random.seed(int(seed))

    # Initial stats
    credits = int(input())
    dice_total = None
    goal = None
    rounds = 0

    while credits != 0:
        #First roll (STEP 1)
        credits, dice_total, goal, goal_set, rounds = roll_dice(die1, die2, credits, goal, rounds)

        print(f"Dice total: {dice_total}")

        #Second roll if goal was set after the first roll (STEP 2)
        if goal_set:
            credits, dice_total, goal = keep_rolling(die1, die2, credits, goal)

        print(f"Credits: {credits}")
    
    print(f"Rounds: {rounds}")


if __name__ == "__main__":
    main()