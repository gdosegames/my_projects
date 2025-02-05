import random 
dice = [1,2,3,4,5,6]
computerwins = 0
playerwins = 0

#player 1 input
p1im = int(input("1 for start: 2 for quit "))

#computer/player roll
if (p1im == 1):
     computerdi = int((random.choice(dice)))
     playerdi = int((random.choice(dice)))
     #print rolls
     print("computer number",computerdi)
     print("player number",playerdi)

     #rerolls
    while (computerdi == playerdi):
     computerdi = ((random.choice(dice)))
     playerdi = (random.choice(dice))

     #print rerolls
     print("rerolling")
     print("new computer number",computerdi)
     print("new player number",playerdi)

    if (computerdi > playerdi):
         print("computer wins")
         (computerwins + 1)

    elif (playerdi > computerdi):
         print("you win")
         (playerwins + 1)

    if (timesplayed >= 3):
         print("Done!")
 #good by
elif (p1im == 2):
     print("see you next time")

 #error
else:
     print("invalid input")

