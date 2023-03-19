"""My Caesar Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
Caesar Cipher is a simple shift cipher that uses addition and subtraction
for encryption and decryption of a message.
Find out more at https://en.wikipedia.org/wiki/Caesar_cipher
This code bases on a project from "Big Book of Small Python Projects".

Tags: cryptography, math, short"""

try:
    import pyperclip  # pyperclip copies output to the clipboard.
except ImportError:
    pass  # If there is no pyperclip, do nothing. It is not mandatory.

# Only below symbols will be encrypted. You can add/remove as you wish.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("""My Caesar Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This program will let you encrypt and decrypt message using
Caesar Cipher. This cipher simply shifts all the symbols in a message
by given value, called 'key'. For example, if key = 3, A is encrypted
as D, B as E, and so on.\n""")

# First, ask user whether he likes to encrypt or decrypt a message:
while True:  # Keep asking until user responses with 'e' or 'd'.
    print('Would you like to (e)ncrypt or (d)ecrypt?')
    response = input('> ')
    response = response.lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Please answer with 'e' or 'd'.")

# Ask user for a key:
while True:  # Keep asking until user responses with correct key length.
    print(f'Please input key value:')
    response = input('> ')
    if response.isdecimal():
        key = int(response)
        break
    else:
        print("Please enter correct key value.")

# Ask user for a message:
print(f'Please enter message to {mode}:')
message = input('> ')
message = message.upper()  # SYMBOLS only contains upper-case letters.

translated = ''  # Prepare empty string for translated symbols.

for symbol in message:
    if symbol in SYMBOLS:  # Encode/decode only symbols from the list.
        num = SYMBOLS.find(symbol)  # Find initial number of symbol.
        if mode == 'encrypt':
            num += key
        if mode == 'decrypt':
            num -= key

        # Handle num's < 0 or > than SYMBOL list:
        while num < 0 or num >= len(SYMBOLS):
            if num < 0:
                num += len(SYMBOLS)
            elif num >= len(SYMBOLS):
                num -= len(SYMBOLS)

        translated += SYMBOLS[num]
    else:  # Just copy other symbols.
        translated += symbol

# Display results:
print('Your {}ed message: '.format(mode))
print(translated)
print('Message copied to clipboard.')

try:
    pyperclip.copy(translated)  # Copy translated message to clipboard.
except:
    pass  # Do nothing.