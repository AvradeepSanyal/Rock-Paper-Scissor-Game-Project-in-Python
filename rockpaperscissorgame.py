import random

emojis = {'r':'rock','p':'paper','s':'scissors'}
choices = ['r', 'p', 's']

while True:
    user_choice = input("Rock, Paper, Scissor? (r/p/s): ").lower()
    if user_choice not in choices:
        print("invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("You Win!")
    else:
        print("You Lose!")

    should_continue = input("Wanna continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing come again afterwards :)")
        break
    elif should_continue == 'y':
        continue