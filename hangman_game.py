print(':::::::::::::::: HANGMAN GAME ::::::::::::::::::::::')

from random import choice
from clear_screen import clear

#Definiton of the list of caracters with will be used for represent the Hangman
status = ['''   

    =========
    |       |
            |
            |
            |
            |
         ======''',
'''

    =========
    |       |
    O	    |
            |
            |
            |
         ======''',
'''

    =========
    |       |
    O	    |
    |	    |
            |
            |
         ======''',

'''

    =========
    |       |
    O	    |
   /|	    |
            |
            |
         ======''',
'''

    =========
    |       |
    O	    |
   /|\	    |
            |
            |
         ======''',

'''

    =========
    |       |
    O	    |
   /|\	    |
   / 	    |
            |
         ======''',

'''

    =========
    |       |
    O	    |
   /|\	    |
   / \ 	    |
            |
         ======'''

]
def print_hangman(chances):
    print('\n', status[chances], '\n')

open_file = open('C:/Users/lucas/Documents/lucastiagooliveira/game.txt','r')
words = open_file.read().split()
open_file.close()
word = choice(words)
underlines = list('_ ' for i in range(len(word)))
underlines = ''.join(underlines)
chances = 0
print(word)
word = list(x for x in word)
word1 = list(0 for i in range(0, len(word)))

while chances <= 6:
    clear()
    print_hangman(chances)
    print(underlines)
    p = str(input('Type a letter to complete the word: '))
    cont = 0
    if p in word:
        for i in list(x for x in word):
            if i == p:
                underlines = list(i for i in underlines)
                underlines[cont] = p
                underlines = ''.join(underlines)
                word1[int(cont/2)] = p
            cont += 2
    else:
        chances += 1
    if word1 == word:
        print('Congratulation! \n You got the word: ', ''.join(word).upper())
        break
    elif chances == 6:
        print('\n \n You lose fella! \n \n The correct word is:', ''.join(word).upper())
        print(print_hangman(6))
        break







