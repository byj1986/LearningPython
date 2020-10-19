# coding=utf-8


from SubItems import House, Medical, Tax, Pension, Unemployment, consts


def calculate(gross: float, exempt=0) -> []:
    """ calculate net salary

    :param gross: gross salary
    :param exempt: tax exempt
    :return: calculate result set
    """
    if gross < consts.MinimumSalary:
        raise ValueError('Gross salary is less local minimum salary!')
    _pension = Pension.pension(gross)
    _unemployment = Unemployment.unemployment(gross)
    _medical = Medical.medical(gross)
    _house = House.house(gross)
    _payTax = round(gross - _pension - _unemployment - _medical - _house, 2)
    tax_after_deduction = Tax.tax(_payTax, exempt)
    tax_before_deduction = Tax.tax(_payTax)
    _deduction_save = round(tax_before_deduction - tax_after_deduction, 2)
    _net_salary = round(_payTax - tax_after_deduction, 2)
    return [_pension, _unemployment, _medical, _house, _deduction_save, _net_salary]


if __name__ == '__main__':
    grossSalaries = [2000, 5000, 8000, 10000, 15000,
                     20000, 25000, 30000, 50000, 80000, 100000]
    for salary in grossSalaries:
        try:
            pension, unemployment, medical, house, deduction_save, net_salary = calculate(
                salary, 2000)
            print("-------------------------")
            print(f"Gross salary: {salary}")
            print(f"Pension:      {pension}")
            print(f"Unemployment: {unemployment}")
            print(f"Medical:      {medical}")
            print(f"House:        {house}")
            print(f"Tax exempt:   {deduction_save}")
            print(f"Net salary:   {net_salary}")
            print("-------------------------")
        except ValueError as e:
            print(e)
