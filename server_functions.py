# server functions
import pickle
import socket
import threading
from task_functions import find_from_config
from task_functions import save_to_file

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
            msg = conn.recv(msg_length)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                try:
                    file = pickle.loads(msg)
                    print(f'[{addr}] received data: {file}')
                    server_config_option = input(' Would you like to print what the client has sent or save to file?')
                    if server_config_option == 'save':
                        filename = input('Name of file: ')
                        file_type = input('File extension (.bin, .json, .xml or .txt): ')
                        save_to_file(file, filename, file_type)
                        conn.send(f'{msg} received'.encode(FORMAT))
                    elif server_config_option == 'print':
                        unpickle_file = pickle.load(file)
                        print(unpickle_file)
                        conn.send(f'{msg} received'.encode(FORMAT))
                except pickle.UnpicklingError:
                    print(f'[{addr}] Received text file data')
                    server_config_option = input('Would you like to print what the client has sent or save to file? '
                                                 'save/print')
                    if server_config_option == 'save':
                        filename = input('Name of file: ')
                        file_type = input('File extension (.txt): ')
                        save_to_file(msg, filename, file_type)
                        conn.send(f'{msg} received'.encode(FORMAT))
                    elif server_config_option == 'print':
                        print(msg)
                        conn.send(f'{msg} received'.encode(FORMAT))
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
