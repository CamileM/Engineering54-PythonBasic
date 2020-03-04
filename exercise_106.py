# Magic Number Game!

# I want you to use operators to equate to something

# TASK:
# User wants to be able to guess a number. Once number is guessed correct then user wins.
# I want to be able to guess a number and know if i got it correct or not.
# However, once number guess is incorrect the Computer wins.


# Assign number to a variable called magic_number - Camile's Method
magic_number = 26
user_input = int
count = 10

while count != 0: # TRUE
    user_input = int(input('Enter A Number\n'))
    print(count)
    print(' ')
    if user_input != magic_number:
        print('Sorry Pal :( but that is not the Magic Number. Try Again!')
        print('CLUE: Camile was Born on the _ _ th September')
        count = count - 1
        continue
    else:
        print('CONGRATULATIONS!!!, You Got The Magic Number :)')
        print('Camile was Born on the 26th September')
        break

# Felipe's Method with if statement:

#   magic_number = 10
#   count = 5
#   user_guess = input('What is your guess? \n')
#   print('Your response was correct', int(user_guess) == magic_number)

