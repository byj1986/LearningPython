tag = '<a href="http://www.python.org">Python web site</a>'

print("Tag 9: " + tag[9])
print("Tag 30: " + tag[30])
print(tag[9:30])

print("Tag 32: " + tag[32])
print("Tag -4: " + tag[-4])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
# meas by default python goes with [::1]
print(numbers[8:3])
print(numbers[8:3:-1])
print(numbers[8:3:-2])
