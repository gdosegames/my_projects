#Garrett j., joaqin, ayden, KORBIN
import random 
dice = [1,2,3,4,5,6]
computerwins = 0
playerwins = 0

#player 1 input
p1in = int(input("1 for start: 2 for quit "))

#computer/player roll
while (p1in == 1) :
     computerdi = int((random.choice(dice)))
     playerdi = int((random.choice(dice)))
     #print rolls
     print("computer number",computerdi)
     print("player number",playerdi)

      #rerolls
     if (computerdi == playerdi):
          computerdi = ((random.choice(dice)))
          playerdi = (random.choice(dice))

          #print rerolls
          print("rerolling")
          print("new computer number",computerdi)
          print("new player number",playerdi)

     if (computerdi > playerdi):
          print("computer wins the round")
          (computerwins + 1)
 
          else (playerdi > computerdi):
               print("you win the round")
               (playerwins + 1)

     if (playerwins == 3):
         print("player wins the game")
         break

          else (computerwins == 3):
               print("computer wins the game")
               break

     if (p1in == 2):
          print("ok by")

          else:
               print("not valid input go away")