first_name = 'Lana'
last_name = 'Smith'
species = 'Human'
eye_color = 'Hazel'
hair_color = 'Black'

first_name = input('Enter a new name\n')
last_name = input('Enter a new last name\n')
species = input('Enter a new species\n')
eye_color = input('Enter a new eye color\n')
hair_color = input('Enter a new hair color\n')
age = int(input("Enter your age\n"))
print(f'Hello {first_name} {last_name}. Your species are {species}, your eye color is {eye_color}, and hair is {hair_color}')
print(f'Did I mention that you said your age is {age}. You were most likely born in ', 2020 - age)

# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age
# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>. This is <difference_y> later than <mom_name> who
# was on on <y_birth_mon>

first_name = input('Enter your name\n')
age = int(input('Enter your age\n'))
mother_name = input('Enter your mother\'s name\n')
mother_age = int(input('Enter your mother\'s age\n'))
print(f'Your name is {first_name}, and you are {age} born on the year of ', 2020 - age, '. This is a difference of ', mother_age -
      age, 'later than your mother ', mother_name, 'who was born on', 2020 - mother_age)
