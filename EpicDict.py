epic_programmer_dict = {
    'jade raymond':['rayjade@someemail.com',111],
    'tracy chou':['trachou@someemail.com', 222],
    'grace hopper':['hoppergrace@someemail.com',333],
    'lady ada Lovelace':['lovelace@someemail.com',444],
    'leah culver':['culeah@someemail.com',555]
    }

def searchPeople(personsName):
    #Looks up the name in the epic dictionary
    try:
                #Tries the following lines of text,
                #and if there are no errors
                #then it runs
                personsInfo = epic_programmer_dict[personsName]
                print 'Name:' + personsName.title()
                print 'Email:' + personsInfo[0]
                print 'Number:' + str(personsInfo[1])
    
    except:
                # If there are errors, then this code gets run.
                print 'No information found for that name'
                
userWantsMore = True
while userWantsMore == True:
                #Asks user to input persons name
                personsName = raw_input('Please enter a name:').lower()
                #Run our new function searchPeople with what was
                #typed in
                searchPeople(personsName)
                userWantsMore == False
                
                #See if user wants to search again
                searchAgain = raw_input('Search again? (y/n)')
                #Look at what they reply
                
                if searchAgain == 'y':
                            #userWantsMore stays as true so loop repeats
                            userWantsMore = True
                            
                elif searchAgain == 'n':
                            #userWantsMore turns to False to stop loop
                            userWantsMore = False
                            
                else:
                            #user inputs an invalid response, so we quit
                            print "I do not understand what you mean, quitting"
                            userWantsMore = False
        

