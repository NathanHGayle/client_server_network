from server_functions import initialise_server
from server_functions import start
from server_functions import handle_client
from task_functions import find_from_config


def main():
    server_activated = initialise_server()
    start(server_activated)


if __name__ == "__main__":
    main()
else:
    pass
