import json
import os

def load_json(filepath):
    full_path = os.path.join('test', 'fixtures', filepath)
    with open(full_path, 'r') as file:
        return json.load(file)


def generate_diff(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = []

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:
            result.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(result) + "\n}"
