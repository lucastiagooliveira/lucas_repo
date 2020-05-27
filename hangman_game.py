print(':::::::::::::::: HANGMAN GAME ::::::::::::::::::::::')

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

open_file = open('C:/Users/lucas/Documents/lucastiagooliveira/game.txt','r')
words = open_file.read().split()
open_file.close()

from random import choice
word = choice(words)
underlines = list('_ ' for i in range(len(word)))
underlines = ''.join(underlines)
chances = 0
print(word)
word = list(x for x in word)
word1 = list(0 for i in range(0, len(word)))
while chances < 5:
    print(underlines)
    p = str(input('Type a letter to complete the word: '))
    cont = 0
    for i in list(x for x in word):
        if i == p:
            underlines = list(i for i in underlines)
            underlines[cont] = p
            underlines = ''.join(underlines)
            word1[int(cont/2)] = p
        cont += 2
    if word1 == word:
        print('Congratulation! \n You got the word: ', ''.join(word))
        break
    chances += 1




