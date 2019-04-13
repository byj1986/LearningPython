# coding=utf-8

import json

import itchat

# add below print to list where files
print
json.__file__
print
itchat.__file__


def update_dict_count(data, key):
    if key in data.keys():
        data[key] += 1
    else:
        data[key] = 1


def get_display_sex(s):
    if s == 1:
        return "Male"
    elif s == 2:
        return "Female"
    else:
        return "Other"


def get_sorted_items(unsorted_items):
    sorted(unsorted_items.items(), key=lambda x: x[1], reverse=True)
    return json.dumps(unsorted_items).encode('utf-8').decode('unicode-escape')


itchat.login()
friends = itchat.get_friends(update=True)[0:]
sortedFriends = sorted(friends, key=lambda obj: obj["NickName"])
male = female = other = 0
provinces = {}
cities = {}

for i in sortedFriends[0:]:
    print(i)
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    province = i["Province"].replace("\n", "")
    city = i["City"].replace("\n", "")
    display = "NickName: " + i["NickName"] + " Sex:" + get_display_sex(i["Sex"])

    if province:
        update_dict_count(provinces, province)
        display += (" Province: " + province)

    if city:
        update_dict_count(cities, city)
        display += (" City: " + city)

    if signature:
        display += (" Signature: " + signature)

    print(display.encode('utf8'))
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

print(get_sorted_items(provinces))
print(get_sorted_items(cities))

print("男性好友： %d人, 占%.2f%%" % (male, (float(male) / total * 100)))
print("女性好友： %d人, 占%.2f%%" % (female, (float(female) / total * 100)))
print("不明性别好友： %d人, 占%.2f%%" % (other, (float(other) / total * 100)))
# print("男性好友： %d人, 占%.2f%%" % (male, (float(male) / total * 100)) + "\n" +
#       "女性好友： %d人, 占%.2f%%" % (female, (float(female) / total * 100)) + "\n" +
#       "不明性别好友： %d人, 占%.2f%%" % (other, (float(other) / total * 100)))

itchat.logout()
