# Write a Bizz and Zzuu Game Project

# As a user I, should be able prompted for a number, as the program will print all the number up to and including said

# number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it
#
# will calculate appropriately until you use the key word: 'pineapple'

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

import time

numb = ''

while numb != 'pineapple':

    numb = int(input('Please enter a number: '))

    for numb in range(1, 101):
        time.sleep(1)

        if numb == 'pineapple':
            break

        elif (numb % 3 == 0) and (numb % 5 == 0):
            print('Bizzuu')

        elif numb % 3 == 0:
            print('Bizz')

        elif numb % 5 == 0:
            print('Zzuu')

        else:
            print(numb)







