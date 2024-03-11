#symbols area
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#head area
import random
comp_choose=random.randint(0,2)
game_image=[Rock,Paper,Scissors]
you_choose=int(input("What do you Choose.Type 0 for Rock , 1 for Paper or 2 for Scissor \n"))
#input print area
if you_choose == 0:
     print(f"you choose {you_choose} Rock")
     print(Rock)
elif you_choose == 1:
     print(f"you choose {you_choose} Paper")
     print(Paper)
else:
     print(f"you choose {you_choose} Scissors")
     print(Scissors)

#computer print area
if comp_choose == 0:
    print(f"computer choose {comp_choose} Rock")
    print(Rock)
elif comp_choose == 1:
    print(f"computer choose {comp_choose} Paper")
    print(Paper)
else:
    print(f"computer choose {comp_choose} Scissors")
    print(Scissors)

#comparison area
if you_choose>=3 or you_choose<0:
 print("invalid number plz check the input ")
elif you_choose==comp_choose:
    print("it's a draw")
elif you_choose==0 and comp_choose==2:
    print("you win")
elif you_choose==2 and comp_choose==0:
    print("you loss")
elif you_choose<comp_choose:
    print("you loss")
elif you_choose>comp_choose:
    print("you win")


print("New Change has been done in Sub branch")