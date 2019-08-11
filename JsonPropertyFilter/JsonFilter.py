import json
import sys

if __name__ == '__main__':
    # "C:\\Codes\\Python\\LearningPython\\JsonPropertyFilter\\SampleData.json"
    # "obj['Gender']== 'Male' or (obj['Age']>=30 and obj['Married'] == True)"
    result = [obj for obj in json.load(open(sys.argv[1], 'rb')) if eval(sys.argv[2])]
    for x in result:
        print(x)
