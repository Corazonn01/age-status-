#age status inside the class 
def check_age():
    try:
        user_age = int(input(("write your age here ")))
        if  user_age <= 11:
            print("you are a child")
        elif user_age <= 19:
            print("you are a teen") 
        elif user_age <= 50:
            print("you are an adult") 
        else:
            print('you are old.')
    except ValueError:
        print("That is not a number, try one more time") 

check_age()
