import os
import shutil

dirOfFiles = raw_input("Please enter the directory with the files:")
numOfLinesToRead = input("please enter the number of liens to read from the file")
filesToCheck = os.listdir(dirOfFiles)

filesToCheckNew = []
for i in filesToCheck:
	if i.endswith(".py"):
		filesToCheckNew.append(i)

for i in filesToCheckNew:
	csvLine = ""
	with open(i, 'r') as currFile:
		fileData = currFile.readlines(int(numOfLinesToRead))

	fileLines = fileData

	for currLine in fileLines:
		if currLine[0] == "#":
			csvLine += currLine.split(" ")[-1] + ","

	csvLine = csvLine[0:-2]

	with open(".\\solutions.csv", 'w') as csvFile:
		csvFile.write(csvLine)
