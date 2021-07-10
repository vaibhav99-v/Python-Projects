import random

again = True
another_roll = input("Want to roll the dice again? (y/n): ")
while again:
    print(random.randint(1, 6))
    another_roll = input("Want to roll the dice again? (y/n): ")
    if another_roll.lower()=="y":
        continue
    else:
        break
