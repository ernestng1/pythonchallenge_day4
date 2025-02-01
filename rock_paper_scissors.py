import random
from urllib.parse import uses_relative

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

rock_paper_scissor = [rock, paper, scissors] # present rock, paper and scissors inside list for access

#gamer selection
gamer_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if gamer_selection <= 2 and gamer_selection >= 0: # to prevent crashing when users keys in values outside of 0 to 2
    print(rock_paper_scissor[gamer_selection])

#computer selection
computer_selection = random.randint(0,len(rock_paper_scissor)-1)
print("Computer chose:")
print(rock_paper_scissor[computer_selection])

if gamer_selection > 2 or gamer_selection < 0:
    print("You typed an invalid input! You lose")
elif gamer_selection == 0 and computer_selection == 2:
    print("You win")
elif computer_selection== 0 and gamer_selection == 2:
    print("You lose")
elif gamer_selection > computer_selection:
    print("You win")
elif computer_selection > gamer_selection:
    print("You lose")
elif gamer_selection == computer_selection:
    print("Draw")
