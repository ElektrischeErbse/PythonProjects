import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif choice == "n":
        print(f"Thanks for playing!")
        break
    else:
        print("Invalid choice!")
