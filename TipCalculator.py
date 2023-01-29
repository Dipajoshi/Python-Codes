print("Welcome to tip calculator!")
bill = float(input("What is the bill amount? $"))
tip = float(input("How  much percent tip would you want to give? "))
bill_with_tip_each_person = (bill + bill/100 * tip)/5
print(f"the amount of bill per person is ${round(bill_with_tip_each_person, 2)}" )

