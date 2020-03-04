# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end

story_1 = {'start': 'In the beginning...', 'middle': 'Then the unthinkable happened...', 'end': 'The End'}

#2 - Print the entire dictionary
print(story_1)

#3 - Print the type of your dictionary
print(type(story_1))

#4 - Print only the keys
print(story_1.keys)

#4 - print only the values
print(story_1.values)

#5 - print the individual values using the keys (individually, lots of print commands)
print(story_1['start'])
print(story_1['middle'])
print(story_1['end'])

#6 - Now let's add a new key:value pair
    # 'hero': yourSuperHero
story_1['hero'] = 'Messi'
print(story_1)