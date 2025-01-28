"""Write a program in Python to implement a blockchain and print the values of all fields as
described in etherscan.io"""

import hashlib
import datetime

class Block:

    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.block_number) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.gas_limit) + str(self.gas_used) + str(self.miner)
        return hashlib.sha256(data_string.encode("utf-8")).hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", 0, 0, "Genesis Miner")

    def add_block(self, transactions, gas_limit, gas_used, miner):
        previous_block = self.chain[-1]
        new_block = Block(
            block_number=previous_block.block_number + 1,
            transactions=transactions,
            previous_hash=previous_block.hash,
            gas_limit=gas_limit,
            gas_used=gas_used,
            miner=miner,
        )
        self.chain.append(new_block)

    def print_block(self, block):
        print("Block Number:", block.block_number)
        print("Timestamp:", block.timestamp)
        print("Transactions:", block.transactions)
        print("Previous Hash:", block.previous_hash)
        print("Gas Limit:", block.gas_limit)
        print("Gas Used:", block.gas_used)
        print("Miner:", block.miner)
        print("Hash:", block.hash)
        print("-" * 60)

    def traverse_chain(self):
        for block in self.chain:
            self.print_block(block)


# Example Usage
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Add blocks to the blockchain
    my_blockchain.add_block(transactions="Transaction 1", gas_limit=1000000, gas_used=500000, miner="Miner 1",)
    my_blockchain.add_block(transactions="Transaction 2", gas_limit=2000000, gas_used=1500000, miner="Miner 2",)
    my_blockchain.add_block(transactions="Transaction 3", gas_limit=3000000, gas_used=2500000, miner="Miner 3",)

    # Traverse the blockchain and print the blocks
    print("Blockchain Data (Etherscan-like Format):")
    print("=" * 60)
    my_blockchain.traverse_chain()
