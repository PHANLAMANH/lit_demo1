from secrets import token_bytes
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from ecies import encrypt
import pickle
from chacha20poly1305 import ChaCha20Poly1305

IdDP = 'hcmus'

class GroupSignature:
    def __init__(self):
        with open("group_signature/manager/private_key.pem", "rb") as f:
            data = f.read()
            self.group_manager_private_key = RSA.import_key(data)
        with open("group_signature/manager/public_key.pem", "rb") as f:
            data = f.read()
            self.group_manager_public_key = RSA.import_key(data)
        self.group_members = {}

    def add_group_member(self, member_id):
        key = RSA.generate(2048)
        self.group_members[member_id] = key.publickey()

    def sign_message(self, message, member_id):
        if member_id not in self.group_members:
            raise ValueError("Member ID not found")
        member_public_key = self.group_members[member_id]
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

group_sig = GroupSignature()

group_sig.add_group_member(IdDP)

def img_to_bin(path):
    with open(path, 'rb') as file:
        image_bin = file.read()
    return image_bin

def hash(bin):
    hash_object = SHA256.new(data=bin)
    return hash_object.digest()

def AES_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, mac = cipher.encrypt_and_digest(data)
    EMD = nonce + cipher_text + mac
    return EMD

def ChaCha20Poly1305_encrypt(data, key):
    cip = ChaCha20Poly1305(key)
    nonce = token_bytes(12)
    ciphertext = cip.encrypt(nonce, data)
    return ciphertext + nonce

def get_rsa_keys():
    with open("privatekey.pem", "rb") as f:
        data = f.read()
        private_key = RSA.import_key(data)
    with open("publickey.pem", "rb") as f:
        data = f.read()
        public_key = RSA.import_key(data)
    return public_key, private_key

def get_ecc_keys():
    public_key = open("ecc_publickey.pem", "r").read()
    private_key = open("ecc_privatekey.pem", "r").read()
    return public_key, private_key

def produce():
    path = "image.jpg"
    img_bin = img_to_bin(path)
    public_key, _ = get_ecc_keys()

    #Step 2
    IdMD = hash(img_bin)

    #Step 3
    AES_key = token_bytes(16)

    #Step 4
    EMD = AES_encrypt(img_bin, AES_key)

    #Step 5
    _DPInfo = IdDP.encode() + AES_key
    DPInfo = encrypt(public_key, _DPInfo)

    #Step 6
    _EId = DPInfo + IdMD
    EId = encrypt(public_key, _EId)

    #Step 7
    SD = group_sig.sign_message(EMD, IdDP)

    #Step 8 
    CERT = {
        "SD": SD,
        "EId": EId
    }

    #Step 9
    open("EMD.bin", "wb").write(EMD)
    open("DPInfo.bin", "wb").write(DPInfo)
    with open("CERT.bin", "wb") as f:
        pickle.dump(CERT, f)

if __name__ == "__main__":
    produce()
