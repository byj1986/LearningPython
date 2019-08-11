import json
import sys


def resolve_Json(filepath):
    file = open(filepath, "rb")
    return json.load(file)


def filter_Person(source, condition):
    filtered_persons = []
    for obj in source:
        if eval(condition):
            filtered_persons.append(obj)
    return filtered_persons
    # return filter(person_filter(,condition), source)
    # res = eval(condition)
    # print(res)
    # return res
    # for x in conditions:
    #     print(x)
    # return [element for element in source if element['Married'] == married]
    # return [element for element in source if eval(condition)]
    # "obj['Age'] >= 30 and obj['Married'] == True"


if __name__ == '__main__':
    # filepath = r"SampleData.json"
    print(sys.argv)
    result = filter_Person(resolve_Json(sys.argv[1]), sys.argv[2])
    for x in result:
        print(x)
