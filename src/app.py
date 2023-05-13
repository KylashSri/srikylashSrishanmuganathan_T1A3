import pandas as pd
import curses
from curses import wrapper

def get_calorie_recommendation(weight, height):
    return 14*weight + 5*height

def create_new_food_item(food_name, calorie_count):
    return {'food_item': food_name, 'calorie_count': calorie_count}

def add_food_item_to_list(new_item, food_dataframe):
    new_food_item = pd.Series(new_item)
    food_dataframe = pd.concat([food_dataframe, new_food_item.to_frame().T], ignore_index=True)
    return food_dataframe

food_item_dict = {'food_item': [], 'calorie_count': []}
food_item_df = pd.DataFrame(food_item_dict)

print("Welcome to Calorie Tracker")
print("This program allows you to track how many calories you've had and compare it against a recommendation")

# user_name = input("What is your username? ")
user_weight = float(input("What is your weight (in kg)? "))
user_height = float(input("What is your height (in cm)? "))

print("your recommended daily calorie intake is " + str(get_calorie_recommendation(user_weight, user_height)))

print("type 'help' for command list")

while True:
    command = input("> ")
    if(command == 'help'):
        # show avail commands
        print("type 'help' to get the list of commands")
        print("type 'info' to show current weight, height and current calorie intake")
        print("type 'meal' to store information on a meal")
        print("type 'sw' to change your weight to a new value")
        print("type 'sh' to change your height to a new value")
        print("type 'rec' to view recommended calorie intake")
        print("type 'ml' to view meal list (meals taken that effect calorie count)")
        print("type 'reset' to reset meal list")
        print("type 'hardreset' to reset meal list and user info")
        print("type 'quit' to quit")
    elif(command == 'info'):
        # loop through meal_list to find current calorie intake
        print("weight: " + str(user_weight) + " kg")
        print("height: " + str(user_height) + " cm")
        print("current calorie intake: " + str(food_item_df['calorie_count'].sum()) + " cal")
        print("recommended calorie intake: " + str(get_calorie_recommendation(user_weight, user_height)) + " cal")
    elif(command == 'meal'):
        # get user input to add a meal in tuple form to 'meal_list' variable
        new_item_name = input("food name: ")
        new_item_calorie_count = float(input("calorie count of said item: "))
        new_item = create_new_food_item(new_item_name, new_item_calorie_count)
        food_item_df = add_food_item_to_list(new_item, food_item_df)
        print("current calorie intake: " + str(food_item_df['calorie_count'].sum()) + " cal")
        print("recommended calorie intake: " + str(get_calorie_recommendation(user_weight, user_height)) + " cal")
    elif(command == 'sw'):
        # set weight
        user_weight = float(input("What is your weight (in kg)? "))
    elif(command == 'sh'):
        # set height
        user_height = float(input("What is your height (in cm)? "))
    elif(command == 'rec'):
        # get cal rec
        print("current calorie intake: " + str(food_item_df['calorie_count'].sum()) + " cal")
        print("recommended calorie intake: " + str(get_calorie_recommendation(user_weight, user_height)) + " cal")
    elif(command == 'ml'):
        # view meal list
        print(food_item_df)
        print("current calorie intake: " + str(food_item_df['calorie_count'].sum()) + " cal")
        print("recommended calorie intake: " + str(get_calorie_recommendation(user_weight, user_height)) + " cal")
    elif(command == 'reset'):
        # reset meal list
        food_item_dict = {'food_item': [], 'calorie_count': []}
        food_item_df = pd.DataFrame(food_item_dict)
        print("All food items added have now been removed")
    elif(command == 'hardreset'):
        # reset meal list and get prompted
        food_item_dict = {'food_item': [], 'calorie_count': []}
        food_item_df = pd.DataFrame(food_item_dict)
        user_weight = float(input("What is your weight (in kg)? "))
        user_height = float(input("What is your height (in cm)? "))
    elif(command == 'quit' or command == "q"):
        break
    else:
        print("'" + command + "' is not a command!")
        print("type 'help' for command list")
    


