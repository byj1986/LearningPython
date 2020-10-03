from .consts import *


def medical(salary) -> float:
    """ calculate medical insurance

    :param salary: gross salary
    :return: medical insurance amount
    """
    if salary > SocialUpperLimit:
        result = SocialUpperLimit * MedicalRate
    elif salary < SocialLowerLimit:
        result = SocialLowerLimit * MedicalRate
    else:
        result = salary * MedicalRate
    return round(result, 2)


if __name__ == '__main__':
    paySalaries = [4000, 5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % medical(paySalary))
