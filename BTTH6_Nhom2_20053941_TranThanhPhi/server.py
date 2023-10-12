import socket

def calculate_total(data):
    numbers = list(map(int, data.split()))
    total = sum(numbers)
    return total

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server đang chờ kết nối từ client...")

client_socket, addr = server_socket.accept()
print(f"Kết nối từ {addr}")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break

    total = calculate_total(data)
    response = f"Tổng chuỗi vừa nhận là: {total}"
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()