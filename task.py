import json


def read_json(file_name, task_array):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
        result_array = []
        print(* task_array, sep=', ')
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
                        for task_data in task_array:
                            try:
                                if name['Key'] == task_data:
                                    result_array.append(f'"{name["Value"]}"')
                            except KeyError:
                                result_array.append('" "')
                except KeyError:
                    continue

            print(* result_array, sep=', ')
            result_array = []

