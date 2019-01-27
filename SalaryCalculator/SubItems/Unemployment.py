from consts import *


def unemployment(salary):
    if salary > SocialUpperLimit:
        result = SocialUpperLimit * UnemploymentRate
    elif salary < SocialLowerLimit:
        result = SocialLowerLimit * UnemploymentRate
    else:
        result = salary * UnemploymentRate
    return round(result, 2)


if __name__ == '__main__':
    paySalaries = [5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % unemployment(paySalary))

