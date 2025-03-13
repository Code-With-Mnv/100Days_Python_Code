# Author : Code_with_Manav
# Task : Ceaser Cipher

#Creating the required dataset
small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o", "p", "q", "r", "s", "t", "u",
                 "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p",
                 "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

capital_letters =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#Defining the encrypting function
def ceasor_cipher(user_msg, shift):

    coded_msg = ""

    for char in user_msg:

        if char.islower():

            index = small_letters.index(char)
            new_index = index + shift
            char_coded = small_letters[new_index]
            coded_msg += char_coded

        elif char.isupper():

            index = capital_letters.index(char)
            new_index = index + shift
            char_coded = capital_letters[new_index]
            coded_msg += char_coded

        else:

            coded_msg += char

    return coded_msg

#Defining the decrypting function
def ceasor_dicipher(code_msg, shift):

    decoded_msg = ""

    for char in code_msg:

        if char.islower():

            index = small_letters.index(char)
            new_index = index - shift
            char_decoded = small_letters[new_index]
            decoded_msg += char_decoded

        elif char.isupper():

            index = capital_letters.index(char)
            new_index = index - shift
            char_decoded = capital_letters[new_index]
            decoded_msg += char_decoded

        else:

            decoded_msg += char

    return decoded_msg

#Greeting the user
print()
print("Welcome to CEASOR CIPHER Encrypting Program!")
print()

while True:

    #Taking the inputs
    print("Type 'ENCRYPT' for encrypting the data and 'DECRYPT' for decrypting!")
    tsk = input(">> ")

    if tsk.lower() == "encrypt":

        print()

        msg = input("Enter the data to be encrypted: ")
        shift = int(input("How much shift do you want: "))
        encrypted_msg = ceasor_cipher(msg, shift)             #Calling the function and encrypting

        print()

        print("Encoded data: ", encrypted_msg)                #Printing the coded data

    elif tsk.lower() == "decrypt":

        print()

        code_msg = input("Enter the coded data: ")
        shift = int(input("How much shift has been used: ")) 
        decrypted_msg = ceasor_dicipher(code_msg, shift)     #Calling the function and decrypting

        print()

        print("Decoded data: ", decrypted_msg)               #Printing the decoded data

    else:

        print()
        print("Errr... Please try again!")
        continue
    
    print()
    ch = input("Do you want to perform more tasks (Y/N): ")  #Asking for more tasks

    if ch in "yY":
        continue

    else:

        print()
        print("Thank You for using this program!")           #Ending the program
        break                                                #Breaking outta while loop
