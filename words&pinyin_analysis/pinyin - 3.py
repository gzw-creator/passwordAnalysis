import collections
import csv

object_list=[]
num=0

def pinyin_word(string):
    '''
    将一段拼音，分解成一个个拼音
    :param string: 匹配的字符串
    :return: 匹配到的拼音列表
    '''
    max_len = 6  # 拼音最长为6
    string = string.lower()
    stringlen = len(string)
    result = []

    # 读本地拼音表
    with open('pinyin.txt', 'r', encoding='utf-8') as fi:
        pinyinLib = fi.readlines()
        for i in range(len(pinyinLib)):
            pinyinLib[i] = pinyinLib[i][:-1]  # 去换行符

    # 逆向匹配
    while True:
        matched = 0
        matched_word = ''
        if stringlen < max_len:
            max_len = stringlen
        for i in range(max_len, 0, -1):
            s = string[(stringlen - i):stringlen]
            # 字符串是否在拼音表中
            if s in pinyinLib:
                matched_word = s
                matched = i
                break
        # 未匹配到拼音
        if len(matched_word) == 0:
            string = string[:(stringlen - 1)]
            stringlen = len(string)
        else:
            result.append(s)
            string = string[:(stringlen - matched)]
            stringlen = len(string)
        if stringlen == 0:
            break
    return result
from tqdm import tqdm

save_path = "./pinyin_result.csv"
# with open("plain_yahoo.csv") as file:   #读入文件
with open('yahoo.csv') as file:   #读入文件

    lines = csv.reader(file)
    print(lines)
    for line in lines:   #逐行读入

        password = ''.join(line)
        print(password)
        fen = pinyin_word(password)
    #             #print(fen)
        for word in fen:    #统计分词列表中的元素
            object_list.append(word)
        # break
    #     print(line)

        # for i in range(1,100):#tqdm(range(1,100)) :
        #     if line[i:i+1]=='"':
        #         break
        # for j in tqdm(range(i+1,100)):    #根据第二个引号找到passwd
        #     if line[j:j+1]=='"':
        #         passwd=line[j+1:]
        #         #print(passwd)
        #         #fen=wordninja.split(passwd)     #对passwd分词
        #         fen = pinyin_word(passwd)
        #         #print(fen)
        #         for word in fen:    #统计分词列表中的元素
        #             object_list.append(word)
        #         break
    #print(object_list)
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts = word_counts.most_common(20)  # 获取前10最高频的词
    print(word_counts)  # 输出检查
    with open(save_path,'w') as sfile:
        pabar = tqdm(word_counts)
        for i in pabar:
            in_str = str(i).strip('(').strip(')').strip()+'\n'
            sfile.writelines(in_str)
            pabar.set_description("Saving!")
        sfile.close()
    file.close()



