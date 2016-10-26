import pyperclip
from random import randint

# the string to be encrypted / decrypted / hacked
message = input("Please enter text: ")

# every possible symbol that can be encrypted
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'

# tells the program to encrypt or decrypt
mode = input("Would you like to 'encrypt', 'decrypt', or 'hack'? ") # set to 'encrypt' or 'decrypt' or 'hack'

if mode == 'encrypt':
    # the encryption/decryption key
    key = randint(0, len(LETTERS))

    # stores the encrypted/decrypted form of the message
    translated = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted or decrypted number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num + int(key)
            


            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)


            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]


        else:
            # just add the symbol without encrypting or decrypting
            translated = translated + symbol
    # print the encrypted/decrypted string to the screen
    print(translated)

    # copy the encrypted/decrypted string to the clipboard
    pyperclip.copy(translated)
    
elif mode == 'decrypt':
    key = input("Please enter your key: ")

    # stores the encrypted/decrypted form of the message
    translated = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted or decrypted number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - int(key)


            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)


            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]


        else:
            # just add the symbol without encrypting or decrypting
            translated = translated + symbol
    # print the encrypted/decrypted string to the screen
    print(translated)

    # copy the encrypted/decrypted string to the clipboard
    pyperclip.copy(translated)
    
elif mode == 'hack':
    a = input("26 or 96 key base? ")
    if a == '26':
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # loop through every possible key
    for key in range(len(LETTERS)):

        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is the same as the original Caesar program:

        # run the encryption/decryption code on each symbol in the message
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) # get the number of the symbol
                num = num - key

                # handle the wrap-around if num is 26 or larger or less than 0
                if num < 0:
                    num = num + len(LETTERS)
                elif num >= len(LETTERS):
                    num = num - len(LETTERS)


                # add number's symbol at the end of translated
                translated = translated + LETTERS[num]

            else:
                # just add the symbol without encrypting/decrypting
                translated = translated + symbol

        # display the current key being tested, along with its decryption
        print ('Key #%s: %s \n' %(key, translated))

