import time
shipName = "Nastrama"
captain = "Wallace"
location = "Earth"
password = "Buttercups"

pAttempt = raw_input("Enter the password: ")
while pAttempt != password:
    print "Password incorrect"
    pAttempt = raw_input("Enter the password: ")
print "Password correct.  Welcome to the " + shipName
print ""
print "The spaceship " + shipName + " is currently visiting " + location + "."

choice = ""
while choice != "/exit":
    print "What would you like to do, " + captain + "?"
    print ""
    print "a. Travel to another planet"
    print "b. Fire cannons"
    print "c. Open the airlock"
    print "d. Self-destruct"
    print "e. Send a message"
    print "/exit to exit"
    print ""
    choice = raw_input("Enter your choice: ")

    if choice == "a":
        destination = raw_input ("Where would you like to go?")
        print "Leaving " + location
        print "Travelling to " + destination
        time.sleep(5)
        print "Arrived at " + destination
        location = destination
    elif choice == "b":
        print "firing cannons"
        time.sleep(1)
        print "BANG!"
        time.sleep(1)
    elif choice == "c":
        print "Opening airlock"
        time.sleep(3)
        print "Airlock open"
        time.sleep(1)
    elif choice == "d":
        confirm = raw_input ("Are you sure you want the ship to self destruct? (y/n)")
        if confirm == "y":
            print "Ship will self-destruct in "
            print "3"
            time.sleep(1)
            print "2"
            time.sleep(1)
            print "1"
            time.sleep(1)
            print "Goodbye"
            print "BOOM"
            choice = "/exit"
    elif choice == "e":
        toField = raw_input ("Who would you like to message: ")
        message = raw_input ("Message: ")
        print "Sending..."
        print message
        print "to " + toField
        print "Thank you for using our messaging service..."
    elif choice == "/exit":
        print "Goodbye"
    else:
        print "Invalid input.  Please select a, b, c or d.  /exit to exit"
        
