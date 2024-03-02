from data_storing import store_data
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

public_key1 = """
        -----BEGIN PUBLIC KEY-----
        MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGx5AEsSQYiPfjCBR4TYuS0mR/RA
        hUiRj7EteqfmerSn5lY9NkP+hcXFKN/u42+UEM7PygkbodvvQoPlGz5XpgpUJRKp
        e5P9xmmX7vJR5DkKpy7x1pEF15tHCCzqsuuv+qeQvWvuLC1VYQfYlu9dmFEf1YHd
        Ct1WBGOyGpPQ0jFjAgMBAAE=
        -----END PUBLIC KEY-----
        """
private_key1 = """
        -----BEGIN RSA PRIVATE KEY-----
        MIICXAIBAAKBgGx5AEsSQYiPfjCBR4TYuS0mR/RAhUiRj7EteqfmerSn5lY9NkP+
        hcXFKN/u42+UEM7PygkbodvvQoPlGz5XpgpUJRKpe5P9xmmX7vJR5DkKpy7x1pEF
        15tHCCzqsuuv+qeQvWvuLC1VYQfYlu9dmFEf1YHdCt1WBGOyGpPQ0jFjAgMBAAEC
        gYBYFvPcA1lg81cBQRu5kN7hAaORggw7YKqWsl5Xl96yc1+lTVSSZ1Jvx6toH/Jn
        nJEBwtFKEDykBWu4/Qfg2wEldXIm8fjQFxo0gzvVeLt3HBTBXaA83htxtxyjHy9Z
        6ocjXKqTso9SNcvjDo4qlSAAJE5/d2iZN/ty6qf9lmWm0QJBALyNmHPCi6LIpHu8
        +AUUocW8PBZvKg7LK3OW32cUHcNINiyLyTjSda815LqBL4h4QgUTNBVyrslvzaoy
        P0oBhTcCQQCTRi+RKa75xPIsXWsrdB1CiFrn8NeJnl/TODnIwfD2JgTlpFpyTZ8J
        GdiFcmUW9lcZiL962Fq4xZiW3gG0mcs1AkEAqftUtvdp/wS3FD5Vse7ZsHN0EB2D
        YvbSY1BecoT2F/jfreUPMMS7B4ukembAPV181ypqx/Mtk7fRR2ApIkSgnQJAFN81
        jpUhvzQyPidfMOFb5Dn+6DAx28cePYkSZ2lVBQ2OVB1e1CQ8DcYj8YWs3fw7i9rd
        iENxWA5o+bis9TN2oQJBALHC+UnMi4joyGviFoJU7J20uAvHRzA2YNemnKyM2NNt
        ZBo5mJhmBA9sVkPbbVWoFQcAVZGYamxt9SC0v0VLpzw=
        -----END RSA PRIVATE KEY-----
        """
public_key2 = """
        -----BEGIN PUBLIC KEY-----
        MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAI74wWhMzg5aSy/zSB19PQEi0/qSGZBo
        1lAsBH54TqEqyb9tyWjtn8ZWF5sP2DQk4Tt2g4GJYD28pwEQ0fQAzosCAwEAAQ==
        -----END PUBLIC KEY-----
        """
private_key2 = """
        -----BEGIN RSA PRIVATE KEY-----
        MIIBOwIBAAJBAI74wWhMzg5aSy/zSB19PQEi0/qSGZBo1lAsBH54TqEqyb9tyWjt
        n8ZWF5sP2DQk4Tt2g4GJYD28pwEQ0fQAzosCAwEAAQJAbzQ/Q0ASOgmzV62T1xQV
        gi+zz78Z0UAqChvitvgeuK3YPoWqQS47TlmxbtiWt0zGZhLEkUWDJpBb1lbL5Iml
        uQIhAP9LYPubfDRiCykfImWzIgspqrdaZiFScZKVgzY1EBBXAiEAj13ofY4+LUfp
        ubl7oRlp0f4LH1+XIggjMo8gVkdnAu0CIE5+KKVzmu6oLnJIRlUqjI8OEpUpUDly
        lcTR/3PNQNElAiEAgD3xXHZjmd+M66xGMVnpNYU4b8zzBOcgjPZIZ8UhGRUCIQCp
        4MCCnad+6Zx/iIMXuTXsBXrkAVLcFY9wHwkhhdfVGw==
        -----END RSA PRIVATE KEY-----
        """
# Load the public keys
public_key1_obj = serialization.load_pem_public_key(public_key1.encode(), backend=default_backend())
public_key2_obj = serialization.load_pem_public_key(public_key2.encode(), backend=default_backend())

# Load the private keys
private_key1_obj = serialization.load_pem_private_key(private_key1.encode(), password=None, backend=default_backend())
private_key2_obj = serialization.load_pem_private_key(private_key2.encode(), password=None, backend=default_backend())

def purchase_data(data_user, group_manager, category, keywords):
    """Simulates data purchase algorithm.

    Args:
        data_user (DataUser): Data user object.
        group_manager (GroupManager): Group manager object.
        category (str): Data category.
        keywords (str): Data keywords.

    Returns:
        bool: True if purchase is successful, False otherwise.
    """

    # Step 1: Find data owners
    data_owners = group_manager.get_data_owners(category, keywords)

    # Step 2: User selects data owner and sends encrypted purchase request
    chosen_owner = data_user.choose_owner(data_owners)
    encrypted_request = data_user.encrypt_request(chosen_owner.public_key, category, keywords)

    # Step 3: Data owner processes request
    decrypted_request = chosen_owner.decrypt_request(encrypted_request)

    # Validate user identity and payment (simulated)
    if not data_user.validate():
        print("Invalid user or payment")
        return False

    # Step 4: Data owner prepares data and key
    data = b"Simulating data content..."  # Replace with actual data
    key = get_random_bytes(16)  # Generate random symmetric key (16 bytes for AES)
    encrypted_data = AES.new(key, AES.MODE_CBC).encrypt(data)
    data_hash = sha256.new(data).hexdigest()

    # Step 5: Send encrypted data and key hash
    chosen_owner.send_data(data_user.public_key, encrypted_data, data_hash)

    # Step 6: User decrypts data and verifies hash
    decrypted_data = data_user.decrypt_data(key, encrypted_data)
    if sha256(decrypted_data).hexdigest() != data_hash:
        print("Data integrity compromised")
        return False

    # Step 7: User confirms purchase
    data_user.confirm_purchase()

    # Step 8: Data owner sends symmetric key
    chosen_owner.send_key(data_user.public_key, key)

    # Step 9: Escrow deposit is returned (simulated)
    group_manager.return_escrow_deposit(chosen_owner)

    return True


def resolve_dispute(data_user, data_owner, encrypted_data, data_hash, key, group_manager):
    """Simulates dispute resolution algorithm.

    Args:
        data_user (DataUser): Data user object.
        data_owner (DataOwner): Data owner object.
        encrypted_data (bytes): Encrypted data.
        data_hash (str): Data hash.
        key (bytes): Symmetric key.
        group_manager (GroupManager): Group manager object.

    Returns:
        bool: True if dispute is resolved in favor of data user, False otherwise.
    """
    # Group manager verifies evidence (simulated)
    if group_manager.verify_evidence(encrypted_data, data_hash, key):
        # Penalize data owner and return deposit to user (simulated)
        group_manager.penalize_data_owner(data_owner)
        group_manager.return_escrow_deposit(data_user)
        print(f"Dispute resolved in favor of {data_user.name}")
        return True
    else:
        # Dismiss complaint and inform user (simulated)
        group_manager.inform_user(data_user)
        print(f"Complaint from {data_user.name} dismissed")
        return False


class DataUser:
    def __init__(self, name, public_key, private_key):
        self.name = name
        self.public_key1 = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        self.private_key1 = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        self.public_key2 = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        self.private_key2 = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())

    def decrypt_request(self, encrypted_request):
        return self.private_key.decrypt(encrypted_request, padding=RSA.PKCS1_OAEP)

    def send_data(self, user_public_key, encrypted_data, data_hash):
        print(f"{self.name} sending encrypted data and hash to user")
        # Simulate sending data and hash over a secure channel (replace with actual implementation)

    def send_key(self, user_public_key, key):
        encrypted_key = user_public_key.encrypt(key, padding=RSA.PKCS1_OAEP)
        print(f"{self.name} sending encrypted key to user")
        # Simulate sending encrypted key over a secure channel (replace with actual implementation)

class DataOwner:
    def __init__(self, name, public_key, private_key):
        self.name = name
        self.public_key1 = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        self.private_key1 = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        self.public_key2 = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        self.private_key2 = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())

    def choose_owner(self, data_owners):
        # Simulate user selection process (replace with actual implementation)
        return data_owners[0]

    def encrypt_request(self, public_key, category, keywords):
        request = f"Requesting data: {category}, {keywords}".encode()
        return public_key.encrypt(request, padding=RSA.PKCS1_OAEP)

    def validate(self):
        # Simulate user identity and payment validation (replace with actual implementation)
        return True

    def decrypt_data(self, key, encrypted_data):
        return AES.new(key, AES.MODE_CBC).decrypt(encrypted_data)

    def confirm_purchase(self):
        print(f"{self.name} confirms purchase")

class GroupManager:
    def __init__(self):
        # Simulate data owner registration (replace with actual implementation)
        
        self.data_owners = {
            "DO1": DataOwner("DO1",public_key1, private_key1),
            "DO2": DataOwner("DO2", public_key2, private_key2)
        }
        self.escrow_deposits = {"DO1": 100, "DO2": 200}  # Simulate escrow deposits

    def get_data_owners(self, category, keywords):
        # Simulate filtering based on category and keywords (replace with actual implementation)
        return list(self.data_owners.values())

    def return_escrow_deposit(self, data_owner):
        print(f"Escrow deposit returned to {data_owner.name}")

    def penalize_data_owner(self, data_owner):
        self.escrow_deposits[data_owner.name] -= 50
        print(f"{data_owner.name} penalized")

    def inform_user(self, data_user):
        print(f"Complaint from {data_user.name} dismissed")

    def verify_evidence(self, encrypted_data, data_hash, key):
        # Simulate evidence verification (replace with actual implementation)
        return True  # Change this to return True/False based on verification logic

# Example usage
  
data_user = DataUser("DU1", public_key1, private_key1)
group_manager = GroupManager()

# Purchase
if purchase_data(data_user, group_manager, "Real estate", ["house prices"]):
    print("Purchase successful")
else:
    print("Purchase failed")

# Dispute (replace with actual dispute details)
resolve_dispute(data_user, group_manager.data_owners["DO1"], b"simulated_encrypted_data", "simulated_hash", b"simulated_key")



