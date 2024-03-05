from functions.server_functions import initialise_server
from functions.server_functions import start


def main():
    server_activated = initialise_server()
    start(server_activated)


if __name__ == "__main__":
    main()
else:
    pass
