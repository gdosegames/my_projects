playerinvin = []
pantreyc = False 
bedroomc = False
officec = False

def startbegining():
    print("my dad is gone with the milk")
    print("i need you to travle to the AWSOMSTORE to get him ")
    print("...")
    print("WAKE UP YOU BIN OF TARTAR SAUCE")
    print("i will give you moneyyyyyyyyy if u get himmm")
    return input("yes or no? \n").lower()

def gamestart():
    if startbegining() == "yes" or "y":
        print("depositing the 10G")
        print("(you wonder how that man found you're house in the middle of the forest)")

    else:
        print("i gess the next person will help me :(")

def homechoice1(firstchoice):
    global pantreyc
    global bedroomc
    global officec
    global playerinvin
    if firstchoice == "pantrey" or "p":
        if pantreyc == False: 
            print("(you go and look for food you find a hamburger) ")
            print("\n")
            playerinvin.append("hamburger") #:) yummy
            pantreyc = True
        else:
            print("(there is nothing to grab)")
            print("\n")

    elif firstchoice == "bedroom" or "b":
        if bedroomc == False:
            print("(you go into you're bedroom and find a gps phone)")
            print("\n")
            playerinvin.append("gps-phone")
            bedroomc = True
        else:
            print("(there is nothing to grab)")
            print("\n")

    elif firstchoice == "office" or  "o":
        if officec == False:
            print("(you find a midevil battle axe on you'er wall)")
            print("\n")
            playerinvin.append("battle-axe")
            officec = True
        else:
            print("(there is nothing to grab)")
            print("\n")


gamestart()

while True:
    print("(well i will need food, wepon, and gps to make the trip)")
    firstchoice = input("(should i go to the pantrey first, mabye the bedroom, or the office?)")
    print("\n")
    homechoice1(firstchoice)
