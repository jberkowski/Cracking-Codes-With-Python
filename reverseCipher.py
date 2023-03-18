"""Reverse Cipher, by Jakub Berkowski jakub.berkowski@gmail.com
This program encrytps/decrypts text messages using reverse cipher."""

try:
    import pyperclip
except ImportError:
    pass

translate = ''  # Make space for encrypted/decrypted message.

message = input('Please input your message: ')
i = len(message) - 1

while i >= 0:
    translate += message[i]
    i -= 1

print(translate)
print('Your message has been copied to clipboard.')

try:
    pyperclip.copy(translate)
except:
    pass
