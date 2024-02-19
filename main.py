import hashlib
from secrets import token_bytes
import string
import rsa
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


HASH_FUNC = "SHA256"
IdDP = 'hcmus'

class GroupSignature:
    def __init__(self):
        self.group_manager_private_key = RSA.generate(2048)
        self.group_manager_public_key = self.group_manager_private_key.publickey()
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
    h = hashlib.new(HASH_FUNC)
    h.update(bin)
    return h.digest()

def AES_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, mac = cipher.encrypt_and_digest(data)
    EMD = nonce + cipher_text + mac
    return EMD

def get_rsa_keys():
    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return public_key, private_key

def main():
    path = "image.jpg"
    img_bin = img_to_bin(path)
    IdMD = hash(img_bin)
    AES_key = token_bytes(16)
    EMD = AES_encrypt(img_bin, AES_key)
    with open("EMD", "wb") as f:
        f.write(EMD)
    public_key, _ = get_rsa_keys()
    _DPInfo = IdDP.encode() + AES_key 
    print(len(_DPInfo))
    DPInfo = rsa.encrypt(_DPInfo, public_key)
    _EId = DPInfo + IdMD
    print(len(DPInfo))
    EId = rsa.encrypt(_EId, public_key)
    



if __name__ == "__main__":
    main()
