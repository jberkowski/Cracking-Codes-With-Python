'''Simple Substitution Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This programs encrypts and decrypts messages using a simple
substitution cipher, and a provided or random key.'''

import pyperclip, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def main():
    '''Main function for simpleSubCipher.'''
    print("Simple Substitution Cipher, by Jakub Berkowski", end = '')
    print(" jakub.berkowski@gmail.com")

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

    # Ask user to input key (or choose random for encryption):
    while True:  # Keep asking until user gives valid key:
        if mode == 'encryption':
            print('Please input key or write "random":')
            key = input('> ')
            if key.lower() == 'random':  # User chose random key.
                key = getRandomKey()
                break
            else:  # User entered own key.
                if keyIsValid(key):  # User entered a valid key:
                    break
                else:
                    print('Invalid key. Try again:')  # Invalid key.
        else:  # Enter key for decryption:
            print('Please input key:')
            key = input('> ')
            if keyIsValid(key):  # User entered a valid key:
                break
            else:
                print('Invalid key. Try again:')  # Invalid key.

    if mode == 'encryption':
        translated = runEncryption(message, key)
    else:
        translated = runDecryption(message, key)

    print(f'Your message after {mode} using key {key}:')
    print(translated)
    pyperclip.copy(translated)
    print('Message has been copied to clipboard.')


def keyIsValid(key):
    '''Check if key is valid.'''
    symbolsList = list(SYMBOLS)
    keyList = list(key)
    symbolsList.sort()
    keyList.sort()
    return keyList == symbolsList


def getRandomKey():
    '''Genreate random, valid key for encryption.'''
    key = list(SYMBOLS)
    random.shuffle(key)
    return ''.join(key)


def runEncryption(message, key):
    '''Wrapper function for encrytpion.'''
    translated = runTranslation(message, key, mode = 'encryption')
    return translated


def runDecryption(message, key):
    '''Wrapper function for decrytpion.'''
    translated = runTranslation(message, key, mode = 'decryption')
    return translated


def runTranslation(message, key, mode):
    '''Translates one character set to other using provided key.'''
    charsA = SYMBOLS
    charsB = key

    translated = ''

    # For decryption, character sets are swapped:
    if mode == 'decryption':
        charsA, charsB = charsB, charsA

    # Iterate through message, substituting letters from one set 
    # with other set:
    for symbol in message:
        if symbol.upper() in charsA:
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            elif symbol.islower():
                translated += charsB[symbolIndex].lower()
        else:
            # Just add symbols which are not on a list:
            translated += symbol
    return translated

# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()