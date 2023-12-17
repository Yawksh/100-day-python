import random
choices = ["rock", "paper", "scissors"]
computer=random.choice(choices)
player=None
while(player not in choices):
 player=input("scissors,paperr,rock")
print("computer"+" "+computer)
print("player"+" "+player)
