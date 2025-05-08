name = input("enter your name pleas: ")
 
while True:
     try:
         age = int(input(f"Hi {name}, please enter your age: "))
         if age > 0:
             break
         else:
             print("Invalid input. Age must be greater than 0.")
     except ValueError:
         print("Invalid input. Please enter a valid number for your age.")


if age < 5:
     print("Sorry, you must be 5 or older to participate.")
if age > 17:
     print("Sorry, you must be 17 or younger to participate.")

#-------------------------------------------------------------------------------------------------------------

activity_choice = ["1. Cultural immersion. This is for 5 days and is considered “easy” and costs $800. ", "2. Kayaking and pancakes. This is for 3 days and is considered “moderate” and costs $ 400. ", "3. Mountain biking. This is for 4 days and is considered “difficult” and costs $900. '"]

print('choose an activity')
print(f'{activity_choice[0]}')
print(f'{activity_choice[1]}')
print(f'{activity_choice[2]}')

while True:
     try:
         activity_choice = int(input("Enter the number of your chosen activity: "))
         if activity_choice in [1, 2, 3]:
             break
         else:
             print("Invalid input. Please enter a number between 1 and 3.")
     except ValueError:
         print("Invalid input. Please enter a valid number.")

if activity_choice == 1:
    activity_fee = 800
elif activity_choice == 2:
    activity_fee = 400
elif activity_choice == 3:
    activity_fee = 900


#-------------------------------------------------------------------------------------------------------------

transport = ["1.yes", "2.no"]

print('campers can make there own way to the camp or take a shuttle for $80. will you be taking a shuttel or making your way there?')
print(f'{transport[0]}')
print(f'{transport[1]}')

while True:
     try:
         transport = int(input("Enter the number of your chosen activity: "))
         if transport in [1, 2]:
             break
         else:
             print("Invalid input. Please enter a number between 1 and 2.")
     except ValueError:
         print("Invalid input. Please enter a valid number.")

if transport == 1:
    transport = 80
elif transport == 2:
    transport = 0

#-------------------------------------------------------------------------------------------------------------

total_fee = activity_fee + transport

#-------------------------------------------------------------------------------------------------------------
meal_options = ["1.standerd meal", "2.vegetarian", "3.vegan"]

print('select a meal')
print(f'{meal_options[0]}')
print(f'{meal_options[1]}')
print(f'{meal_options[2]}')

while True:
     try:
         meal_options = int(input("Enter the number of your chosen activity: "))
         if meal_options in [1, 2, 3]:
             break
         else:
             print("Invalid input. Please enter a number between 1 and 3.")
     except ValueError:
         print("Invalid input. Please enter a valid number.") 
print(f'{name}, aged {age}, has chosen activity option "{activity_choice}", meal option: "{meal_options}". The total fee is ${total_fee}.')