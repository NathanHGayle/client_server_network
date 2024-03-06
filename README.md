# Sever and Client Project

This project consists of client and server applications that communicate using sockets (python library). The client and server are implemented in `client.py` and `server.py`. Additionally, there are separate function files for client and server functionality: `client_functions.py` and `server_functions.py`. The `client_functions.py` file contains functions relevant to the client side, such as `client_send`, while `server_functions.py` contains functions for handling clients, like `handle_client`. 

## Functionality

The project aims to allow clients to perform the following tasks:

1. **Create, Serialize, and Send a Dictionary**: Clients can create a dictionary and choose to serialize it into various formats such as Binary, JSON, or XML. The client application sends this dictionary to the server for further processing.

2. **Create and Send a Text File**: Clients have the option to create a text file and send it to the server. (The option to encrypt this file is TBC)

On the server side, the application is responsible for saving these received files.

## File Structure

- `client.py`: Main client application responsible for establishing communication with the server and invoking client functions.
- `server.py`: Main server application responsible for accepting client connections and invoking server functions.
- `client_functions.py`: Contains functions relevant to client-side operations, including sending data to the server.
- `server_functions.py`: Contains functions for server-side operations, such as handling client connections and saving received files.
- `task_functions.py`: Contains additional functions related to the tasks mentioned above, including dictionary serialization, file creation and saving files.

## Usage

1. Start by running `server.py`.
2. Then run the client.py in debug - you should see a connection appear on the server console.
3. Answer the prompts written to the client
4. Answer the response prompts written to the server
5. Disconnect 
