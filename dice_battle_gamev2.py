import random 
dice = [1,2,3,4,5,6]

#player 1 input
p1im = int(input("1 for start: 2 for quit "))

#computer/player roll
if (p1im == 1):
    computerdi = int((random.choice(dice)))
    playerdi = int((random.choice(dice)))
    #print rolls
    print("computer number",computerdi)
    print("player nember",playerdi)

     #rerolls
    while (computerdi == playerdi):
     print("rerolling")
     computerdi = ((random.choice(dice)))
     playerdi = (random.choice(dice))
     #print rerolls
     print("new computer number",computerdi)
     print("new player nember",playerdi)

 #good by
elif (p1im == 2):
    print("see you next time")

 #eror 
else:
    print("invalid input")

print("Done!")