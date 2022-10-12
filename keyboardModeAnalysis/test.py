from tqdm import tqdm
import collections
KeyboardRow1 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ""]
KeyboardRow2 = ["", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", ""] 
KeyboardRow3 = ["", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "", "", ""] 
KeyboardRow4 = ["", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "", "", ""]
KeyboardRow1S = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", ""]
KeyboardRow2S = ["", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|"]
KeyboardRow3S = ["","A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "", "", ""] 
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
print(ConvertToCoordinates("qwer"))

def isAdjacent(Coord1, Coord2):
    if (abs(Coord1[0] - Coord2[0]) > 1 or abs(Coord1[1] - Coord2[1]) > 1) or (abs(Coord1[0] - Coord2[0]) == 0 and abs(Coord1[1] - Coord2[1]) == 0):
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
            if i+1 == len(Coordinates)-1:
                strTmp = strTmp + Rows[Coordinates[i+1][0]][Coordinates[i+1][1]]
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
    if len(strTmpDict)>0:
        maxLength = max(strTmpDict.values())
        for key in strTmpDict:
            if strTmpDict[key] == maxLength:
                return key
    else:
        return "null"

print(CheckForAdjacency(ConvertToCoordinates("1qwertyuio")))

print("ok")

save_path = "./key_result.csv"
object_list=[]
with open("D:\mine\passwordAnalysis\passwordAnalysis\keyboardModeAnalysis\data\plain_yahoo.csv") as file:   #读入文件

    for line in file:   #逐行读入
        #print(line)

        for i in range(1,100):#tqdm(range(1,100)) :
            if line[i:i+1]=='"':
                break
        for j in tqdm(range(i+1,100)):    #根据第二个引号找到passwd
            if line[j:j+1]=='"':
                passwd=line[j+1:]
                #print(passwd)
                #fen=wordninja.split(passwd)     #对passwd分词
                fen = CheckForAdjacency(ConvertToCoordinates(passwd))
                if fen!="null":
                    object_list.append(fen)
                break
    print(object_list)
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts = word_counts.most_common(100)  # 获取前10最高频的词
    print(word_counts)  # 输出检查
    with open(save_path,'w') as sfile:
        pabar = tqdm(word_counts)
        for i in pabar:
            in_str = str(i).strip('(').strip(')').strip()+'\n'
            sfile.writelines(in_str)
            pabar.set_description("Saving!")
        sfile.close()
    file.close()
# print(Rows[1][1])