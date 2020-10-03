from .consts import *


def tax(after_decution_salary: float, exempt=0) -> float:
    """ calculate tax

    :param after_decution_salary: after deduction salary
    :param exempt: tax exempt
    :return: medical insurance amount
    """
    pay_tax_part = after_decution_salary - TaxThreshold - exempt
    for taxLevel in TaxLevelsDict:
        if taxLevel["upper"] > pay_tax_part:
            return pay_tax_part * taxLevel["rates"] - taxLevel["quickNumber"]


if __name__ == '__main__':
    paySalaries = [2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % tax(paySalary))
