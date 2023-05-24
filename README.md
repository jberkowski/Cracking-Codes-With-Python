# Cracking-Codes-With-Python

Here I uploaded all my projects which I created while learning cryptography
from 'Cracking Codes With Python' book, written by Al Sweigart,

While this projects are based on what I learned from Al's book, I wrote all of
them by myself, so you will find numerous changes and improvements.

Below is a full list of files included in this repository, together with
all dependencies. Each file also has its own description and is pretty
much self-explanatory.

## List of files and programs in this repository:
- reverseCipher.py - Encrypts/decrypts message using reverse cipher. Input is user's text string entered via terminal. Output is this string reversed (first character becomes last etc.).\
**Imported modules:**
    - pyperclip (not compulsory).
    
 - caesarCipher.py - Encrypts/decrypts message using Caesar Cipher. It is a simple shift cipher, which shifts all the symbols in a message by a given value, called 'key'. Input is user's text string and a key (integer). Output is this string shifted ('upwards' for encryption and 'downwards' for decryption).
 **Note:** SYMBOLS constant must be the same for encryption and decyption of the message. It can be changed to match required list of symbols.\
 **Imported modules:**
    - pyperclip (not compulsory).
    
- caesarHacker.py - Performs a brute-force attack against message encrypted with Caesar Cipher. Input is a text string (encrypted message). Output is list of strings, each line represents encrypted string shifted 'downwards' by a 'key' value. User has to check for correct decryption manually.\
**Note:** SYMBOLS constant must be the same as in program that encrypted the message.\
**Imported modules:**
    - none.

- transpositionCipher.py - Encrypts/decrypts message using columnar transposition cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition)). Input is user's text string and a key (integer). Output is text string (encrypted/decrypted message).\
**Imported modules:**
    - sys, math (compulsory),
    - pyperclip (not compulsory).
    
- transpositionFileCipher.py - Encrypts/decrypts message stored in a text file using columnar transposition cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition)). Input is location of text file containing message for processing and a key (integer). Output is a text file with processed message, named "*input_file_name*.crypted.txt".\
**Imported modules:**
    - sys, os, time (compulsory),
    - transpositionCipher.py (compulsory).
    
- english_dictionary.txt - file that contain English words. Each word starts in a new line. File required for detectEnglish.py module.

- detectEnglish.py - Compares a string with English dictionary and returns True or False, based on percentage of English words. Input is a text string. Output is True or False, based on comparision criteria specified in isEnglish function. If you like to change the language, put a .txt dictionary in the same folder as this module. Rename file in line 13. If you like to change the default criteria, change the values in line 49.\
**Imported modules:**
    - none.
    
- transpositionHacker.py - Performs a brute-force attack against message encrypted with transposition cipher. Input is location of text file containing message for hacking. Output is a .txt file with possible decryption (possible decryption occurs when detectEnglish.isEnglish value is True). User has to manually check if decryption is correct and accept or refuse the result.\
**Imported modules:**
    - sys, os, time (compulsory),
    - transpositionCipher.py, detectEnglish.py (compulsory).
    
- transpositionTest.py - Runs 1000 enryptions/decryptions on a random text strings to test if transpositionCipher.py works properly. There is no input. Outpust is message generated after each test which informs user if test was succesfull. At the end a total number of failed test is displayed.\
**Imported modules:**
    - random, sys (compulsory),
    - runEncryption, runDecryption from transpositionCipher.py (compulsory).
    
- cryptomath.py - Module required for Affine Cipher program. Contains functions for finding Greatest Common Divisor and Modular Inverse.\
**Imported modules:**
    - none.
    
- affineCipher.py - Encrypts/decrypts message using affine cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Substitution_cipher)). Input is user's text string and a key (integer, for encryption randomly generated key can be chosen). Output is text string (encrypted/decrypted message) and generated key (if chosen randomly for encryption).\
**Imported modules:**
    - sys, random (compulsory),
    - gcd, findModInverse from cryptomath.py (compulsory),
    - pyperclip (not compulsory).
    
- affineHacker.py - Performs a brute-force attack against message encrypted with affine cipher. Input is text string (encrypted message). Output is text string (decrypted message) or error message ("Decryption failed", if no possible decryptions are found). If any key provides plaintext that meets requirements of detectEnglish.py module, it is displayed to user which has to decide if encryption is completed (by typing "D" and enter) or program has to look for another solution (any other user response).\
**Imported modules:**
    - pyperclip (not compulsory),
    - affineCipher.py, detectEnglish.py, cryptomath.py (compulsory).
    
