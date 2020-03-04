# For Loops

# Syntax

# for item in iterable:
    # block of code

import time

cool_cars = ['Skoda felicia fun', 'Fiat abarth the old one', 'Toyota corola', 'Fiat panda 4x4', 'Fiat multipla']

count = 0 # First number is being used and it needs to be initiated outside the for loop.

for car in cool_cars:
    print(count + 1, ' -', car)
    count += 1
    time.sleep(1)

# For Loops for Dictionaries

boris_dict = {'name': 'Boris', 'last_name': 'Johnson', 'phone':'07388940937','address':'10 Downing Street'}

for key in boris_dict:
    print(key)