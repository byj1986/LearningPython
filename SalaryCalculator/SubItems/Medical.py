from consts import *


def medical(salary):
    if salary > SocialUpperLimit:
        result = SocialUpperLimit * MedicalRate
    elif salary < SocialLowerLimit:
        result = SocialLowerLimit * MedicalRate
    else:
        result = salary * MedicalRate
    return round(result, 2)


if __name__ == '__main__':
    print("%.2f" % medical(22680))
