num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") #gives error needs to be int

#type check
print(type(num_char))

#then change type storing into a new variable

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print(type(new_num_char))

#Exercise one========================================
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))

num_one = two_digit_number[0] #num_one = int(two_digit_number[0])
num_two = two_digit_number[1] #num_two =  int(two_digit_number[1])

result = int(num_one) + int(num_two) #result = num_one + num_two
print(result)

#Exercise two========================================
weight = input("How much do you weigh in pounds? ")
height = input("How tall are you in inches? ")

weight = float(weight) # convert weight to a floating-point number
height = float(height) # convert height to a floating-point number

bmi = weight * 703 / height ** 2
bmi_int = int(bmi) # convert bmi to an integer
print (bmi_int)

#Exercise three=====================================
age = (input("What is your current age?\n"))

age_int = int(age)
years_remaining = 90 - age_int
days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")





