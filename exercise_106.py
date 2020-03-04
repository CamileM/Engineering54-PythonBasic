# Magic Number Game!

# I want you to use operators to equate to something

# TASK:
# User wants to be able to guess a number. Once number is guessed correct then user wins.
# I want to be able to guess a number and know if i got it correct or not.
# However, once number guess is incorrect the Computer wins.


# Assign number to a variable called magic_number - Camile's Method
magic_number = 26
user_input = int
COUNT = 10

while COUNT != 0:
    user_input = int(input('Enter A Number\n'))
    if user_input != magic_number:
        print(' ')
        print('Sorry Pal :( but that is not the Magic Number. Try Again!')
        print(' ')
        print('CLUE: Camile was Born on the _ _ th September')
        COUNT = COUNT - 1
        continue
    else:
        print('CONGRATULATIONS!!!, You Got The Magic Number :)')
        print('Camile was Born on the 26th September')
        break

# Felipe's Method


