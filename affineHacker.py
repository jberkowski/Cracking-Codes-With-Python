'''Affine Hacker, by Jakub Berkowski jakub.berkowski@gmail.com
Brute-force hacker for affine cipher.'''

import pyperclip

import affineCipher, detectEnglish, cryptomath

def main():
    '''Main function for Affine Hacker.'''
    print('Affine Hacker, by Jakub Berkowski jakub.berkowski@gmail.com')
    print('Please enter message for decryption: ')
    ciphertext = input('> ')

    plaintext = hackAffine(ciphertext)

    if plaintext == None:
        print('Decryption failed.')
    else:
        print(plaintext)
        print('Decrypted message copied to clipboard.')
        pyperclip.copy(plaintext)  # Copy encrypted message to clipboard.


def hackAffine(message):
    '''Brute-force decryption of message, 
    encrypted using affine cipher.'''
    print('Hacking...')

    # Try every possible key:
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = key // len(affineCipher.SYMBOLS)
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue  # KeyA and len(SYMBOLS) must be relatively prime.
        else:
            plaintext = affineCipher.runDecryption(message, key)
        if detectEnglish.isEnglish(plaintext):
            print('Possible encryption hack:')
            print(f'Key {key}')
            print(plaintext[:50])
            print("Type 'D' if you are done. Press Enter to continue hacking.")
            answer = input('> ')
            if answer.upper() == 'D':
                return plaintext
    return None

# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()