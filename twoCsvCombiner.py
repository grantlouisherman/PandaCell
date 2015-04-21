#@author:Grant Herman
#Python 2.7
import pandas as pd

class twoCSVCombiner:

    def _init_(self,fileOne,fileTwo,outPath):
		self.fileOne = self.fileOne
		self.fileTwo = self.fileTwo
		self.outPath = self.outPath
    

    def readerWriter(self,fileOne,fileTwo,outPath):
        # This is the outpath that you want to write the two files to
        outPath = open(outPath,'wb')
	#This reads in both csv files using pandas and sets the dtype to object. 
	# If you want to do mathematical operations you can change the dtype to float32-64 
        fileOne = pd.read_csv(fileOne,sep=',',dtype=object)
        fileTwo = pd.read_csv(fileTwo,sep=',',dtype=object)
	#These are the data frames that will write to the specified outpath 
        fileOneDataframe = pd.DataFrame(fileOne)
	fileTwoDataFrame = pd.DataFrame(fileTwo)
	#This is the writing to the outpath via the DataFrames
        fileOneOut = fileOneDataframe.to_csv(outPath,sep=',',header=True)
	fileTwoOut = fileTwoDataFrame.to_csv(outPath,sep=',',header=True)
   








