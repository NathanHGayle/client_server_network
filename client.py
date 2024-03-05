from task_functions import find_from_config
from task_functions import create_and_serialize
from task_functions import create_text_file
from server_functions import initialise_connection
from client_functions import client_send


def main():  # add while statement to complete the loop
    client_activate = initialise_connection()
    DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')
    while True:
        # you can put an input here for a dictionary
        option_one = input('Would you like to create and send a dictionary? y/n: ')
        if option_one == 'y':
            client_dict = create_and_serialize()
            print('sending file...')
            client_send(client_dict, client_activate)
        else:
            option_two = input('Would you like to create and send a text file? y/n: ')
            if option_two == 'y':
                client_text = create_text_file()
                print('sending text file...')
                client_send(client_text, client_activate)
        disconnect = input('Would you like to disconnect now?: ')
        if disconnect == 'y':
            client_send(DISCONNECT_MESSAGE, client_activate)
            break


if __name__ == "__main__":
    main()
else:
    pass
