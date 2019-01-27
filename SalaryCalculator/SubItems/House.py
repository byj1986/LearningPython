# coding=utf-8
from consts import *


def house(salary):
    if salary > HouseUpperLimit:
        result = HouseUpperLimit * HouseRate
    elif salary < HouseLowerLimit:
        result = HouseLowerLimit * HouseRate
    else:
        result = salary * HouseRate
    return round(result, 2)


if __name__ == '__main__':
    print("%.2f" % house(22680))
