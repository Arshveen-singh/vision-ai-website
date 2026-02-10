import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def get_key(master_key: str, salt: bytes):
    """Derive an AES key from the master key and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(master_key.encode())

def encrypt_api_key(api_key: str, master_key: str):
    """Encrypt the API key using AES-GCM."""
    salt = os.urandom(16)
    key = get_key(master_key, salt)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, api_key.encode(), None)
    
    # Store salt + nonce + ciphertext encoded in base64
    combined = salt + nonce + ciphertext
    return base64.b64encode(combined).decode('utf-8')

def decrypt_api_key(encrypted_data: str, master_key: str):
    """Decrypt the API key using AES-GCM."""
    try:
        data = base64.b64decode(encrypted_data)
        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:]
        
        key = get_key(master_key, salt)
        aesgcm = AESGCM(key)
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted.decode('utf-8')
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None

if __name__ == "__main__":
    # Internal utility to help user encrypt
    import sys
    if len(sys.argv) > 2:
        cmd = sys.argv[1]
        if cmd == "encrypt":
            key_to_encrypt = sys.argv[2]
            m_key = sys.argv[3] if len(sys.argv) > 3 else "default_master_key"
            print(f"Encrypted Value: {encrypt_api_key(key_to_encrypt, m_key)}")
