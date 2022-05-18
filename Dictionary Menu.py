#Definition Finder - Adam Eade

def dictopen():
    global dictfile
    global worddict
    dictfile = "DictFile.txt"
    worddict = {}
    with open(dictfile) as f:
        for line in f:
            (key, val) = line.strip().split(", ")

            worddict[key] = val

def validation():
    global loop
    global passtoken
    while True:
        try:
            response = input("Enter Y for Yes, or N for No: \n").upper()
            if response == "Y":
                loop = 1
                passtoken = 1
            elif response == "N":
                loop = 0
                passtoken = 0
            else:
                raise SyntaxError
            break
        except:
            print("That is not a valid option")

def login():
    global loop
    global passtoken
    global accdets
    accfile = "AccountDetails.txt"
    accdets = {}
    with open(accfile) as g:
        for line in g:
            (key, val) = line.strip().split(", ")
            accdets[key] = val

        username = accdets["username"]
        password = accdets["password"]
            
    loop = 1
    while loop == 1:
        loginresponse = input("Please enter your username: \n")
        if loginresponse == username:
            passwordresponse = input("Please enter your password: \n")
            if passwordresponse == password:
                print("Login successful. Welcome", username)
                passtoken = 1
                loop = 0
            else:
                print("Incorrect password entered")
                validation()
        else:
            print("Incorrect username entered")
            validation()

def emqoption2():
    global emq
    global loop
    global password
    
    #search for emergency question
    if emq == 1:
        emqresponse = input("What is the name of your first teacher?: \n")
    elif emq == 2:
        emqresponse = input("What is the name of your fist pet?: \n")
    elif emq == 3:
        emqresponse = input("What is the name of your childhood bestfriend?: \n")
    elif emq == 4:
        emqresponse = input("What is the name of the street you lived at in your childhood?: \n")
    elif emq == 5:
        emqresponse = input("What is your mother's middle name?: \n")
    elif emq == 6:
        emqresponse = input("Where was your father born?: \n")
    else:
        print("CODE OP ERROR - 0010")
          
    #validation of correct answer to emergency question
    if emqresponse == emans:
        newpassword = input("Please enter your new password: \n")
        newpassword2 = input("Please enter your new password one more time: \n")

        #successful reset password through double validation
        if newpassword == newpassword2:
            print("Password reset successful")
            password = newpassword
            loop = 0
        #failed password match through double validation
        else:
            print("Those passwords do not match")
            print("Do you want to try again?")
            validation()

    #failed response to emergency question
    else:
        print("Incorrect emergency answer entered")
        print("Do you want to try again?")
        validation()

def emqoption():           
    global menuemq
    global loop
    global emq
    global emans
    if menuemq == 1:
        emqresponse = "What is the name of your first teacher?: \n"
    elif menuemq == 2:
        emqresponse = "What is the name of your fist pet?: \n"
    elif menuemq == 3:
        emqresponse = "What is the name of your childhood bestfriend?: \n"
    elif menuemq == 4:
        emqresponse = "What is the name of the street you lived at in your childhood?: \n"
    elif menuemq == 5:
        emqresponse = "What is your mother's middle name?: \n"
    elif menuemq == 6:
        emqresponse = "Where was your father born?: \n"
    else:
        print("CODE OP ERROR - 0009")

    
    print("Please enter a new answer for your emergency question")
    newemans = input(emqresponse)
    newemans2 = input("Please enter your new answer one more time: \n")

    #successful double validation for emergency answer
    if newemans == newemans2:
        accfile = open("AccountDetails.txt", "r")
        list_of_lines = accfile.readlines()
        menuemq = str(menuemq)
        newline = "emq, " + menuemq + "\n"
        list_of_lines[2] = newline

        accfile = open("AccountDetails.txt", "w")
        accfile.writelines(list_of_lines)
        accfile.close()

        accfile = open("AccountDetails.txt", "r")
        list_of_lines = accfile.readlines()
        newline = "emans, " + newemans + "\n"
        list_of_lines[3] = newline

        accfile = open("AccountDetails.txt", "w")
        accfile.writelines(list_of_lines)
        accfile.close()
        print("Your emergency question has been updated")
        emq = menuemq
        emans = newemans
        loop = 0
        
    #failed double validationfor emergency answer
    else:
        print("Those answers do not match")
        print("Do you want to try again?")
        validation()

