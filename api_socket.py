"""import socket
import threading

# Configura la dirección IP y el puerto en el que el servidor escuchará.
host = '127.0.0.1'
port = 8080

# Crea un socket TCP/IP.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asocia el socket con la dirección IP y el puerto.
server_socket.bind((host, port))

# Escucha un número máximo de conexiones entrantes (puedes ajustar esto según tus necesidades).
server_socket.listen(5)
print(f"Servidor escuchando en {host}:{port}")

def handle_client(client_socket):
    # Maneja la lógica de comunicación con el cliente aquí.
    request = client_socket.recv(1024)
    print(f"Recibido: {request.decode('utf-8')}")
    
    # Envía una respuesta al cliente.
    response = "Hola, cliente!\r\n"
    client_socket.send(response.encode('utf-8'))
    
    # Cierra la conexión con el cliente.
    client_socket.close()

while True:
    # Acepta una conexión entrante.
    client_socket, addr = server_socket.accept()
    print(f"Conexión aceptada desde {addr[0]}:{addr[1]}")
    
    # Inicia un hilo para manejar la conexión del cliente.
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
"""