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
underlines = ('_ ' for i in range(len(word)))
print(''.join(underlines))

# w = input('Type one letter for complete the word:')



