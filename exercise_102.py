# # Create a little program that ask the user for the following details:
#  - Name
#  - height
#  - favourite color
#  - a secret number

first_name = input("What is your name?")

height = int(input("How tall are you?"))

colour_choice = input("What is your favourite colour?")

secret_number = input("What is your secret number?")

print(f"So {first_name}, You are {height}, your favourite colour is {colour_choice} and your secret number is {secret_number}")

# Capture these inputs
# Print a tailored welcome message to the user

# print other details gathered, except the secret of course
print(f"So now I know your name is {first_name}, and that your favourite colour is {colour_choice}. I know your secret number is {secret_number} "
      f"but that will be our secret")
# hint, think about casting your data type.
