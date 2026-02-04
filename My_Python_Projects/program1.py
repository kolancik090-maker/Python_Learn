import socket
import threading
import os
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Параметры
SERVERS = {  # Не забудьте заменить адреса!
    "germany": ("vpn.germany.example.com", 5001),
    "netherlands": ("vpn.netherlands.example.com", 5002),
    "finland": ("vpn.finland.example.com", 5003),
}
KEY = os.environ.get('VPN_KEY', secrets.token_bytes(32)) # AES-256 key!
BUFFER_SIZE = 4096

def encrypt(data, key): # AES encryption
    iv = secrets.token_bytes(16) # Initialization vector
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize() # PKCS7 padding
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return iv + encryptor.update(padded_data) + encryptor.finalize()

def decrypt(data, key): # AES decryption
    iv = data[:16]
    ciphertext = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(unpadded_data) + unpadder.finalize()

def handle_client(client_socket, server_address):
    try:
        data = encrypt(data, KEY)
                server_socket.sendall(encrypted_data)
                response = server_socket.recv(BUFFER_SIZE)
                if not response: break
                decrypted_response = decrypt(response, KEY)
                client_socket.sendall(decrypted_response)
    except Exception as e: print(f"Error: {e}")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 5000))
    sock.listen(5)
    try:
        while True:
            client_sock, addr = sock.accept()
            server_addr = secrets.choice(list(SERVERS.values()))
            threading.Thread(target=handle_client, args=(client_sock, server_addr)).start()
    except KeyboardInterrupt: pass
    finally: sock.close()

if __name__ == "__main__":
    main()
