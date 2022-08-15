from task import read_json
example_array = ['Phone : Number', 'Name : Title', 'Name : First Name', 'Name : Middle Name', 'Name : Last Name', 'Name : Full Name']

if __name__ == "__main__":
    input_data = input('Enter path to the file: ')
    with open(input_data, 'r') as f:
        data = f.read().splitlines()
    print(read_json(input_data=data, task_array=example_array))
