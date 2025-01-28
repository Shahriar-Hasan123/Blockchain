"""Program to Prove Membership and Nonmembership in a Merkle Tree 
Blockchain """

import hashlib


class MerkleTree:

    def __init__(self, data_blocks):
        self.data_blocks = data_blocks
        self.tree = []
        self.buildTree()

    def hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

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

    def get_merkle_path(self, data_block):

        if data_block not in self.data_blocks:
            return None

        index = self.data_blocks.index(data_block)
        path = []

        for layer in self.tree[:-1]:  # Exclude the root layer
            sibling_index = (
                index ^ 1
            )  # Get sibling index (XOR to flip between odd/even)
            if sibling_index < len(layer):
                sibling_hash = layer[sibling_index]
                direction = "left" if sibling_index < index else "right"
                path.append((sibling_hash, direction))
            index //= 2  # Move to the parent node

        return path

    def verify_membership(self, proof, data_block):
        if not proof:
            return False

        computed_hash = self.hash(data_block)

        for sibling_hash, direction in proof:
            if direction == "left":
                computed_hash = self.hash(sibling_hash + computed_hash)
            else:
                computed_hash = self.hash(computed_hash + sibling_hash)

        return computed_hash == self.getRoot()

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
    print()

    # Target block to verify
    target_block = "date"
    proof = merkleTree.get_merkle_path(target_block)
    is_member = merkleTree.verify_membership(proof, target_block)
    print(f"Is '{target_block}' a member of the tree? {is_member}")
