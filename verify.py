from secrets import token_bytes
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from ecies import encrypt, decrypt
import os
import pickle

class GroupSignature:
    def __init__(self):
        with open("group_signature/manager/private_key.pem", "rb") as f:
            data = f.read()
            self.group_manager_private_key = RSA.import_key(data)
        with open("group_signature/manager/public_key.pem", "rb") as f:
            data = f.read()
            self.group_manager_public_key = RSA.import_key(data)

        self.group_members = os.listdir("group_signature/members")

    def sign_message(self, message, member_id):
        if member_id not in self.group_members:
            raise ValueError("Member ID not found")
        hash_obj = SHA256.new(message)
        signature = pkcs1_15.new(self.group_manager_private_key).sign(hash_obj)
        return signature

    def verify_signature(self, message, signature):
        hash_obj = SHA256.new(message)
        try:
            pkcs1_15.new(self.group_manager_public_key).verify(hash_obj, signature)
            return True
        except (ValueError, TypeError):
            return False

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

group_sig = GroupSignature()

def verify():
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
    
    #Step 5 Verify
    _EId = DPInfo + IdMD
    
    #Step 6: Verify Group Signature

    if group_sig.verify_signature(EMD, CERT["SD"]):
        print("Verification succeed")
    else:
        print("Verification faied")

if __name__ == "__main__":
    verify()