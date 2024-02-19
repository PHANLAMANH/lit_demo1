from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

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

# Example usage
group_sig = GroupSignature()

# Add group members
group_sig.add_group_member("Alice")
group_sig.add_group_member("Bob")

# Alice signs a message
message = b"Hello, world!"
alice_signature = group_sig.sign_message(message, "Alice")
print("Alice's Signature:", alice_signature)

# Verify Alice's signature
is_valid = group_sig.verify_signature(message, alice_signature)
print("Alice's Signature is valid:", is_valid)

