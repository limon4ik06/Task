import json


def read_json(input_data, task_array):
    output_array = []
    result_array = []
    output_array.append(task_array)
    for i in input_data:
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

            output_array.append(result_array)
            result_array = []
    return output_array
