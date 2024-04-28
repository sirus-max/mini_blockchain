import time
from block import Block
from helper import computeMerkelRoot, computeBlockHeaderHash

class Blockchain:
    def __init__(self):
        # def __init__(self, ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData, blockHeight)
        self.genesisBlock = Block(1, "8888888888888888888888888888888888888888888888888888888888888888", "GenesisBlock", time.time(), 100, "Genesis Block Miner", "Init Transactions", 1)
        self.max_height = 1
        self.all_blocks = [self.genesisBlock]

    def propagateBlockToPeers(self, block):
        # this function sends a block to its peers once it has verified and added that block to its blockchain
        pass

    def listenToPeers(self):
        # keep listening to the peers from the open port and when a new block comes with enter code verify and add this to the blockchain
        pass

    def addBlock(self, block):
        self.max_height = max(self.max_height, block.getHeight())
        self.all_blocks.append(block)
        self.propagateBlockToPeers(block)
        return True

    def verifyBlock(self, block):
        isValid = True
        # finding previous block
        found = False
        for b in self.all_blocks:
            if block.getPreviousBlockHash() == b.getHash():
                previousBlock = b
                found = True
        if found == False:
            print("Previous Block is not present in the blockchain.")
            isValid = False
            return False
        
        header = block.getHeader()

        if header.previousHash != previousBlock.getHash():
            print("Previous Hash does not match.")
            isValid = False
            return False
        elif block.getTimeStamp() <= previousBlock.getTimeStamp():
            print("Timestamp of block is not greater than previous block's timestamp.")
            isValid = False
            return False
        elif header.merkle_root != computeMerkelRoot(block.getTxData()):
            print("Merkel root in header not matching the computed Merkel root.")
            isValid = False
            return False

        if not self.verifyTX(block.getTxData()):
            print("Transactions not verified.")
            return False


        # Add checks for difficulty, nonce, hash
        block_hash = computeBlockHeaderHash(block.header)
        if block.getHash() != block_hash:
            print("Block Hash does not match.")
            isValid = False
            return False
        
        difficulty_target = self.calculateBlockDifficulty(block)
        if block.getDifficulty() != difficulty_target:
            print("Difficulty does not match.")
            print("Expected value: ", difficulty_target)
            print(block.getDifficulty())
            print(difficulty_target)
            isValid = False
            return False
        
        if block_hash > difficulty_target:
            print("Block hash is greater than the difficulty target. Try different Nonce.")
            isValid = False
            return False
        
        if block.getHeight() != previousBlock.getHeight()+1:
            print("Height not valid.")
            isValid = False
            return False

        return isValid

    def calculateBlockDifficulty(self, toBeAddedBlock):
        for b in self.all_blocks:
            if toBeAddedBlock.getPreviousBlockHash() == b.getHash():
                prevBlock = b
        print(prevBlock.getDifficulty())
        diff = int(prevBlock.getDifficulty(), 16)
        print(diff)
        if prevBlock.getHeight() % 2016 == 0:
            targetTime = 2 * 7 * 24 * 60 * 60  # 2 weeks in seconds
             
            endBlock = toBeAddedBlock
            actualTime = endBlock.getTimeStamp() - toBeAddedBlock.previous_2016_block_timestamp
            print(endBlock.getTimeStamp())
        


            
            print(toBeAddedBlock.previous_2016_block_timestamp)
            # Calculate the adjustment factor
            adjustmentFactor = actualTime / targetTime
            print(actualTime)
            
            print(adjustmentFactor)
            
            # Adjust the difficulty
            diff = diff * adjustmentFactor
            diff = int(diff)
            toBeAddedBlock.previous_2016_block_timestamp = toBeAddedBlock.getTimeStamp()
        else:
            toBeAddedBlock.previous_2016_block_timestamp = prevBlock.previous_2016_block_timestamp
        # print(hex(diff)[2:])
        return hex(diff)[2:]

    def displayBlockchain(self):
        for block in reversed(self.all_blocks):
            block.display()

    def verifyTX(self, txData):
        return True
        # Implement transaction verification logic here
        pass
    


    def verifyAndAdd(self, toBeAddedBlock):

        # finding previous block
        found = False
        for block in self.all_blocks:
            if toBeAddedBlock.getPreviousBlockHash() == block.getHash():
                previousBlock = block
                found = True
        if found == False:
            print("Previous Block is not present in the blockchain.")
            return False

        
        
        if not self.verifyBlock(toBeAddedBlock):
            print("Block verification failed.")
            return False
        
        

        print("Adding New Block to Blockchain")
        time.sleep(0.01)
        self.addBlock(toBeAddedBlock)
        return True