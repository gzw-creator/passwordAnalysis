import os
from multiprocessing.pool import Pool

import pandas as pd


def match_pwd(guess_pwd_file, test_pwds):
    pwds = pd.read_csv(guess_pwd_file, header=None, quoting=3)[0].astype(str).values.tolist()
    match_number = 0
    for pwd in pwds:
        if pwd in test_pwds:
            match_number = match_number + 1
    return match_number


def write_num(num):
    with open('result.csv', 'a+', encoding='UTF-8') as f:
        f.write('{}\n'.format(num))


def compute_result(guess_pwd_dir, test_pwd_file):
    all_guess_pwd = os.listdir(guess_pwd_dir)
    test_pwds = pd.read_csv(test_pwd_file, header=None)  # 获取所有测试口令
    test_pwds = test_pwds[0].astype(str).values.tolist()
    p = Pool(10)
    for guess_pwd in all_guess_pwd:
        if '.txt' not in guess_pwd:
            continue
        p.apply_async(match_pwd, args=(guess_pwd_dir+'/'+guess_pwd, test_pwds), callback=write_num)
    p.close()
    p.join()
    return len(test_pwds)


if __name__ == '__main__':
    test_pwd_len = compute_result('./guess_csdn', './csdn/train_test/train.csv')
    data = pd.read_csv('result.csv', header=None)
    print('acc:', data[0].sum()/test_pwd_len)
