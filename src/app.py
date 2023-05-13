# A list of tuples (tuples are added to meal_list via user prompt)

meal_list = []
user_weight = input("What is your weight (in kg)? ")
user_height = input("What is your height (in cm)? ")
daily_rec_cal = get_calorie_recommendation(user_weight, user_height)
current_cal_intake = 0

print("recommended daily calorie intake is " + daily_rec_cal + " calories")
print("your current calorie intake today is " + current_cal_intake + " calories")
meal_name = input("what have you eaten today? ")
meal_calories = input("how many calories did it have? ") 
if(meal_calories != meal_calories): # error handle for NaN
    print("meal_calories is must be a number")
    break
print("your recommended calorie intake is " + get_calorie_recommendation(user_weight, user_height))

while:
    print("type 'help' for command list")
    command = input()
    if(command == 'help')
        print("type 'help' to get the list of commands")
        print("type '' to ")
        print("type '' to ")
        print("type '' to ")
        print("type '' to ")
        print("type '' to ")
        print("type '' to ")
        print("type 'quit' to quit")
    

def get_calorie_recommendation(weight, height):
    return 14*weight + 5*height

def set_user_weight():
    user_weight = input("What is your weight (in kg)? ")
    return

def set_user_height():
    user_height = input("What is your height (in cm)? ")
    return


