#Garrett j., joaqin, ayden, KORBIN
import random 
dice = [1,2,3,4,5,6]
computerwins = 0
playerwins = 0
def diceroller():
     return random.choice(dice)

def player_round_winner():

     if (playerdi > computerdi):
          playerwins = (playerwins + 1)
          print("player wins round")

     else (computerdi > playerdi):
          computerwins = (computerwins + 1)
          print("computer wins round")

def player_game_winner():
     if (playerwins >= 3):
          print("player wins game")

     else (computerwins >= 3):
          print("computer wins game")
     
+