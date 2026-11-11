# problems on (if else statements):

# 1. Check if a year is a leap year
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a Leap Year")    


# 2. Check if a character is a vowel or consonant
# ch = input("Enter a character: ")
# if 'a' <= ch <= 'z':
#     ch = chr(ord(ch) - 32)
#     if ch in 'AEIOU':
#         print("Vowel")
#     else: 
#         print("Consonant")
# else:
#     print("It is not a character")                


# b = ["a","e","i","o","u"]
# if a in b:
#     print("It is a vowel")
# else:
#     print("It is a consonant")    

# 3. Check if a year is a century year
# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     print("It is a century year")
# else:
#     print("It is not a century year")    

# 4. Check if a number is prime
# a = int(input("Enter a number: "))
# count = 0
# for i in range(1,a + 1):
#     if a % i == 0:
#         count += 1
# if count == 2:
#     print("prime Number")
# else:
#     print("Not a prime number")   


# 5. Check voting eligibility
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")    

# 6. Check if a number is positive or non-positive
# number = int(input("Enter a number: "))
# if number >= 0:
#     print("The number is Positive")
# else:
#     print("The number is Non-positive")    

# 7. Compare two numbers and print the largest
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(f"The number {num1} is largest")
# else:
#     print(f"The number {num2} is largest")    


# 8. Check if a character is a letter
# ch = input("Enter a character: ")
# if len(ch) == 1 and (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
#     print("It is a Character")
# else:
#     print("It is not a character")    


# 9. Find the smallest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if (a < b) and (a < c):
#     print("smallest number is: ",a)
# else:
#     if (b < a) and (b < c):
#         print("smallest is: ",b)    
#     else:
#         print("smallest is: ",c)    


# 10. Check if a string is a palindrome
# a = input("Enter a string: ").lower()
# if a[::-1] == a:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")  

# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# if s == rev:
#     print("The given string is a palindrome")
# else:
#     print("The given string is not a palindrome")

# x = int(input("Enter a number: "))
# rev = 0
# orginal = x
# while x > 0:
#     digit = x % 10
#     rev = rev * 10 + digit
#     x = x // 10
# if orginal == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome") 

# 10. largest
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if (a > b) and (a > c) and (a > d):
#     print("The Largest number is: ",a)
# else:
#     if (b > a) and (b > c) and (b > d):
#         print("The largest number is: ",b)    
#     else: 
#         if (c > a) and (c > b) and (c > d):
#             print("The largest number is: ",c)
#         else:
#             print("The largest number is: ",d)        


# 12. Determine the sign of the difference of two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# difference = a - b
# if difference < 0:
#     print("Difference is Negative")
# else:
#     if difference == 0:
#         print("Difference is Zero")
#     else:
#         print("The difference is Positive")  

# 13. Check leap year (alternative method)
# year = int(input("Enter a year: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# 14. Check if a number is a multiple of 7
# a = int(input("Enter a number: "))
# if a % 7 == 0:
#     print("Multiple of 7")
# else:
#     print("Not a Multiple of 7")

# 15. Find absolute value
# a = int(input("Enter a number: "))
# if a < 0:
#     b = -a
#     print(b)
# else:
#     print(a)    