# 口令生成算法
import logging
import os
import re
from multiprocessing import Pool

import pandas as pd
from sklearn.utils import shuffle
import shutil

# 定义全局变量
STRUCT_NUM = -1  # 口令结构的数量（小于0，取所有口令结构）
FILE_SIZE = 36999999  # 生成的猜测口令文件的上限大小
SMALL_PATTERN = -1  # 读取每个口令子结构对应的文件的内容的数量（小于0，读取所有内容）


def get_all_pwd_struction():
    """
    获取所有分析得到的口令结构，返回口令结构列表。每个口令结构应该形如"L1DS1"
    :return:
    """
    pwd_struction = []
    if STRUCT_NUM < 0:
        data = pd.read_csv('./str_analysis_csdn.csv')
    else:
        data = pd.read_csv('./str_analysis_csdn.csv', nrows=STRUCT_NUM)
    pwd_struction = data['structure'].astype(str).values.tolist()
    return pwd_struction


def get_test_pwds(pwd_file, num):
    """
    获取测试用的所有口令
    :param pwd_file: 口令文件
    :param num: 测试口令数量
    :return:
    """
    if num < 0:
        pwd = pd.read_csv(pwd_file, header=None)
    else:
        pwd = pd.read_csv(pwd_file, nrows=num, header=None)
    return pwd[0].astype(str).values.tolist()


def identify_small_pattern(pwd_struction):
    """
    将口令结构划分为一个个的小模块，即将"L1D1S1"划分为"L1"、"D1"、"S1"
    :param pwd_struction: 口令结构
    :return:
    """
    indexes = []
    patterns = []
    for index, s in enumerate(pwd_struction):
        if s in ['L', 'S', 'D']:
            indexes.append(index)
    for i in range(len(indexes)):
        if i < len(indexes)-1:
            patterns.append(pwd_struction[indexes[i]:indexes[i + 1]])
        else:
            patterns.append(pwd_struction[indexes[i]:])
    return patterns


def generte_pwd(father_pwd, child_pwd, position, pattern_num, candidate_small_pattern_pwd, file_name):
    """
    生成口令
    :return:
    """
    if position < pattern_num - 1:
        father_pwd = child_pwd
        for i in range(len(candidate_small_pattern_pwd[position])):  # 遍历某个小模块所有的可能
            child_pwd = father_pwd + str(candidate_small_pattern_pwd[position][i])
            a = generte_pwd(father_pwd, child_pwd, position + 1, pattern_num, candidate_small_pattern_pwd, file_name)
            if not a:
                return False
        return True
    else:
        father_pwd = child_pwd
        for i in range(len(candidate_small_pattern_pwd[position])):
            child_pwd = father_pwd + str(candidate_small_pattern_pwd[position][i])
            # print(child_pwd)
            if os.path.exists(file_name) and os.path.getsize(file_name) > FILE_SIZE:  # 当对一个结构的口令的猜测数量太多时，直接停止
                return False
            with open(file_name, 'a+', encoding='UTF-8') as f:
                f.write('{}\n'.format(child_pwd))
        return True


def get_all_small_pattern_pwd(patterns):
    """
    根据口令的每个小模块，获取对应模块的所有可能的密码
    :param patterns:
    :return:
    """
    candidate_small_pattern_pwd = []
    for pattern in patterns:
        if 'L' in pattern:
            if SMALL_PATTERN < 0:
                data = pd.read_csv('./csdn/L/'+pattern+'.txt', header=None, names=['pwd', 'p'])
            else:
                data = pd.read_csv('./csdn/L/'+pattern+'.txt', header=None, names=['pwd', 'p'], nrows=SMALL_PATTERN)
            candidate_small_pattern_pwd.append(data['pwd'].astype(str).values.tolist())
        if 'D' in pattern:
            if SMALL_PATTERN < 0:
                data = pd.read_csv('./csdn/D/'+pattern+'.txt', header=None, names=['pwd', 'p'])
            else:
                data = pd.read_csv('./csdn/D/'+pattern+'.txt', header=None, names=['pwd', 'p'], nrows=SMALL_PATTERN)
            candidate_small_pattern_pwd.append(data['pwd'].astype(str).values.tolist())
        if 'S' in pattern:
            if SMALL_PATTERN < 0:
                data = pd.read_csv('./csdn/S/'+pattern+'.txt', header=None, names=['pwd', 'p'], quoting=3)
            else:
                data = pd.read_csv('./csdn/S/'+pattern+'.txt', header=None, names=['pwd', 'p'], quoting=3, nrows=SMALL_PATTERN)
            candidate_small_pattern_pwd.append(data['pwd'].astype(str).values.tolist())
    return candidate_small_pattern_pwd


def generate_pwds_by_struction(pwd_struction):
    """
    根据口令结构，读取相应的口令分析文件，生成该结构的口令
    :param pwd_struction: 口令结构，字符串类型
    :return: 所有猜测的口令
    """
    # guessing_pwds = []
    patterns = identify_small_pattern(pwd_struction)
    candidate_small_pattern_pwd = get_all_small_pattern_pwd(patterns)
    pattern_num = len(patterns)

    generte_pwd('', '', 0, pattern_num, candidate_small_pattern_pwd, './guess_csdn/'+pwd_struction+'.txt')
    # return guessing_pwds


def generate_pwd_and_test(pwd_struction):
    """
    根据口令结构生成口令，并与测试口令匹配，返回匹配上的口令的个数
    :param pwd_struction: 口令结构
    :return: 生成的口令与真是口令匹配的个数
    """
    generate_pwds_by_struction(pwd_struction)  # 根据口令结构生成所有可能的口令
    # matched_num = match_test_pwds(test_pwds, guessing_pwds)
    # return matched_num


# def match_pwd(guess_pwd_file, test_pwds):
#     pwds = pd.read_csv(guess_pwd_file, header=None, quoting=3)[0].astype(str).values.tolist()
#     match_number = 0
#     for pwd in pwds:
#         if pwd in test_pwds:
#             match_number = match_number + 1
#     return match_number


# def write_num(num):
#     with open('train_result.csv', 'a+', encoding='UTF-8') as f:
#         f.write('{}\n'.format(num))


def main(test_num):
    """
    主函数
    :return:
    """
    pwd_structions = get_all_pwd_struction()  # 获取所有的口令结构
    # test_pwds = get_test_pwds('./csdn/train_test/train.csv', test_num)  # 获取所有测试口令
    # print('test&train pwd len:', len(test_pwds))
    p = Pool(10)
    for pwd_struction in pwd_structions:
        p.apply_async(generate_pwd_and_test, args=(pwd_struction, ))
    p.close()
    p.join()

    # 计算准确率
    # all_guess_pwd = os.listdir('./guess_csdn')
    # right_pwd = []
    # p = Pool(10)
    # for guess_pwd in all_guess_pwd:
    #     if '.txt' not in guess_pwd:
    #         continue
    #     p.apply_async(match_pwd, args=('./guess_csdn/'+guess_pwd, test_pwds), callback=write_num)
    # p.close()
    # p.join()
    # print('accuracy:{}'.format(match_num/len(test_pwds)))


if __name__ == '__main__':
    # 删除guess文件夹下的内容
    # shutil.rmtree('./guess_yahoo')
    # os.mkdir('./guess_yahoo')
    # print('创建guess成功')
    # print('start')
    main(-1)
    # data = pd.read_csv('train_result.csv', header=None)
    # print('match num:', data[0].sum())
