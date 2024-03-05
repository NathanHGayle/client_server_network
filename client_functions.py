from task_functions import find_from_config
import socket
from server_functions import initialise_connection

# client sever constants
# CLIENT_SEVER = find_from_config('client_details', 'CLIENT_SEVER')
CLIENT_SEVER = socket.gethostbyname(socket.gethostname())
FORMAT = find_from_config('client_details', 'FORMAT')
HEADER = find_from_config('client_details', 'HEADER')
DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')

# functions
def client_send(msg,connection):
    if isinstance(msg,str):
        message_bytes = msg.encode(FORMAT) # convert str to bytes
    elif isinstance(msg, bytes):
        message_bytes = msg
    else:
        raise ValueError('This message must be either string or bytes')
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message_bytes)
    print(connection.recv(2048).decode(FORMAT))


def main():
    client_activate = initialise_connection()
    client_send(DISCONNECT_MESSAGE, client_activate)


if __name__ == "__main__":
    main()
else:
    pass
