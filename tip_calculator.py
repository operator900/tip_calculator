print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?: \n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: \n"))
amount_ppl = int(input("How many people to split the bill?: \n"))

total_bill = tip / 100 * bill + bill
split_bill = total_bill / amount_ppl
split_bill = "{:.2f}".format(round(split_bill, 2))

print(f"Each person should pay: ${split_bill} ")