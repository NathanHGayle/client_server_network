import pickle
import json
import xml.etree.ElementTree as ET


# task_functions

# CONFIG:

def find_from_config(key, name):
    import yaml
    with open('0.config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        return config[key][name]


# CLIENT:

def create_dictionary():
    input_keys = input("Type keys separated by spaces ").split()
    input_vals = input('Type values separated by spaces ').split()
    # Handle Exception when keys are not unique because zip requires this.
    if len(set(input_keys)) != len(set(input_keys)):
        raise ValueError('Keys must be distinct, please try again')
    if len(input_keys) != len(input_vals):
        raise ValueError('The length of the keys and values must be the same')
    client_dictionary = dict(zip(input_keys, input_vals))
    return client_dictionary


def create_and_serialize(format='binary'):
    tool_one = create_dictionary()
    if format == 'binary':
        serialise = pickle.dumps(tool_one)
    elif format == 'JSON':
        serialise = json.dumps(tool_one)
    elif format == 'XML':
        root = ET.Element(tool_one)
        for key, value in tool_one.items():
            ET.SubElement(root, key).text = value
        serialise = ET.tostring(root).decode()
    else:
        raise ValueError(f'{format} was not a valid format for pickling this dictionary'
                         f'please choose from the following: Binary, JSON, or XML')
    return serialise


def save_to_file(client_file , name , type):
    filename = f'{name}{type}'
    if type == '.bin':
        with open(filename, 'wb') as file:
            pickle.dump(client_file, file)
            print(f'Binary File saved to {filename}')
    elif type == '.json':
        with open(filename, 'w') as file:
            json.dump(client_file, file)
            print(f'JSON saved to {filename}')
    elif type == '.xml':
        with open(filename, 'wb') as file:
            ET.ElementTree(client_file).write(file)
            print(f'XML saved to {filename}')
    else:
        raise ValueError(f'The file type {type} is not permitted, please use either .bin, .json or .xml')


# def create_text_file(fine_name, string):
# with file open(file_name, 'w'):
# if file is empty
# file.write(string)
#  elif file is not empty:
#                 file.write('/n',string)
# return file path


# def_send_file(file,encrypt == none):

# encrypt_file(file):
# encrypted_file = 'this_logic'
# return encrypted_file

# if file.type != .txt:
# Exception('This file type cannot be sent using this function')
#  else:
# prepare_file = encrypt_file(file)
# return prepare_file.send(server,code)


# SERVER:
# def print_contents(option):
# contents = open_file(read_mode)

# if option not in('screen','file'):
# Exception ('This option for printing is not allowed, please select an option from
# the following: 'screen', or 'file')

#           if option == 'screen':
# file =
#                  print(contents)
#           elif: option == 'file':
# create_text_file(f'{datetime.now()}_server_download',contents)


def main():
    tool_one = create_and_serialize()
    print(tool_one)


# stance name finisher
# southpaw kennith slam!

if __name__ == "__main__":
    main()

else:
    pass
