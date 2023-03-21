"""Caesar Cracker, by Jakub Berkowski jakub.berkowski@gmail.com
Program that does a brute-force attack against Caesar-ciphered
message. Learn more at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
Code based on project from "Big Book of Small Python Projects."

Tags: tiny, math, cryptography, beginner."""

# Encrypted symbols list:
# (This list must be identical as list in encrypting program!)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

print("Caesar Cracker, by Jakub Berkowski jakub.berkowski@gmail.com")
print("Enter the message encrypted with Caesar cipher:")
message = input('> ')

for key in range(len(SYMBOLS)):
    translated = ''  # Create empty string for translated message.
    for symbol in message:
        if symbol in SYMBOLS:  # Handle encrypted symbols:
            num = SYMBOLS.find(symbol)  # Find symbol number on the list.
            num -= key

            # Handle the wrap-around if num < 0:
            if num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]
        else:  # Handle non-encrypted symbols:
            translated += symbol

    # Print results of each try:
    print(f'Key #{key}: {translated}')