import socket

def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345  # Port of your choice

    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening on {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from:", client_address)

        data = client_socket.recv(1024).decode("utf-8")
        print("Received data from client:", data)

        client_socket.sendall(data.encode("utf-8"))
        print("Sent data back to client:", data)

        client_socket.close()
        print("Connection closed with:", client_address)

if __name__ == "__main__":
    echo_server()