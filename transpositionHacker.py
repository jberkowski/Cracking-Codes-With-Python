'''Transposition Hacker, by Jakub Berkowski jakub.berkowski@gmail.com
Brute-force decryption of message, encrypted using transposition cipher.
Make sure to use correct language detection module.'''

import sys, os, time

import transpositionCipher, detectEnglish

def main():
    '''Brute-force decryption of message, 
    encrypted using transposition cipher.'''

    # Get the path to encrypted file:
    print('Please provide an Input File Name (or QUIT):')
    while True:  # Keep asking until user gives name of existing file:
        inputFilename = input('> ')
        if inputFilename.lower() == 'quit':
            print('Quitting...')
            sys.exit()
        elif not os.path.exists(inputFilename):
            print('File does not exist.')
        else:
            break  # Filename is valid, exit loop.

    # Create ciphertext from chosen file:
    fileObj = open(inputFilename)
    message = fileObj.read()
    fileObj.close()

    startTime = time.time()
    result = hackTransposition(message)
    endTime = time.time()
    totalTime = endTime - startTime

    if result:
        print(f'Decryption completed. Check results above. Time: {totalTime}s')
    else:
        print(f'Decryption failed: no valid kay found. Time: {totalTime}s')

def hackTransposition(message):
    '''Use all possible key to decrypt a message, then check if any
    of them is a valid english message.'''
    for key in range(1, len(message)):
        # Print % of checked keys:
        if key % 100 == 0:
            print(f'Trying key# {key}...')
        decrypted = transpositionCipher.runDecryption(message, key)
        if detectEnglish.isEnglish(decrypted):
            print(f'Key {key} is possible answer.', end = ' ')
            print(f'Saved result as decrypted.{key}.txt')
            # Create and output file with encrypted/decrypted message:
            outputFilename = 'decrypted.' + str(key) + '.txt'
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(decrypted)
            outputFileObj.close()
            # Ask user to check result and if continue:
            print('Continue decryption? (Y/N):')
            while True:  # Keep asking until answer is correct:
                answer = input('> ')
                if answer.lower().startswith('y'):
                    break
                else:
                    return True
    return False
# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()