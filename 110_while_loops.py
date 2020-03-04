# While loops

# syntax

# while <condition>:
    # run block of code
    # if <condition>:
        # break
import time

counter = 0

while counter <= 10:
    print(counter)
    print('This is cool')
    counter += 1

user_input = input('Do you want to play?\n')

# while user_input == 'yes' or user_input == 'y':...

# reserved words
# break - used to break the while loop
# continue - skips to the next iteration without running the following code/blocks

while True:
    user_input = input('Choose 1 for pancakes, 2 for cake, 3 to exit.. or just exit')

    if user_input == '!':
        print('pancakes!')
        print('plus what ever pancake logic you have')
    elif user_input == '2':
        print('Cakes!')
    elif 'exit' in user_input or user_input == 3:
        print('Goodbyee!')
        break
    else:
        print('USE YOUR NUMBERS ON KEYBOARD...')

    #random_num = 10
    # print('Welcome to our random game')
    # user_input = input('What is your guess?\n')
    #
    # if int(user_input == random_num):
    #     print('WELL DONE!')
    # else:
    #     print('Sorry, you where wrong!')
    #
    # user_input = input('Play Again?\n')