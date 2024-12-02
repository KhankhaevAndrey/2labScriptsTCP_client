import socket


def run_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Сервер запущен на {host}:{port}")

        server_socket.listen(1)
        print("Ожидание подключения")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Подключено")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Получено сообщение: {data.decode('utf-8')}")
                conn.sendall(data)
            print("Соединение закрыто")


if __name__ == "__main__":
    run_server()