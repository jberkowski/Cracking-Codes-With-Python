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

## Contributing:

Pull requests are welcome. You can also contact me on jakub.berkowski@gmail.com

## License:

[MIT License](https://choosealicense.com/licenses/mit/)
