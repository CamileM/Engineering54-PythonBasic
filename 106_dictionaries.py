# Dictionaries

# Work with key and value pairs
# Work like a real dictionary, you just lookup the information for the specgic key
# The big difference with list is they are organised with index and here we use keys

# We just make a list of cring_landlords, but we need more infromation. For instance, phone numbers and address.

# Syntax
dict_variable_name = {'key': 'value'}
boris_dict = {'name': 'Boris', 'last_name': 'Johnson', 'phone':'07388940937','address':'10 Downing Street'}

print(boris_dict)
print(type(boris_dict))

# Access one key value pair
# Follow the same principle of a list
last_name = boris_dict['last_name']
print(last_name)
# OR
print(boris_dict['last_name'])

# Change the value of a key pair
boris_dict['phone'] = '+7 749949973'
print(boris_dict['phone'])


# Assign a new key value
boris_dict['home_phone'] = '+44 74329467343'

boris_dict['number_budgets_pass'] = 0
print(boris_dict)

#
# boris_dict['number_budgets_pass'] = boris_dict['number_budgets_pass'] + 1

boris_dict['number_budgets_pass'] += 1
print(boris_dict)

# Get all keys
print(boris_dict.keys)

# Get all the values
print(boris_dict.values)