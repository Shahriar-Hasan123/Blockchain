"""Problem: Program to Create a Merkle Tree in Blockchain"""

import hashlib


class MerkleTree:

    def __init__(self, data_blocks):
        self.data_blocks = data_blocks
        self.tree = []
        self.buildTree()

    def buildTree(self):
        current_layer = [hashlib.sha256(data.encode()).hexdigest() for data in self.data_blocks]
        self.tree.append(current_layer)

        while len(current_layer) > 1:
            next_layer = []
            for i in range(0, len(current_layer), 2):
                if i + 1 < len(current_layer):
                    combined = current_layer[i] + current_layer[i + 1]
                else:
                    combined = current_layer[i] + current_layer[i]
                next_layer.append(hashlib.sha256(combined.encode()).hexdigest())
            self.tree.append(next_layer)
            current_layer = next_layer

    def getRoot(self):
        if self.tree:
            return self.tree[-1][0]
        return None

    def displayTree(self):
        print("Merkel Tree Layer: ")
        for layer_indx, layer in enumerate(self.tree):
            print(f"Layer {layer_indx}:")
            for hash_value in layer:
                print(f" {hash_value} ")
            print()


if __name__ == "__main__":
    data_blocks = ["apple", "banana", "cherry", "date"]
    merkleTree = MerkleTree(data_blocks)
    merkleTree.displayTree()
    print(f"Root Hash: {merkleTree.getRoot()}")
