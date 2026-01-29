import random
usernameDict = {}

def assign():
    print("Hello there, welcome to PAU streets!")
    user_name = input("What's should we call you? ")
    print("Hey " + user_name + ", nice to meet you!")
    if user_name in usernameDict:
        print ("Someone beat you to it. . ." \
        "Do you have another name we can use?")
        return assign()    
    
    print ("""Would you like to be assigned an I.D number? 
           We're not tagging you as a slave or anything, promise😁""")
    response = input("Type 'yes' or 'no': ")
   

    if response == 'yes':
        id_number = random.randint(
            00000,99999)
        print("Great! Your I.D number is: "+ str(id_number))
    elif response == 'no':
        print("No worries! Enjoy your stay at PAU streets, "+user_name+"!")

   
              
    print("If you need any help, feel free to ask!")

assign()
