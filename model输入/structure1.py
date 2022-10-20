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
        df1.to_csv("../data/yahoo/L.txt",index = False)
        #print(df1)
        
        df2 = DataFrame(columns=('str', 'freq')) 
        for x in strDListDict:
            ge = '{:.18f}'.format(int(strDListDict[x]) * 1.0 / sum(strDListDict.values()))  # 计算频率
            df2.loc[x] = [x,ge]  # 将结构串，数量，以及频率存储到DataFrame中
            
        df2 = df2.sort_values(by='freq',ascending=False)  # 根据nums进行排序
        df2.to_csv("../data/yahoo/D.txt",index = False)
        #print(df2)
        
        df3 = DataFrame(columns=('str','freq')) 
        for x in strSListDict:
            # fileName = "S"+len(x)+".txt"
            ge = '{:.18f}'.format(int(strSListDict[x]) * 1.0 / sum(strSListDict.values())) 
            df3.loc[x] = [x, ge]  
            
        df3 = df3.sort_values(by='freq',ascending=False) 
        df3.to_csv("../data/yahoo/S.txt",index = False)

            #统计口令各结构频数
    def countStrucFre(self):

        strLListDict={}
        strDListDict={}
        strSListDict={}
        for passwd in self.passwdList:  # 遍历每一行口令
            passwd = str(passwd)  # 将passwd对象转为字符串
            # print(passwd)
            strL = ""
            strD = ""
            strS = ""
            for i in range(0,len(passwd)):  # 遍历每口令中的每一个字符
                ch = passwd[i]
                if ch.isdigit():
                    if len(strL)>0:
                        if strL in strLListDict.keys():
                            strLListDict[strL] += 1
                        else:
                            strLListDict[strL] = 1
                    if len(strS)>0:
                        if strS in strSListDict.keys():
                            strSListDict[strS] += 1
                        else:
                            strSListDict[strS] = 1
                    strL = ""
                    strS = ""
                    strD += ch
                elif ch.isalpha():
                    if len(strD)>0:
                        if strD in strDListDict.keys():
                            strDListDict[strL] += 1
                        else:
                            strDListDict[strL] = 1
                    if len(strS)>0:
                        if strS in strSListDict.keys():
                            strSListDict[strS] += 1
                        else:
                            strSListDict[strS] = 1
                    strD = ""
                    strS = ""
                    strL += ch
                else:
                    if len(strL)>0:
                        if strL in strLListDict.keys():
                            strLListDict[strL] += 1
                        else:
                            strLListDict[strL] = 1
                    if len(strD)>0:
                        if strD in strDListDict.keys():
                            strDListDict[strD] += 1
                        else:
                            strDListDict[strD] = 1
                    strL = ""
                    strD = ""
                    strS += ch
                if len(passwd)==i+1:
                    if len(strL)>0:
                        if strL in strLListDict.keys():
                            strLListDict[strL] += 1
                        else:
                            strLListDict[strL] = 1
                    if len(strD)>0:
                        if strD in strDListDict.keys():
                            strDListDict[strD] += 1
                        else:
                            strDListDict[strD] = 1
                    if len(strS)>0:
                        if strS in strSListDict.keys():
                            strSListDict[strS] += 1
                        else:
                            strSListDict[strS] = 1
                    strL = ""
                    strD = ""
                    strS = ""
        return strLListDict,strDListDict,strSListDict






if __name__ == '__main__':
    time1 = time.perf_counter()

    data = pd.read_csv('../data/yahoo/train_test/test.csv',encoding='gbk')
    passwdList = pd.Series(data['passwd'].values)

    ana = Analysis(passwdList)

    ana.calcStrucFreFile(ana.countStrucFre())