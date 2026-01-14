# HIT137_2025_SS_SYDN35-Assignment02
Software Now - Assignment 2

## Overview
This repository contains the assignment task for HIT137 Group Assignment 02. <br>
The assignment focuses on file handling, encryption/decryption, data analysis, recursion, and visualization using Python. <br>
All tasks were developed collaboratively and tracked using GitHub as per the assignment requirements. <br>

## Question 1<br>
Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple encryption method, and writes the encrypted text to a new file "encrypted_text.txt". Then create a function to decrypt the content and a function to verify the decryption was successful.<br>
*Requirements*<br>
The encryption should take two user inputs (shift1, shift2), and follow these rules:<br>
  • For lowercase letters:<br>
    o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * shift2 positions<br>
    o If the letter is in the second half (n-z): shift backward by shift1 + shift2 positions<br>
  • For uppercase letters:<br>
    o If the letter is in the first half (A-M): shift backward by shift1 positions<br>
    o If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)<br>
  • Other characters:<br>
    o Spaces, tabs, newlines, special characters, and numbers remain unchanged<br>
*Main Functions to Implement*<br>
**Encryption function:** Reads from "raw_text.txt" and writes encrypted content to "encrypted_text.txt".<br>
**Decryption function:** Reads from "encrypted_text.txt" and writes the decrypted content to "decrypted_text.txt".<br>
**Verification function:** Compares "raw_text.txt" with "decrypted_text.txt" and prints whether the decryption was successful or not.<br>
*Program Behavior*<br>
When run, your program should automatically:<br>
  1. Prompt the user for shift1 and shift2 values<br>
  2. Encrypt the contents of "raw_text.txt"<br>
  3. Decrypt the encrypted file<br>
  4. Verify the decryption matches the original<br>