def menuone():
    global worddict
    global dictfile
    login()
    if passtoken == 0:
        menu()
    print("\n*** Welcome to the Definition Finder! ***")

    #find word in dictionary if present
    inputfound = True
    while inputfound == True:
        wordfind = str(input("Please enter the word you wish to find a definition for: \n")).upper()
        
        #search for word in dictionary
        if wordfind in worddict:
            print("The definition of", wordfind, "is: " + "'" + worddict[wordfind] + " '")
            print("Would you like to find another definition?")           
            validation()

            #send back to main menu
            if loop == 0:
                inputfound = False
                
        #reattempt search after failed find in dictionary                
        else:
            print("That word isn't found. Do you want to enter a new word?")
            validation()

            #send back to main menu
            if loop == 0:
                inputfound = False

def menutwo():
    global dictfile
    global worddict
    login()
    if passtoken == 0:
        menu()
    newword = str(input("Please enter a word to add to the dictionary: \n")).upper()
    if newword in worddict:
        print("Sorry, that word is already in the dictionary")
        print(newword, "means'" + worddict[newword] + "'")
        
    else:
        
        loop = 1
        while loop == 1:
            newdefin = str(input("What does: " + newword + " mean?: \n"))

            if len(newdefin) > 100:
                print("That definition is too long! Please enter a shorter definition for: " + newword)
            else:
                loop = 0
                print("Word successfully added to the dictionary!")
                dictfile = open("DictFile.txt","a")
                dictfile.write("\n")
                dictfile.write(newword)
                dictfile.write(", ")
                dictfile.write(newdefin)
                dictfile.close()
                

    
