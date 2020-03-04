# Strings
# Text and characters
# Syntax
# " " AND ' '

# Define  a string
my_string = "Hey, I am cool String :)"
print(my_string)

# check its type
print(type(my_string))
# Concatenation

joint_string = my_string + "This is another String"
print(joint_string)

# Example 2
name = 'Camile'
welcome_text = "Welcome To SPARTAAA (300)"
print(welcome_text, name) #overloading the print method

# interpolation
# inserting a string inside another string
# or running python inside a string
print(" ")
print(f'WELCOME {name} TO CLASS, WE ARE CONTESTED TERRAIN')
print('WELCOME {} TO CLASS, WE ARE CONTESTED TERRAIN'.format(name))

print(" ")

# useful methods
# are like functions but belong to a specific data type
# for example, it would not make sense to try to capitalise integers
example_long_str = "    HELLO, This is a VERY badLY formaTTED texT? "

# Remove trailling white space
print(example_long_str.strip())

# Make it lower case
print(example_long_str.strip().lower())

# Make it upper case
print(example_long_str.strip().upper())

# Make the first character of a word capital.
print(example_long_str.strip().title())

# Make the first character of each word
# Make the first character of each word Capitalized
print(example_long_str.strip().capitalize())

# Change the '?' into an '!'
# Make the first character of each word Capitalized
print(example_long_str.strip().replace('?', '!'))

# Chain some methods and:
    # remove trailling white spaces
    # make it nicely formated

# Make the first character of each word Capitalized
print(example_long_str.strip().capitalize().replace('?', '!').replace('badly','well'))


# Create a list with individual words
# split() --> list
# Make the first character of each word Capitalized
print(example_long_str.split())


