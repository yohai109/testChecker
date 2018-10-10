import os


def testchecker(dirOfFiles, sol, csvDir):
	filesToCheck = list(filter(lambda x: x.endswith(".py"), os.listdir(dirOfFiles)))

	# filesToCheckNew = []
	# for i in filesToCheck:
	# 	if i.endswith(".py"):
	# 		filesToCheckNew.append(i)

	for i in filesToCheck:
		csvLine = []
		with open(i, 'r') as currFile:
			fileData = currFile.readlines(len(sol) + 2)

		fileLines = fileData

		for currLine in fileLines:
			if currLine[0] == "#":
				csvLine.append(currLine.split(" ")[-1])

		finalcsvline = [csvLine[0], csvLine[1]]
		for currsol, currans in sol, csvLine.split(",")[2:-1]:
			finalcsvline.append("true" if currsol == currans else "false")

		with open(csvDir, 'a') as csvFile:
			csvFile.writelines(",".join(finalcsvline))

