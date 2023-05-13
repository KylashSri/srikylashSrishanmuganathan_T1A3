# A list of tuples (tuples are added to meal_list via user prompt)

meal_list = []
user_weight = input("What is your weight (in kg)? ")
user_height = input("What is your height (in cm)? ")
daily_rec_cal = get_calorie_recommendation(user_weight, user_height)
current_cal_intake = 0

while:
    print("recommended daily calorie intake is " + daily_rec_cal + " calories")
    print("your current calorie intake today is " + current_cal_intake + " calories")
    meal_name = input("what have you eaten today? ")
    meal_calories = input("how many calories did it have? ") # error handle for NaN
    break

def get_calorie_recommendation(weight, height):
    return 14*weight + 5*height
