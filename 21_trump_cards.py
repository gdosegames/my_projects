import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []
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
    player_deck_sum = (player_deck(1) + player_deck(2))
    if (player_deck_sum < 21):
        draw1 = imput("do you want to draw?")
            
    elif (player_deck_sum = 21):
        print("you have 21 you win!")
    elif (player_deck_sum > 21):

    
