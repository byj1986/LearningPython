import json
import sys


def resolve_json(filepath):
    file = open(filepath, "rb")
    return json.load(file)


if __name__ == '__main__':
    result = [obj for obj in resolve_json(sys.argv[1]) if eval(sys.argv[2])]
    for x in result:
        print(x)
