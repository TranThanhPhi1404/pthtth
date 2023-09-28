import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345  # Port of your choice

    client_socket.connect((host, port))
    print("Connected to the server")

    message = input("Enter a message to send to the server: ")
    client_socket.sendall(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print("Received modified response from server:", response)

    client_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    client()