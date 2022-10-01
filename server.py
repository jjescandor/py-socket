import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.0.220"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected. ")

    connected = True
    while connected:
        msg = conn.recv()

def start():
    server.listen()
    while True:
        print("Listening for connection...")
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(conn, addr)
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()
print("[STARTING] server is starting...")


