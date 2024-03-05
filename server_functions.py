# server functions
import socket
import threading
from task_functions import find_from_config

# server constants
HEADER = find_from_config('server_details', 'HEADER')
PORT = find_from_config('server_details', 'PORT')
FORMAT = find_from_config('server_details', 'FORMAT')
DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')
# dynamic server name config
SERVER = socket.gethostbyname(socket.gethostname())
# binding details
ADDR = (SERVER, PORT)


def initialise_server(family=socket.AF_INET, conn_type=socket.SOCK_STREAM):
    server = socket.socket(family, conn_type)
    server.bind(ADDR)
    return server


def initialise_connection(family=socket.AF_INET, conn_type=socket.SOCK_STREAM, client_addr=ADDR):
    client = socket.socket(family, conn_type)
    client.connect(client_addr)
    return client


# handle individual connections
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')
    conn.close()


# handle new connections
def start(server):
    server.listen()
    print(f'[LISTENING] server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTION]:{threading.active_count() - 1}')


def main():
    server_activated = initialise_server()
    start(server_activated)


if __name__ == "__main__":
    main()
else:
    pass
