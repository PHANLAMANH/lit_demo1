from chacha20poly1305 import ChaCha20Poly1305
from secrets import token_bytes

key = token_bytes(32)  # Replace with your actual 32-byte key
aead = ChaCha20Poly1305(key)

nonce = token_bytes(12) # Generate a random nonce for each encryption
plaintext = b'your_data_to_encrypt'

ciphertext = aead.encrypt(nonce, plaintext)

# Decryption
decrypted_data = aead.decrypt(nonce, ciphertext)

print(decrypted_data)  # Should print your original plaintext
