from consts import *


def pension(salary: float) -> float:
    """ calculate pension

    :param salary: gross salary
    :return: pension amount
    """
    if salary > SocialUpperLimit:
        result = SocialUpperLimit * PensionRate
    elif salary < SocialLowerLimit:
        result = SocialLowerLimit * PensionRate
    else:
        result = salary * PensionRate
    return round(result, 2)


if __name__ == '__main__':
    paySalaries = [5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % pension(paySalary))
