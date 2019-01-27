from consts import *


def pension(salary):
    if salary > SocialUpperLimit:
        result = SocialUpperLimit * PensionRate
    elif salary < SocialLowerLimit:
        result = SocialLowerLimit * PensionRate
    else:
        result = salary * PensionRate
    return round(result, 2)


if __name__ == '__main__':
    print("%.2f" % pension(22680))
