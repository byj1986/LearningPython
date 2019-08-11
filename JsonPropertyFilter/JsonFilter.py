import json
import sys

if __name__ == '__main__':
    # "C:\\Codes\\Python\\LearningPython\\JsonPropertyFilter\\SampleData.json"
    condition = "len(obj['Children']) > 0"

    # persons = json.load(open(sys.argv[1], 'rb'))
    # for x in persons:
    #     print(len(x["Children"]))

    # result = [obj for obj in json.load(open(sys.argv[1], 'rb')) if eval(condition)]
    result = [obj for obj in json.load(open(sys.argv[1], 'rb')) if eval(sys.argv[2])]
    for x in result:
        print(x)
