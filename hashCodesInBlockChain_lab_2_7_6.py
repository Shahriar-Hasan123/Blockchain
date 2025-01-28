"""Problem: Program to Demonstrate a Simple Implementation of a Blockchain Using 
Hash Codes as a Chain of Blocks"""

import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(datetime.datetime.now(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        # Check the validity of the blockchain by ensuring the hashes are consistent
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash of the current block matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
    def print_chain(self):
        """
        Print the entire blockchain.
        """
        for index, block in enumerate(self.chain):
            print(f"Block {index}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print("-" * 50)
            
# Create a blockchain and add blocks
blockchain = Blockchain()
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")
blockchain.print_chain()

print("Is blockchain valid?", blockchain.is_valid())
blockchain.chain[1].data = "Modified Block"
print("Is manipulated blockchain valid?", blockchain.is_valid())
