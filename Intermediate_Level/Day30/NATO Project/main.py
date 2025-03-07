import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
except KeyError:
    print("Error! only letters/words are allowed in the input!")
