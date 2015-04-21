import pandas as pd

class twoCSVCombiner:

    def _init_(self,fileOne,fileTwo,outPath):
		self.fileOne = self.fileOne
		self.fileTwo = self.fileTwo
		self.outPath = self.outPath
    

    def readerWriter(self,fileOne,fileTwo,outPath):
        outPath = open(outPath,'wb')

        fileOne = pd.read_csv(fileOne,sep=',',dtype=object)
        fileTwo = pd.read_csv(fileTwo,sep=',',dtype=object)

        fileOneDataframe = pd.DataFrame(fileOne)
		fileTwoDataFrame = pd.DataFrame(fileTwo)

        fileOneOut = fileOneDataframe.to_csv(outPath,sep=',',header=True)
		fileTwoOut = fileTwoDataFrame.to_csv(outPath,sep=',',header=True)
   








