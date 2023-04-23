'''Frequency Analysis, by Jakub Berkowski jakub.berkowski@gmail.com
This module analyses the frequency of occurence for each letter in a
provided string. Requires string of letters sorted by frequency of
occurence in analysed language.
(E.g. for English it is 'ETAOINSHRDLCUMWFGYPBVKJXQZ').'''

# Change this for language other than English:
LANGFREQ = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def countLetters(message):
    '''Return dictionary with letters as keys and number of occurences 
    in message as values.'''
    # Create dictionary with letters as keys and 0 values:
    letterCount = {}
    for letter in LETTERS:
        letterCount[letter] = 0

    for symbol in message:
        if symbol.upper() in LETTERS:
            letterCount[symbol.upper()] += 1
    return letterCount


def getItemAtIndexZero(items):
    '''Return first element from a tuple.'''
    return items[0]


def lettersFreq(message):
    '''Returns a string of letters sorted by frequency of occurence
    in message (from highest to lowest). If two or more letters occur the
    same amount of times in message, their order is reversed compared
    to a key string.'''

    # Step one:
    # Count each letter from the message:
    letterCount = countLetters(message)

    # Step two:
    # create a dictionary where numbers of occurence in message 
    # are keys and letters are values (reversed dictionary
    # from 'countLetters' function).
    lettersFreqDict = {}
    for letter in letterCount:
        if letterCount[letter] not in lettersFreqDict:
            lettersFreqDict[letterCount[letter]] = [letter]
        else:
            lettersFreqDict[letterCount[letter]].append(letter)

    # Step three:
    # If there are two or more letters with same number of occurence,
    # sort them in reverse order compared to LANGFREQ.
    # This is in order to minimize random impact on our analysis.
    for key in lettersFreqDict:
        lettersFreqDict[key].sort(key = LANGFREQ.find, reverse = True)
        # Convert each value list to a string:
        lettersFreqDict[key] = ''.join(lettersFreqDict[key])

    # Step four:
    # Sort the letters by frequency of occurence, from highest.
    lettersFreqList = list(lettersFreqDict.items())
    lettersFreqList.sort(key = getItemAtIndexZero, reverse = True)

    # Step five:
    # Convert the list to string of letters ordered by frequency:
    freqOrder = []
    for freqPair in lettersFreqList:
        freqOrder.append(freqPair[1])

    lettersFreqOrder = ''.join(freqOrder)
    return lettersFreqOrder


def getLanguageMatchScore(message):
    '''Return the number of matches that the string in the message
    parameter has when its letter frequency is compared to language
    letter frequency. A "match" is how many of its six most and six 
    least frequent letters are among six most and six least frequent
    letters for given language.'''
    freqOrder = lettersFreq(message)

    matchScore = 0  # Set initial score to 0.

    for symbol in freqOrder[:6]:
        if symbol in LANGFREQ[:6]:
            matchScore += 1

    for symbol in freqOrder[-6:]:
        if symbol in LANGFREQ[-6:]:
            matchScore += 1
    return matchScore