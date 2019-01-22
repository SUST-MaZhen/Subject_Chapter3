# -*- coding:utf-8 -*-   
# Author : Mazhen 
# Date: 2019/1/22
import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
names = ['5', '10', '15', '20', '25']
x = range(len(names))
y = [700, 750, 770, 850, 900]
y1 = [800, 850, 900, 950, 1000]
# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11)  # 限定横轴的范围
# pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='o', mec='r', mfc='w', label="SUSAN角点检测")
plt.plot(x, y1, marker='*', ms=10, label="Harris角点检测")
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=0)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("参数k")  # X轴标签
plt.ylabel("角点数量")  # Y轴标签
plt.title("角点检测数量随参数变化")  # 标题

plt.show()
