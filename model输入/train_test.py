import pandas
from sklearn.model_selection import train_test_split

data0 = pandas.read_csv("../data/csdn/csdn.csv", header=None)
data1 = pandas.read_csv("../data/yahoo/yahoo.csv", header=None)


data0=pandas.DataFrame(data0)
data1=pandas.DataFrame(data1)



X_train, X_test = train_test_split(data0, test_size=0.3, random_state=42)
X_train1, X_test1 = train_test_split(data1, test_size=0.3, random_state=42)

# X_train = pandas.DataFrame(X_train)
# X_test = pandas.DataFrame(X_test)
# X_train1 = pandas.DataFrame(X_train1)
# X_test1 = pandas.DataFrame(X_test1)

print('Save processed files')
X_train.to_csv("../data/csdn/train_test/train.csv",mode='a',index=False,header=None,sep=",")
X_test.to_csv("../data/csdn/train_test/test.csv",mode='a',index=False,header=None,sep=",")
X_train1.to_csv("../data/yahoo/train_test/train.csv",mode='a',index=False,header=None,sep=",")
X_test1.to_csv("../data/yahoo/train_test/test.csv",mode='a',index=False,header=None,sep=",")
