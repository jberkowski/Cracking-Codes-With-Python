'''Make Word Patterns, by Jakub Berkowski jakub.berkowski@gmail.com
Takes a .txt dictionary and creates a python dictionary with
all words patterns (e.g. '0.0.1.2: ['EELS', 'OOZE']).'''

def main():
    '''Create a patterns dictionary using .txt english dictionary.'''
    wordsList = loadDictionary()
    wordsDictionary = wordPatterns(wordsList)
    allPatterns = reverseDictionary(wordsDictionary)

    filename = 'wordPatterns.py'
    with open(filename, 'w') as file_object:
        file_object.write('allPatterns = {')
        for key in allPatterns:
            file_object.write(f"'{key}': {allPatterns[key]},\n")
        file_object.write('}')

def loadDictionary():
    '''Load a dictionary file into a python list.'''
    dictionaryFile = open('english_dictionary.txt')
    wordsList = []
    for word in dictionaryFile.read().split('\n'):
        wordsList.append(word)
    dictionaryFile.close()
    return wordsList


def wordPatterns(wordsList):
    '''Create dictionary with words as keys and their patterns as values.'''
    wordsDictionary = {}
    for word in wordsList:  # Loop through every word from a list.
        patternIndex = 0  # Reset patternIndex.
        patternCreation = ''  # String for checked letters.
        patternValue = ''  # String for pattern.
        for letter in word:  # Loop through every letter from a word.
            if letter not in patternCreation:
                patternCreation += letter  # Add letter to checked letters.
                letterInWordIndex = patternCreation.find(letter)
                patternValue += str(letterInWordIndex) + '.'
            else:
                letterInWordIndex = patternCreation.find(letter)
                patternValue += str(letterInWordIndex) + '.'
        patternValue = patternValue[:-1]
        wordsDictionary[word] = patternValue
    return wordsDictionary


def reverseDictionary(wordsDictionary):
    '''Reverses dictionary to have patterns as keys and all
    matching words as values.'''
    allPatterns = {}
    for word in wordsDictionary:
        pattern = wordsDictionary[word]
        try:
            allPatterns[pattern].append(word)
        except KeyError:
            allPatterns[pattern] = []
            allPatterns[pattern].append(word)
    return allPatterns


# If program is run (instead of imported), run main():
if __name__ == '__main__':
    main()