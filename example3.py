# problems on if-elif-else statements:

# 1. Celsius ↔ Fahrenheit Converter
# choice = input(" C to F or F to C: ").upper()
# if choice == "C":
#     c = float(input("Enter Celsius: "))
#     f = (c * 9/5) + 32
#     print("Fahrenheit =",f)
# elif choice == "F":
#     f = float(input("Enter fahrenheit: "))
#     c = (f - 32) * 5/9
#     print("Celsius =",c)    
# else:
#     print("Invalid Choice")    

# 2. Simple Calculator:

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# option = input("Enter operation (+,-,/,*): ")
# if option == "+":
#     print(a + b)
# elif option == "-":
#     print(a - b)    
# elif option == "/":
#     print(a / b)
# elif option == "*":
#     print(a * b)
# else:
#     print("Invalid operator")  


# 3. Guess the Number Game
# import random
# num = random.randint(1,10)
# while True:
#     guess = int(input("Guess a number (1-10): "))
#     if guess == num:
#         print("Correct Guess!")
#         break
    
#     elif guess > num:
#         print("Too High")
#     else: 
#         print("Too Low")        


# 4. Password Strength Checker
# password = input("Enter your Password: ")
# if len(password) <= 5:
#     print("Weak Password")
# elif len(password) <= 10:
#     print("Medium password")
# else:
#     print("Strong password")        



# 5. Final Price After Discount
# amount = float(input("Enter your amount: "))

# if amount >= 10000:
#     discount = 20
# elif amount >= 5000:
#     discount = 10
# else:
#     discount = 5
# total_amount = amount - ((amount * discount)/ 100)
# print("The Total Amount: ",total_amount)    


# 6. ATM Machine
# balance = 10000
# print("1. Check Balance")
# print("2. Withdraw Amount")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print("Balace =",balance)
# elif choice == 2:
#     amount = float(input("Enter amount: "))
#     if amount <= balance:
#         balance = balance - amount
#         print("Withdraw successfully!")
#         print("Remaing Amount: ",balance)
#     else:
#         print("Insufficent Amount")
# else:
#     print("Invalid Choice")


# 7. Greeting Based on Time
# hour = int(input("Enter hour (0-23): "))
# if hour < 0 or hour > 23:
#     print("Invalid Hour")
# elif hour < 12:
#     print("Good Morning!")
# elif hour < 17:
#     print("Good Afternoon!")
# elif hour < 21:
#     print("Good Evening")
# else:
#     print("Good Night")          


# 8. Discount Coupon Program
# amount = float(input("Enter amount: "))
# coupon = input("Enter Coupon code: ").upper()
# if coupon == "SAVE10":
#     amount = amount - (amount * 0.10)
# elif coupon == "Save5":
#     amount = amount - (amount * 0.5)
# else:
#     print("Invalid Coupon")
# print("Total Amount: ",amount)    

# 9. Grade Calculator with Validation
# marks = int(input("Enter your marks: "))
# if marks < 0 or marks > 100:
#     print("Invalid Marks")
# elif marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 50:
#     print("Grade D")        
# elif marks >= 40:
#     print("Grade E")
# else:
#     print("Fail")                


# 10. Menu Driven Calculator
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Exponential")

# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print(a + b)
# elif choice == 2:
#     print(a - b) 
# elif choice == 3:
#     print(a * b)
# elif choice == 4:
#     print(a / b)
# elif choice == 5:
#     print(a ** b)
# else: 
#     print("Invalid choice")                   


# 11. Number of Days in given month
# month = int(input("Enter month number (1-12): "))
# if month < 0 or month > 12:
#     print("Invalid month")
# elif month in [1,3,5,7,8,10,12]:
#     print("31 Days")
# elif month in [4,6,9,11]:
#     print("30 Days")
# else:
#     print("28 or 29 Days")            