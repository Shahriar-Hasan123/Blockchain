"""Problem: Program to Create Hash Code from Given Input String"""

import hashlib 

message = input("Enter the message to hash: ")
hash_object = hashlib.sha256()
hash_object.update(message.encode('utf-8')) 
hex_dig = hash_object.hexdigest() 
print("String: {}".format(message)) 
print("Hash value (SHA-256): {}".format(hex_dig))
