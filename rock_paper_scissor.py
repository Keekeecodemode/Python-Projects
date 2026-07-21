import random
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
rock_paper_scissors=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if(user_choice>=0 and user_choice<=2):
    print(rock_paper_scissors[user_choice])
    print("Computer chose:\n")
    Computer_choice=random.randint(0,2)
    print(rock_paper_scissors[Computer_choice])
    if(user_choice==Computer_choice):
     print("Draw")
    elif(user_choice==0 and Computer_choice==2):
        print("You won")
    elif(user_choice==2 and Computer_choice==0):
        print("You lose")
    elif(user_choice> Computer_choice):
        print("You win")
    else:
        print("you lose")
else:
    print("Invalid Choice")