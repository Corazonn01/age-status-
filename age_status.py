# age-status-
print("What is your age status")
while(True):
    try:
        UserInput = int(input(("Your answer here:")))
        if(UserInput <=11):
            print("You are a child")
            break
        elif(UserInput <=19):
            print("You are a teen")
            break
        elif(UserInput <=60):
            print("You are an adult")
            break
        elif(UserInput <=100):
            print("You are old")
        else:
            print("That is incorrect. Try again!")
    except ValueError:
        print("That is not a number. Try again!")
