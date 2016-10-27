# Python progam for solving anagrams

import itertools, detectEnglish, pprint, sys

dict = open('dictionary.txt')
DICT = dict.readlines()
dict.close()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('Enter your scrambled letters:')
    scrambledLetters = input('> ')

    solvedWords = unscramble(scrambledLetters.upper())

    if solvedWords == []:
        print('No word matches found in the English dictionary.')
        sys.exit()

    
    print('Anagram solved')
    print()
    print('Here are your unscrambled words:')
    for word in solvedWords:
        print(word.title())

    print('--------')
    print('Re-run program?')
    h = input('> ')
    if h.strip().lower().startswith('y'):
        main()

def unscramble(scrambledLetters):
    solvedWords = []
    searchLetters = list(itertools.permutations(scrambledLetters, r=len(scrambledLetters)))
    
    for i in range(len(searchLetters)):
        word = ''.join(searchLetters[i])
        if detectEnglish.isEnglish(word):
            if word not in solvedWords:
                solvedWords.append(word)
    
    return solvedWords

if __name__ == "__main__":
    main()
