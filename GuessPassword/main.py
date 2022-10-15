# 口令生成算法
import logging
from multiprocessing import Pool


def get_all_pwd_struction():
    """
    获取所有分析得到的口令结构，返回口令结构列表。每个口令结构应该形如"L1DS1"
    :return:
    """
    pwd_struction = []
    return pwd_struction


def get_test_pwds():
    """
    获取测试用的所有口令
    :return:
    """
    test_pwds = []
    return test_pwds


def generate_pwds_by_struction(pwd_struction):
    """
    根据口令结构，读取相应的口令分析文件，生成该结构的口令
    :param pwd_struction: 口令结构，字符串类型
    :return: 所有猜测的口令
    """
    guessing_pwds = []
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
