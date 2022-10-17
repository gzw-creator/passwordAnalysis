from datetime import datetime
import re
import sys
from time import time
import pandas as pd
from pandas import Series, DataFrame
import chardet
from tqdm import tqdm

# 正则中的%s分割
# 分成32类
splits = [
    {1: [('年', '月', '日', '点', '分', '秒'), ('-', '-', '', ':', ':', ''), ('\/', '\/', '', ':', ':', ''),
         ('\.', '\.', '', ':', ':', '')]},
    {2: [('年', '月', '日', '点', '分'), ('-', '-', '', ':', ''), ('\/', '\/', '', ':', ''), ('\.', '\.', '', ':', '')]},
    {3: [('年', '月', '日'), ('-', '-', ''), ('\/', '\/', ''), ('\.', '\.', '')]},
    {4: [('年', '月', '日'), ('-', '-', ''), ('\/', '\/', ''), ('\.', '\.', '')]},

    {5: [('月', '日', '点', '分', '秒'), ('-', '', ':', ':', ''), ('\/', '', ':', ':', ''), ('\.', '', ':', ':', '')]},
    {6: [('月', '日', '点', '分'), ('-', '', ':', ''), ('\/', '', ':', ''), ('\.', '', ':', '')]},
    {7: [('月', '日'), ('-', ''), ('\/', ''), ('\.', '')]},

    {8: [('点', '分', '秒'), (':', ':', '')]},
    {9: [('点', '分'), (':', '')]},
]

# 匹配正则表达式
matchs = {
    1: (r'\d{4}%s\d{1,2}%s\d{1,2}%s \d{1,2}%s\d{1,2}%s\d{1,2}%s', '%%Y%s%%m%s%%d%s %%H%s%%M%s%%S%s'),
    2: (r'\d{4}%s\d{1,2}%s\d{1,2}%s \d{1,2}%s\d{1,2}%s', '%%Y%s%%m%s%%d%s %%H%s%%M%s'),
    3: (r'\d{4}%s\d{1,2}%s\d{1,2}%s', '%%Y%s%%m%s%%d%s'),
    4: (r'\d{2}%s\d{1,2}%s\d{1,2}%s', '%%y%s%%m%s%%d%s'),

    # 没有年份
    5: (r'\d{1,2}%s\d{1,2}%s \d{1,2}%s\d{1,2}%s\d{1,2}%s', '%%m%s%%d%s %%H%s%%M%s%%S%s'),
    6: (r'\d{1,2}%s\d{1,2}%s \d{1,2}%s\d{1,2}%s', '%%m%s%%d%s %%H%s%%M%s'),
    7: (r'\d{1,2}%s\d{1,2}%s', '%%m%s%%d%s'),

    # 没有年月日
    8: (r'\d{1,2}%s\d{1,2}%s\d{1,2}%s', '%%H%s%%M%s%%S%s'),
    9: (r'\d{1,2}%s\d{1,2}%s', '%%H%s%%M%s'),
}

dic = {}

class TimeFinder(object):

    def __init__(self,):
        self.match_item = []
        self.init_match_item()

    def init_match_item(self):
        # 构建穷举正则匹配公式 及提取的字符串转datetime格式映射
        for item in splits:
            for num, value in item.items():
                match = matchs[num]
                for sp in value:
                    tmp = []
                    for m in match:
                        tmp.append(m % sp)
                    self.match_item.append(tuple(tmp))

    def find_time(self, text):
        for num in range(len(self.match_item)):
            x = self.match_item[num]
            parten = x[0]
            match_list = re.search(parten,text)
            if match_list:
                return num+1
        return 0

def handleDate(time_str):
    # 定义日期格式
    timefinder = TimeFinder()
    parsed_time = timefinder.find_time(time_str.replace("\t", "").replace("\n", ""))
    return str(parsed_time)

if __name__ == '__main__':
    data = pd.read_csv('../data/csdn/csdn.csv')
    passwdList = pd.Series(data['passwd'].values)
    for passwd in tqdm(passwdList):
        res_num = handleDate(str(passwd))
        if res_num in dic.keys():
            dic[res_num] += 1
        else:
            dic[res_num] = 1
    print(dic)

