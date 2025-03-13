# AUTHOR : MANAV
# TASK : TIP CALCULATOR

print("Welcome to the tip calculator!")

bill_amnt = float(input("Enter your total bill amount (in USD): $"))
tip_amnt = float(input("How much tip would you like to give in (%) (10/12/15): "))
people = float(input("Among how many people would you like to split the bill: "))

final_amnt = bill_amnt + ((tip_amnt/100)*bill_amnt)
indv_pay = final_amnt / people

print(f"Each person should pay: ${round(indv_pay, 2)}")