import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []
computer_deck = []



def pick_cardsplayer(player_deck,onetwofor,cards1,cards2,cards3,cards4):
    deck1 = random.choice(onetwofor)
    if (deck1 == 1):
        player_deck.append(random.choice(cards1))
    elif (deck1 == 2):
        player_deck.append(random.choice(cards2))
    elif (deck1 == 3):
        player_deck.append(random.choice(cards3))
    elif (deck1 == 4):
        player_deck.append(random.choice(cards4))


    deck2 = random.choice(onetwofor)
    if (deck2 == 1):
        player_deck.append(random.choice(cards1))
    elif (deck2 == 2):
        player_deck.append(random.choice(cards2))
    elif (deck2 == 3):
        player_deck.append(random.choice(cards3))
    elif (deck2 == 4):
        player_deck.append(random.choice(cards4))
    return

def pick_cardscomputer(computer_deck,onetwofor,cards1,cards2,cards3,cards4):
    deck1 = random.choice(onetwofor)
    if (deck1 == 1):
        computer_deck.append(random.choice(cards1))
    elif (deck1 == 2):
        computer_deck.append(random.choice(cards2))
    elif (deck1 == 3):
        computer_deck.append(random.choice(cards3))
    elif (deck1 == 4):
        computer_deck.append(random.choice(cards4))


    deck2 = random.choice(onetwofor)
    if (deck2 == 1):
        computer_deck.append(random.choice(cards1))
    elif (deck2 == 2):
        computer_deck.append(random.choice(cards2))
    elif (deck2 == 3):
        computer_deck.append(random.choice(cards3))
    elif (deck2 == 4):
        computer_deck.append(random.choice(cards4))
    return

play = input("do you want to play?")

while play:
    pick_cardsplayer(player_deck,onetwofor,cards1,cards2,cards3,cards4)
    pick_cardscomputer(computer_deck,onetwofor,cards1,cards2,cards3,cards4)
    print("youre cards are ")
    print(player_deck)
    player_deck_sum = (player_deck[0] + player_deck[1])
    computer_deck_sum = (computer_deck[0] + computer_deck[1])
    print("\n")
    playing = True
    while playing:

        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break

        if (player_deck_sum < 21):
            draw1 = input("do you want to draw?")

        if (computer_deck_sum < 18):
            deck1 = random.choice(onetwofor)
        if (deck1 == 1):
            computer_deck.append(random.choice(cards1))
        elif (deck1 == 2):
            computer_deck.append(random.choice(cards2))
        elif (deck1 == 3):
            computer_deck.append(random.choice(cards3))
        elif (deck1 == 4):
            computer_deck.append(random.choice(cards4))
        
        if (computer_deck_sum == 21):
            print("the npc has 21 you lose!")
            break

        if (computer_deck_sum > 21):
            print("the npc is over 21 you win")
            break

        if draw1 == True:
            print("drawing")
            deck1 = random.choice(onetwofor)
            if (deck1 == 1):
                player_deck.append(random.choice(cards1))
            elif (deck1 == 2):
                player_deck.append(random.choice(cards2))
            elif (deck1 == 3):
                player_deck.append(random.choice(cards3))
            elif (deck1 == 4):
                player_deck.append(random.choice(cards4))
        print(player_deck(0-3))
        if (player_deck_sum == 21):
            print("you have 21 you win!")
            break

        if (player_deck_sum > 21):
            print("you are over 21 game over")
            break

        if (player_deck_sum < 21):
            draw1 = input("do you want to draw?")
        

