'''Transposition File Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This program encrypts/decrypts entire text file, using
Transposition Cipher and a user-provided key.'''

import sys, os, time

from transpositionCipher import runEncryption, runDecryption

def main():
    '''This program imports a text file, and then runs encryption
    or decryption using Transposition Cipher. Key is provided by a user.'''
    print('Transposition File Cipher, by Jakub Berkowski', end = '')
    print(' jakub.berkowski@gmail.com', end = '\n\n')
    
    print('Please provide an Input File Name (or QUIT):')
    while True:  # Keep asking until user gives name of existing file:
        inputFilename = input('> ')
        if inputFilename.lower() == 'quit':
            print('Quitting...')
            sys.exit()
        elif not os.path.exists(inputFilename):
            print('File does not exist.')
        else:
            outputFilename = inputFilename[:-4] + '.crypted.txt'
            if os.path.exists(outputFilename):  # Check if no overwrite:
                print(f'Do you want to overwrite existing {outputFilename}? (Y/N):')
                overwrite = input('> ')
                if overwrite.lower().startswith('y'):
                    break
                else:
                    print('Quitting...')
                    sys.exit()
            else:
                break  # Filename is valid, exit loop.

    # Create plaintext from chosen file:
    fileObj = open(inputFilename)
    message = fileObj.read()
    fileObj.close()

    print('Do you want to (e)ncrypt od (d)ecrypt?')
    while True:  # Keep asking until user chooses valid mode:
        mode = input('> ')
        if mode.lower().startswith('e'):
            mode = 'encryption'
            break
        elif mode.lower().startswith('d'):
            mode = 'decryption'
            break
        else:
            print('Please choose (e)ncryption or (d)ecryption mode.')

    print(f'Enter the key for {mode}:')
    while True:  # Keep asking until user gives valid key:
        key = input('> ')
        if not key.isdecimal():
            print('Key must be an integer bigger than 0.')
        elif int(key) == 0:
            print('Key must be an integer bigger than 0.')
        else:
            key = int(key)
            break

    # Check the starting time of operation:
    startTime = time.time()
    # Encrypt/decrypt file:
    translated = ''
    if mode == 'encryption':
        translated = runEncryption(message, key)
    else:
        translated = runDecryption(message, key)
    # Calculate how long the operation took:
    totalTime = round(time.time() - startTime, 2)

    # Create and output file with encrypted/decrypted message:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    # Show the results of operation:
    print(f'{mode.title()} completed in {totalTime} seconds.')
    print(f'Saved as {outputFilename}.')


# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()