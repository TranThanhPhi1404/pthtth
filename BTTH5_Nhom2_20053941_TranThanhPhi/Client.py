import socket

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    return client_socket

def request_service(client_socket, service):
    client_socket.sendall(service.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def reverse_string_and_capitalize_first_word(client_socket):
    request_service(client_socket, "1")
    string = input()
    client_socket.sendall(string.encode())
    response = client_socket.recv(1024).decode()
    print(f"Trả lại: {response}")

def calculate_integer_sum(client_socket):
    request_service(client_socket, "2")
    numbers = input()
    client_socket.sendall(numbers.encode())
    response = client_socket.recv(1024).decode()
    print(f"Tổng: {response}")

def disconnect(client_socket):
    request_service(client_socket, "3")
    client_socket.close()

def start_client():
    client_socket = connect_to_server()
    while True:
        print("Cung cấp danh sách các dịch vụ: ")
        print("1. Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ ")
        print("2. Tính tổng chuỗi các số nguyên")
        print("3. Thoát ")
        choice = input("Nhập dịch vụ cần sử dụng: ")
        if choice == "1":
            reverse_string_and_capitalize_first_word(client_socket)
        elif choice == "2":
            calculate_integer_sum(client_socket)
        elif choice == "3":
            disconnect(client_socket)
            break
        else:
            print("Lựa chọn không hợp lệ, hãy thử lại !")

start_client()