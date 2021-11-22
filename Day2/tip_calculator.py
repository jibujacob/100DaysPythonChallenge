#Tip Calculator Task
print("Weclome to the Tip Calculator.")
bill=input("What was the total bill? $")
tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
users=input("How many people to split the bill? ")

total_bill = (float(bill) * (float(tip)/100)) +float(bill)
split_up = round(total_bill/float(users),2)
print(f"Each person should pay: {split_up}")
