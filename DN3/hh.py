import random

# Define a list of characters that will be used for encryption
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              ' ', ',', '.', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
              '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '\"', '\\', '|', 
              '<', '>', '/', '~', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


plaintext = input('Enter your message: ')

yy = int(input("Enter Degree of Encryption [1 - 5] = "))

ll = [7, 9, 11, 13, 15]

# Generate a random binary string of length 131072 for each character
binary_strings = {}
for char in characters:
    binary_strings[char] = ''.join(random.choice(['0', '1']) for _ in range(2**ll[yy-1]))

# print(binary_strings)


# Convert plaintext to binary string
binary_plaintext = ''
for char in plaintext.lower():
    if char in binary_strings:
        binary_plaintext += binary_strings[char]
        
print('Plaintext: ', plaintext)
print('Binary string: ', binary_plaintext)




def generate_random_binary_string(length):
    binary_string = ""
    for i in range(length):
        # Generate a random integer between 0 and 1
        random_int = random.randint(0, 1)
        # Append the integer to the binary string
        binary_string += str(random_int)
    return binary_string


def encrypt(binary_text, key):
    encrypted = ""
    for i in range(len(binary_text)):
        # Perform XOR operation between binary_text and key
        temp = int(binary_text[i]) ^ int(key[i % len(key)])
        encrypted += str(temp)
    return encrypted


def decrypt(encrypted_text, key):
    decrypted = ""
    for i in range(len(encrypted_text)):
        # Perform XOR operation between encrypted_text and key
        temp = int(encrypted_text[i]) ^ int(key[i % len(key)])
        decrypted += str(temp)
    return decrypted




key = generate_random_binary_string(len(binary_plaintext))
print("The Random Key is = ",key)

cc = encrypt(binary_plaintext, key)
print("The Encypted Key is = ",cc)

kk = decrypt(cc,key)
print("The Decrypted key is = ",kk)

if binary_plaintext == kk :
    print(True)
    
    
def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    # If the value is not found, return None
    return None


def split_string(s, n):
    # calculate the length of each substring
    part_len = len(s) // n
    # check if the string can be divided into n equal parts
    if len(s) % n != 0:
        return None
    # create a list of substrings
    substrings = [s[i:i+part_len] for i in range(0, len(s), part_len)]
    return substrings

lol = split_string(kk, len(plaintext))

# print(lol)
jjnj = "The Decrypted text is = "
for i in range(len(lol)) :
    jjnj += get_key_from_value(binary_strings, lol[i])
print(jjnj)