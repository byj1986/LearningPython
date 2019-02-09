# coding=utf-8


from House import *
from Unemployment import *
from Pension import *
from Medical import *
from Tax import *


def calcSalary(salary, deduction=0):
    pensionRes = pension(salary)
    unemploymentRes = unemployment(salary)
    medicalRes = medical(salary)
    houseRes = house(salary)
    payTax = round(salary - pensionRes - unemploymentRes - medicalRes - houseRes, 2)
    withDeductionTax = tax(payTax, deduction)
    withoutDeductionTax = tax(payTax)
    deductionSave = round(withoutDeductionTax - withDeductionTax, 2)
    netSalary = round(payTax - withDeductionTax, 2)
    return [deductionSave, netSalary]


if __name__ == '__main__':
    paySalaries = [5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]

    for salary in paySalaries:
        result = calcSalary(salary, 2000)
        print("Deduction save you " + str(result[0]) + " per month.Pre-tax: " + str(salary) +
              " Net salary: " + str(result[1]))
