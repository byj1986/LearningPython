from consts import *


def tax(salary, deduction=0):
    taxPart = salary - TaxThreshold - deduction
    for taxLevel in TaxLevelsDict:
        if taxLevel["upper"] > taxPart:
            return taxPart * taxLevel["rates"] - taxLevel["quickNumber"]


if __name__ == '__main__':
    paySalaries = [5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for paySalary in paySalaries:
        print("%.2f" % tax(paySalary))
