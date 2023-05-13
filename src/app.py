
def get_calorie_recommendation(weight, height):
    return 14*weight + 5*height

def set_user_weight():
    user_weight = input("What is your weight (in kg)? ")
    return

def set_user_height():
    user_height = input("What is your height (in cm)? ")
    return
    # A list of tuples (tuples are added to meal_list via user prompt)

meal_list = []
current_cal_intake = 0

print("this program allows you to track how many calories you've had and compare it against a recommendation")

user_weight = input("What is your weight (in kg)? ")
while user_weight != user_weight:
    print(user_weight + " is not a valid input, please enter a number")
    user_weight = input("What is your weight (in kg)? ")

user_height = input("What is your height (in cm)? ")
while user_height != user_height:
    print(user_height + " is not a valid input, please enter a number")
    user_height = input("What is your height (in cm)? ")

daily_rec_cal = get_calorie_recommendation(user_weight, user_height)
print("your recommended daily calorie intake is " + get_calorie_recommendation(user_weight, user_height))

print("your current calorie intake today is " + current_cal_intake + " calories")
# meal_name = input("what have you eaten today? ")
# meal_calories = input("how many calories did it have? ") 
# if(meal_calories != meal_calories): # error handle for NaN
#     print("meal_calories is must be a number")

while True:
    print("type 'help' for command list")
    command = input()
    if(command == 'help'):
        print("type 'help' to get the list of commands")
        print("type 'info' to show current weight, height and current calorie intake")
        print("type 'meal' to store information on a meal")
        print("type 'sw' to change your weight to a new value")
        print("type 'sh' to change your height to a new value")
        print("type 'rec' to view recommended calorie intake")
        print("type 'ml' to view meal list (meals taken that effect calorie count)")
        print("type 'reset' to reset meal list")
        print("type 'hardreset' to reset meal list and weight")
        print("type 'quit' to quit")
    elif(command == 'info'):
        # loop through meal_list to find current calorie intake
        print("info")
    elif(command == 'meal'):
        # get user input to add a meal in tuple form to 'meal_list' variable
        print("info")
    elif(command == 'meal'):
        # add meal
        print("info")
    elif(command == 'sw'):
        # set weight
        print("info")
    elif(command == 'sh'):
        # set height
        print("info")
    elif(command == 'rec'):
        # get cal rec
        print("info")
    elif(command == 'ml'):
        # meal list
        print("info")
    elif(command == 'reset'):
        # reset meal list
        print("info")
    elif(command == 'reset'):
        # reset meal list
        print("info")
    elif(command == 'quit'):
        break
    else:
        print(command + " is not a command!")
    


