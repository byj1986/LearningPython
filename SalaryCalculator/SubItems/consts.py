# coding=utf-8

# 最低工资
MinimumSalary = 2480

# 社保上限
SocialUpperLimit = 21396
# 下限
SocialLowerLimit = 4279

# 养老保险
PensionRate = 0.08

# 医疗保险
MedicalRate = 0.02

# 失业保险金
UnemploymentRate = 0.005

# 公积金缴纳比例
HouseRate = 0.07
# 上限
HouseUpperLimit = 21400
# 下限
HouseLowerLimit = 2300

# 个税起征点
TaxThreshold = 5000

# 个税税率级别
TaxLevelsDict = [
    {"upper": 0, "rates": 0, "quickNumber": 0},
    {"upper": 3000, "rates": 0.03, "quickNumber": 0},
    {"upper": 12000, "rates": 0.1, "quickNumber": 210},
    {"upper": 25000, "rates": 0.2, "quickNumber": 1410},
    {"upper": 35000, "rates": 0.25, "quickNumber": 2660},
    {"upper": 55000, "rates": 0.3, "quickNumber": 4410},
    {"upper": 80000, "rates": 0.35, "quickNumber": 7160},
    {"upper": 9999999999999999, "rates": 0.45, "quickNumber": 15160}
]
