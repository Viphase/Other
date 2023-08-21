adminCode = "Rabbit"
allIDs = []

def AddID():
    newID = input("Enter new ID (5 nums, 5 lets): ")
    print("-------------------------------")
    allIDs.append(newID)
    print("ID was successfuly added")
    print("-------------------------------")
    AdminMenu()

    return allIDs

def EnterID():
   global currID 
   currID = input("Enter your id: ")
   return currID

def UserMenu():
    info = ["Coming Soon!"] 

    print("----------------------------")
    print(info)
    print("----------------------------")

def AdminMenu():
    print("----------------------------")
    print("******* Admin Panel ********")
    print("----------------------------")
    print("***** 1. Add NewID *********")
    print("***** 2. Change AdminCode **")
    print("***** 3. Exit **************")
    print("----------------------------")
    print("**** Enter Your Choice *****")
    print("----------------------------")

    ADchoice = int(input(">> "))

    if ADchoice == 2:
        print("----------------------------")
        adminCode = input("*** Enter new admin code >> ")
        print("----------------------------")
        print("*** New password was set ***")
        print("----------------------------")
        AdminMenu()

        return adminCode

    elif ADchoice == 3:
        Main()
    
    elif ADchoice == 1:
        AddID()

    else:
        print("----------------------------")
        print("Invalid Input⛔️")
        print("----------------------------")
        AdminMenu()

def Main():

    print("----------------------------")
    print("****** Album Beta 0.1 ******")
    print("----------------------------")
    print("******* 1. Enter ID ********")
    print("******* 2. Admin Panel *****")
    print("******* 3. Exit ************")
    print("----------------------------")
    print("**** Enter Your Choice *****")
    print("----------------------------")

    choice = int(input(">> "))

    if choice == 1:
        ProtocolID()

    elif choice == 2:

        password = input("Enter AdminCode: ")

        if password == adminCode:
            print("------------")
            print("**** ✅ ****")
            print("------------")
            AdminMenu()
        
        else:
            print("Invalid Input⛔️")
            Main()

    elif choice == 3:
        print("Thank you for testing Album Beta 0.1!")
        print("-------------------------------------")
        exit(0)
    
    else:
        print("Invalid Input⛔️")
        Main()

def ProtocolID():

    EnterID()

    if currID in allIDs:
        print("----------------------------")
        print("**** ID was verified✅ *****")
        print("----------------------------")
        UserMenu()
        return True

    else:
        print("----------------------------")
        print("*** ID wasn't verified❌ ***")
        print("----------------------------")
        print("***** Please try again *****")
        print("----------------------------")
        UserMenu()
        return False

Main()