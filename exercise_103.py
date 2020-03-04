# Define the following variables

# name, last_name, species, eye_color, hair_color

name = '    '
age = int
last_name = '   '
eye_colour = '  '
hair_colour = ' '

# Prompt user for input and Re-assign these
name = input('what new name would you like?')
last_name = input('what new last name would you like?')
age = int(input('How old are you?'))
eye_colour = input('What is your eye colour?')
hair_colour = input('What is your hair colour?')

# Print them back to the user as conversation

# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print(f'Hello {name}, Welcome to Sparta, your age is {age}, you have {eye_colour} eyes and you have {hair_colour} hair.' )

