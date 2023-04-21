'''Simple Substitution Cipher Hacker (simpleSubHacker),
by Jakub Berkowski jakub.berkowski@gmail.com
Hacks simple substitution cipher using word patterns in English.'''

import re, pyperclip

import makeWordPatterns, wordPatterns, simpleSubCipher

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#  Function to remove chars other than capital letters and whitespaces:
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')


def main():
    '''Main function for simpleSubHacker.'''
    print('Simple Substitution Cipher Hacker, by Jakub', end ='')
    print(' Berkowski jakub.berkowski@gmail.com')
    print('Please input message for decryption:')
    ciphertext = input('> ')
    print('Hacking...')
    finalLettermap = hackSimpleSub(ciphertext)  # Create lettermap.
    
    print('Mapping:')
    print(finalLettermap)  # Print final lettermap.
    
    print('Ciphertext:')
    print(ciphertext)  # Print original message.
    
    print('Plaintext:')
    plaintext, key = decryptWithLettermap (ciphertext, finalLettermap)
    print(key)
    print(plaintext)  # Print decrypted message.
    pyperclip.copy(plaintext)  # Copy decrypted message to clipboard.
    print('Plaintext has been copied to clipboard.')


def getEmptyLettermapping():
    '''Creates dictionary with all capital letters as keys and
    empty values.'''
    emptyLettermap = {}
    for letter in LETTERS:
        emptyLettermap[letter] = []
    return emptyLettermap


def mapWord(cipherword):
    '''Creates a lettermap for one word.'''
    cipherList = []
    cipherList.append(cipherword)  # Transform word into a one-element list.
    patternDict = makeWordPatterns.wordPatterns(cipherList)
    pattern = patternDict[cipherword]  # Get pattern word the cipherword.

    candidatesMap = getEmptyLettermapping()
    # Get a list of all possible candidates for this cipherword:
    if pattern not in wordPatterns.allPatterns:
        return candidatesMap  # No valid candidates for this pattern.
    else:
        candidates = wordPatterns.allPatterns[pattern]

    # For every candidate, append corresponding letter to cipherletter:
    for candidate in candidates:
        for i in range(len(candidate)):
            if candidate[i].upper() not in candidatesMap[cipherword[i]]:
                candidatesMap[cipherword[i]].append(candidate[i].upper())
    return candidatesMap


def intersectMap(mapA, mapB):
    '''Compares two lettermaps and returns one, which contains only
    these values, which appear in both maps.'''
    # Create empty map:
    intersectedMap = getEmptyLettermapping()
    for letter in mapA:  # Loop through every letter:
        # If letter is empty in one map, simply copy from the other map:
        if mapA[letter] == []:
            intersectedMap[letter] = mapB[letter]
        elif mapB[letter] == []:
            intersectedMap[letter] = mapA[letter]
        else:  # For letters existing in both maps, choose common ones:
            for cipherletter in mapA[letter]:
                if cipherletter in mapB[letter]:
                    intersectedMap[letter].append(cipherletter)
    return intersectedMap


def removeSolvedLetters(intersectedMap):
    '''If any cipherletter has only one solution, consider it solved
    and remove this solution from other cipherletters. Repeat until
    no more solutions are found with next iteration.'''
    loopAgain = True  # There will be always at least one iteration.
    solvedLetters = []
    while loopAgain:
        # Assume not more iterations, until any changes are made:
        loopAgain = False

        # Create list of solved letters:
        for cipherletter in intersectedMap:
            mappedValue = intersectedMap[cipherletter]
            if len(mappedValue) == 1:
                if mappedValue[0] not in solvedLetters:
                    solvedLetters.append(mappedValue[0])
        
        # Remove solved letters from other cipherletters:
        for letter in solvedLetters:
            for cipherletter in intersectedMap:
                mappedValue = intersectedMap[cipherletter]
                if letter in mappedValue and len(mappedValue) != 1:
                    mappedValue.remove(letter)
                    loopAgain = True  # Changes were made, so loop again.
    return intersectedMap

def hackSimpleSub(ciphertext):
    '''Returns dictionary with completed lettermap.'''
    # Create a list of all words in ciphertext, with only capital letters
    # and all all special characters and numbers removed.
    cipherWordsList = nonLettersOrSpacePattern.sub('', ciphertext.upper()).split()
    intersectedMap = getEmptyLettermapping()
    # Create a lettermap for each word. After every word is completed
    # intersect the maps.
    for cipherword in cipherWordsList:
        mapA = intersectedMap
        mapB = mapWord(cipherword)
        # Update the intersectedMap with every word:
        intersectedMap = intersectMap(mapA, mapB)

    # Remove solved letters from the intersectedMap:
    finalLettermap = removeSolvedLetters(intersectedMap)
    return finalLettermap


def decryptWithLettermap(ciphertext, lettermap):
    '''Create key with solved letters, unsolved letters leave blank.
    Then decrypt ciphertext using this key.'''
    # Create key:
    key = ['x'] * len(LETTERS)
    for cipherletter in lettermap:
        if len(lettermap[cipherletter]) == 1:
            keyIndex = LETTERS.find(lettermap[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')

    key = ''.join(key)

    plaintext = simpleSubCipher.runDecryption(ciphertext, key)
    return plaintext, key


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()