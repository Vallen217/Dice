import random    

while True:
    try:
        num_side = int(input("Input the type of dice you wish to roll: [4, 6, 8, 10, 12, 20, 100]: "))
        num_dice = int(input("Input the amount of dice do You wish to roll: "))
        rolls = []        
        for die in range(num_dice):
            dice_roll = random.randint(1, num_side)
            rolls.append(dice_roll)
        print ("You rolled: {}".format(rolls))
    except ValueError:
        print("Invalid input. Try again.")                
    roll_again = input("Do You wish to roll again?: (y/n):")
    if roll_again.lower() == "y":
        continue
    elif roll_again.lower() == "n":break                
    while roll_again.lower() not in "y" "n":
        ask_again = input("Invalid input, Enter (y/n): ")
        if ask_again.lower() == "y":
            break
        elif ask_again.lower() == "n":
            break
    if ask_again.lower() == "n":
        break
