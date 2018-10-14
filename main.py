import testChecker
import solutionReader

dirOfFiles = raw_input("Please enter the directory with the files:")
dirOfSol = raw_input("Please enter the directory with the solution:")
# dirOfcsv = raw_input("Please enter the directory of the csv:")
dirOfcsv = ".\\solutions.csv"

sol = solutionReader.solution_reader(dirOfSol)

testChecker.testchecker(dirOfFiles, sol, dirOfcsv)
