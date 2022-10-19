import sys

import configparser
import time
import re
import csv

import pandas as pd
from pandas import Series, DataFrame


class Analysis(object):
    def __init__(self, passwdList):
        self.passwdList = passwdList

    #计算各结构频率并保存到文件
    def calcStrucFreFile(self,*args):

        strLListDict = args[0][0]
        strDListDict = args[0][1]
        strSListDict = args[0][2]
        
        df1 = DataFrame(columns=('str',  'freq')) 
        for x in strLListDict:
            ge = '{:.18f}'.format(int(strLListDict[x]) * 1.0 / sum(strLListDict.values()))  # 计算频率
            df1.loc[x] = [x, ge]  # 将结构串，数量，以及频率存储到DataFrame中
            
        df1 = df1.sort_values(by='freq',ascending=False)  # 根据nums进行排序
        df1.to_csv("./L.txt",index = False)
        #print(df1)
        
        df2 = DataFrame(columns=('str', 'freq')) 
        for x in strDListDict:
            ge = '{:.18f}'.format(int(strDListDict[x]) * 1.0 / sum(strDListDict.values()))  # 计算频率
            df2.loc[x] = [x,ge]  # 将结构串，数量，以及频率存储到DataFrame中
            
        df2 = df2.sort_values(by='freq',ascending=False)  # 根据nums进行排序
        df2.to_csv("./D.txt",index = False)
        #print(df2)
        
        df3 = DataFrame(columns=('str','freq')) 
        for x in strSListDict:
            # fileName = "S"+len(x)+".txt"
            ge = '{:.18f}'.format(int(strSListDict[x]) * 1.0 / sum(strSListDict.values())) 
            df3.loc[x] = [x, ge]  
            
        df3 = df3.sort_values(by='freq',ascending=False) 
        df3.to_csv("./S.txt",index = False)







if __name__ == '__main__':
    time1 = time.perf_counter()

    data = pd.read_csv('../data/yahoo/yahoo.csv',encoding='gbk')
    passwdList = pd.Series(data['passwd'].values)

    ana = Analysis(passwdList)
