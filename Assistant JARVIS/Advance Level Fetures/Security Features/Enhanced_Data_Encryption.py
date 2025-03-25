import os
import hashlib
import argparse
import logging
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import time

# Set up logging
logging.basicConfig(filename='data_encryption.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataEncryption:
    def __init__(self, password=None):
        self.password = password
        self.key = self.generate_key()

    def generate_key(self):
        """Generate a key based on the provided password."""
        if self.password:
            password_bytes = self.password.encode()
            salt = b'\x00' * 16  # Use a static salt for demonstration (not secure)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
            logging.info("Key generated from password.")
            return key
        else:
            key = Fernet.generate_key()
            logging.info("Generated and saved a new key.")
            return key

    def encrypt_file(self, input_file, output_file):
        """Encrypt a file."""
        fernet = Fernet(self.key)
        with open(input_file, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
        with open(output_file, 'wb') as file:
            file.write(encrypted)

        original_hash = self.hash_file(input_file)
        encrypted_hash = self.hash_file(output_file)

        logging.info("Encrypted file %s and saved to %s", input_file, output_file)
        logging.info("Original file hash: %s", original_hash)
        logging.info("Encrypted file hash: %s", encrypted_hash)

    def decrypt_file(self, input_file, output_file):
        """Decrypt a file."""
        fernet = Fernet(self.key)
        with open(input_file, 'rb') as file:
            encrypted = file.read()
        
        decrypted = fernet.decrypt(encrypted)
        with open(output_file, 'wb') as file:
            file.write(decrypted)

        decrypted_hash = self.hash_file(output_file)

        logging.info("Decrypted file %s and saved to %s", input_file, output_file)
        logging.info("Decrypted file hash: %s", decrypted_hash)

    def hash_file(self, file_path):
        """Return the SHA-256 hash of the file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def process_batch(self, file_paths, output_dir, action):
        """Process multiple files in a batch."""
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            output_file = os.path.join(output_dir, file_name)

            if action == 'encrypt':
                self.encrypt_file(file_path, output_file)
            elif action == 'decrypt':
                self.decrypt_file(file_path, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files using Fernet encryption.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform: encrypt or decrypt')
    parser.add_argument('input_file', type=str, help='Path to the input file or directory for batch processing')
    parser.add_argument('output_file', type=str, help='Path to save the output file or directory for batch processing')
    parser.add_argument('--password', type=str, help='Password for key derivation')

    args = parser.parse_args()

    encryption_tool = DataEncryption(password=args.password)

    # Check if input is a directory for batch processing
    if os.path.isdir(args.input_file):
        file_paths = [os.path.join(args.input_file, f) for f in os.listdir(args.input_file)]
        encryption_tool.process_batch(file_paths, args.output_file, args.action)
    else:
        if args.action == 'encrypt':
            encryption_tool.encrypt_file(args.input_file, args.output_file)
        elif args.action == 'decrypt':
            encryption_tool.decrypt_file(args.input_file, args.output_file)

    print(f"File(s) {args.action}ed successfully.")
