import random 
dice = [1,2,3,4,5,6]

#computer input
computerdi = int((random.choice(dice)))

#player 1 input
p1im = int(input("1 for start: 2 for quit "))


if (p1im == 1):

    playerdi = (random.choice(dice))

elif (p1im == 2):
    Print("see you next time")
    
else:
    Print("invalid input pluh")

print(computerdi)
print(playerdi)

if (computerdi == playerdi):
    