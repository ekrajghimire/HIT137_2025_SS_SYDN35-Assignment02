"""
Group Name: SYDNEY-35 (SYD-35)
Authors: Ekraj Ghimire (S398831),  Sudip Sunar (S398629)

Group Members:
Roshan Lamichhane - S399178
Ekraj Ghimire - S398831
Sudip Sunar - S398629
Shrijan Neupane - S398335 



###############################
Question 1
Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple encryption method, and writes the encrypted text to a new file
"encrypted_text.txt". Then create a function to decrypt the content and a function to verify the decryption was successful.

Requirements
The encryption should take two user inputs (shift1, shift2), and follow these rules:

- For lowercase letters:
  - If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * shift2 positions
  - If the letter is in the second half (n-z): shift backward by shift1 + shift2 positions
- For uppercase letters:
  - If the letter is in the first half (A-M): shift backward by shift1 positions
  - If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)
- Other characters:
  - Spaces, tabs, newlines, special characters, and numbers remain unchanged

Main Functions to Implement

Encryption function: Reads from "raw_text.txt" and writes encrypted content to "encrypted_text.txt".
Decryption function: Reads from "encrypted_text.txt" and writes the decrypted
content to "decrypted_text.txt".
Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints whether the decryption was successful or not.

Program Behavior

When run, your program should automatically:
1. Prompt the user for shift1 and shift2 values
2. Encrypt the contents of "raw_text.txt"
3. Decrypt the encrypted file
4. Verify the decryption matches the original


###########################
References:
- https://docs.python.org/3/library/functions.html#ord
-  https://www.geeksforgeeks.org/python/encrypt-and-decrypt-files-using-python/
- https://docs.python.org/3/library/stdtypes.html#str.join
- https://en.wikipedia.org/wiki/Caesar_cipher
"""


#######################
# Functions
######################


def shift_char_in_range(char, shift, start, end):
    """shifts character between the specified range"""

    # Example: shift_char_in_range('m', 8, 'a','m') -> 'h'
    #     range_size = 109 - 97 + 1 = 12
    #     diff_start = 109 - 97 = 12
    #     shift_value  = (12 + 8) % 13 = 7
    #     return chr(97 + 7 = 104) = 'b'

    # total range value of characters
    range_size = ord(end) - ord(start) + 1
    # difference between given character and start character
    diff_start = ord(char) - ord(start)
    # shift value, which is dereived from remainder of  (diff_start and provided shift) divided by range_size
    shift_value = (diff_start + shift) % range_size
    return chr(ord(start) + shift_value)


def encrypt_text(text, shift1, shift2):
    """encrypts text using the encryption algorithm"""
    # list is used to append the encrypted characters, later converted to a string
    encrypted_chars = []

    for ch in text:
        if "a" <= ch <= "m":
            shift_value = shift1 * shift2
            encrypted_chars.append(shift_char_in_range(ch, shift_value, "a", "m"))
        elif "n" <= ch <= "z":
            shift_value = -(shift1 + shift2)
            encrypted_chars.append(shift_char_in_range(ch, shift_value, "n", "z"))
        elif "A" <= ch <= "M":
            shift_value = -shift1
            encrypted_chars.append(shift_char_in_range(ch, shift_value, "A", "M"))
        elif "N" <= ch <= "Z":
            shift_value = shift2**2
            encrypted_chars.append(shift_char_in_range(ch, shift_value, "N", "Z"))
        else:
            encrypted_chars.append(ch)

    return "".join(encrypted_chars)


def decrypt_text(text, shift1, shift2):
    """decrypts text using the decryption algorithm"""
    # list is used to append the decrypted characters, later converted to a string
    decrypted_chars = []

    for ch in text:
        if "a" <= ch <= "m":
            shift_value = -(shift1 * shift2)
            decrypted_chars.append(shift_char_in_range(ch, shift_value, "a", "m"))
        elif "n" <= ch <= "z":
            shift_value = shift1 + shift2
            decrypted_chars.append(shift_char_in_range(ch, shift_value, "n", "z"))
        elif "A" <= ch <= "M":
            shift_value = shift1
            decrypted_chars.append(shift_char_in_range(ch, shift_value, "A", "M"))
        elif "N" <= ch <= "Z":
            shift_value = -(shift2**2)
            decrypted_chars.append(shift_char_in_range(ch, shift_value, "N", "Z"))
        else:
            decrypted_chars.append(ch)

    return "".join(decrypted_chars)


def verify_decryption(original_text, decrypted_text):
    """returns true if the original text and decrypted text are same(meaning decryption works)"""
    return original_text == decrypted_text

#################
# Main Program

# file name to read content from
raw_text_file = "raw_text.txt"
# file name to write encrypted data into
encrypted_text_file = "encrypted_text.txt"
# file to write decrypted text into
decrypted_text_file = "decrypted_text.txt"


# Take shift1 and shift2 values from user with validation
try:
    shift1 = int(input("Enter value for shift1: "))
    shift2 = int(input("Enter value for shift2: "))
except ValueError:
    print("Invalid input. Please enter integers.")
    exit()
try:
    # Read content from raw_text.txt file
    with open(raw_text_file, "r") as file:
        raw_text = file.read()

    # Encrypt the content from raw_text.txt file
    encrypted = encrypt_text(raw_text, shift1, shift2)

    # Write the encrypted data into encrypted_text.txt file
    with open(encrypted_text_file, "w") as file:
        file.write(encrypted)

    # Decrypt the encrypted data
    decrypted_data = decrypt_text(encrypted, shift1, shift2)

    # Write decrypted data into decrypted_text.txt file
    with open(decrypted_text_file, "w") as file:
        file.write(decrypted_data)

    # Check if decrypted data and raw data are same
    if verify_decryption(raw_text, decrypted_data):
        print("Decryption was successfull!")
    else:
        print("Decryption failed!")

except Exception as e:
    print("Something went wrong.", e)
