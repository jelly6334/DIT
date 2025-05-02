name = input("what is your name: ")
age = input("what is your age: ")

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

