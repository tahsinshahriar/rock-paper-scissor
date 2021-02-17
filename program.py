#importing the random module
import random

print("***rock***")
print("***paper***")
print("***scissor***")

user_input = input("Enter your choice: ")

pc_input = random.randint(1,3)

if pc_input == 1:
    pc_input = "rock"
elif pc_input == 2:
    pc_input = "paper"
else:
    pc_input = "scissor"

# print("\n\nUser input: " + user_input)

print("The computer plays: " + pc_input)

if user_input == "rock":
    if pc_input == "paper":
        print("Pc wins!")
    elif pc_input == "scissor":
        print("User wins!")
    else:
        print("It's a draw!")
elif user_input == "paper":
    if pc_input == "scissor":
        print("Pc wins!")
    elif pc_input == "rock":
        print("User wins!")
    else:
        print("It's a draw!")
elif user_input == "scissor":
    if pc_input == "rock":
        print("Pc wins!")
    elif pc_input == "paper":
        print("User wins!")
    else:
        print("It's a draw!")
else:
    print("Invalid input :(")
