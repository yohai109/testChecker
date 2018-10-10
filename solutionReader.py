

def solutionReader(solutionFileDir):
	"""
	this function reads the solution file and returns the solutions from it
	"""
	with open(solutionFileDir, 'r') as solFile:
		filedata = solFile.readlines()

	sollist = ""
	for i in filedata:
		if i.startswith("#"):
			sollist += "," + i.split(" ")[-1]

	return sollist.split(',')[1:-1]
