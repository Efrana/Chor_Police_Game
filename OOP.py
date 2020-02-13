import random

S = "global"
S = int(input("Number of time u want to play : "))
i = 1

while i <= S:
    print(".....START THE GAME....")
    print(".....**************....")
    items = [100, 80, 0, 60]
    random.shuffle(items)
    print(items)
    card = [n for n in items]
    # print (card.index(100))
    x = int(input("Please Enter a Number From 0-3:"))
    P1 = card[x]
    card.remove(card[x])
    P2 = card[0]
    P3 = card[1]
    P4 = card[2]
    print('P1 value: ', +P1)
    print('P2 value: ', +P2)
    print('P3 value: ', +P3)
    print('P4 value: ', +P4)

    upcard = [n for n in card]
    print(upcard)


    def find_babu():
        if P2 == 100:
            print("P2 Im THE BOSS")

        elif P3 == 100:
            print("P3 Im THE BOSS")

        elif P4 == 100:
            print("P4 Im THE BOSS")


    def find_dakat():
        if P2 == 60:
            print("P2 Im THE DAKAT")

        elif P3 == 60:
            print("P3 Im THE DAKAT")

        elif P4 == 60:
            print("P4 Im THE DAKAT")


    def find_police():

        if P2 == 80:
            print("P2 Im THE POLICE")

        elif P3 == 80:
            print("P3 Im THE POLICE")

        elif P4 == 80:
            print("P4 Im THE POLICE")


    # for babu
    def call_police():

        y = (upcard.index(80))
        upcard.remove(upcard[y])
        print("upcard value")
        print(upcard)
        rand = [0, 1]  # for check thief
        random.shuffle(rand)
        thf = rand[0]
        if upcard[thf] == 0:
            if upcard[thf] == P2:
                print("YESSS....P2 IS THE THIEF")
            elif upcard[thf] == P3:
                print("YESSS....P3 IS THE THIEF")
            elif upcard[thf] == P4:
                print("YESSS....P2 IS THE THIEF")

        else:
            print("MESSAGE : POLICE CANNOT CATCH THE THIEF")


    # for police
    def find_thief():

        y = (upcard.index(100))
        upcard.remove(upcard[y])
        print(upcard)
        thf = int(input("Who is Thief..Enter 0 OR 1 : "))
        if upcard[thf] == 0:
            if upcard[thf] == P2:
                print("YESSS....P2 IS THE THIEF")
            elif upcard[thf] == P3:
                print("YESSS....P3 IS THE THIEF")
            elif upcard[thf] == P4:
                print("YESSS....P4 IS THE THIEF")

        else:
            print("OOOHHHH....CAN'T CATCH THE THIEF")

        # for babu


    # for thief/robber
    def call_police_thief():

        y = (upcard.index(80))
        upcard.remove(upcard[y])
        z = (upcard.index(100))
        upcard.remove(upcard[z])
        # print("upcard value")
        print(upcard)
        upcard.append(P1)
        # print("upcard value after append")
        # print(upcard)
        rand = [0, 1]  # for check thief
        random.shuffle(rand)
        thf = rand[0]

        if upcard[thf] == 0:
            if upcard[thf] == P1:
                print("YESSS....Efrana IS THE THIEF")
            # print(upcard[thf])
            # print(P1)
            elif upcard[thf] == P2:
                print("YESSS....P2 IS THE THIEF")
            # print(upcard[thf])
            # print(P2)
            elif upcard[thf] == P3:
                print("YESSS....P3 IS THE THIEF")
                # print(upcard[thf])
                # print(P3)
            elif upcard[thf] == P4:
                print("YESSS....P2 IS THE THIEF")
                # print(upcard[thf])
                # print(P4)

        else:
            print("MESSAGE : POLICE CANNOT CATCH THE THIEF")


    if P1 == 100:
        print("Efrana YOU ARE THE BOSS...PLEASE COMMAND POLICE")
        find_police()  # for finding police
        call_police()
    elif P1 == 80:
        print("Efrana YOU ARE THE POLICE...FIND THIEF")
        find_thief()

    elif P1 == 0:
        print("Efrana YOU ARE THE THIEF...KEEP SILENT")
        find_babu()
        find_police()
        call_police_thief()

    elif P1 == 60:
        print("Efrana ARE THE DAKAT...KEEP SILENT")
        find_babu()
        find_police()
        call_police_thief()

    i = i + 1
