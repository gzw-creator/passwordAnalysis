import pandas
import numpy as np

path = "../data/csdn/"

data0 = pandas.read_csv(path+"L.txt", header=None)
data1 = pandas.read_csv(path+"D.txt", header=None)
data2 = pandas.read_csv(path+"S.txt", header=None)

data0 = pandas.DataFrame(data0)
data1 = pandas.DataFrame(data1)
data2 = pandas.DataFrame(data2)



for i in range(1,len(data0)):

    if len(str(data0.loc[i][0])) == 1:
        data0.loc[[i]].to_csv(path+"L/L1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==2):

        data0.loc[[i]].to_csv(path+"L/L2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==3):
    
         data0.loc[[i]].to_csv(path+"L/L3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==4):
  
         data0.loc[[i]].to_csv(path+"L/L4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==5):
       
         data0.loc[[i]].to_csv(path+"L/L5.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==6):
  
         data0.loc[[i]].to_csv(path+"L/L6.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==7):
      
         data0.loc[[i]].to_csv(path+"L/L7.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==8):
    
         data0.loc[[i]].to_csv(path+"L/L8.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==9):
     
        data0.loc[[i]].to_csv(path+"L/L9.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==10):
    
        data0.loc[[i]].to_csv(path+"L/L10.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==11):
     
        data0.loc[[i]].to_csv(path+"L/L11.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==12):

        data0.loc[[i]].to_csv(path+"L/L12.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==13):
       
        data0.loc[[i]].to_csv(path+"L/L13.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==14):
       
        data0.loc[[i]].to_csv(path+"L/L14.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==15):
      
        data0.loc[[i]].to_csv(path+"L/L15.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==16):
        
        data0.loc[[i]].to_csv(path+"L/L16.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==17):
   
        data0.loc[[i]].to_csv(path+"L/L17.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==18):
        
        data0.loc[[i]].to_csv(path+"L/L18.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==19):

        data0.loc[[i]].to_csv(path+"L/L19.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data0.loc[i][0]))==20):
 
        data0.loc[[i]].to_csv(path+"L/L20.txt",mode='a',index=False,header=None,sep=",")

for i in range(1,len(data1)):
    if len(str(data1.loc[i][0])) == 1:
        data1.loc[[i]].to_csv(path+"D/D1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==2):
        data1.loc[[i]].to_csv(path+"D/D2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==3):
        data1.loc[[i]].to_csv(path+"D/D3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==4):
        data1.loc[[i]].to_csv(path+"D/D4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==5):
        data1.loc[[i]].to_csv(path+"D/D5.txt",mode='a',index=False,header=None,sep=",")
    elif (len(str(data1.loc[i][0]))==6):
        data1.loc[[i]].to_csv(path + "D/D6.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 7):
        data1.loc[[i]].to_csv(path + "D/D7.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 8):
        data1.loc[[i]].to_csv(path + "D/D8.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 9):
        data1.loc[[i]].to_csv(path + "D/D9.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 10):
        data1.loc[[i]].to_csv(path + "D/D10.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 11):
        data1.loc[[i]].to_csv(path + "D/D11.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 12):
        data1.loc[[i]].to_csv(path + "D/D12.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 13):
        data1.loc[[i]].to_csv(path + "D/D13.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 14):
        data1.loc[[i]].to_csv(path + "D/D14.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 15):
        data1.loc[[i]].to_csv(path + "D/D15.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 16):
        data1.loc[[i]].to_csv(path + "D/D16.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 17):
        data1.loc[[i]].to_csv(path + "D/D17.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 18):
        data1.loc[[i]].to_csv(path + "D/D18.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 19):
        data1.loc[[i]].to_csv(path + "D/D19.txt", mode='a', index=False, header=None, sep=",")
    elif (len(str(data1.loc[i][0])) == 20):
        data1.loc[[i]].to_csv(path + "D/D20.txt", mode='a', index=False, header=None, sep=",")

for i in range(1,len(data2)):
    if len(data2.loc[i][0]) == 1:
        data2.loc[[i]].to_csv(path+"S/S1.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==2):
        data2.loc[[i]].to_csv(path+"S/S2.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==3):
        data2.loc[[i]].to_csv(path+"S/S3.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==4):
        data2.loc[[i]].to_csv(path+"S/S4.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==5):
        data2.loc[[i]].to_csv(path+"S/S5.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0]) == 6):
        data2.loc[[i]].to_csv(path + "S/S6.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 7):
        data2.loc[[i]].to_csv(path + "S/S7.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 8):
        data2.loc[[i]].to_csv(path + "S/S8.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 9):
        data2.loc[[i]].to_csv(path + "S/S9.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 10):
        data2.loc[[i]].to_csv(path + "S/S10.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0])==11):
        data2.loc[[i]].to_csv(path+"S/S11.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==12):
        data2.loc[[i]].to_csv(path+"S/S12.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==13):
        data2.loc[[i]].to_csv(path+"S/S13.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0])==14):
        data2.loc[[i]].to_csv(path+"S/S14.txt",mode='a',index=False,header=None,sep=",")
    elif (len(data2.loc[i][0]) == 15):
        data2.loc[[i]].to_csv(path + "S/S15.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 16):
        data2.loc[[i]].to_csv(path + "S/S16.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 17):
        data2.loc[[i]].to_csv(path + "S/S17.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 18):
        data2.loc[[i]].to_csv(path + "S/S18.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 19):
        data2.loc[[i]].to_csv(path + "S/S19.txt", mode='a', index=False, header=None, sep=",")
    elif (len(data2.loc[i][0]) == 20):
        data2.loc[[i]].to_csv(path + "S/S20.txt", mode='a', index=False, header=None, sep=",")