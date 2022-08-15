from task import read_json
example_array = ['Phone : Number', 'Name : Title', 'Name : First Name', 'Name : Middle Name', 'Name : Last Name', 'Name : Full Name']

if __name__ == "__main__":
    file_name = input('Enter path to the file: ')
    read_json(file_name, example_array)
