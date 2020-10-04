'''This is my first real progam to suggest me some random movies to watch.
Its a small program but taken me a whole day to write it'''

import os
import random

movies_list = []

pointer = ""

path = os.listdir('Desktop/Movies')


while True:
    pointer = input("> ").lower()
    for folder in path:
        if folder.isdigit():
            new_path = os.listdir(f'Desktop/Movies/{folder}')
            for movies in new_path:
                movies_list.append(f"{folder} : {movies}")           
    if pointer == 'show' or pointer == 's':
            movie = random.choice(movies_list)
            print(f'Lets watch:\n{movie}')         
    elif pointer == 'open':
        if movie.startswith('2019'):
            os.system('xdg-open Desktop/Movies/2019')
        elif movie.startswith('2020'):
            os.system('xdg-open Desktop/Movies/2020')
        elif movie.startswith('2018'):
            os.system('xdg-open Desktop/Movies/2018')
        elif movie.startswith('2017'):
            os.system('xdg-open Desktop/Movies/2017')
        else:
            os.system('xdg-open Desktop/Movies')
    elif pointer == 'help':
        print(f"My commands are:\n show - To get a random movie name \n open - To open the movie folder \n quit - To exit this program")
    elif pointer == 'quit' or pointer == 'q':
        print('This program is closed.Have a great time :)')
        break
    else:
        print(f"This is not a valid command.\nType 'help' to see my commands.")
    





          