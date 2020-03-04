# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.

user_input = input('Which movie ratings would you like to view? \n')

movie_ratings = {'universal':'everyone can watch',
                 'pg': 'General viewing, but some scenes may be unsuitable for young children',
                 '12':'Films classified 12A and contain material that is not generally suitable for children aged under 12.',
                 '15': 'No one younger than 15 may see a 15 film in a cinema.',
                 '18':'No one younger than 18 may see an 18 film in a cinema.'}

if user_input == 'universal':
    print(movie_ratings['universal'])
elif user_input == 'pg':
    print(movie_ratings['pg'])
elif user_input == '12':
    print(movie_ratings['12'])
elif user_input == '15':
    print(movie_ratings['15'])
elif user_input == '18':
    print(movie_ratings['18'])
else:
    print('Sorry, I did not catch that. Have a good day')