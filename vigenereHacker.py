'''Vigenere Hacker, by Jakub Berkowski, jakub.berkowski@gmail.com
Hacks Vigenere Cipher. Uses Kasiski Examination to narrow down
number of possible keys. Then brute-forces through them, using
English detectiont tool to recognize the correct decryption.'''

import pyperclip, itertools, re

import detectEnglish, vigenereCipher, freqAnalysis

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 16  # Will not try keys longer than this.
NUM_MOST_FREQ_LETTERS = 5  # This many most freq letters per subkey.
NONLETTERS_PATTERN = re.compile('[^A-Z]')  # Remove redundant characters.


def main():
    '''Main function for Vigenere Hacker.'''
    print('Vigenere Cipher Hacker, by Jakub', end ='')
    print(' Berkowski jakub.berkowski@gmail.com')
    print('Please input message for decryption:')
    ciphertext = input('> ')
    plaintext = []
    print('Hacking...')
    translated, key = hackVigenere(ciphertext)

    if translated != None:
        # Use correct casing for decrypted message:
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                plaintext.append(translated[i].upper())
            else:
                plaintext.append(translated[i].lower())
        plaintext = ''.join(plaintext)
        print(f'Hacking completed with key {key}:')
        print(plaintext)
        pyperclip.copy(plaintext)
        print('Message copied to clipboard.')
    else:
        print('Hacking failed.')


def findSequencesSpacings(message):
    '''Return dictionary with repeating sequences as keys and 
    lists of spacings between them as values.'''
    # Remove any nonletter chars from ciphetext:
    message = NONLETTERS_PATTERN.sub('', message.upper())
    seqSpacings = {}
    for seqLen in range(3, 6):  # Check seqs 3-5 letters long:
        for seqStart in range(len(message) - seqLen):
            # Call every substring of SeqLen a sequence:
            seq = message[seqStart:seqStart + seqLen]
            # Check if sequence repeats further down the message:
            for i in range(seqStart + seqLen, len(message) - seqLen + 1):
                if message[i:i + seqLen] == seq:  # If repeats:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []
                    seqSpacings[seq].append(i - seqStart)

    return seqSpacings


def findSequencesFactors(seqSpacings):
    '''Return dictionary with repeating sequences as keys and lists
    of factors of spacings between them as values.'''
    seqFactors = {}
    for sequence in seqSpacings:  # Loop through each key:
        for spacing in seqSpacings[sequence]:  # Loop through each spacing:
            for i in range(2, MAX_KEY_LENGTH + 1):
                if spacing % i == 0:
                    if sequence not in seqFactors:
                        seqFactors[sequence] = []
                    seqFactors[sequence].append(i)

    # Remove duplicates and sort the lists nicely:
    for sequence in seqFactors:
        seqFactors[sequence] = list(set(seqFactors[sequence]))
        seqFactors[sequence].sort()

    return seqFactors


def getItemAtIndexOne(x):
    '''Return item with index number 1.'''
    return x[1]


def getItemAtIndexZero(x):
    '''Return item with index number 0.'''
    return x[0]


def getMostCommonFactors(seqFactors):
    '''Return list of tuples where 1st item in tuple is factor 
    and 2nd is number of occurences in seqFactors.'''
    mostCommonFactors = {}
    for sequence in seqFactors:
        for factor in seqFactors[sequence]:
            if factor not in mostCommonFactors:
                mostCommonFactors[factor] = 0
            mostCommonFactors[factor] += 1

    # Turn the dictionary into list of tuples:
    factorsByCount = []
    for factor in mostCommonFactors:
        factorsByCount.append((factor, mostCommonFactors[factor]))

    # Sort the list by number of occurences of factor (i.e. by tuple items
    # with index 1).
    factorsByCount.sort(key = getItemAtIndexOne, reverse = True)

    return factorsByCount


