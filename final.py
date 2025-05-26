
# name input with number error
while True:
    name = input("Enter your name please: ")
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid input. Please enter a name without numbers or symbols.")

# blanck line
print()

# age input
while True:
     try:
         age = int(input(f"Hi {name}, please enter your age: "))
         if age > 0:
             break
         else:
             print("Invalid input. Age must be greater than 0.")
     except ValueError:
         print("Invalid input. Please enter a valid number for your age.")

# Age validation
if age < 5:
     print("Sorry, you must be 5 or older to participate.")
if age > 17:
     print("Sorry, you must be 17 or younger to participate.")

# blanck line
print()

#-------------------------------------------------------------------------------------------------------------
# activity list
activity_choice = ["1. Cultural immersion. This is for 5 days and is considered “easy” and costs $800. ", "2. Kayaking and pancakes. This is for 3 days and is considered “moderate” and costs $ 400. ", "3. Mountain biking. This is for 4 days and is considered “difficult” and costs $900. '"]

print('choose an activity')
print(f'{activity_choice[0]}')
print(f'{activity_choice[1]}')
print(f'{activity_choice[2]}')

# activity validation
while True:
     try:
         activity_choice = int(input("Enter the number of your chosen activity: "))
         if activity_choice in [1, 2, 3]:
             break
         else:
             print("Invalid input. Please enter a number between 1 and 3.")
     except ValueError:
         print("Invalid input. Please enter a valid number.")

# activity calculator
if activity_choice == 1:
    activity_fee = 800
elif activity_choice == 2:
    activity_fee = 400
elif activity_choice == 3:
    activity_fee = 900

# blanck line
print()

#-------------------------------------------------------------------------------------------------------------

# shuttle option
def def_shuttle():
    while True:
        Shuttle = input('Do you require a shuttle bus for $80? (yes/no) (y/n): ')
        if Shuttle in ['yes', 'y']:
            shuttle_fee = 80
            return shuttle_fee
        elif Shuttle in ['no', 'n']:
            shuttle_fee = 0
            return shuttle_fee
        else:
            print('Invalid input. Please enter "yes" or "no".')
            print()

#-------------------------------------------------------------------------------------------------------------

# meal list
meal_options = ["1.standerd meal", "2.vegetarian", "3.vegan"]

print('select a meal')
print(f'{meal_options[0]}')
print(f'{meal_options[1]}')
print(f'{meal_options[2]}')

# meal validation
while True:
     try:
         meal_options = int(input("Enter the number of your chosen meal: "))
         if meal_options in [1, 2, 3,]:
             break
         else:
             print("Invalid input. Please enter a number between 1 and 3.")
     except ValueError:
         print("Invalid input. Please enter a valid number.")

#-------------------------------------------------------------------------------------------------------------

# blanck line
print()  

# shuttle print out
shuttle_fee = def_shuttle()
print(f'Your shuttle bus fee is: ${shuttle_fee}')

total_fee = activity_fee + shuttle_fee

# blanck line
print()       

#-------------------------------------------------------------------------------------------------------------
 
# final print out
print(f'{name}, aged {age}, has chosen activity option "{activity_choice}", meal option: "{meal_options}". The total fee is ${total_fee}.')

# blanck line
print()     

# Camp Confirmation
camp_confirmation = input("is this corect use (yes/no) \n\nAns = ").strip().lower()

if camp_confirmation == "yes":
    print("\nOk great see you soon!")
elif camp_confirmation == "no":
    print("\nIf something is wrong with your choice's please start again")
else:
    print("\nInvalid input. Please answer with 'yes' or 'no'.")
