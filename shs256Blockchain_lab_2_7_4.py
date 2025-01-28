"""Problem: Write a program in Python that Demonstrates How to Use the SHA-256 Hash Function and Its
Application in a Simple Blockchain"""

import hashlib
import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print("-" * 50)


# Example Usage
if __name__ == "__main__":

    blockchain = Blockchain()
    # Add some blocks to the blockchain
    blockchain.add_block("Block 1 : Hello")
    blockchain.add_block("Block 2 : Hi")
    blockchain.add_block("Block 3 : Bye")

    # Print the blockchain
    print("Blockchain:")
    blockchain.print_chain()

    # Validate the blockchain
    print("Is the blockchain valid?", blockchain.is_chain_valid())

    # Tamper with the blockchain to demonstrate validation
    print("\nTampering with the blockchain...")
    blockchain.chain[1].data = "Block 1: Alice sends 100 BTC to Eve"
    print("Is the blockchain valid after tampering?", blockchain.is_chain_valid())
