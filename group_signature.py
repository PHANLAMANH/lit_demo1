from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

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
        directory = 'group_signature/members/' + member_id
        if not os.path.exists(directory):
            os.makedirs(directory)
        # with open("group_signature/members/"+ member_id +"/private_key.pem", "wb") as f:
        #     data = key.export_key()
        #     f.write(data)
        # with open("group_signature/members/"+ member_id +"/public_key.pem", "wb") as f:
        #     data = key.public_key().export_key()
        #     f.write(data)
        print("Added "+ member_id)

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

IdDP = 'hcmus'

group_sig.add_group_member(IdDP)