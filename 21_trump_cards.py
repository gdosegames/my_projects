import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []
computer_deck = []

def give_card(cards1,cards2,cards3,cards4,onetwofor):
    random.choice(onetwofor)

play = input("do you want to play?")

while play:
    player_deck.append
    print("youre cards are ")
    print(player_deck)
    player_deck_sum = (player_deck[0] + player_deck[1])
    computer_deck_sum = (computer_deck[0] + computer_deck[1])
    print("\n")
    playing = True
    while playing:
#player deck check 1
        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break

        if (player_deck_sum < 21):
            draw1 = input("do you want to draw?")
            if (draw1 == True):
                new_card_player(onetwofor,player_deck,cards1,cards2,cards3,cards4)
                print(player_deck)
#computer deck check 1
        if (computer_deck_sum == 21):
            print("the npc has 21 you lose!")
            break

        if (computer_deck_sum > 21):
            print("the npc is over 21 you win")
            break
            
        if (computer_deck_sum < 17):
            new_card_computer(onetwofor,cards1,cards2,cards3,cards4,computer_deck)
#player deck check 2
        print(player_deck)
        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break

        if (player_deck_sum < 21):
            draw1 = input("do you want to draw?")
            if (draw1 == True):
                new_card_player(onetwofor,player_deck,cards1,cards2,cards3,cards4)
                print(player_deck)



