import base64
# Write a program for encoding text
# "Encoding" is the process of putting text in a different format
#
# your job is to write the functions base (to encode) and debase (to decode)
#
# use the python built-in base64 module (you will need to import it)
#
# notes:
# the b64encode function returns a byte string
# the b64decode function returns a string
# using s.encode() converts a string s to a byte string
# using b.decode() converts a byte string b to a string

# encode a string to base64
def base(word):
    # convert the word to binary
    bword = word.encode()
    # use b64
    eword = base64.b64encode(bword)
    # return the value
    return eword.decode()

# decode a string from base64
def debase(code):
    # convert the code to binary
    bcode = code.encode()
    # use b64
    dcode = base64.b64decode(bcode)
    # convert the code to string
    word = dcode.decode()
    # return the value
    return word

def testEncode():
    print("\nTEST ENCODE\n")
    words = ['be', 'one', 'or', 'be', 'fun']

    print("start encoding")
    encoded = []
    for word in words:
        code = base(word)
        encoded.append(base(word))
    print("encoded: ", encoded)

    print("start decoding")
    decoded = []
    for cypher in encoded:        
        word = debase(cypher)
        decoded.append(word)
    print("decoded: ", decoded)

testEncode()