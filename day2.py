num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") #gives error needs to be int

#type check
print(type(num_char))

#then change type storing into a new variable

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print(type(new_num_char))