# -*- coding: utf-8 -*
from imp import reload
from tqdm import tqdm
import pandas as pd
import codecs
import sys
reload(sys)
sys.getdefaultencoding()

f = codecs.open('D:\\下载\\plaintxt_yahoo\\plaintxt_yahoo.txt', mode='r', encoding='ISO-8859-1')  # 打开txt文件，以‘utf-8’编码读取
line = f.readline()  # 以行的形式进行读取文件
list1 = []
count = 1
while line:
    count += 1
    line = line.strip()
    a = line.split(':')
    if len(a) >= 3:
        b = a[2]  # 这是选取需要读取的位数
        list1.append(b)  # 将其添加在列表之中
        line = f.readline()
        print(count)
    else:
        line = f.readline()
f.close()

# 保存为csv格式
data1 = pd.DataFrame(list1)
data1.columns = ['passwd']  # 设置列表头
data1.to_csv('../data/yahoo.csv', index=False)
