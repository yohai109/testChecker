

def solution_reader(solution_file_dir):
	"""
	this function reads the solution file and returns the solutions from it
	"""
	with open(solution_file_dir, 'r') as solFile:
		filedata = solFile.readlines()

	sol_list = []
	for i in filedata:
		if i.startswith("#"):
			sol_list.append(i.split(" ")[-1])

	return sol_list
