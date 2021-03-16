import hashlib
import time

class Block(object):

    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
        self.index = index
        self.proof_number = proof_number
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        # self - is used to refer to the class itself. Any variable associated with the class can accessed using it
        # index - is used to track the position of a block within the BlockChain
        # previous_hash - is used to refeence the hash of the previous block within the blockchain
        # data - it gives details of the transactions done, for example, the amount bought
        # timestamp - it inserts a timestamp for all the transactions performed
# Initial structure of the blockchain class

    @property

    def compute_hash(self):
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
        # We import the SHA-256 algorithm into the crypto currency block chain project to help in getting the hashes of the blocks

        return hashlib.sha256(string_block.encode()).hexdigest()
        # Once the values have been placed inside the hashing module, the algorithm will return a 256-bit string denoting the contents
        # of the block

# producing the cryptographic hash of each block based on the above values
# A cryptographic hash function is an algorithm that takes an arbitrary amount of data input- a credential - and produces
# a fixed-size output of enciphered text caled a hash value or "hash"
# The enciphered text can then be stored instead of the password or data itself

class BlockChain(object):

    def __init__(self):
# Building the blockchain, this method will chain together each block and will keep the transactions and include other helper methods
        self.chain = []
# This variable stores all the blocks
        self.current_data = []
# This variable stores information about the transactions in the block
        self.nodes = set()

        self.number_of_blocks = []

        self.build_genesis()
# Used to create the intial block in the chain

    def build_genesis(self):
        self.build_block(proof_number=0, previous_hash=0)
#Creating the genesis block which is the inital or first block in a bloack chain

    def build_block(self, proof_number, previous_hash):
        block = Block(
                index = len(self.chain),
                proof_number = proof_number,
                previous_hash = previous_hash,
                data = self.current_data
        )
        self.current_data = []
        self.chain.append(block)
        return block
# Builds a new block and adds to the chain

    @staticmethod
    def confirm_validity(block,previous_block):
# Checks whether the blockchain is confirm_validity
# This is important for ensuring the integrity of the block chain and making sure there are minimal inconsitencies
        if previous_block.index + 1 != block.index:
            return False
        elif previous_block.compute_hash != block.previous_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False
        return True
# Hashes are important to the security of blockchain, a slight aleration in an object will result in the creation
# of an entirely different hash
# This method utilizes a series of of if statements to assess whether the hash of each block has been compromised


    def get_data(self, closing_date, price, closing_cost, signatures, buyer,seller):
# Declares data of transactions onto a block
        self.current_data.append({
                 'closing_date' : closing_date,
                 'price' : price,
                 'closing_cost' : closing_cost,
                 'signatures' : signatures,
                 'buyer' : buyer,
                 'seller' : seller
        })
        return True
# This method takes the sender's information, reciever's information, and amount and adds the transaction data
# to the current_data list

    @staticmethod

    def proof_of_work(last_proof):
        pass
# Adds to the security of the BlockChain
# In block chain tecnology the Proof of Work (POW) refersto the complexity in mining or generating new blocks on the block chain.
# For example, the PoW can be implemented by identifying a number that solves a problem whenever a user completes some computing work
# The number should be complex to identify but easy to verify

    @property

    def latest_block(self):
        return self.chain[-1]
# Returns the last block in the chain

    def chain_validity(self):
        pass

    def block_mining(self, details_miner):
        self.get_data(
            sender = "0", # This immplies this node has created a new block
            reciever = details_miner,
            quantity = 1, # creating a new block (or identifying the proof number) is awarded with 1
        )
        last_block = self.latest_block
        last_proof_number = last_block.proof_number
        proof_number = self.proof_of_work(last_proof_number)
        last_hash = last_block.compute_hash
        block = self.build_block(proof_number, last_hash)
        return vars(block)

    def create_node(self, address):
        return Block(
            block_data['index'],
            block_data['proof_number'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp = block_data['timestamp']
        )

blockchain = BlockChain()
print("Creating Genesis Block...")
print(blockchain.build_genesis)

# print("\n Mining about to start...")
# print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_number = last_block.proof_number
proof_number = blockchain.proof_of_work(last_proof_number)

def newPurchase():
    blockchain.get_data(
        closing_date = input("Enter the closing date: "),
        price = input("Enter the price: "),
        closing_cost = input("Enter the closing cost: "),
        signatures = input("Enter the parties inital's "),
        buyer = input("Enter buyer name: "),
        seller = input("Enter seller name: ")
        )
    last_hash = last_block.compute_hash
    block = blockchain.build_block(proof_number, last_hash)
    print("\n Purchase Approved")
    print(blockchain.chain)


def menu():
    while True:
        makePurchase = input("Hello would you like to make a purchase? y/n ").lower()
        if (makePurchase == "y"):
            newPurchase()
        else:
            print("Okay, goodbye!")
            break
menu()