#interact menu 3
def menuthree():
    
    #open text file for account details
    global menuemq
    global loop
    global emq
    global emans
    global accdets

    accfile = "AccountDetails.txt"
    accdets = {}
    with open(accfile) as g:
        for line in g:
            (key, val) = line.strip().split(", ")
            accdets[key] = val

        username = accdets["username"]
        password = accdets["password"]
            
    loopmenu3 = 1

    #interact account information menu
    while loopmenu3 == 1:
        print("*** Welcome to the Account Information Menu! ***")
        print("1) Change Username")
        print("2) Change Password")
        print("3) Change Emergency Answer")
        print("4) Reset Password")
        print("5) Return to Home Menu")

        #validation check for valid menu number
        while True:
            try:
                menuop = int(input("Please type the corresponding number: \n"))
                if menuop < 1 or menuop > 5:
                    raise ValueError
                break
            except:
                print("That is not a valid option")

        #change username attempt
        if menuop == 1:
            loop = 1
            while loop == 1:
                print("Your current username is:", accdets["username"])
                passwordresponse = input("Please enter your password to continue")

                #successful password entered
                if passwordresponse == password:
                    newusername = input("Please enter your new username: \n")
                    accfile = open("AccountDetails.txt", "r")
                    list_of_lines = accfile.readlines()
                    newline = "username, " + newusername + "\n"
                    list_of_lines[0] = newline

                    accfile = open("AccountDetails.txt", "w")
                    accfile.writelines(list_of_lines)
                    accfile.close()
                     
                    print("Username change successful")
                    loop = 0

                #failed password entered
                else:
                    print("Incorrect password entered")
                    print("Do you want to try again?")
                    validation()

        #change password attempt
        if menuop == 2:
            loop = 1
            while loop == 1:
                passwordresponse = input("Please enter your current password to continue")

                #successful password entered
                if passwordresponse == password:
                    newpassword = input("Please enter your new password: \n")
                    newpassword2 = input("Please enter your new password one more time: \n")

                    #successful double validation for new password
                    if newpassword == newpassword2:
                        accfile = open("AccountDetails.txt", "r")
                        list_of_lines = accfile.readlines()
                        newline = "password, " + newpassword + "\n"
                        list_of_lines[1] = newline

                        accfile = open("AccountDetails.txt", "w")
                        accfile.writelines(list_of_lines)
                        accfile.close()
                        print("Password change successful")
                        password = newpassword
                        loop = 0

                    #unsuccessful double validation for new password
                    else:
                        print("Those passwords do not match")
                        print("Do you want to try again?")
                        validation()
                                
                #double entered new passwords don't match
                else:
                    print("Incorrect password entered")
                    print("If this problem persists, try resetting your password via option 4 from the Account Information Menu")
                    print("Do you want to try again?")
                    validation()

        #change emergency question
        if menuop == 3:
            emq = int(accdets["emq"])
            emans = accdets["emans"]
            
            loop = 1
            while loop == 1:
                if emq == 1:
                    emansresponse = input("What is the name of your first teacher?: \n")
                elif emq == 2:
                    emansresponse = input("What is the name of your first pet?: \n")
                elif emq == 3:
                    emansresponse = input("What is the name of your childhood bestfriend?: \n")
                elif emq == 4:
                    emansresponse = input("What is the name of the street you lived at in your childhood?")
                elif emq == 5:
                    emansresponse = input("What is your mother's middle name?")
                elif emq == 6:
                    emansresponse = input("Where was your father born?")
                else:
                    print("CODE OP ERROR - 0007")

                #validate emans response
                if emansresponse == emans:
                    print("Would you like to change your emergency question?")
                    validation()

                    #select new emergency question
                    while loop == 1:
                        print("Please select a new emergency question")
                        print("1) What is the name of your first teacher?")
                        print("2) What is the name of your fist pet?")
                        print("3) What is the name of your childhood bestfriend")
                        print("4) What is the name of the street you lived at in your childhood?")
                        print("5) What is your mother's middle name?")
                        print("6) Where was your father born?")

                        #valid response to new emergency question
                        while True:
                            try:
                                menuemq= int(input("Please type the corresponding number: \n"))
                                if menuemq < 1 or menuemq > 6:
                                    raise ValueError
                                break
                            except:
                                print("That is not a valid option")

                        emqoption()
                    
                #incorrect response to emergency question   
                else:
                    print("Incorrect emergency answer entered")
                    print("Do you want to try again?")
                    validation()
                    

        #reset password
        if menuop == 4:
            #reset password
            loop = 1
            while loop == 1:
                usernameresponse = input("Please enter your username: \n")

                #successful match for current username
                if usernameresponse == username:
                    emqoption2()
                #failed match for current username
                else:
                    print("Incorrect username entered")
                    print("Do you want to try again?")
                    validation()

        #return to home menu
        if menuop == 5:
            loopmenu3 = 0
 
#exit program
def menufour():
    exit()

#interact home menu
def menu():

    while True:
        print("*** Welcome to the Dictionary Service Menu! ***")
        print("1) Find Definition")
        print("2) Add Definition")
        print("3) Account Information")
        print("4) Exit")

        while True:
            try:
                menunum = int(input("Please type the corresponding number: \n"))
                if menunum < 1 or menunum > 5:
                    raise ValueError
                break
            except:
                print("That is not a valid option")

        #redirect to func based on response
        if menunum == 1:
            menuone()
        elif menunum == 2:
            menutwo()
        elif menunum == 3:
            menuthree()
        elif menunum == 4:
            menufour()
        else:
            print("CODE OP ERROR - 0001")
    
#run
dictopen()
menu()
