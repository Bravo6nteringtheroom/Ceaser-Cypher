Letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]}{;:'\",.<>?/|~"
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

input = "Im The Best #1"
print(f"\33[33m[X] Input: {input} \033[0m")
print(f"\33[31m[X] Encrypted: {Encrypt_Ceaser(input,3)}\033[0m")
ENc = Encrypt_Ceaser(input,3)
print(f"\33[32m[X] Decrypted: {Decrypt_Ceaser(ENc,3)}\033[0m")
