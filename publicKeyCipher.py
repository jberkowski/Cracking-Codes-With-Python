# Public Key Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Changes by Jakub Berkowski jakub.berkowski@gmail.com

import os, sys, math

# The public and private keys for this program are created by
# the makePublicPrivateKeys.py program.
# This program must be run in the same folder as the key files.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,'
PUBKEYFILE = 'j_berkowski_pubkey.txt'
PRIVKEYFILE = 'j_berkowski_privkey.txt'

def main():
    '''Runs a test that encrypts a message to a file or decrypts a 
    message from a file.'''
    # Make user choose encryption or decryption mode:
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

    if mode == 'encryption':
        print('Please provide an Output File Name:')
        while True:
            outputFile = input('> ')
            if os.path.exists(outputFile):  # Check if no overwrite:
                print(f'Do you want to overwrite existing {outputFile}? (Y/N):')
                overwrite = input('> ')
                if overwrite.lower().startswith('y'):
                    break
                else:
                    print('Please provide an Output File name:')
            else:
                break  # Filename is valid, exit loop.
        print('Please input message:')
        message = input('> ')
        print(f'Encrypting and writing to {outputFile}...')
        encryptedText = encryptAndWriteToFile(outputFile, PUBKEYFILE, message)

        print('Encrypted text:')
        print(encryptedText)

    elif mode == 'decryption':
        print('Please provide an Input File Name:')
        while True:
            inputFile = input('> ')
            if os.path.exists(inputFile):  # Check if file exists:
                break
            else:
                print('File does not exist. Please provide an Input File Name:')
        print(f'Reading from {inputFile} and decrypting...')
        decryptedText = readFromFileAndDecrypt(inputFile, PRIVKEYFILE)

        print('Decrypted text:')
        print(decryptedText)


def getBlocksFromText(message, blockSize):
    '''Converts a string message to a list of block integers.'''
    for character in message:
        if character not in SYMBOLS:
            print('ERROR: The symbol set does not have ', end = '')
            print(f'the "{character}" character.')
            sys.exit()
    blockInts = []
    for blockStart in range(0, len(message), blockSize):
        # Calculate the block integer for this block of text:
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(message))):
            a = SYMBOLS.index(message[i])
            b = len(SYMBOLS)
            c = i % blockSize
            blockInt +=  a * b ** c
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize):
    '''Converts a list of block integers into a string message.
    Requires messageLength for correct conversion of the last block.'''
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode to message string for the blockSize
                # characters from this block integer.
                charIndex = blockInt // (len(SYMBOLS) ** i)
                blockInt = blockInt % (len(SYMBOLS) ** i)
                blockMessage.insert(0, SYMBOLS[charIndex])
        message.extend(blockMessage)
    return ''.join(message)


def encryptMessage(message, key, blockSize):
    '''Converts the message string into a list of block integers, and 
    then encrypts each block integer. Pass the PUBLIC key to encrypt.'''
    encryptedBlocks = []
    n, e = key
    for block in getBlocksFromText(message, blockSize):
        # ciphertext = plaintext ** e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
    '''Decrypts a list of encrypted block integers into the original
    string. The messageLength is required to decrypt the last block.
    Pass the PRIVATE key to decrypt.'''
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ** d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFile):
    '''Given the filename of a file that contains a public or private
    key, returns the key as a (n,e) or (n,d) tuple.'''
    fo = open(keyFile)
    content = fo.read()
    keySize, n, EorD = content.split(',')
    return(int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(outputFile, keyFile, message, blockSize = None):
    '''Using a key from a keyFile, encrypts the message and saves it to 
    outputFile. Returns the encrypted message string.'''
    keySize, n, e = readKeyFile(keyFile)
    if blockSize == None:
        # If blockSize isn't given, assume the largest allowed:
        blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))

    # Check that keySize is large enough for the block size:
    if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('''ERROR: Block size is too large for the key and symbol
        set size. Did you specify the correct key and encrypted file?''')

    # Encrypt the message:
    encryptedBlocks = encryptMessage(message, (n,e), blockSize)

    # Convert the list of block integers to one string value:
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    # Write the encrypted string to the output file:
    encryptedContent = f'{len(message)}_{blockSize}_{encryptedContent}'

    fo = open(outputFile, 'w')
    fo.write(encryptedContent)
    fo.close()
    # Also, return the encrypted string:
    return encryptedContent


def readFromFileAndDecrypt(inputFile, keyFile):
    '''Using a key from a keyFile, reads an encrypted message from an
    inputFile and then decrypts it. Returns the decrypted message string.'''
    keySize, n, d = readKeyFile(keyFile)

    # Read the message length and the encrypted message from the file:
    fo = open(inputFile)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that keySize is large enough for the block size:
    if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('''ERROR: Block size is too large for the key and symbol
        set size. Did you specify the correct key and encrypted file?''')

    # Convert the encryptedMessage string into list of of block integers:
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    # Decrypt the encrypted block integers and convert them into
    # a string message:
    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()