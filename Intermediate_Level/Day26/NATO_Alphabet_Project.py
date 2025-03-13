# Concept : List and Dictionary Comprehension

alpha_name = [
    "Attribute",
    "Boolean",
    "Compile",
    "Debug",
    "Exception",
    "ForeignKey",
    "Glitch",
    "Hacking",
    "Inheritance",
    "JavaScript",
    "Kotlin",
    "Library",
    "Mapping",
    "NodeJS",
    "OOPs",
    "Printf",
    "Query",
    "Recursion",
    "Syntax",
    "Tuple",
    "Udacity",
    "VisualStudio",
    "Workspace",
    "XML",
    "Youtube",
    "Zetta byte",
]

word = input("Enter the word to explain: ")

word_list = [letters.upper() for letters in word]

letter_explain = [
    name for letter in word_list for name in alpha_name if name[0] == letter
]

print(letter_explain)
