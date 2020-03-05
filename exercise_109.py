
# - You can vote and driversß
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'

age = int(input('How old are you? \n')) # Change age too see the different output
driver_licence = True # Change the boolean statement to either True or False

# while

if age >= 19 and driver_licence:
    print('You are old enough to drive and vote')
elif age >= 19 and driver_licence != True:
    print('You are old enough but you do not have a licence')
elif 19 < age >= 16:
    print('You cant legally drink but your friends can buy you your drinks')
elif age < 19 and driver_licence != True:
    print('You are joking, Right!. Not old enough and do not even own a licence')
else:
    print('You are too young. Go back to school KID!')


