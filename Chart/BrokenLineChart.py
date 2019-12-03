# coding=UTF=8

import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = (19.2, 10.8)
plt.rcParams['font.sans-serif'] = ['SimHei']

x_axis_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y_axis_basis_total_hour_data = [9, 9, 9, 9, 9]
y_axis_basis_core_hour_data = [6, 6, 6, 6, 6]
y_axis_total_hour_data = [6.7, 8.7, 6.9, 3.5, 10.7]
y_axis_core_hour_data = [4.8, 7, 6.2, 1.9, 9.6]

# plot中参数的含义分别是横轴值，纵轴值，颜色，透明度和标签
plt.plot(x_axis_data, y_axis_total_hour_data, 'ro-', color='#4682B4', alpha=1, label='本周总时间')
plt.plot(x_axis_data, y_axis_core_hour_data, 'ro-', color='#FFE4C4', alpha=1, label='本周核心时间')
plt.plot(x_axis_data, y_axis_basis_total_hour_data, 'ro-', color='#8B7355', alpha=1, label='基准总时间')
plt.plot(x_axis_data, y_axis_basis_core_hour_data, 'ro-', color='#FF0000', alpha=1, label='基准核心时间')

# 显示标签，如果不加这句，即使加了label='一些数字'的参数，最终还是不会显示标签
plt.legend(loc="upper left")
plt.xlabel('日期 12/2 - 12/5')
plt.ylabel('时间 Hours')

# plt.show()
plt.savefig('demo.png')  # 保存该图片
