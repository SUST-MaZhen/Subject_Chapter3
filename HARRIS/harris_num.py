# -*- coding:utf-8 -*-   
# Author : Mazhen 
# Date: 2019/1/22
import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
names = ['0.01', '0.02', '0.03', '0.04', '0.05']
x = range(len(names))
y = [700, 750, 770, 850, 900]
y1 = [750, 870, 899, 977, 1020]
# plt.plot(x, y, marker='o', mec='r', mfc='w', label="SUSAN角点检测")
# plt.plot(x, y1, marker='*', mec='g', mfc='w', ms=10, label="Harris角点检测")
# plt.plot(x, y, marker='o', mec='r', mfc='w')
plt.plot(x, y1, marker='*', mec='g', mfc='w', ms=10)
# plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=0)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("参数tg")  # X轴标签
plt.ylabel("角点数量")  # Y轴标签
plt.title("SUSAN角点检测数量随参数变化")  # 标题

plt.show()
