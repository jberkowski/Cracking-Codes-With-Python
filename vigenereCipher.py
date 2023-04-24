'''Vigenere Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
Program for encryption/decryption of message, using Vigenere cipher
and key provided by user.'''

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    '''Main function for Vigenere Cipher.'''
    print('Vigenere Cipher, by Jakub Berkowski jakub.berkowski@gmail.com')

    # Ask user to input mode:
    print('Please choose (e)ncryption or (d)ecryption mode:')
    while True:  # Keep asking until user gives valid mode:
        mode = input('> ')
        if mode.lower().startswith('e'):
            mode = 'encryption'
            break
        elif mode.lower().startswith('d'):
            mode = 'decryption'
            break
        else:
            print('Please choose (e)ncryption or (d)ecryption mode:')

    # Ask user to input message:
    print(f'Please enter your message for {mode}:')
    message = input('> ')

    # Ask user to input key:
    print('Please input key:')
    while True:  # Keep asking until user gives valid key:
        key = input('> ')
        keyCorrect = True
        for symbol in key:
            if symbol.upper() not in LETTERS:
                keyCorrect = False  # Characters in key must be letters.
        if keyCorrect:
            break
        else:
            print('Incorrect key. Please try again:')

    if mode == 'encryption':
        translated = runEncryption(message, key)
    elif mode == 'decryption':
        translated = runDecryption(message, key)

    # Print results:
    print(f'Your message after {mode} using key {key}:')
    print(translated)
    pyperclip.copy(translated)
    print('Message has been copied to clipboard.')


def runEncryption(message, key):
    '''Wrapper function for encryption.'''
    translated = runTranslation(message, key, mode = 'encryption')
    return translated


def runDecryption(message, key):
    '''Wrapper function for decryption.'''
    translated = runTranslation(message, key, mode = 'decryption')
    return translated


def runTranslation(message, key, mode):
    '''Translates one character set to other using provided key.'''
    key = key.upper()
    keyIndex = 0  # We start reading the key from 1st character.
    translated = []
    for symbol in message:  # Loop through each symbol.
        if symbol.upper() in LETTERS:  # Translate symbols from the list.
            symbolIndex = LETTERS.find(symbol.upper())
            if mode == 'encryption':
                symbolIndex += LETTERS.find(key[keyIndex])
            elif mode == 'decryption':
                symbolIndex -= LETTERS.find(key[keyIndex])

            symbolIndex %= len(LETTERS)  # Handle the wrap-around.

            if symbol.isupper():
                translated.append(LETTERS[symbolIndex].upper())
            elif symbol.islower():
                translated.append(LETTERS[symbolIndex].lower())
            keyIndex += 1  # Jump to next letter in the key.
            
            # When we reach end of the key, start it over:
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)  # Else, add without translating.
    translated = ''.join(translated)
    return translated


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()