from web3 import Web3

# Initialize web3 connection (replace with your Ethereum node URL)
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Load the contract ABI and address (replace with your own)
contract_abi = [
	{
		"inputs": [],
		"name": "getCert",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getDpInfo",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEmdLink",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getPaymentAdd",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getPrice",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getSC",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_cert",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dpInfo",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_emdLink",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_paymentAdd",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_sc",
				"type": "string"
			}
		],
		"name": "setData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
  # Contract ABI (from compilation)
contract_address = "0x8f0dDb7221C0F43FB5FA3098825eE5cB6E19EBc3"  # Example address

# Initialize the contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def store_data(ipfs_cid):
    try:
        # Example values for the missing arguments
        _cert = "example_cert"
        _dpInfo = "example_dpInfo"
        _emdLink = "example_emdLink"
        _paymentAdd = "example_paymentAdd"
        _price = 100 # Example price, adjust as needed
        _sc = "example_sc"

        # Specify the account from which the transaction is being sent
        from_address = "0x8f0dDb7221C0F43FB5FA3098825eE5cB6E19EBc3"
        private_key = "0x6e75e1873a64c873e1b9ba8f16c0ddbff1be679d43095ad6d56d072ce3b28fca"

        # Create a transaction dictionary with the necessary details
        tx = {
            'from': from_address,
            'nonce': w3.eth.get_transaction_count(from_address),
            'gas': 2000000,
            'gasPrice': Web3.to_wei('20', 'gwei'),
        }

        # Sign the transaction with the private key
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)

        # Send the signed transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction to be mined
        w3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"Data stored successfully in transaction: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error storing data: {e}")
if __name__ == "__main__":
    # Example IPFS CID (replace with your own)
    sample_ipfs_cid = "QmVz1LLyMNEK6MbqEpbpUDHswkgZzrhQssTc2xXARJGoQB"

    store_data(sample_ipfs_cid)
