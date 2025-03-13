import random

print("Welcome to the ROCK PAPER SCISSORS game!")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors.")

pch = int(input("Choice: "))
chr = ["Rock", "Paper", "Scissors"]
cch = random.randint(0, 2)

if chr[pch] == chr[cch]:
	print("You chose " + chr[pch] + ".")
	print("Computer chose " + chr[cch] + ".")
	print("It's a draw.")

elif (chr[pch] == "Rock" and chr[cch] == "Scissors") or (chr[pch] == "Paper" and chr[cch] == "Scissors") or (chr[pch] == "Scissors" and chr[cch] == "Rock"):
		print("You chose " + chr[pch] + ".")
		print("Computer chose " + chr[cch] + ".")
		print("You lose!")

elif (chr[cch] == "Rock" and chr[pch] == "Scissors") or (chr[cch] == "Paper" and chr[pch] == "Scissors") or (chr[cch] == "Scissors" and chr[pch] == "Rock"):
		print("You chose " + chr[pch] + ".")	
		print("Computer chose " + chr[cch] + ".")
		print("You lose!")

else:
	print("Invalid!")