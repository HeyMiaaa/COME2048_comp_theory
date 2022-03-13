# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcde fghijklmnopqrstuvwxyz ABCDE FGHIJKLMNOPQRSTUVWXYZ'

#message = "The quick brown fox jumped over the lazy dog" #type your message here
message = "Mia is getting the top GPA " #type your message here
print("Message:", message)

#create the Caesar cypher
offset = 5 #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup for encrypt
    if index < totalLetters: #lowercase
        if index in range (0, 26 - offset):
            keys[letters[index]] = letters[index + offset]
        else:
            keys[letters[index]] = letters[index + offset - 26]
    else: #uppercase
        if index in range(26,47):
            keys[letters[index]] = letters[index + offset]

        if index in range (47,52):
            keys[letters[index]] = letters[offset + index - 26 ]

        # cypher setup for decrypt
    if index < totalLetters:  # lowercase
        if index in range(offset, 26 ):
            invkeys[letters[index]] = letters[index - offset]
        else:
            invkeys[letters[index]] = letters[index - offset + 26]

    else:  # uppercase
        if index in range(26 + offset, 52):
            invkeys[letters[index]] = letters[index - offset]

        if index in range(26, 26 + offset):
            invkeys[letters[index]] = letters[index - offset + 26]

print("Cypher Dict:", keys)
print("Cypher Dict:", invkeys)


#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string

#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string
