Letters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]}{;:'\",.<>?/|~"

def Encrypt_Ceaser(input,key):
    output = ""
    for x in range(len(input)):
        current_letter = input[x]
        if current_letter == ' ':
            current_letter = "_"
            
        if current_letter == "_":
            output += ' '
        else:
            index_of_current = Letters.find(current_letter)
            swap = (index_of_current+key) % len(Letters)
            output += Letters[swap]
    return output

def Decrypt_Ceaser(input,key):
    output = ""
    for x in range(len(input)):
        current_letter = input[x]
        if current_letter == '_':
            current_letter = ' '
            
        if current_letter == ' ':
            output += ' '
        
        else:
            index_of_current = Letters.find(current_letter)
            swap = (index_of_current-key) % len(Letters)
            output += Letters[swap]
    return output

# ✅ Test Suite for Caesar Cipher

test_cases = [
    "Im The Best #1",
    "Hello World!",
    "Python3.11 is cool",
    "1234567890",
    "Symbols: !@#$%^&*()",
    "Backslash \\ and quotes \"",
    "MixEd CaSe LeTtErS"
]

key = 3

for i, input_text in enumerate(test_cases, 1):
    encrypted = Encrypt_Ceaser(input_text, key)
    decrypted = Decrypt_Ceaser(encrypted, key)
    
    print(f"\n\033[33m[Test {i}] Input: {input_text}\033[0m")
    print(f"\033[31m[Test {i}] Encrypted: {encrypted}\033[0m")
    print(f"\033[32m[Test {i}] Decrypted: {decrypted}\033[0m")
