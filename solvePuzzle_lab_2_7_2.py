"""Problem: Python Program that Takes a String and the Desired Number of Leading Zeros from 
the User and Outputs the Input String, the Nonce Value for Which the Leading 
Zeros Puzzle Is Solved, and the Corresponding Hash Generated"""

import hashlib

def solve_puzzle(string, leading_zeros):
    nonce = 0
    while True:
        nonce_str = str(nonce)
        data = string + nonce_str
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value.startswith("0" * leading_zeros):
            return nonce_str, hash_value
        nonce += 1

input_string = input("Enter the string: ")
input_zeros = int(input("Enter the number of leading zeros: "))
nonce_value, hash_result = solve_puzzle(input_string, input_zeros)

print("\n=== Puzzle Solved ===")
print("Input String:", input_string)
print("Nonce value for which the puzzle is solved:", nonce_value)
print("Generated Hash:", hash_result)
