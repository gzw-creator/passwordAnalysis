import pandas
import numpy as np

data0 = pandas.read_csv("../data/yahoo/L.txt", header=None)
data1 = pandas.read_csv("../data/yahoo/D.txt", header=None)
data2 = pandas.read_csv("../data/yahoo/S.txt", header=None)

data0 = pandas.DataFrame(data0)
data1 = pandas.DataFrame(data1)
data2 = pandas.DataFrame(data2)



for i in range(1,len(data0)):

    if len(str(data0.loc[i][0])) == 1:
        data0.loc[[i]].to_csv("../data/yahoo/L/L1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==2):

        data0.loc[[i]].to_csv("../data/yahoo/L/L2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==3):
    
         data0.loc[[i]].to_csv("../data/yahoo/L/L3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==4):
  
         data0.loc[[i]].to_csv("../data/yahoo/L/L4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==5):
       
         data0.loc[[i]].to_csv("../data/yahoo/L/L5.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==6):
  
         data0.loc[[i]].to_csv("../data/yahoo/L/L6.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==7):
      
         data0.loc[[i]].to_csv("../data/yahoo/L/L7.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==8):
    
         data0.loc[[i]].to_csv("../data/yahoo/L/L8.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==9):
     
        data0.loc[[i]].to_csv("../data/yahoo/L/L9.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==10):
    
        data0.loc[[i]].to_csv("../data/yahoo/L/L10.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==11):
     
        data0.loc[[i]].to_csv("../data/yahoo/L/L11.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==12):

        data0.loc[[i]].to_csv("../data/yahoo/L/L12.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==13):
       
        data0.loc[[i]].to_csv("../data/yahoo/L/L13.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==14):
       
        data0.loc[[i]].to_csv("../data/yahoo/L/L14.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==15):
      
        data0.loc[[i]].to_csv("../data/yahoo/L/L15.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==16):
        
        data0.loc[[i]].to_csv("../data/yahoo/L/L16.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==17):
   
        data0.loc[[i]].to_csv("../data/yahoo/L/L17.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==18):
        
        data0.loc[[i]].to_csv("../data/yahoo/L/L18.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==19):

        data0.loc[[i]].to_csv("../data/yahoo/L/L19.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==20):
 
        data0.loc[[i]].to_csv("../data/yahoo/L/L20.txt",mode='a',index=False,header=None,sep=",")

for i in range(1,len(data1)):
    if len(str(data1.loc[i][0])) == 1:
      
        data1.loc[[i]].to_csv("../data/yahoo/D/D1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==2):
 
        data1.loc[[i]].to_csv("../data/yahoo/D/D2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==3):
   
        data1.loc[[i]].to_csv("../data/yahoo/D/D3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==4):
     
        data1.loc[[i]].to_csv("../data/yahoo/D/D4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==5):
   
        data1.loc[[i]].to_csv("../data/yahoo/D/D5.txt",mode='a',index=False,header=None,sep=",")

for i in range(1,len(data2)):
    if len(data2.loc[i][0]) == 1:

        data2.loc[[i]].to_csv("../data/yahoo/S/S1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==2):
 
        data2.loc[[i]].to_csv("../data/yahoo/S/S2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==3):
 
        data2.loc[[i]].to_csv("../data/yahoo/S/S3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==4):

        data2.loc[[i]].to_csv("../data/yahoo/S/S4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==5):

        data2.loc[[i]].to_csv("../data/yahoo/S/S5.txt",mode='a',index=False,header=None,sep=",")