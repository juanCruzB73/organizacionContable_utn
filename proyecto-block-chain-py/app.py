import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash 
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"  # Corrected variable name
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"BLOCK MINED: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash 
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1] 

            if current_block.hash != current_block.calculate_hash():
                print("Current block hash is not valid")
                return False
            if current_block.previous_hash != previous_block.hash:
                print("Previous block hash is not valid")
                return False
        return True

# Testing the implementation
if __name__ == "__main__":
    blockchain = Blockchain()

    print("Mining block 1...")
    blockchain.add_block(Block(1, "", "Block 1 Data"))

    print("Mining block 2...")
    blockchain.add_block(Block(2, "", "Block 2 Data"))

    print("\nBlockchain is valid:", blockchain.is_chain_valid())

    # Print the entire blockchain
    for block in blockchain.chain:
        print(f"\nIndex: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Data: {block.data}")
        print(f"Nonce: {block.nonce}")
        print(f"Timestamp: {block.timestamp}")
        print("---------")

