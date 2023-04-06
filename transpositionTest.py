'''Transposition Test, by Jakub Berkowski jakub.berkowski@gmail.com
This program runs multiple encryption/decryption tests to check
if Transposition Cipher program works properly.'''

import random, sys

from transpositionCipher import runEncryption, runDecryption

def main():
    random.seed(42)  # Set random seed to a static value.
    # Set initial number of Failed tests to 0:
    numberFail = 0

    for i in range(1000):  # Run 1000 tests.
        # Generate random message to test.
        # The message wil have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Convert list back to a string.

        testFailed = False  # Set testFailed flag to False.
        
        for key in range (1, int(len(message) / 2)):
            # Check every possible key for a message.
            encrypted = runEncryption(message, key)
            decrypted = runDecryption(encrypted, key)

            # Inform user about error if message differs after decryption.
            if message != decrypted:
                print(f'Error with {message} and key {key}.', end = ' ')
                numberFail += 1
                testFailed = True  # Set testFailed flag to True.

        if not testFailed:
            print(f'Test {i+1} succesful.')
        else:
            print(f'Test {i+1} failed.')

    print(f'Test completed. {numberFail} tests failed.')


# If run (instead of imported), run the program:
if __name__ == '__main__':
    main()