# problems on nested if

# 1. Check x and y
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# if x > y:
#     print("x is grater than y")
#     if x > 15:
#         print("x is grater than 15")
#     else:
#         print("x is not grater than 15")
# else:
#     print("x is not grater than y")

# 2. Grade and Failure Check
# marks = int(input("Enter a number: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")    
# elif marks >= 70:
#     print("Grade C")    
# else:
#     print("Grade F")
#     print("You Failed")

# 3. Credit Card Eligibility
# age = int(input("Enter you age: "))
# income = int(input("Enter your income: "))
# if age < 18:
#     print("You are Underage")
# else:
#     if income > 30000:
#         print("You are eligible for credit card")
#     else:
#         print("Your income to low for a credit card")        


# 4. Even/Odd and Greater Than 10
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
#     if number > 10:
#         print("number is grater than 10")
#     else:
#         print("number is less than 10")    
# else:
#     print("Odd")        

# 5. Theme Park Ticket Price
# age = int(input("Enter age: "))
# height = float(input("Enter height (feet): "))
# if age < 12:
#     if height < 4:
#         price = 10
#     else:
#         price = 15
# else:
#     if height >= 4:
#         price = 20
#     else:
#         price = 15
# print("Ticket Price = $", price)

# 6. User Authentication
# corect_username = "Bhargav@2122"
# correct_password = "Bhargav@200"

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == corect_username:
#     if password == correct_password:
#         print("Login Successfully!")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid user!")            

# 7. Food Ordering System
# food = input("choose pizza or Burger: ")
# if food.lower() == "pizza":
#     cheese = input("Do you want extra ? (yes/no): ")
#     print("Order: Pizza")
#     if cheese.lower() == "yes":
#         print("Added cheese")
# elif food.lower() == "burger":
#     fries = input("Do you want fries ? (yes/no): ")
#     print("Order: Burger")
#     if fries.lower() == "yes":
#         print("Added fries")
# else:
#     print("Invalid choice")        


# 8. Positive, Negative or Zero
# number = int(input("Enter a number: "))
# if number > 0:
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# elif number == 0:
#     print("Zero")
# else:
#     print("Negitive")                


# 9. Driving Eligibility
# age = int(input("Enter your age: "))
# license = input("Do you have license ? (yes,no): ")
# if age > 18:
#     if license.lower() == "yes":
#         print("You are eligible to drive a vehicle")
#     else:
#         print("You need a license to drive a vehicle")    
# else:
#     print("You are not eligible to drive a car")        


# 10. Voting Eligibility
# age = int(input("Enter your age: "))
# citizen = input("You are citizen (yes/no): ")
# if age >= 18:
#     if citizen.lower() == "yes":
#         print("You are eligible to vote")
#     else:
#         print("You are not eligible to vote")
# else:
#     print("You are not eligible to vote")            


# 11. Ascending Order of Three Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# numbers = [a,b,c]
# numbers.sort()
# print(numbers)

# 12. Store Discount Calculator
# amount = float(input("Emter your amount: "))
# member = input("Are you a member (yes/no): ")
# if amount > 100:
#     if member.lower() == "yes":
#         discount = amount * 0.20
#     else:
#         discount = amount * 0.10    
# else:
#     discount = 0
# final_amount = amount - discount
# print("Discount amount = ",discount)
# print("Final Amount = ",final_amount)            

# 13. Vowel, Consonant or Neither
# ch = input("Enter a character: ")
# if ch.isalpha():
#     if ch.lower() in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonants") 
# else:
#     print("Neither")           


# 14. Book Recommendation
# age = int(input("Enter age: "))
# genre = input("Favorite genre (Mystery/Fantasy/Science Fiction): ")
# if genre.lower() == "mystery":
#     print("Recommended: Sherlock Holmes")
# elif genre.lower() == "fantasy":
#     print("Recommended: Harry Potter")
# elif genre.lower() == "science fiction":
#     print("Recommended: Dune")
# else:
#     print("No recommendation available")

# 15. Movie Ticket Price
# age = int(input("Enter your age: "))
# matinee = input("Matinee show (yes/no)? : ")
# if age > 12 or age < 65:
#     ticket = 8
# else:
#     ticket = 12
# if matinee.lower() == "yes":
#     ticket -= 2
# print("Ticket = ",ticket)            

# 16. Delivery Charge Calculator
# distance = float(input("Enter distance: "))
# amount = int(input("Enter your amount: "))
# if distance <= 5:
#     charge = 5
# elif distance >= 15:
#     charge = 20    
# else:
#     charge = 10
# if amount > 50:
#     charge -= 2        
# print("Delivery charge = ",charge)    

# 17. Employee Bonus Calculator
# rating = input("Enter rating (excellent/good/average): ")
# years = float(input("Enter years of Experience: "))
# if rating.lower() == "excellent":
#     bonous = 5000
# elif rating.lower() == "good":
#     bonous = 3000
# else:
#     bonous = 1000
# if years >= 5:
#     bonous += 2000
# print("Bonous Amount = ",bonous)            

# 18. Library Late Fee
# days = int(input("Number of days: "))
# book_type = input("Book type (regular / reference): ")
# if book_type.lower() == "regular":
#     fee = days * 1
# else:
#     fee = days * 2
# print("Total fee = ",fee)        


# 19. Scholarship Eligibility
# gpa = float(input("Enter GPA: "))
# activities = int(input("Enter number of activities: "))
# if gpa > 3.5:
#     if activities >= 3:
#         print("Scholarship Awarded")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")

# 20. Clothing Recommendation
# temp = float(input("Enter temperature (°C): "))
# rain = input("Is it raining? (yes/no): ")
# if temp < 15:
#     print("Wear a jacket.")
# elif temp < 25:
#     print("Wear light clothing.")
# else:
#     print("Wear summer clothes.")

# if rain.lower() == "yes":
#     print("Carry an umbrella.")

# 21. Movie Recommendation
# genre = input("Enter preferred genre (Action/Comedy/Drama): ")
# age = int(input("Enter age: "))
# if genre.lower() == "action":
#     if age >= 13:
#         print("Recommended: Avengers")
#     else:
#         print("Recommended: The Incredibles")

# elif genre.lower() == "comedy":
#     print("Recommended: Home Alone")

# elif genre.lower() == "drama":
#     print("Recommended: The Pursuit of Happyness")
# else:
#     print("No recommendation available")


# 22. Credit Card Application Approval
# credit_score = int(input("Enter your credit score: "))
# income = int(input("Enter your annual income: "))
# if credit_score >= 700 and income >= 300000:
#     print("Credit Card Application Approved")
# else:
#     print("Credit Card Application Rejected")

# 23. Vehicle Registration Based on Type and Emissions
# vehicle = input("Enter vehicle type (car/truck): ").lower()
# emissions = input("Enter emissions status (clean/high): ").lower()
# if vehicle == "car":
#     if emissions == "clean":
#         print("Registration fee: Rs.5000")
#     elif emissions == "high":
#         print("Registration fee: Rs.8000")
#     else:
#         print("Invalid emissions status")
# elif vehicle == "truck":
#     if emissions == "clean":
#         print("Registration fee: Rs.10000")
#     elif emissions == "high":
#         print("Registration fee: Rs.15000")
#     else:
#         print("Invalid emissions status")
# else:
#     print("Invalid vehicle type")