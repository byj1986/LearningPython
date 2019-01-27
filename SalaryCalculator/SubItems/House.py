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
    paySalaries = [5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % house(paySalary))
