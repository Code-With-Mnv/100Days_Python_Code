# Author  :  Manav
# Task    :  Re-write the same letter with different names from different files
# Concept :  Reading and Writing in Text Files using Pyton

names = []
letter = []

with open(file="./Input/Names/names.txt", mode="r") as name_file:
    names_str = name_file.read()
    names_list = names_str.split()
    for name in names_list:
        names.append(name)

with open(file="./Input/Letters/Letter_Text.txt", mode="r") as letter_file:
    letter_text = letter_file.readlines()
    for text in letter_text:
        letter.append(text)

send_to = input("To whom you want to send the letter: ")
send_to.capitalize()

letter.pop(0)
new_text = "Dear " + send_to
letter.insert(0, new_text)

with open(file=f"./Output/Ready_to_Send/Letter_to_{send_to}.txt", mode="w") as sending_file:
    sending_file.writelines(letter)
    print("\nLetter ready! Check the output directory!")



