import random as r

zeros = ["00", "0"]
first = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
second = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
third = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]

def main():
    test = "ahhh random aahhhhh 32"
    test = removeLetters(test)
    print("testing removeLetters: {:s}".format(test))
    print(spin())
    countSpins()
    print()
    print()
    print()
    print()
    print()
    playGame(100.00)
    
def removeLetters(word):
    hold = ""
    for char in word:
        try:
            _ = int(char)
            hold += char
        except:
            None
    return hold
            

def spin():
    sets = r.randint(0, 8)
    if(sets == 0):
        num = r.randint(0, (len(zeros)-1))
        return zeros[num]
    elif(sets == 1 or sets == 2):
        num = r.randint(0, (len(first)-1))
        return first[num]
    elif(sets == 3 or sets == 4 or sets == 7):
        num = r.randint(0, (len(second)-1))
        return second[num]
    elif(sets == 5 or sets == 6 or sets == 8):
        num = r.randint(0, (len(third)-1))
        return third[num]
    else:
        return "how"

def countSpins():
    zero = 0
    doubleZero = 0
    one = 0
    two = 0
    three = 0
    for x in range(8000):
        num = spin()
        if(num == "0"):
            zero += 1
        elif(num == "00"):
            doubleZero += 1
        num = int(num)
        if(num < 13):
            one += 1
        elif(num < 25):
            two += 1
        elif(num < 37):
            three += 1
        else:
            print("what")
    print("0: {:d}".format(zero))
    print("00: {:d}".format(doubleZero))
    print("first: {:d}".format(one))
    print("second: {:d}".format(two))
    print("third: {:d}".format(three))
        
def playGame(bank):
    deduct = 0
    firstThird = False
    secondThird = False
    thirdThird = False
    red = False
    black = False
    redun = False
    num = -1
    payout = 0
    while(True):
        play = input("Would you like to play Roulette? (y/n) ")
        if("n" in play):
            print("Sorry to see you go!")
            break
        while(True):
            if(not redun):
                print("Your credit: ${:.2f}".format(bank))
                bet = input("What do you bet on? ")
                if("red" in bet):
                    deduct += 1
                    red = True
                if("black" in bet):
                    deduct += 1
                    black = True
                if("first" in bet):
                    deduct += 1
                    firstThird = True
                if("second" in bet):
                    deduct += 1
                    secondThird = True
                if("third" in bet):
                    deduct += 1
                    thirdThird = True
                else:
                    deduct += 1
                    num = removeLetters(bet)
            amount = int(input("Enter your bet, minimum $5: "))
            if(amount < 5):
                redun = True
                continue
            if((deduct * amount) > bank):
                print("insufficient funds, exiting now")
                return 0
            break
        bank -= deduct * amount
        while(True):
            ready = input("Enter \"r\" when you're ready to spin! ")
            if(ready != "r"):
                continue
            break
        house = spin()
        print("The House spun a {:s}".format(house))
        if(house == "00" or house == "0"):
            if(r.randint(0,1)):
                house = r.randint(1,36)
        if(deduct == 0):
            print("There was an error, we are taking your money anyway.")
        else:
            if(num == house):
                payout += amount * 35
            if(int(house) > 0 and int(house) < 13 and firstThird):
                payout += amount * 2
            if(int(house) > 0 and int(house) < 25 and secondThird):
                payout += amount * 2
            if(int(house) > 0 and int(house) < 37 and thirdThird):
                payout += amount * 2
            if(int(house) > 0 and (int(house) % 2) == 0 and red):
                payout += amount * 2
            if(int(house) > 0 and (int(house) % 2) == 1 and black):
                payout += amount * 2
        bank += payout
        if(payout == 0):
            print("Better luck next time!")
        else:
            print("You won ${:.2f}!".format(payout))
        print("You now have ${:.2f} credits!".format(bank))
        firstThird = False
        secondThird = False
        thirdThird = False
        red = False
        black = False
        redun = False
        deduct = 0
        num = -1
        payout = 0
            
        
            
    return payout



main()