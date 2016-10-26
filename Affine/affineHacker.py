# Affine Cipher Hacker

import pyperclip, affineCipher, detectEnglish, cryptoMath

SILENT_MODE = True

def main():
    myMessage = '''TTxWREA6JiVTKCcpRTxXNUU7JzFPKCY1Uz0mNEA8RjVUO1JYT itCIVQ5MiFRPTY1RDgyIU05NllPPFIhUA0KRzg3KUEoJlFMOTY9QT xCIUEoJlFBKCY5STtGJUwoJjVOKCYtWThGNVI4ViVNPCJgUiwjJF UNCmA='''
    
    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        print('Copying hacked message to clipboard: ')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print ('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' %(key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key: %s' %(key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking: \n')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If affineHacker.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
