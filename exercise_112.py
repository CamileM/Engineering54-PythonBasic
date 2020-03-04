# Write a Bizz and Zzuu Game Project

# As a user I, should be able prompted for a number, as the program will print all the number up to and including said

# number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it
#
# will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

numb = ''

while numb != 'exit':

    numb = input('Please enter a number: ')
    if numb == 'exit':
        break

    elif (int(numb) % 3 and int(numb) % 5) == 0:
        print('Bizzuu')

    elif int(numb) % 3 == 0:
        print('Bizz')

    elif int(numb) % 5 == 0:
        print('Zzuu')
    else:
        print()





