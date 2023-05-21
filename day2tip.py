#Tip calculator
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill?\n$")
total_bill_float = float(total_bill)

tip = input("What percentage tip would you like to give?\n%")
tip_float = float(tip)

number_of_people = input("How many people to split the bill?\n")
number_of_people_float = float(number_of_people)

tip_given = tip_float / 100
bill_split = total_bill_float * tip_given

each_person_pay =bill_split + total_bill_float / number_of_people_float
final_bill = round(each_person_pay, 2)
final_bill = "{:.2f}".format(each_person_pay)
result =(f"Each person should pay: ${final_bill}")
print(result)
