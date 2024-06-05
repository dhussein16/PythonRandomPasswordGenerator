# ________________________________________________________
# PROJECT DESCRIPTION
# This is a python project in order to practice and brush up on Python skills
# by creating a Random Password Generator project. By using the ASCII
# values of alphanumeric symbols, we are able to generate different passwords
# every time. The rules used to create these passwords is as follows
# * The passwords are 8 characters long
# * Passwords will have two uppercase and two lowercase letters
# * Passwords will have 2 digits from 0 - 9
# * Two punctuation signs such as !, ?, " , #, or something else
# ________________________________________________________
import random
from random import shuffle

# generate a random ASCII value for two uppercase letters
# two lowercase letters, two numbers, and two puntuation signs, which
# only considered that within the ASCII values of 33-64
firstUpperCaseLetter = chr(random.randint(65, 90)) 
secondUpperCaseLetter = chr(random.randint(65, 90))

firstLowerCaseLetter = chr(random.randint(97, 122))
secondLowerCaseLetter = chr(random.randint(97, 122))

firstDigit = chr(random.randint(0,9))
secondDigit = chr(random.randint(0,9))

# ISSUES HERE: for some reason, it sometimes generates an integer instead of the punctuation. Why is that?
firstPuncSymbol = chr(random.randint(33,64))
secondPuncSymbol = chr(random.randint(33,64))

# Print Checkers to see if it is the appropriate values for every char
# print(firstUpperCaseLetter + " " + secondUpperCaseLetter)
# print(firstLowerCaseLetter + " " + secondLowerCaseLetter)
# print(str(firstDigit) + " " + str(secondDigit))
# print(str(firstPuncSymbol) + " " + str(secondPuncSymbol))

# put all the generated characters into a list
passwordChars = [
    firstUpperCaseLetter, secondUpperCaseLetter, 
    firstLowerCaseLetter, secondLowerCaseLetter, 
    firstDigit, secondDigit, 
    firstPuncSymbol, secondPuncSymbol
]

# Shuffle the list to ensure randomness
shuffle(passwordChars)

# Join the list into a single string
password = ''.join(passwordChars)

print(password)


