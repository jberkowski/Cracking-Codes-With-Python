'''Vigenere Dictionary Hacker, by Jakub Berkowski jakub.berkowski@gmail.com
A dictionary attempt to hack message encrypted using Vigenere cipher
(provided that a key is a whole proper word).'''

import pyperclip

import detectEnglish, vigenereCipher, makeWordPatterns

def main():
    '''Main function for Vigenere Dictionary Hacker.'''
    print('Vigenere Dictionary Hacker, by', end = '')
    print('Jakub Berkowski, jakub.berkowski@gmail.com')

    print('Enter message for hacking: ')
    ciphertext = input('> ')
    print('Hacking...')

    plaintext = hackVigenereDictionary(ciphertext)

    if plaintext != None:
        print(f'Decryption succesful.')
        print(f'Decrypted message has been copied to clipboard:')
        print(plaintext)
        pyperclip.copy(plaintext)
    else:
        print('Decryption failed.')


def hackVigenereDictionary(ciphertext):
    '''Use dictionary method to hack encryption.'''
    # Create list of possible keys, using language dictionary:
    words = makeWordPatterns.loadDictionary()

    # Try decryption using every word from the list:
    for word in words:
        word = word.rstrip('\n')  # Remove the newline from the end.
        plaintext = vigenereCipher.runDecryption(ciphertext, word)

        # Check if result is a message in English:
        if detectEnglish.isEnglish(plaintext):
            print('Possible encryption hack:')
            print(f'Key: {word}')
            print(plaintext[:50])
            print("Type 'D' if you are done. Press Enter to continue.")
            answer = input('> ')
            if answer.upper() == 'D':
                return plaintext
    return None


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()