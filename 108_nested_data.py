# Nested Data Structure
import time

weird_land_lord_1 = {'name': 'Boris', 'phone':'07388940937','address_of_rent':'10 Chelsea Street', 'age': 55}

weird_land_lord_2= {'name': 'John', 'phone':'+44 6715086674','address_of_rent':'67 Brixton Hill', 'age': 28}


nested_dictionary =  {'Boris' : weird_land_lord_1, 'John': weird_land_lord_2}

print(nested_dictionary.keys())

for keys in nested_dictionary:
    print(keys)
    data_nested = nested_dictionary[keys]
    print(data_nested)
    print(type(data_nested))
    print(data_nested.keys)
    print(data_nested['name'])
    print(data_nested['address_of_rent'])
    time.sleep(1)

nest_list = [[1, 2, 3], [4, 5, 6]]
print(nest_list[0])
print(nest_list[1])
print(nest_list[1][0])

for data in nest_list:
    print(data)
    breakpoint()
    for num in data:
        print(num * 20)


