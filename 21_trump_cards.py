import random
cards1 = [1,2,3,4,5,6,7,8,9,10,11]
cards2 = [1,2,3,4,5,6,7,8,9,10,11]
cards3 = [1,2,3,4,5,6,7,8,9,10,11]
cards4 = [1,2,3,4,5,6,7,8,9,10,11]
onetwofor = [1,2,3,4]
player_deck = []
computer_deck = []
player_deck_sum = 0
computer_deck_sum = 0
random.shuffle(cards1)
random.shuffle(cards2)
random.shuffle(cards3)
random.shuffle(cards4)
#gives new card
def give_card():
    global onetwofor, cards1, cards2, cards3, cards4
    deck = random.choice(onetwofor)
    if (deck == 1):
        return cards1.pop(0)
    if (deck == 2):
        return cards2.pop(0)
    if (deck == 3):
        return cards3.pop(0)
    if (deck == 4):
        return cards4.pop(0)
#counts player cards
def count_cards(cards_in_deck):
    sum = 0
    for i in range(len(cards_in_deck)):
        sum += cards_in_deck[i]
    return sum

def draw_or_stay():
    global player_deck_sum
    if (check_sum()):
            print("player 1")
            print("1 to draw")
            print("2 to skip")
            draw1 = int(input("what is you're choice?"))
            #draw new card player
            if (draw1 == 1):
                player_deck.append(give_card())
                print(player_deck)
                player_deck_sum = count_cards(player_deck)
                print("you have", player_deck_sum)

def draw_or_stay2():
    global computer_deck_sum
    if (check_sum()):
        print("player 2")
        print("1 to draw")
        print("2 to skip")
        draw2 = int(input("what is you're choice?"))
        #draw new card player
        if (draw2 == 1):
            computer_deck.append(give_card())
            print(computer_deck)
            computer_deck_sum = count_cards(computer_deck)
            print("you have", computer_deck_sum)
    


print("21 by")
print("garrett")
print("ayden")
print("korbin")
print("joaquin")
print("\n")
print("you're options are")
print("1 to play")
print("2 to quit")
play = int(input("what is you're choice? "))

if (play == 1):
    player_deck.append(give_card())
    player_deck.append(give_card())

    computer_deck.append(give_card())
    computer_deck.append(give_card())

    print("youre cards are ")
    print(player_deck)
    computer_deck_sum = (computer_deck[0] + computer_deck[1])
    player_deck_sum = (player_deck[0] + player_deck[1])
    print("you have", player_deck_sum)

    playing = True
    while playing:
    #player deck check 1
        draw_or_stay()

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
        #draw new card computer
        
        draw_or_stay2()
       
        
        print("you have", player_deck_sum)
        print("the computer has", computer_deck_sum)
        if (computer_deck_sum > player_deck_sum):
            print("you lose ")
            break
        elif (computer_deck_sum < player_deck_sum):
            print("you win ")
            break
        elif (computer_deck_sum == player_deck_sum):
            print("tie ")
            break

elif(play == 2):
    print("ok by")  
else:
    print("not valid input")

# print(f"DEBUG: Deck 1: {cards1}\nDEBUG: Deck 2: {cards2}\nDEBUG: Deck 3: {cards3}\nDEBUG: Deck 4: {cards4}")
# print(give_card())
# print(f"DEBUG: Deck 1: {cards1}\nDEBUG: Deck 2: {cards2}\nDEBUG: Deck 3: {cards3}\nDEBUG: Deck 4: {cards4}")

