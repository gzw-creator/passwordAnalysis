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
        # print(args[1])
        # print(len(args))
        strLListDict = args[0][0]
        strDListDict = args[0][1]
        strSListDict = args[0][2]
        # print(strLListDict)
        # print(strDListDict)
        # print(strSListDict)
        # print(max(map(len, strDListDict)))
        
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
            ge = '{:.18f}'.format(int(strSListDict[x]) * 1.0 / sum(strSListDict.values()))  # 计算频率
            df3.loc[x] = [x, ge]  # 将结构串，数量，以及频率存储到DataFrame中
            
        df3 = df3.sort_values(by='freq',ascending=False)  # 根据nums进行排序
        df3.to_csv("./S.txt",index = False)
        #print(df3)

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
            
    #统计口令结构
    def countStruc(self):
        strucList = []
        for passwd in self.passwdList:  # 遍历每一行口令
            struc = ''
            passwd = str(passwd)  # 将passwd对象转为字符串
            for ch in passwd:  # 遍历每口令中的每一个字符
                if ch.isdigit():
                    struc += 'D'
                elif ch.isalpha():
                    struc += 'L'
                else:
                    struc += 'S'
            strucList.append(struc)

        # print("step one:", strucList)  # step one : for test

        # 统计每种结构的口令数量
        nums = {}  # 定义一个dic,键为口令结构，值为结构数量
        for stru in strucList:  # 在结构数组中遍历每一种结构

            if stru in nums.keys():  # 如果该结构已经被统计（即在字典nums的键中能找），则结构出现次数+1
                nums[stru] += 1
            else:  # 如果该结构没有被统计过，则更新字典，并将出现次数设定为1
                nums[stru] = 1

        # print("step two:", nums)  # step two for test
        df = DataFrame(columns=('structure', 'nums', 'freq'))  # 输出csv文件的列名，共存储三列，分别存储口令结构，口令数量以及该结构口令出现的频率
        for x in nums.keys():  # 遍历字典的每一个键，即遍历每一种结构

            char = x[0]  # 将第一个字母定为标志字符
            stru = x[1:]  # stru为结构的第二个字符往后的字符串
            c = 1  # 计数器置为1
            res = ''
            for i in stru:  # 遍历第二个字符往后的每一个字符
                if i == char:  # 如果某一个字符与第一个字符相同
                    c += 1  # 计数器加一
                else:  # 如果该字符与第一个字符不想图
                    res += char  # 则将该字符存入结果字符串中
                    res += str(c)  # 并且记录该字符的个数
                    char = i  # 更新当前字符为标志字符
                    c = 1  # 重置计数器
            res += char
            res += str(c)

            ge = '{:.18f}'.format(int(nums[x]) * 1.0 / len(strucList))  # 计算频率
            df.loc[x] = [x, nums[x], ge]  # 将结构串，数量，以及频率存储到DataFrame中
            pd.set_option('mode.chained_assignment', None)

            df['structure'][x] = res

        df = df.sort_values(by='nums',ascending=False)  # 根据nums进行排序

        # print("step three:", df)
        return df




if __name__ == '__main__':
    time1 = time.perf_counter()

    # --------------------读文件模块--------------------#
    # 读取文件
    data = pd.read_csv('../data/csdn/Y.csv',encoding='gbk')
    passwdList = pd.Series(data['passwd'].values)
    # print(passwdList)
    # 记录读文件的时间
    time2 = time.perf_counter()
    #print( 'read file time : ', (time2 - time1))

    # --------------------分析模块--------------------#
    ana = Analysis(passwdList)
    # --------------------统计模块--------------------#
    
    ana.calcStrucFreFile(ana.countStrucFre())
    
    # # 分析生成口令结构/对应数量/出现概率的字符串
    # ana.countStruc().to_csv('../data/csdn/str_analysis_csdn.csv',index = False)


    # # 记录分析生成的时间
    # time3 = time.perf_counter()
    # #print( 'Analysis time : ', (time3 - time2))