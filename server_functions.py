# server functions
import socket
import threading
from task_functions import get_from_config

HEADER = 64
PORT = get_from_config('sever_details','PORT')
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) # bind details


sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind(ADDR)

# handle individual connections
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.' )
    connected = True
    while connected:
        msg = conn.recv()

 # handle new connections
def start():
    sever.listen()
    while True:
        conn, addr = sever.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTION]:{threading.active_count()-1}')
def initialise_server():
        # import socket...

# def secure_server():

