### Cipher
This project is a two-layer text encryption program written in Python.
It encrypts user-provided messages by first applying a Caesar cipher shift to all alphanumeric characters, and then reversing each individual word (considering only alphabetic characters) to add an extra level of obfuscation.
The program runs in the terminal and allows the user to control the encryption strength by choosing a custom shift value. It also preserves punctuation, spacing, and special characters, ensuring the original structure of the message remains intact after encryption.

EXAMPLE:
'Hello World!' with jump value 2 will become -- 'qnngJ fntqY!'


###Working

##ENCRYPTION
Step 1: Shifting for alphabets and numerics using a caeser cipher method. In this, each alphnumeric value is shifted by a 'key' or 'jump value' that is entered by user. 
Step 2: Each individual word(considering only alphabets) is reversed within itself. 

##DECRYPTION
STEP 1: The encrypted message is first un-reversed word by word.
STEP 2: The Caesar cipher shift is then reversed using the same key value.

(-The original message is restored exactly if the correct key is provided-)



###FEATURES

-- Two-step encryption process for stronger encoding
-- Caesar cipher applied to letters and numbers
-- Customizable shift value chosen by the user
-- Word-level reversal applied only to alphabetic characters
-- Preserves punctuation, spaces, and special symbols
-- Maintains uppercase and lowercase formatting
-- Interactive command-line interface
-- Fast and lightweight execution