def kasiskiExamination(message):
    '''Return a list of most likely key lengths.'''
    print('Running Kasiski Examination...')
    # Step one: 
    # Find all 3-5 chars long sequences in messsage, return dictionary 
    # with sequences as keys and lists of spacings as values.
    seqSpacings = findSequencesSpacings(message)

    # Step two:
    # Get factors of spacings. Return dictionary with sequences as keys
    # and lists of factors of corresponding spacings.
    seqFactors = findSequencesFactors(seqSpacings)

    # Step three:
    # Count which factors occur most frequently. Return list of tuples
    # where 1st item in tuple is factor and 2nd is number of occurences.
    mostCommonFactors = getMostCommonFactors(seqFactors)

    # Step four:
    # Extract factors from tuples and store them in a list of
    # most likely key lengths.
    allLikelyKeyLengths = []
    for keyFreqPair in mostCommonFactors:
        allLikelyKeyLengths.append(keyFreqPair[0])
    print('Examination completed. Most likely key lengths are:', end = ' ')
    print(allLikelyKeyLengths)

    return allLikelyKeyLengths


def getEveryNthLetter(message, keyLength):
    '''With keylength of n, return list of n strings, where each string 
    is every nth letter in ciphertext.'''
    # Remove any nonletter chars from ciphetext:
    message = NONLETTERS_PATTERN.sub('', message.upper())
    index = 0  # Set inital symbol index to 0.

    nStringsList = [''] * keyLength  # Create list of n empty strings.
    for symbol in message:
        nth = index % keyLength
        index += 1
        nStringsList[nth] += symbol

    return nStringsList


def getMatchingLetters(nString):
    '''Decrypt nString with each possible letter (subkey). Run frequency 
    analysis for each result. Return list of subkeys that get the 
    highest match score.'''
    matchScores = []
    for letter in LETTERS:
        decrypted = vigenereCipher.runDecryption(nString, letter)
        matchScore = freqAnalysis.getLanguageMatchScore(decrypted)
        matchTuple = (letter, matchScore)
        # Create list of tuples such as (subkey, match score):
        matchScores.append(matchTuple)

    matchScores.sort(key = getItemAtIndexOne, reverse = True)
    matchingTuples = matchScores[:NUM_MOST_FREQ_LETTERS]

    # Change list of tuples into list of subkeys:
    matchingSubkeys = []
    for matchingTuple in matchingTuples:
        matchingSubkeys.append(matchingTuple[0])

    return matchingSubkeys


def runHackWithLikelyKeyLengths(message, keyLength):
    '''Try hacking message with a keylength determined by
    Kasiski Examination.'''
    
    print(f'Trying decryption with key length {keyLength}...')
    # Divide ciphertext into n strings:
    nStringsList = getEveryNthLetter(message, keyLength)

    # Get the most matching letters (subkeys) for each string:
    matchingSubkeys = []
    for nString in nStringsList:
        # For each nString add list of subkeys:
        # E.g. [('A', )]
        matchingSubkeys.append(getMatchingLetters(nString))

    print(matchingSubkeys)
    # Combine most matching subkeys into most likely keys:
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS),
        repeat = keyLength):
        possibleKey = ''
        for i in range(keyLength):
            possibleKey += matchingSubkeys[i][indexes[i]]

        # Try decryption with each key:
        translated = vigenereCipher.runDecryption(message, possibleKey)

        # Check if result is message in english:
        if detectEnglish.isEnglish(translated):
            print(f'Possible encryption hack with key {possibleKey}:')
            print(translated[:200])  # Show only 200 first characters.
            print('Enter D if done, press Enter to continue:')
            response = input('> ')

            if response.upper().startswith('D'):
                return translated, possibleKey

    # If no valid decryption found, return None:
    return None, None


def hackVigenere(message):
    '''Try hacking message with a keylength determined by Kasiski Examination. 
    If unsuccesful, try every other key until MAX_KEY_LENGTH.'''

    # Step one: 
    # perform the Kasiski Examination to find most likely key lengths:
    allLikelyKeyLengths = kasiskiExamination(message)

    # Step two:
    # try decryption for each likely length of key:
    for keyLength in allLikelyKeyLengths:
        translated, key = runHackWithLikelyKeyLengths(message, keyLength)
        if translated != None:
            return translated, key

    # Step three:
    # decryption using likely lengths of key was unsuccesful. Try every
    # other key until MAX_KEY_LENGTH:
    print('Hacking with Kasiski failed. Trying every possible key length:')
    for keyLength in range(1, MAX_KEY_LENGTH + 1):
        if keyLength not in allLikelyKeyLengths:
            translated, key = runHackWithLikelyKeyLengths(message, keyLength)
            if translated != None:
                return translated, key

    # If we reach this point, hacking has failed.:
    return None, None


# If the program is run (instead of imported) run main:
if __name__ == '__main__':
    main()