import hashlib
import json
from time import time
import random

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGenesisBlock()
        currentBlock.previousHash = self.chain[-1].currentHash        
        isBlockMined = currentBlock.mineBlock()
        if(isBlockMined):
            self.chain.append(currentBlock)
            return True
        return False   
    
    def createGenesisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        previousBlockHash = previousBlock.calculateHash()
        if(previousBlockHash != currentBlock.previousHash):
            return False
                
        return True
        
class Block:
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.isValid = None
        self.difficulty = 3
        # Create nonce variable and set it to 0
        
        self.currentHash = self.calculateHash()
    
    # Remove the randomString
    def calculateHash(self, randomString = "", timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp
        # Replace the randomString with self.nonce
        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions, default=str)+ str(randomString)
        return generateHash(blockString)
    
    def mineBlock(self):
        target = "0" * self.difficulty
         
        miningLimit = 4000
        # Replace attempts with nonce object variable using nonce value we will validate the block
        attempts = 1
        
        while self.currentHash[:self.difficulty] != target:
            # Remove generating randomString
            randomString = str(random.random()).encode('utf-8')
            
            # Increment self.nonce instead of attempts

            # Remove passing randString to calculateHash() method
            self.currentHash = self.calculateHash(randomString)
                        
            # Comment following
            if(attempts >= miningLimit):
               return False
            
            # Remove increment attempts
            attempts += 1
            
        return True

    def addTransaction(self, transaction):
        if transaction:
            self.transactions.append(transaction)
            if len(self.transactions) == 3:
                    return "Ready"
            return "Add more transactions"


       
