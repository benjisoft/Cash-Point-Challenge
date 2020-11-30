# Setup balances
aBal = 500
bBal = 400
overdraft = -50

#Balance Checker
def balCheck(uID):
    if uID == "101":
        print("Your balance is: " + str(aBal))
    else:
        print("Your balance is: " + str(bBal))

#Cash Withdrawal
def withCash(uID):
    global overdraft
    global aBal
    global bBal
    complete = False
    while complete != True:
        cashOut = input("Withdrawal Amount: ")
        if cashOut.isdigit() == False:
            print("Stop it, how did you even do that? This ATM doesn't even have that button!")
        else:
            if uID == "101":
                if int(cashOut) < 0:
                    print("Value must be greater than 0")
                elif aBal - int(cashOut) > overdraft:
                    print("Thank you for withdrawing from Lewis Banking! {Withdrawal Command: £" + str(cashOut) + "}")
                    aBal = aBal - int(cashOut)
                    print("Remaining balance: " + str(aBal))
                    complete = True
                else:
                    print("Not enough money")
            else:
                if int(cashOut) < 0:
                    print("Value must be greater than 0")
                elif bBal - int(cashOut) > overdraft:
                    print("Thank you for withdrawing from Lewis Banking! {Withdrawal Command: £" + str(cashOut) + "}")
                    bBal = bBal - int(cashOut)
                    complete = True
                    print("Remaining balance: " + str(bBal))
                else:
                    print("Not enough money")

# Menu Function
def menu(uID, pWord):
    if (uID == "101" and pWord == "1234"):
                choice = input("Would you like to: (1) Check your balance or (2) Withdraw Cash")
                if choice.isdigit():
                    if choice == "1":
                        balCheck(uID)
                    elif choice == "2":
                        withCash(uID)
                    else:
                        print("Invalid Choice. Please pick 1 or 2. ")
                else:
                    print("Invalid Choice. Please pick 1 or 2.")
    elif (uID == "102" and pWord == "9876"):
                choice = input("Would you like to: (1) Check your balance or (2) Withdraw Cash")
                if choice.isdigit():
                    if choice == "1":
                        balCheck(uID)
                    elif choice == "2":
                        withCash(uID)
                    else:
                        print("Invalid Choice. Please pick 1 or 2. ")
                else:
                    print("Invalid Choice. Please pick 1 or 2.")

def checkLogin(uID, pWord):
    # Checks that username is valid
    if (uID != "" and pWord != ""):
        if (int(uID) > 102 or int(uID) < 101):
            print("Invalid login")
        else:
            menu(uID, pWord)
    else:
        print("Invalid input")

while True:
    # Requests user to login
    uID = input("User ID: ")
    uPass = input("Password: ")
    if uID.isdigit() and uPass.isdigit():
        checkLogin(uID, uPass)
    else:
        print("Invalid input")