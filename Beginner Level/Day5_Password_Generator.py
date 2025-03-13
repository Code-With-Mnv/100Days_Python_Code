# Author : Code_with_Manav
# Task : Strong password generator

import random

# Greet the user
print("Welcome to the PyPassword Generator!")

# Ask user for password length
l = int(input("How long password do you want to generate: "))

# Ask for number of digits and symbols
d = int(input("Enter the number of digits you want in your password: "))
s = int(input("Enter the number of symbols you want in your password: "))
ltr = l - d - s

# Defining the valid dataset
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", ":", ";", "'", "<", ",", ">", ".", "?", "/"]

# Lenghts of the valid datasets
len_letter = len(letters)
len_digi = len(digits)
len_sym = len(symbols)

# Generate password
password = ""
for di in range (0, d):
    index = random.randint(0, len_digi-1)
    password += digits[index]

for si in range (0, s):
    index = random.randint(0, len_sym-1)
    password += symbols[index]

for li in range (0, ltr):
    index = random.randint(0, len_letter-1)
    password += letters[index]

# conert password string to list
password_list = []
for i in password:
   password_list.append(i)

# shuffle the list to make the password unpredictable
random.shuffle(password_list)

# convert list back to string and return the final password
final_password = ""
for i in password_list:
    final_password = final_password + i

print("Your generated password is:", final_password)