- simpleSubCipher.py - Encrypts/decrypts message using substitution cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Affine_cipher)). Input is user's text string and a key (string containing every letter from SYMBOLS string exactly once, for encryption randomly generated key can be chosen). Output is text string (encrypted/decrypted message) and used key.\
**Imported modules:**
    - pyperclip (not compulsory),
    - random (compulsory).
    
- makeWordPatterns.py - creates a word patterns dictionary required by simpleSubHacker.py. Input is a english_dictionary.txt file with single word in a row (name of the file can be changed in line 20). Output is a wordPatterns.py file which contains word patterns dictionary like: 0.0.1.2: ['EELS', 'OOZE'].\
**Note:** The longer the dictionary, the more possible decryptions will be found while hacking. Use longer dictionaries for longer messages!\
**Imported modules:**
    - none.
    
- wordPatterns.py - word pattern dictionary file required by simpleSubHacker.py. Contains word patterns dictionary like: 0.0.1.2: ['EELS', 'OOZE']. Can be downloaded or created by makeWordPatterns.py program.\
**Imported modules:**
    - none
    
- simpleSubHacker.py - performs an attack on message encrypted with simple substitution cipher using English word patterns. Decoding other languages requires 1) changing possible symbols list in line 9 and 2) using wordPatterns.py file created from language disctionary. Input is a text string (encrypted message). Output is a text string (decrypted message), with unknown letters marks as "_" and a key.\
**Imported modules:**
    - re (compulsory),
    - makeWordPatterns.py, wordPatterns.py, simpleSubCipher.py (compulsory),
    - pyperclip (not compulsory).
    
- freqAnalysis.py - required for hacking the Vigenere cipher. In code line 8 is a LANGFREQ string. It lists the letter from the most frequently appearing to least frequently appearing in English language (if you wish to crack messages in language other than English, change this string). Program compares number of occurences of all letters in input string with LANGFREQ string. Any match for the six most and six least frequent letters increases matchScore by 1. The Input is a text string. Output is a match score integer.\
**Imported modules:**
    - none.
    
- vigenereCipher.py - encrypts/decrypts message using Vigenere cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Vigenere_cipher)). Input is a text string (message) and key (text string, containing only letters used in LETTERS constant (line code 7)). Output is a text string (processed message).\
**Imported modules:**
    - pyperclip (not compulsory).

- vigenereDictHacker.py - attempts a dictionary hack of message encrypted with Vigenere cipher. Works if key is a full proper English word. Refer to makeWordPatterns.py and detectEnglish.py description in order to change the key/message language. Input is a text string (encrypted message). Output is text string: first 50 characters of attemted decryption. If decryption looks correct, type "D" to accept and display full message.\
**Imported modules:**
    - detectEnglish.py, vigenereCipher.py, makeWordPatterns.py (compulsory),
    - pyperclip (not compulsory).
    
- primeNum.py - contains functions related to checking/generating prime numbers. Required for some other programs.\
**Imported modules:**
    - math, random (compulsory).
    
- vigenereHacker.py - hacks a message encoded with a Vigenere Cipher (see [Wikipedia article](https://en.wikipedia.org/wiki/Vigenere_cipher)). First, it performs Kasiski Examination (see [Wikipedia article](https://en.wikipedia.org/wiki/Kasiski_examination)) to narrow down the number of possible keys. Then brute-froces through them, using English detection tool to recognize correct decryption. By changing the values of constants in lines 10, 11 and 12 you can change the number of keys tried to hack the message. Input is a text string (encrypted message). Output is a text string: encrypted message an a key used.\
**Imported modules:**
    - pyperclip (non-compulsory),
    - itertools, re (compulsory),
    - detectEnglish, vigenereCipher, freqAnalysis (compulsory).
    
- makePublicPrivateKeys.py - generates private and public key and stores them in a separate .txt files.\
**Imported modules:**
    - random, sys, os (compulsory),
    - primeNum, cryptomath (compulsory).

## Contributing:

Pull requests are welcome. You can also contact me on jakub.berkowski@gmail.com

## License:

[MIT License](https://choosealicense.com/licenses/mit/)
