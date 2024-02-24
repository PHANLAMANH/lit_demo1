from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import binascii

privKey = generate_eth_key()
privKeyHex = privKey.to_hex()
pubKeyHex = privKey.public_key.to_hex()
open("ecc_publickey.pem", "w").write(pubKeyHex)
open("ecc_privatekey.pem", "w").write(privKeyHex)
print("Key generated!")
