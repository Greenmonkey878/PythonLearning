print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Exercise==========One================

number = int(input("Which number do you want to check? "))

if number % 2 != 1:
    print("This is an even number")
else:
    print("This is an odd number")

#Exercise two
weight =int(input("How much do you weight? "))
height =int(input("How tall are you? "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
    if bmi < 25:
        print(f"Your BMI is {bmi} , you are normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slighty over weight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#Exercise=============three=============
year = int(input("Which year do you want to check"))

if year % 4  == 0:
    print("Leapyear")
    if year % 100 == 0:
        print("Leapyear")
    else: 
        print("not a leapyear")
        if year % 400 == 0:
          print("Leapyear")
        else:
            print("not a leapyear")
else:
    print("not a leapyear")

#Exercise=========four============
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

else:
    print(f"Your final bill is: ${bill}")