# task_functions

# CONFIG:

def find_from_config(key, name):
    import yaml
    with open('0.config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        return config[key][name]

# CLIENT:

    # create_dictionary(keys **kargs, values **kargs):
           # if key already exist:
                    # Exception('Keys must be distinct, please try again')
            # elif len(values) != len(keys):
                    # Exception('The length of the keys and values must be the same')
           # client_dictionary = zip(keys,values)
           # return client dictionary

    # def populate_dictionary(dictionary_name,new_keys **kargs,new_values *kargs):
            # if key already exist:
            # Exception('Keys must be distinct, please try again')
            # elif len(values) != len(keys):
            # Exception('The length of the keys and values must be the same')
            # dictionary_name.update(new_keys,new_values)

    # def serialise_and_send(dictionary,format)
#
            # def serialise_file(file):
               # return
#
#            if format not in(Binary, JSON, OR XML):
         #       Exception(f'{format} was not a valid option for pickling this dictionary
                            # please choose from the following: Binary, JSON, or XML.
        #    if format == binary:

             # return serialise_file(binary_file)
        #    if format == JSON:
#               return serialise_file(json_file)
        #    if format == XML:
            #   return serialise_file(json_file)

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
                #Exception('This file type cannot be sent using this function')
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




