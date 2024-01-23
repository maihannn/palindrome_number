# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 9: Check Palindrome Number

# Given number.

number = int(input("Enter a number: "))
original = number
reversed_number = 0
# Check if the given number is a palindrom number.

while (number>0):
    num = number % 10
    reversed_number = reversed_number * 10 + num
    number = number // 10

if original == reversed_number:
    print ("The given number "," '", original, "'", "is a palindrome number.")
else: 
    print ("The given number ", original, "is not a palindrome number.")