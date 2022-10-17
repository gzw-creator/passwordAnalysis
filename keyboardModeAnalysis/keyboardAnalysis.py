from tqdm import tqdm
import collections

KeyboardRow1 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ""]
KeyboardRow2 = ["", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", ""]
KeyboardRow3 = ["", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "", "", ""]
KeyboardRow4 = ["", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "", "", ""]
KeyboardRow1S = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", ""]
KeyboardRow2S = ["", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|"]
KeyboardRow3S = ["", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "", "", ""]
KeyboardRow4S = ["", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "", "", ""]
Rows = [KeyboardRow1, KeyboardRow2, KeyboardRow3, KeyboardRow4, \
        KeyboardRow1S, KeyboardRow2S, KeyboardRow3S, KeyboardRow4S]


def ConvertToCoordinates(Password):
    Coordinates = []
    for c in Password:
        for i, r in enumerate(Rows):
            try:
                Coordinates.append((i % 4, r.index(c)))
            except:
                pass
    return Coordinates


def isAdjacent(Coord1, Coord2):
    if (abs(Coord1[0] - Coord2[0]) > 1 or abs(Coord1[1] - Coord2[1]) > 1) or (
            abs(Coord1[0] - Coord2[0]) == 0 and abs(Coord1[1] - Coord2[1]) == 0):
        return False
    else:
        return True


def CheckForAdjacency(Coordinates):
    Adjacent = 0
    strTmp = ''
    strTmpDict = {}
    # print(len(Coordinates))
    for i in range(len(Coordinates) - 1):
        if isAdjacent(Coordinates[i], Coordinates[i + 1]):
            Adjacent += 1
            strTmp = strTmp + Rows[Coordinates[i][0]][Coordinates[i][1]]
            if i + 1 == len(Coordinates) - 1:
                strTmp = strTmp + Rows[Coordinates[i + 1][0]][Coordinates[i + 1][1]]
                Adjacent += 1
            strTmpDict[strTmp] = Adjacent
        else:
            if isAdjacent(Coordinates[i], Coordinates[i - 1]):
                strTmp = strTmp + Rows[Coordinates[i][0]][Coordinates[i][1]]
                Adjacent += 1
                strTmpDict[strTmp] = Adjacent
            Adjacent = 0
            strTmp = ''
    # print(strTmpDict)
    if len(strTmpDict) > 0:
        maxLength = max(strTmpDict.values())
        for key in strTmpDict:
            if strTmpDict[key] == maxLength:
                return key
    else:
        return "null"


save_path = "./key_result.csv"
save_path_2 = "./key_result2.csv"
object_list = []
with open("./csdn.csv") as file:  # 读入文件

    for line in file:  # 逐行读入
        print(line)
        passwd = line
        if passwd!="passwd":
            # print(passwd)
            # fen=wordninja.split(passwd)     #对passwd分词
            fen = CheckForAdjacency(ConvertToCoordinates(passwd))
            if fen != "null":
                object_list.append(fen)

    print(object_list)
    object_list_2 = []
    for ob in object_list:
        if len(ob) > 4:
            if ob.isdigit() is not True:
                object_list_2.append(ob)

    # print(object_list_2)
    word_counts_2 = collections.Counter(object_list_2)  # 对分词做词频统计
    word_counts_2 = word_counts_2.most_common(15)  # 获取前10最高频的词
    print(word_counts_2)  # 输出检查

    with open(save_path_2, 'w') as sfile:
        # sfile.writelines("key,frequency"+'\n')
        pabar = tqdm(word_counts_2)
        for i in pabar:
            in_str = str(i).strip('(').strip(')').strip() + '\n'
            sfile.writelines(in_str)
            pabar.set_description("2 Saving!")
        sfile.close()
    file.close()

    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts = word_counts.most_common(15)  # 获取前10最高频的词
    print(word_counts)  # 输出检查
    with open(save_path, 'w') as sfile:
        # sfile.writelines("key,frequency"+'\n')
        pabar = tqdm(word_counts)
        for i in pabar:
            in_str = str(i).strip('(').strip(')').strip() + '\n'
            sfile.writelines(in_str)
            pabar.set_description("1 Saving!")
        sfile.close()
    file.close()
# print(Rows[1][1])
