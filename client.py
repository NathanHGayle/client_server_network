# from task_functions import create_dictionary
# from task_functions import populate_dictionary
# from task_functions import serialise_and_send
# from task_functions import serialise_file
# from task_functions import create_text_file
# from task_functions import send_file
from task_functions import find_from_config
from server_functions import initialise_connection
from client_functions import client_send


DISCONNECT_MESSAGE = find_from_config('server_details', 'DISCONNECT_MESSAGE')

input_keys = ['person_name', 'birth_date', 'status', 'height', 'weight']
input_vals = ['Matt', '2000', 'single', 182, 74]

def main():
    client_activate = initialise_connection()
    # you can put an input here for a dictionary
    client_send('Hello World', client_activate)
    client_send('Hello World', client_activate)
    client_send('Hello World', client_activate)
    client_send(DISCONNECT_MESSAGE, client_activate)


if __name__ == "__main__":
    main()
else:
    pass
