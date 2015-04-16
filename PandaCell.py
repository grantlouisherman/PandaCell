import csv
import pandas as pd
#@author: Grant Herman

#This will combine two csv files into on output file
def twoCSVCombiner(fileONE,fileTWO,outPath):
    
    fileONE = pd.read_csv(fileONE,sep=',')
    fileTWO = pd.read_csv(fileTWO,sep=',')
    outPath = open(outPath,'wb')
    fileOneDataFrame = pd.DataFrame(fileONE)
    fileTwoDataFrame = pd.DataFrame(fileTWO)
    
    fileOneDataFrame.to_csv(outPath,sep=',',header=True)
    fileTwoDataFrame.to_csv(outPath,sep=',',header=True)

#This is still a work in progress
def CSVCombinerInput(fileIn,outPath):
    fileIn = pd.read_csv(fileIn, sep=',')
        outPath = open(outPath,'wb')
        fileDataFrame = pd.DataFrame(fileIn)
        fileDataFrame.to_csv(outPath,sep=',',header=True)
        
        more = input("Do you want to add another file?(y/n)[Note: Please put "" around your answer")
        
        if(more == "y"):
            File = input("Name of file input")
            Path = input("Name of path")
                return CSVCombinerInput(File,Path)
        else:
            return


    
    





	








