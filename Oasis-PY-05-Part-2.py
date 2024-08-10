import socket
import threading
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

clients = []

def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")
    client_socket.send(key)  # Send the encryption key to the client

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decrypted_message = cipher_suite.decrypt(message).decode()
            broadcast(decrypted_message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            encrypted_message = cipher_suite.encrypt(message.encode())
            client.send(encrypted_message)

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
