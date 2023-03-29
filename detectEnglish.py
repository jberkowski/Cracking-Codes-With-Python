'''This module detects if string contains English words,
based on a comparision with English dictionary.'''

# There must be an 'english_dictionary.txt' file in this directory,
# one word per line.

# Define constants:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'

def loadDictionary():
    '''Load a dictionary file into a python dictionary.'''
    dictionaryFile = open('english_dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message):
    '''Return percentage of words from message that occur in our english 
    dictionary ('english words').'''
    message = message.lower()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # No words at all, so return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords) * 100


def removeNonLetters(message):
    '''Returns message only with letters and spaces/tabs.'''
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=80, letterPercentage=80):
    '''Checks if at least 20% of words from message exist in dictionary
    and at least 85% of all characters are letters and spaces.'''
    wordsMatch = getEnglishCount(message) >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch