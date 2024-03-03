from Crypto.PublicKey import RSA

def generate_rsa_keys():
    group_manager_private_key = RSA.generate(2048)
    group_manager_public_key = group_manager_private_key.publickey()
    with open("group_signature/manager/private_key.pem", "wb") as f:
        data = group_manager_private_key.export_key()
        f.write(data)
    with open("group_signature/manager/public_key.pem", "wb") as f:
        data = group_manager_public_key.export_key()
        f.write(data)
    print("Key generated.")

if __name__ == "__main__":
    generate_rsa_keys()
