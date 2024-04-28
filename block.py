import time
from helper import computeMerkelRoot, computeBlockHeaderHash

class BlockHeader:
    def __init__(self, ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData):
        self.version = ver
        self.difficulty_threshold = difficulty_threshold  # Adjust after every 2016 blocks
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.nonce = nonce
        self.minerID = minerID
        self.merkle_root = computeMerkelRoot(TxData)

class Block:
    def __init__(self, ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData, blockHeight):
        self.data = TxData
        self.header = BlockHeader(ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData)
        self.blockHeight = blockHeight
        self.blockHash = computeBlockHeaderHash(self.header)
        self.previous_2016_block_timestamp = timestamp

    def getHeader(self):
        return self.header
    
    def getDifficulty(self):
        return self.header.difficulty_threshold

    def getPreviousBlockHash(self):
        return self.header.previousHash

    def getTimeStamp(self):
        return self.header.timestamp

    def getTxData(self):
        return self.data
    
    def getHash(self):
        return self.blockHash

    def getHeight(self):
        return self.blockHeight

    def display(self):
        print("\n--------------------------------------")

        print("Version:", self.header.version)
        print("Diffculty Threshold:", self.header.difficulty_threshold)
        print("Previous blockHash:", self.header.previousHash)
        print("Timestamp:", time.ctime(self.header.timestamp))
        print("Nonce:", self.header.nonce)
        print("Miner ID:", self.header.minerID)
        print("Merkle Root:", self.header.merkle_root)

        print("Data:", self.data)
        print("Block Height:", self.blockHeight)    
        print("blockHash:", self.blockHash)
        print("previous_2016_block_timestamp:", self.previous_2016_block_timestamp)
        

        print("--------------------------------------\n")