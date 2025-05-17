import random

def getCount():
    count = int(input("How many times do you want to roll: "))
    return count

def rollDice():
    a = random.randint(1,6)
    b = random.randint(1,6)
    total = a + b
    print(f"🎲 You rolled: {a} and {b} — Total: {total}")

def getChoice():
    roll = (input("Roll the Dice? (y/n): ")).lower()
    return roll

total_count = getCount()
while(total_count):
    choice = getChoice()
    if (choice=='y'):
        rollDice()
        total_count-=1
        print(f"Rolls left: {total_count}")
    elif (choice == 'n'):
        print("Thanks for Playing!!")
        break
    else:
        print("Invalid Choice. Please enter 'y' or 'n'")