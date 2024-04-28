import hashlib

def computeMerkelRoot(data):
    # Implement your Merkle root calculation here
    # For now, returning a placeholder
    return "merkelRoot"

def computeBlockHeaderHash(header):
    blockInString = ""
    blockInString += str(header.version) + "#"
    blockInString += str(header.difficulty_threshold) + "#"
    blockInString += header.previousHash + "#"
    blockInString += str(header.timestamp) + "#"  # Assuming timestamp is already a string
    blockInString += str(header.nonce) + "#"
    blockInString += header.minerID + "#"
    blockInString += header.merkle_root

    # Using SHA-256 for hashing
    hash_object = hashlib.sha256(blockInString.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig