# 口令生成算法
import logging
from multiprocessing import Pool

import pandas as pd
from sklearn.utils import shuffle


def get_all_pwd_struction():
    """
    获取所有分析得到的口令结构，返回口令结构列表。每个口令结构应该形如"L1DS1"
    :return:
    """
    pwd_struction = []
    with open('./base_struct.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            pwd_struction.append(line.split('\t')[0])
    return pwd_struction


def get_test_pwds(pwd_file, num):
    """
    获取测试用的所有口令
    :param pwd_file: 口令文件
    :param num: 测试口令数量
    :return:
    """
    pwd = pd.read_csv(pwd_file)
    pwd = shuffle(pwd)
    test_pwds = pwd.iloc[:num, :]['passwd'].values.tolist()
    return test_pwds


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


def generte_pwd(father_pwd, child_pwd, position, pattern_num, candidate_small_pattern_pwd, guess_pwds):
    """
    生成口令
    :return:
    """
    if position < pattern_num - 1:
        father_pwd = child_pwd
        for i in range(len(candidate_small_pattern_pwd[position])):  # 遍历某个小模块所有的可能
            child_pwd = father_pwd + str(candidate_small_pattern_pwd[position][i])
            generte_pwd(father_pwd, child_pwd, position + 1, pattern_num, candidate_small_pattern_pwd, guess_pwds)
    else:
        father_pwd = child_pwd
        for i in range(len(candidate_small_pattern_pwd[position])):
            child_pwd = father_pwd + str(candidate_small_pattern_pwd[position][i])
            # print(child_pwd)
            guess_pwds.append(child_pwd)


def get_all_small_pattern_pwd(patterns):
    """
    根据口令的每个小模块，获取对应模块的所有可能的密码
    :param patterns:
    :return:
    """
    candidate_small_pattern_pwd = []
    for pattern in patterns:
        if 'L' in pattern:
            data = pd.read_csv('./base_alpha/'+pattern+'.txt', header=None, names=['pwd', 'p'], sep='\t')
            candidate_small_pattern_pwd.append(data['pwd'].values.tolist())
        if 'D' in pattern:
            data = pd.read_csv('./base_digit/'+pattern+'.txt', header=None, names=['pwd', 'p'], sep='\t')
            candidate_small_pattern_pwd.append(data['pwd'].values.tolist())
        if 'S' in pattern:
            data = pd.read_csv('./base_special/'+pattern+'.txt', header=None, names=['pwd', 'p'], sep='\t', quoting=3)
            candidate_small_pattern_pwd.append(data['pwd'].values.tolist())
    return candidate_small_pattern_pwd


def generate_pwds_by_struction(pwd_struction):
    """
    根据口令结构，读取相应的口令分析文件，生成该结构的口令
    :param pwd_struction: 口令结构，字符串类型
    :return: 所有猜测的口令
    """
    guessing_pwds = []
    patterns = identify_small_pattern(pwd_struction)
    candidate_small_pattern_pwd = get_all_small_pattern_pwd(patterns)
    pattern_num = len(patterns)
    generte_pwd('', '', 0, pattern_num, candidate_small_pattern_pwd, guessing_pwds)
    return guessing_pwds


def match_test_pwds(real_pwds, guessing_pwds):
    """
    将猜测的口令与真实口令进行比对，比对成功的口令输出到日志中，将匹配成功的口令数量返回
    :param real_pwds: 真实口令列表
    :param guessing_pwds: 猜测的口令列表
    :return: 与真实口令匹配的数量
    """
    matched_pwd_num = 0
    for guessing_pwd in guessing_pwds:
        if guessing_pwd in real_pwds:
            matched_pwd_num += 1
            logging.info('pwd: {} match!'.format(guessing_pwd))
    return matched_pwd_num


def generate_pwd_and_test(pwd_struction, test_pwds):
    """
    根据口令结构生成口令，并与测试口令匹配，返回匹配上的口令的个数
    :param pwd_struction: 口令结构
    :param test_pwds: 真实的口令
    :return: 生成的口令与真是口令匹配的个数
    """
    guessing_pwds = generate_pwds_by_struction(pwd_struction)  # 根据口令结构生成所有可能的口令
    matched_num = match_test_pwds(test_pwds, guessing_pwds)
    return matched_num


def main():
    """
    主函数
    :return:
    """
    pwd_structions = get_all_pwd_struction()  # 获取所有的口令结构
    test_pwds = get_test_pwds()  # 获取所有测试口令

    p = Pool(10)
    matched_nums = []
    for pwd_struction in pwd_structions:
        p.apply_async(generate_pwd_and_test, args=(pwd_struction, test_pwds), callback=matched_nums.append)
    p.close()
    p.join()

    # 计算准确率
    num = 0
    for i in matched_nums:
        num += i
    print('accuracy:{}'.format(num/len(test_pwds)))


if __name__ == '__main__':
    main()
