# Write a program for encrypting and encoding text
# "Encrypting" is the process of making a text unreadable
#
# you will get the function rot() and the test functions
# your job is to write the function encrypt and decrypt
#
# rotate a letter in the alphabet by n letters
# n is an integer between 0 and 25
# returns the rotated letter
def rot(c, n):
    return chr((ord(c) - ord('a') + n) % 26 + ord('a'))

# encrypt a word by rotating each letter by a given offset
def encrypt(word, offset = 13):
    output = ''
    for letter in word:
        rotatedLetter = rot(letter, offset)
        output += rotatedLetter
    
    return output

# decrypt a word by rotating each letter by a given offset
def decrypt(code, offset = 13):
    output = ''
    for letter in code:
        rotatedLetter = rot(letter, -offset)
        output += rotatedLetter
    
    return output

def testEncrypt():
    print("\nTEST ENCRYPT\n")

    words = ['be', 'one', 'or', 'be', 'fun']
    print("start encrypting")
    encrypted = []
    for word in words:
        code = encrypt(word)
        encrypted.append(code)
    print("encrypted: ", encrypted)

    print("start decrypting")
    decrypted = []
    for cypher in encrypted: 
        word = decrypt(cypher)
        decrypted.append(word)
    print("decrypted: ", decrypted)

testEncrypt()
