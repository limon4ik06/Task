import json


def read_json(file_name, example_array):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
        result_array = []
        print(* example_array, sep=', ')
        for i in data:
            i = i.split(';')
            i[3] = i[3].replace(f"'", '"')
            smth = i[3]
            data_line = json.loads(smth)
            for data in data_line:
                try:
                    answer = data['peer_response_with_source']['Payload']['All Categories']['Answers']
                    result_array.append(f'"{i[0]}"')
                    for name in answer[0]['Answer']:
                        try:
                            if name['Key'] == example_array[1]:
                                result_array.append(f'"{name["Value"]}"')
                            elif name['Key'] == example_array[2]:
                                result_array.append(f'"{name["Value"]}"')
                            elif name['Key'] == example_array[3]:
                                result_array.append(f'"{name["Value"]}"')
                            elif name['Key'] == example_array[4]:
                                result_array.append(f'"{name["Value"]}"')
                            elif name['Key'] == example_array[5]:
                                result_array.append(f'"{name["Value"]}"')
                        except KeyError:
                            result_array.append('" "')
                except KeyError:
                    continue

            print(* result_array, sep=', ')
            result_array = []

