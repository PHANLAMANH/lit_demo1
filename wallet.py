from web3 import Web3

# Connect to your local Ganache instance
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Set the chain ID for transactions
w3.eth.defaultAccount = w3.eth.accounts[0]  # Use the first account for transactions
w3.eth.defaultBlock = 'latest'
w3.eth.chainId =  1337  # Use the chain ID for Ganache

# Make sure you have the private key and the recipient's address
private_key = '0x9a7ffe71c4660d44226bcf84ac10544a820cce9157263867c3697aa76afe63d4'
recipient_address = '0x10E8131d1b046B4d1A551cE85209529f42738686'

# Get the nonce for the sender's address
nonce = w3.eth.get_transaction_count(w3.eth.defaultAccount)

# The amount of Ether to send (in Wei)
amount_in_ether =  0.3
amount_in_wei = w3.to_wei(amount_in_ether, 'ether')

# Prepare the transaction
transaction = {
    'to': recipient_address,
    'value': amount_in_wei,
    'gas':  210000000,
    'gasPrice': w3.to_wei('50', 'gwei'),
    'nonce': nonce,
    'chainId': w3.eth.chainId,
    'data': '0x'  # Include any data you want to send with the transaction
}

# Sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

# Print the transaction hash
print(f"Transaction Hash: {transaction_hash.hex()}")

# Get the transaction receipt
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print(f"Transaction Receipt: {transaction_receipt}")