# coding=utf-8
from random import *
from time import *

print(random())
# 2的8次方
print(getrandbits(8))
print(uniform(1, 10))

date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)

date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

random_time = uniform(time1, time2)
print(random_time)
print(asctime(localtime(random_time)))

values = range(1, 11) + 'J Q K'.split()
print(values)
suits = '方块 梅花 红桃 黑桃'.split()
deck = ['%s%s' % (s, v) for v in values for s in suits]
shuffle(deck)

players = {'Zhao': [], 'Qian': [], 'Sun': [], 'Li': []}

for k, v in players.items():
    # players[k].append()
    i = 0
    while i < 12:
        # players[k] = deck.pop()
        val = deck.pop()
        print(val)
        players[k].append(val)
        i += 1
# players = {'a': deck[0, 12], 'b': deck[13, 24], 'c': [25, 36], 'd': [37, 48]}

#
# for k, v in players.items():
#     print(v)
#     print('%s has %s' % (k, v))

print(players)
# while deck:
#     print(deck.pop())


# print(deck)
