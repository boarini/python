print("Welcome to the tip calculator!")
bill_total = float(input("Whats was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people  = int(input("How many people are spliting the bill? ")) 
per_person_pay = bill_total * (tip_percent/100 + 1) / number_of_people
final_amount = round(per_person_pay,  2)
print(f"Each person should pay: ${final_amount}")