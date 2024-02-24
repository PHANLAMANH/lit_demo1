from secrets import token_bytes
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from ecies import encrypt, decrypt
import pickle

def AES_decrypt(EMD, key):
    nonce_size = 16
    mac_size = 16

    nonce = EMD[:nonce_size]
    cipher_text = EMD[nonce_size:-mac_size]
    mac = EMD[-mac_size:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    decrypted_data = cipher.decrypt(cipher_text)

    try:
        cipher.verify(mac)
        return decrypted_data
    except ValueError:
        print("MAC verification failed. The data may have been tampered with.")
        return None

def hash(bin):
    hash_object = SHA256.new(data=bin)
    return hash_object.digest()

def get_ecc_keys():
    public_key = open("ecc_publickey.pem", "r").read()
    private_key = open("ecc_privatekey.pem", "r").read()
    return public_key, private_key

def main():
    EMD = open("EMD.bin", "rb").read()
    DPInfo = open("DPInfo.bin", "rb").read()
    with open("CERT.bin", "rb") as f:
        CERT = pickle.load(f)
    public_key, private_key = get_ecc_keys()

    #Step 1  
    _DPInfo = decrypt(private_key, DPInfo)
    IdDP = _DPInfo[:len(_DPInfo)-16].decode()
    AES_key = _DPInfo[-16:]

    #Step 2 DO compares IdDP with the DP’s information that DO knew before. => True

    #Step 3
    MD = AES_decrypt(EMD, AES_key)
    open('verify_image.jpg', "wb").write(MD)

    #Step 4
    IdMD = hash(MD)
    
    #Step 5
    _EId = DPInfo + IdMD
    print(_EId)
    if encrypt(public_key, _EId) != CERT["EId"]:
        print("Verification failed!")
        return
    
        



if __name__ == "__main__":
    main()