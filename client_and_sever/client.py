from functions.task_functions import find_from_config
from functions.task_functions import create_and_serialize
from functions.task_functions import create_text_file
from functions.server_functions import initialise_connection
from functions.client_functions import client_send


def main():  # add while statement to complete the loop
    client_activate = initialise_connection()
    DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')
    FORMAT = find_from_config('server_details', 'FORMAT')
    while True:
        option_one = input('Would you like to create and send a dictionary? y/n: ')
        if option_one == 'y':
            client_dict = create_and_serialize()
            print('sending file...')
            client_send(client_dict, client_activate)
            server_response = client_activate.recv(2048).decode(FORMAT)
            print('Server response: ', server_response)
            client_send(DISCONNECT_MESSAGE, client_activate)
            if 'received' in server_response:
                disconnect = input('Would you like to disconnect now?: ')
                if disconnect == 'y':
                    client_send(DISCONNECT_MESSAGE, client_activate)
                    break
        else:
            option_two = input('Would you like to create and send a text file? y/n: ')
            if option_two == 'y':
                client_text = create_text_file()
                print('sending text file...')
                client_send(client_text, client_activate)
                server_response = client_activate.recv(2048).decode(FORMAT)
                print('TEST Sever response: ', server_response)
                client_send(DISCONNECT_MESSAGE, client_activate)
                if 'received' in server_response:
                    disconnect = input('Would you like to disconnect now?: ')
                    if disconnect == 'y':
                        client_send(DISCONNECT_MESSAGE, client_activate)
                        break


if __name__ == "__main__":
    main()
else:
    pass
