import os


def testchecker(dirOfFiles, sol, csvDir):
	filesToCheck = list(filter(lambda x: x.endswith(".py"), os.listdir(dirOfFiles)))

	for i in filesToCheck:
		csvLine = []
		with open((dirOfFiles if dirOfFiles.endswith("/") else dirOfFiles+"/")+i, 'r') as currFile:
			file_data = currFile.readlines(len(sol) + 2)

		for j in file_data:
			if j[0] == "#":
				csvLine.append(j.split(" ")[-1].replace("\n", ""))

		finalcsvline = [csvLine[0], csvLine[1]]
		for (currsol, currans) in zip(sol, csvLine[2:]):
			finalcsvline.append("true" if currsol == currans else "false")

		with open(csvDir, 'a') as csvFile:
			csvFile.write(",".join(finalcsvline) + "\n")
