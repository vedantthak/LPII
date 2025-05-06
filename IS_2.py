import math

def encryptMessage(msg, key):
    cipher = ""
    msg = msg.replace(" ", "#")  # Replacing spaces with "#" for easier handling
    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))  # Number of rows in the grid
    fill_null = int((row * col) - msg_len)  # Adding null values to fill the grid
    msg_lst.extend('_' * fill_null)  # Extend the message with "_" to fill the grid
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]  # Create the matrix
    key_order = sorted(range(len(key)), key=lambda x: key[x])  # Sorting key indices to determine the order
    
    for i in range(col):
        curr_idx = key_order[i]  # Get column order from the sorted key
        cipher += ''.join([row[curr_idx] for row in matrix])  # Add the characters column-wise
    return cipher

def decryptMessage(cipher, key):
    msg = ""
    msg_indx = 0
    msg_len = len(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))  # Number of rows in the grid
    key_lst = sorted(list(key))
    dec_cipher = [[None] * col for _ in range(row)]  # Initialize empty matrix
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])  # Sorting key indices
    
    for k in range(col):
        curr_idx = key_order[k]  # Get column order from sorted key
        for j in range(row):
            dec_cipher[j][curr_idx] = cipher[msg_indx]  # Place cipher characters into the matrix
            msg_indx += 1
            
    msg = ''.join(sum(dec_cipher, []))  # Flatten the matrix to get the decrypted message
    msg = msg.replace("_", "")  # Remove padding characters
    msg = msg.replace("#", " ")  # Replace "#" back to space
    return msg

# Main driver
msg = input("Enter the Plain Text: ")
key = input("Enter the Key: ")

# Encrypt and Decrypt the message
cipher = encryptMessage(msg, key)
print("Encrypted Message:", cipher)

decrypted_msg = decryptMessage(cipher, key)
print("Decrypted Message:", decrypted_msg)
