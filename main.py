from blockchain import Blockchain
from block import *

blockchain = Blockchain()
print("BlockChain Created.")

# __init__(self, ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData, blockHeight)

last_block = blockchain.genesisBlock


while(True):
    print("Press 1 to enter a new Block.")
    print("Press 2 to add a sample block for testing purposes.")
    print("Press 3 to Display all the current blockchain blocks.")
    print("Press 4 to Display the changing difficulty.")
    print("Press 5 to exit the code.")

    command = int(input())

    if command == 1:
        print("Enter the input fields")
        ver = int(input("Enter version number: "))
        difficulty_threshold = int(input("Enter difficulty_threshold: "))
        previousHash = (input("Enter previousHash: "))

        timestamp = (input("Enter timestamp: "))
        nonce = int(input("Enter nonce: "))
        minerID = (input("Enter minerID: "))
        TxData = (input("Enter TxData: "))
        blockHeight = int(input("Enter blockHeight: "))
        block = Block( ver, difficulty_threshold, previousHash, timestamp, nonce, minerID, TxData, blockHeight)
        blockchain.verifyAndAdd(block)


    elif command == 2:

        difficulty_threshold = "8888888888888888888888888888888888888888888888888888888888888888"
        height = last_block.getHeight()+1
        curr_time = time.time()
        for nonce in range(10):

            new_test_block = Block(1, difficulty_threshold, last_block.getHash(), curr_time, nonce, "Test Miner", "Block Transaction number" + str(height), height)
            if blockchain.verifyAndAdd(new_test_block):
                last_block = new_test_block
                print("Block added.")
                break
            else:
                print("Trying another nonce...")

        
        

    elif command == 3:
        blockchain.displayBlockchain()



    elif command == 4:
        for i in range(2018):
            difficulty_threshold = "8888888888888888888888888888888888888888888888888888888888888888"
            height = last_block.getHeight()+1
            # curr_time = time.time()
            for nonce in range(10):
                new_test_block = Block(1, difficulty_threshold, last_block.getHash(), time.time(), nonce, "Test Miner", "Block Transaction number" + str(height), height)
                if blockchain.verifyAndAdd(new_test_block):
                    last_block = new_test_block
                    print("Block added.\n")
                    time.sleep(0.01)
                    break
                else:
                    print("Trying another nonce...")


    elif command == 5:
        print("Exiting blockchain. Everything is deleted.")
        break

    else:
        print("Invalid command")


