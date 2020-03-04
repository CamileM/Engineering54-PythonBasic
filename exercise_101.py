# Practice String

# Welcome To Sparta - Class Exercise

# VERSION 1 SPECS

# Define a Variable name and assign a String with a name
first_name = '  '
last_name = '   '
age = int

# Prompt the user for input and ask the user for his/her name
# reasssign the original variable with this input
first_name = (input('Hello, what is your name?'))

# Use concatenation to print a welcome message and use method to format the name/input (remove white spaces)
print(input("What is your name?"))

# Version 2 - with interpolation

# Ask the user for a first name, save it in a variable
first_name = input('What is your first name?')

# Ask the user for a lst name, save it in a variable
last_name = input('What is your second name?')

# Calculate year of birth
age = int((input('How old are you?')))
# gather details on age and name

# Oh Woow <person>, you are <age> years old so you were born in <years>
print(f'Oh Woow {first_name} {last_name} ,  you are {age} years old. So you were born in {2020 - age}')


