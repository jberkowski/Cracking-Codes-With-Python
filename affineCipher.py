'''Affine Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This program enables encryption/decryption of message using the 
affine cipher and key provided by user.'''

import pyperclip, random, sys

from cryptomath import gcd, findModInverse

# Set up constants:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!.'

def main():
    print('Affine Cipher, by Jakub Berkowski jakub.berkowski@gmail.com')
    
    # Choose mode:
    print('Would you like to (e)ncrypt or (d)ecrypt a message? (or QUIT)')
    while True:  # Keep asking until user gives valid answer:
        mode = input('> ')
        if mode.lower().startswith('q'):
            sys.exit()
        elif mode.lower().startswith('e'):
            mode = 'encrypt'
            break
        elif mode.lower().startswith('d'):
            mode = 'decrypt'
            break
        else:
            print('Please choose "encrypt", "decrypt" or QUIT:')
    print()

    print(f'Write down your message for {mode}ion:')
    message = input('> ')

    if mode == 'encrypt':
        translated = runEncryption(message)
    elif mode == 'decrypt':
        print('Please enter decryption key:')
        while True:  # Keep asking until user gives valid key:
            key = input('> ')
            if key.isdecimal():
                key = int(key)
                break
            else:
                print('Please enter valid key.')
        translated = runDecryption(message, key)

    # Print result and copy it to clipboard:
    print(f'Your {mode}ed message has been copied to clipboard:')        
    print(translated)
    pyperclip.copy(translated)

def runEncryption(message):
    '''Encrypts message provided by user.'''
    keyA, keyB = getKey()
    translated = ''  # Prepare empty string for processed message.

    for symbol in message:
        if symbol in SYMBOLS:  # Encrypt symbols from the SYMBOLS list.
            symbolIndex = SYMBOLS.find(symbol)
            index = (symbolIndex * keyA + keyB) % len(SYMBOLS)
            translated += SYMBOLS[index]
        else:  # Just append other symbols.
            translated += symbol
    return(translated)


def runDecryption(message, key):
    '''Decrypts message based on key provided by user.'''
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)

    invertedKeyA = findModInverse(keyA, len(SYMBOLS))
    translated = ''  # Prepare empty string for processed message.

    for symbol in message:
        if symbol in SYMBOLS:  # Encrypt symbols from the SYMBOLS list.
            symbolIndex = SYMBOLS.find(symbol)
            index = ((symbolIndex - keyB) * invertedKeyA) % len(SYMBOLS)
            translated += SYMBOLS[index]
        else:  # Just append other symbols.
            translated += symbol
    return translated


def getKey():
    '''Validates user key or provides random one.'''
    print('Please enter encryption key, or choose (r)andom:')
    while True:  # Keep asking until user gives valid key:
        key = input('> ')
        if key.isdecimal():
            key = int(key)
            keyA = key // len(SYMBOLS)
            keyB = key % len(SYMBOLS)
            if keyA == 1:
                print('Cipher is weak if key A is 1. Choose another key.')
            elif keyB == 0:
                print('Cipher is weak if key B is 0. Choose another key.')
            elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
                print(f'''Key A must be greater than 0. 
                    Key B must be between 0 and {len(SYMBOLS) -1}.''')
                print('Choose another key.')
            elif gcd(keyA, len(SYMBOLS)) != 1:
                print('Key A and the symbol set size must be relatively prime.')
                print('Choose another key.')
            else:
                break
        elif key.lower().startswith('r'):
            keyA, keyB = getRandomKey()
            break
        else:
            print('Please enter encryption key, or choose (r)andom.')
    return (keyA, keyB)


def getRandomKey():
    '''Chooses a random valid key for encryption.'''
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            print('Used key:', keyA * len(SYMBOLS) + keyB)
            return (keyA, keyB)


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()