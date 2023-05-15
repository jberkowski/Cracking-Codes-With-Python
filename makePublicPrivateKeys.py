'''Public Key Generator - generates private and public keys and
stores them in a separate .txt files.
https://www.nostarch.com/crackingcodes/ (BSD Licensed).'''

import random, sys, os

import primeNum, cryptomath


def main():
    '''Main function for Public Key Generator.'''
    print('Making key files...')
    makeKeyFiles('j_berkowski', 1024)
    print('Key files made.')

def generateKey(keySize):
    '''Generates public and private keys of chosen size.'''
    p = 0
    q = 0
    print('Generating prime numbers...')
    
    # Step 1:
    # Create two prime numbers, p and q. Calculate n = p * q:
    while p == q:  # Keep going until two distinct primes are generated.
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    # Step 2:
    # Create a number e, relatively prime to (p - 1) * (q - 1):
    print('Generating e, relatively prime to (p - 1) * (q - 1):')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3:
    # Calculate d, the mod inverse of e:
    print('Calculating d, a mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    '''Creates two files: 'x_pubkey.txt' and 'x_privkey.txt' (where x is
    the value in name) with n,e and n,d integers written in them,
    delimited by a comma.'''

    # Our safety check will prevent us from overwriting our old key files:
    if (os.path.exists(f'{name}_pubkey.txt') or
        os.path.exists(f'{name}_privkey.txt')):
        sys.exit(f'''WARNING! The file {name}_pubkey.txt or {name}_privkey.txt 
            already exists! Use a different name or delete these files 
            and rerun this program.''')

    publicKey, privateKey = generateKey(keySize)

    print()
    print(f'The public key is a {len(str(publicKey[0]))} ', end = '')
    print(f'and a {len(str(publicKey[1]))} digit number.')
    print(f'Writing public key to file {name}_pubkey.txt...')
    fo = open(f'{name}_pubkey.txt', 'w')
    fo.write(f'{keySize}, {publicKey[0]}, {publicKey[1]}')
    fo.close()

    print()
    print(f'The private key is a {len(str(privateKey[0]))} ', end = '')
    print(f'and a {len(str(privateKey[1]))} digit number.')
    print(f'Writing private key to file {name}_privkey.txt...')
    fo = open(f'{name}_privkey.txt', 'w')
    fo.write(f'{keySize}, {privateKey[0]}, {privateKey[1]}')
    fo.close()


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()