import json
example_array = ['Name : Title', 'Name : First Name', 'Name : Middle Name', 'Name : Last Name', 'Name : Full Name']


def read_json(file_name):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
        result_array = []
        for i in data:
            i = i.split(';')
            i[3] = i[3].replace(f"'", '"')
            smth = i[3]
            data_line = json.loads(smth)
            for data in data_line:
                try:
                    answer = data['peer_response_with_source']['Payload']['All Categories']['Answers']
                    result_array.append(i[0])
                    for name in answer[0]['Answer']:
                        try:
                            if name['Key'] == example_array[0]:
                                result_array.append(name['Value'])
                                continue
                            elif name['Key'] == example_array[1]:
                                result_array.append(name['Value'])
                                continue
                            elif name['Key'] == example_array[2]:
                                result_array.append(name['Value'])
                                continue
                            elif name['Key'] == example_array[3]:
                                result_array.append(name['Value'])
                                continue
                            elif name['Key'] == example_array[4]:
                                result_array.append(name['Value'])
                                continue
                        except KeyError:
                            continue
                except KeyError:
                    continue

            print(result_array)
            result_array = []

