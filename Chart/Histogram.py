# coding=UTF=8

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
from matplotlib.font_manager import FontProperties

workday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
total_hour_data = [6.7, 8.7, 6.9, 3.5, 10.7, 0, 0]
core_hour_data = [4.8, 7, 6.2, 1.9, 9.6, 0, 0]

x = range(len(workday))
# plt.plot(workday, y_axis_basis_total_hour_data, 'ro-', color='#4C92C3', alpha=1, label='Basis Total')
# plt.plot(workday, y_axis_basis_core_hour_data, 'ro-', color='#FF7F0E', alpha=1, label='Basis Core')

plt.axhline(9, color='#4C92C3', alpha=0.6)
plt.axhline(6, color='#FF7F0E', alpha=0.6)
plt.bar(x=x, height=total_hour_data, width=0.4, label='Total')
plt.bar(x=[i + 0.4 for i in x], height=core_hour_data, width=0.4, label='Core')

plt.xticks([index + 0.2 for index in x], workday)

for index, data in enumerate(total_hour_data):
    plt.text(index - 0.2, data, "%s" % str(data))

for index, data in enumerate(core_hour_data):
    plt.text(index + 0.3, data, "%s" % str(data))

plt.xlabel('Workday')
plt.ylabel('Hours')
plt.ylim(0, 15)

plt.legend()

plt.title(u'Histogram for yb61723')

plt.show()
