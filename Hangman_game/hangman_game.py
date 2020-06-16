from random import choice

# Definiton of the list of caracters with will be used for represent the Hangman
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


def print_hangman(chances):  # function for print the hangman relative your errors
    print('\n:::::::::::::::: HANGMAN GAME ::::::::::::::::::::::\n', status[chances], '\n')


open_file = open('C:/Users/lucas/Documents/lucastiagooliveira/game.txt', 'r')  # open the .txt file to get the words
words = open_file.read().split()  # read that file and split the words
open_file.close()  # close the file
word = choice(words)  # choice a random word
underlines = list('_ ' for i in range(len(word)))  # make a list with underlines to print
underlines = ''.join(underlines)  # join that list for one string
chances = 0  # varible to count the quantity has tried

word = list(x for x in word)  # sepation of letters in the choiced word
word1 = list(0 for i in range(0, len(word)))
missed_letter = []  # List with the wrong letters
accept_letter = []  # List with the right letters

while chances <= 6:
    print_hangman(chances)
    print(underlines)
    p = str(input('\nType a letter to complete the word: '))
    while (p in missed_letter) or (p in accept_letter):
        p = str(input('\nType a letter to complete the word: '))
    cont = 0
    if p in word:
        for i in list(x for x in word):
            if i == p:
                underlines = list(i for i in underlines)
                underlines[cont] = p
                underlines = ''.join(underlines)
                word1[int(cont / 2)] = p
                accept_letter.append(p)
            cont += 2
    else:
        chances += 1
        missed_letter.append(p)
    if word1 == word:
        print('Congratulation! \n You got the word: ', ''.join(word).upper())
        break
    elif chances == 6:
        print('\n \n You lose fella! \n \n The correct word is:', ''.join(word).upper())
        print(print_hangman(6))
        break
