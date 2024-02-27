from web3 import Web3

# Initialize web3 connection (replace with your Ethereum node URL)
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Load the contract ABI and address (replace with your own)
contract_abi = [...]  # Contract ABI (from compilation)
contract_address = "0xYourContractAddress"  # Example address

# Initialize the contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def store_data(ipfs_cid):
    try:
        # Call the smart contract function to store the IPFS CID
        tx_hash = contract.functions.storeData(ipfs_cid).transact()

        # Wait for the transaction to be mined
        w3.eth.waitForTransactionReceipt(tx_hash)

        print(f"IPFS CID stored successfully in transaction: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error storing IPFS CID: {e}")

if __name__ == "__main__":
    # Example IPFS CID (replace with your own)
    sample_ipfs_cid = "QmYourIPFSCID"

    store_data(sample_ipfs_cid)
