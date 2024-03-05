# from task_functions import create_dictionary
# from task_functions import populate_dictionary
# from task_functions import serialise_and_send
# from task_functions import serialise_file
# from task_functions import create_text_file
# from task_functions import send_file
from task_functions import find_from_config
from server_functions import initialise_connection

# client sever constants
CLIENT_SEVER = find_from_config('client_details', 'CLIENT_SEVER')
FORMAT = find_from_config('client_details', 'FORMAT')
HEADER = find_from_config('client_details', 'HEADER')
DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')

# functions
def client_send(msg,connection):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message)

def main():
    client_activate = initialise_connection()
    client_send('Hello World', client_activate)
    client_send('Hello World', client_activate)
    client_send('Hello World', client_activate)
    client_send(DISCONNECT_MESSAGE, client_activate)


if __name__ == "__main__":
    main()
else:
    pass
