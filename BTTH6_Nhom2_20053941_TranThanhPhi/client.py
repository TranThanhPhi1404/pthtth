import socket

def send_data_to_server(client_socket, data):
    if data == ".":
        return False
    client_socket.send(data.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    return True

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    with open('d:\Python_vscode\pthtth_coKhoa\pthtth\BTTH6_Nhom2_20053941_TranThanhPhi\data.txt', 'r') as file:
        lines = file.readlines()

    while True:
        choice = input("Nhập (1) để nhập dữ liệu từ bàn phím, (2) để chọn dữ liệu từ file, (3) để thoát: ")

        if choice == '1':
            while True:
                data = input("Nhập chuỗi số nguyên (dừng lại bằng dấu \".\"): ")
                if not send_data_to_server(client_socket, data):
                    break
        elif choice == '2':
            print("Chọn một dòng dữ liệu:")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")

            while True:
                line_choice = input("Nhập số thứ tự của dòng bạn muốn chọn (dừng lại bằng dấu \".\"): ")
                if line_choice == ".":
                    break

                try:
                    index = int(line_choice) - 1
                    if 0 <= index < len(lines):
                        data = lines[index].strip()
                        if not send_data_to_server(client_socket, data):
                            break
                    else:
                        print("Lựa chọn không hợp lệ.")
                except ValueError:
                    print("Nhập vào phải là một số.")
        elif choice == '3':
            print("Thoát.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

    client_socket.close()

if __name__ == "__main__":
    main()