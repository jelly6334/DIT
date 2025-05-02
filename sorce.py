name = input("enter your name pleas: ")
 
  # Age input with validation
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
 if age < 12:
      print("Sorry, you must be 12 or older to participate.")
 if age > 17:
      print("Sorry, you must be 17 or younger to participate.")
  # Blank line
 print()
 
  #list for the activitys
 activity_choice = ["1. Music Jam Session (2 hours, easy, $5 fee)", "2. Science Experiments Lab (3 hours, moderate, $10 fee)", "3. Sports leadership traning (4 hours, challenging, $12 fee)'"]
 
  #the list for activitys
 print('choose an activity')
 print(f'{activity_choice[0]}')
 print(f'{activity_choice[1]}')
 print(f'{activity_choice[2]}')
 
  #input awnsers
 while True:
      try:
          activity_choice = int(input("Enter the number of your chosen activity: "))
          if activity_choice in [1, 2, 3]:
              break
          else:
              print("Invalid input. Please enter a number between 1 and 3.")
      except ValueError:
          print("Invalid input. Please enter a valid number.")
 
 
 # Chosen activity fee calculation
 if activity_choice == 1:
     activity_fee = 5
 elif activity_choice == 2:
     activity_fee = 10
 elif activity_choice == 3:
     activity_fee = 12
 
  # Blank line
 print()       
 
 @@ -66,8 +74,17 @@
      except ValueError:
          print("Invalid input. Please enter a valid number.")
 
 # Chosen meal fee calculation
 if meal_option == 1 or meal_option == 2 or meal_option == 3 or meal_option == 4: 
     meal_fee = 7
 else:
     meal_fee = 0
  
 # Total fee calculation
 total_fee = activity_fee + meal_fee
 
  # Blank line
 print()
 
  #final print out 
 print(f'{name}, aged {age}, has chosen activity option "{activity_choice}", meal option: "{meal_option}".')
 print(f'{name}, aged {age}, has chosen activity option "{activity_choice}", meal option: "{meal_option}". The total fee is ${total_fee}.')