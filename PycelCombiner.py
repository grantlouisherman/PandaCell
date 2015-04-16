import csv
import pandas as pd



def twoCSVCombiner(fileONE,fileTWO,outPath):
    
    fileONE = pd.read_csv(fileONE,sep=',')
    fileTWO = pd.read_csv(fileTWO,sep=',')
    outPath = open(outPath,'wb')
    fileOneDataFrame = pd.DataFrame(fileONE)
    fileTwoDataFrame = pd.DataFrame(fileTWO)
    
    fileOneDataFrame.to_csv(outPath,sep=',',header=True)
    fileTwoDataFrame.to_csv(outPath,sep=',',header=True)


    
    





	








