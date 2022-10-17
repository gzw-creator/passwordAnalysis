import csv
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('./key_result2.csv', header=None)

#自定义列名，可改
data.columns=["key","frequency"]

xdata = []
y1data = []
y2data = []

#读取列表名
xdata = data.loc[:, 'key']
y1data = data.loc[:, 'frequency']

#作图
plt.plot(xdata, y1data, color='r', marker='o', mec='r', mfc='w', label=u'frequency')
plt.xticks(rotation=90)
# plt.plot(xdata, y2data, color='b', marker='o', mec='r', mfc='w', label=u'列名3')  # color可自定义折线颜色，marker可自定义点形状，label为折线标注
plt.title(u"keyboard", size=10)
plt.legend()
plt.xlabel(u'key', size=10)
plt.ylabel(u'frequency', size=10)
plt.savefig("key_board_csdn_2.png",dpi=300)
plt.show()
