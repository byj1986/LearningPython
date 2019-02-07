# coding=utf-8

from SubItems import House
from SubItems import Unemployment
from SubItems import Pension
from SubItems import Medical
from SubItems import Tax


def calcSalary(salary, deduction=0):
    pension = Pension.pension(salary)
    medical = Medical.medical(salary)
    unemployment = Unemployment.unemployment(salary)
    house = House.house(salary)
    payTax = round(salary - pension - medical - unemployment - house, 2)
    withDeductionTax = Tax.tax(payTax, deduction)
    withoutDeductionTax = Tax.tax(payTax)
    deductionSave = round(withoutDeductionTax - withDeductionTax, 2)
    netSalary = round(payTax - withDeductionTax, 2)
    return [deductionSave, netSalary]


if __name__ == '__main__':
    paySalaries = [5000, 8000, 10000, 15000, 20000, 22680, 25000, 30000, 50000, 80000, 100000]

    for salary in paySalaries:
        result = calcSalary(salary, 2000)
        print("Deduction save you " + str(result[0]) + " per month.Pre-tax: " + str(salary) +
              " Net salary: " + str(result[1]))
