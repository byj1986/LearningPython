# coding=utf-8


from House import *
from Unemployment import *
from Pension import *
from Medical import *
from Tax import *


def calculate(gross: float, exempt=0) -> []:
    """ calculate net salary

    :param gross: gross salary
    :param exempt: tax exempt
    :return: calculate result set
    """
    if gross < MinimumSalary:
        raise ValueError('Gross salary is less local minimum salary!')
    _pension = pension(gross)
    _unemployment = unemployment(gross)
    _medical = medical(gross)
    _house = house(gross)
    _payTax = round(gross - _pension - _unemployment - _medical - _house, 2)
    tax_after_deduction = tax(_payTax, exempt)
    tax_before_deduction = tax(_payTax)
    _deduction_save = round(tax_before_deduction - tax_after_deduction, 2)
    net_salary = round(_payTax - tax_after_deduction, 2)
    return [_pension, _unemployment, _medical, _house, _deduction_save, net_salary]


if __name__ == '__main__':
    grossSalaries = [2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000]
    for salary in grossSalaries:
        try:
            result = calculate(salary, 2000)
            print("-------------------------")
            print("Gross salary: " + str(salary))
            print("Pension:      " + str(result[0]))
            print("Unemployment: " + str(result[1]))
            print("Medical:      " + str(result[2]))
            print("House:        " + str(result[3]))
            print("Tax exempt:   " + str(result[4]))
            print("Net salary:   " + str(result[5]))
            print("-------------------------")
        except ValueError as e:
            print(e)
