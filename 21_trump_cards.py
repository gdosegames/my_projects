import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []



play = input("do you want to play?")

while play:
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

    print("youre cards are ")
    print(player_deck)



    