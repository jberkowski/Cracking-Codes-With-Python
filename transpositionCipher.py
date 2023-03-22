'''Transposition Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This program encrypts/decrypts message using column cipher
and key given by the user.'''

import sys, math

try:
    import pyperclip
except ImportError:
    pass

def main():
    print('''Transposition Cipher, by Jakub Berkowski jakub.berkowski@gmail.com)

Use for encryption/decryption of message using column cipher,
with key given by user.''')

    print('Would you like to (e)ncrypt or (d)ecrypt a message? (or QUIT)')
    while True:  # Keep asking until user gives valid answer:
        mode = input('> ')
        if mode.upper().startswith('Q'):
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

    print('Please enter key value:')
    while True:  # Keep asking until user gives valid answer:
        key = input('> ')
        if not key.isdecimal():
            print('Please enter integer.')
        elif int(key) == 0:
            print('Key must be greater than 0.')
        else:
            key = int(key)
            break
    print()
    if mode == 'encrypt':
        printtext = runEncryption(message, key)
    else:
        printtext = runDecryption(message, key)

    # Print ciphertext:
    print(printtext + '|')  # In case space is the last char.
    print('Your message has been copied to clipboard.')
    pyperclip.copy(printtext)  # Copy ciphertext to clipboard.




def runEncryption(message, key):
    '''Encrypts message using given key.'''
    # Each element on below list is one column in the grid:
    ciphertext = [''] * key

    for column in range(key):  # Loop through each column in ciphertext:
        currentIndex = column

        # Keep looping until currentIndex exceeds the message length:
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            # Move to the next row in a column:
            currentIndex += key
    # Join all columns into one string:
    return ''.join(ciphertext)


def runDecryption(message, key):
    '''Decrypts message using given key.'''
    # Number of columns in our transposition grid:
    numberOfCols = int(math.ceil(len(message) / float(key)))
    # Number of rows in our transposition grid:
    numberOfRows = key
    # Number of "shaded boxes" in our last grid column:
    numOfShadedBoxes = (numberOfCols * numberOfRows) - len(message)

    # Each string in plaintext represents a column i the grid:
    plaintext = [''] * numberOfCols

    # The col and row variables point to where in the grid the next
    # character in ciphertext will go:
    column = 0
    row = 0
    
    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Point to the next column

        # If there are no more columns OR we are at a shaded box, go back
        # to the first column and the next row:
        if (column == numberOfCols) or (column == numberOfCols - 1 and
            row >= numberOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    # Join all rows into one string:
    return ''.join(plaintext)

# If program run (instead of imported), run main:
if __name__ == '__main__':
    main()