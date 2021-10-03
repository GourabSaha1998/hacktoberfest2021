import random

print("Welcome!")
print("Let's start the game")
print("You have maximum 5 chances")
name_1 = input("Please enter your name\n")
name = name_1.strip()
guess = ["Rock", "Paper", "Scissor"]
user_point = 0
computer_point = 0
i = 0
while i < 5:
    user_guess = input("Enter Rock, Paper or Scissor: ")
    user_guess = user_guess.title()
    computer_guess = random.choice(guess)

    if user_guess == computer_guess:
        print(f"{name.title()} and computer have the same guess")

    elif user_guess == "Rock" and computer_guess == "Paper":
        computer_point += 1
        print("Computer win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    elif user_guess == "Paper" and computer_guess == "Rock":
        user_point += 1
        print(f"{name} win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    elif user_guess == "Paper" and computer_guess == "Scissor":
        computer_point += 1
        print("Computer win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    elif user_guess == "Scissor" and computer_guess == "Paper":
        user_point += 1
        print(f"{name} win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    elif user_guess == "Scissor" and computer_guess == "Rock":
        computer_point += 1
        print("Computer win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    elif user_guess == "Rock" and computer_guess == "Scissor":
        user_point += 1
        print(f"{name.title()} win this chance")
        print(f"Computer's Point is {computer_point} and {name.title()}'s Point is {user_point}")

    print(f"Computer guess is {computer_guess}")
    print(name.title(), "have", 4 - i, "chances left")
    print("\n")
    i += 1

if computer_point < user_point:
    print(f"\n{name.title()} win the game")

else:
    print("\nComputer win the game")

print("Game over!")
print(f"Thank you for playing {name.title()}...")
