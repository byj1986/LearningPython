# coding=utf-8

from SubItems import House
from SubItems import Unemployment
from SubItems import Pension
from SubItems import Medical
from SubItems import Tax

# salaries = [5000, 10000, 15000, 20000, 25000, 30000, 50000, 80000, 100000, 1000000]
# for salary in salaries:
#     pension = Pension.pension(salary)
#     medical = Medical.medical(salary)
#     unemployment = Unemployment.unemployment(salary)
#     house = House.house(salary)
#     payTax = round(salary - pension - medical - unemployment - house, 2)
#     tax = Tax.tax(payTax)
#     print("Pre-tax: " + str(salary) + " Net salary: " + str(round(payTax - tax, 2)))


salary = 22680
deduction = 0000

pension = Pension.pension(salary)
medical = Medical.medical(salary)
unemployment = Unemployment.unemployment(salary)
house = House.house(salary)
payTax = round(salary - pension - medical - unemployment - house, 2)
withDeductionTax = Tax.tax(payTax, deduction)
withoutDeductionTax = Tax.tax(payTax)
deductionSave = withoutDeductionTax - withDeductionTax
print("Deduction save you " + str(round(deductionSave, 2))+" per month.")
print("Pre-tax: " + str(salary) + " Net salary: " + str(round(payTax - withDeductionTax, 2)))
