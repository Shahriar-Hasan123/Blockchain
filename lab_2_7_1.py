"""Problem: Program in Python that Demonstrates the Use of Hashlib Library to Generate the 
SHA-3 Hash of a Message"""

import hashlib 

message = input("Enter the message to hash: ").encode()
sha3_256 = hashlib.sha3_256() 
sha3_256.update(message) 
digest = sha3_256.digest() 
hexdigest = digest.hex() 
print(hexdigest)
