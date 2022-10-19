import pandas
import numpy as np

data0 = pandas.read_csv("./L.txt", header=None)
data1 = pandas.read_csv("./D.txt", header=None)
data2 = pandas.read_csv("./S.txt", header=None)

data0 = pandas.DataFrame(data0)
data1 = pandas.DataFrame(data1)
data2 = pandas.DataFrame(data2)



for i in range(1,len(data0)):

    if len(str(data0.loc[i][0])) == 1:
        data0.loc[[i]].to_csv("../L/L1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==2):

        data0.loc[[i]].to_csv("../L/L2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==3):
    
         data0.loc[[i]].to_csv("../L/L3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==4):
  
         data0.loc[[i]].to_csv("../L/L4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==5):
       
         data0.loc[[i]].to_csv("../L/L5.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==6):
  
         data0.loc[[i]].to_csv("../L/L6.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==7):
      
         data0.loc[[i]].to_csv("../L/L7.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==8):
    
         data0.loc[[i]].to_csv("../L/L8.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==9):
     
        data0.loc[[i]].to_csv("../L/L9.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==10):
    
        data0.loc[[i]].to_csv("../L/L10.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==11):
     
        data0.loc[[i]].to_csv("../L/L11.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==12):

        data0.loc[[i]].to_csv("../L/L12.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==13):
       
        data0.loc[[i]].to_csv("../L/L13.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==14):
       
        data0.loc[[i]].to_csv("../L/L14.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==15):
      
        data0.loc[[i]].to_csv("../L/L15.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==16):
        
        data0.loc[[i]].to_csv("../L/L16.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==17):
   
        data0.loc[[i]].to_csv("../L/L17.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==18):
        
        data0.loc[[i]].to_csv("../L/L18.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==19):

        data0.loc[[i]].to_csv("../L/L19.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==20):
 
        data0.loc[[i]].to_csv("../L/L20.txt",mode='a',index=False,header=None,sep=",")

for i in range(1,len(data1)):
    if len(str(data1.loc[i][0])) == 1:
      
        data1.loc[[i]].to_csv("../D/D1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==2):
 
        data1.loc[[i]].to_csv("../D/D2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==3):
   
        data1.loc[[i]].to_csv("../D/D3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==4):
     
        data1.loc[[i]].to_csv("../D/D4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==5):
   
        data1.loc[[i]].to_csv("../D/D5.txt",mode='a',index=False,header=None,sep=",")

for i in range(1,len(data2)):
    if len(data2.loc[i][0]) == 1:

        data2.loc[[i]].to_csv("../S/S1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==2):
 
        data2.loc[[i]].to_csv("../S/S2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==3):
 
        data2.loc[[i]].to_csv("../S/S3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==4):

        data2.loc[[i]].to_csv("../S/S4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==5):

        data2.loc[[i]].to_csv("../S/S5.txt",mode='a',index=False,header=None,sep=",")