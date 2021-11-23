#Rock , Papaer and Scissors
import random

#Pre-requisite
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def imgSelector(option):
    if (option == "rock"):
        return rock
    elif (option == "paper"):
        return paper
    else:
        return scissors

posibilities = ["rock","paper","scissors"]
player1_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(imgSelector(posibilities[player1_choice]))

computer_choice=random.randint(0,2)
print("Computer Choice:")
print(imgSelector(posibilities[computer_choice]))

if ((posibilities[player1_choice] == "rock" and posibilities[computer_choice] == "scissors") or (posibilities[player1_choice] == "scissors" and posibilities[computer_choice] == "paper") or (posibilities[player1_choice] == "paper" and posibilities[computer_choice] == "rock")):
    print("You Win")
elif (posibilities[player1_choice] == posibilities[computer_choice]):
    print("Draw")
else:
    print("You Lose")