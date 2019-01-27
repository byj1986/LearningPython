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
    print("%.2f" % unemployment(22680))
