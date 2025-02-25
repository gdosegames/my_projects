import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []
computer_deck = []
player_deck_sum = []


def give_card(cards1,cards2,cards3,cards4,onetwofor):
    deck = random.choice(onetwofor)
    if (deck == 1):
        return random.choice(cards1)
    if (deck == 2):
        return random.choice(cards2)
    if (deck == 3):
        return random.choice(cards3)
    if (deck == 4):
        return random.choice(cards4)
    

play = input("do you want to play?")

while play:
    player_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))
    player_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))

    computer_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))
    computer_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))

    print("youre cards are ")
    print(player_deck)

    player_deck_sum = (player_deck[0] + player_deck[1])
    computer_deck_sum = (computer_deck[0] + computer_deck[1])
    print("\n")

    playing = True
    while playing:
#player deck check 1
        if (player_deck_sum < 21):
                    draw1 = input("do you want to draw?")
                    if (draw1):
                        player_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))
                        print(player_deck)

        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break

#computer deck check 1
        if (computer_deck_sum == 21):
            print("the npc has 21 you lose!")
            break

        if (computer_deck_sum > 21):
            print("the npc is over 21 you win")
            break

        if (computer_deck_sum < 17):
            computer_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))
#player deck check 2
        if (player_deck_sum < 21):
                    draw1 = input("do you want to draw?")
                    if (draw1):
                        player_deck.append(give_card(cards1,cards2,cards3,cards4,onetwofor))
                        print(player_deck)

        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break


