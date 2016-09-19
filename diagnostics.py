# Authors: Anand Jetha Dylan Delaney Kuong Tran Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: Calculate sample covariance and correlation
# Description: Takes data from CVS parse and lists to calculate sample
#				covariance and correlation against all other data lists
#				collected from the file

import sys
import math
import eecsCsv
import measures

"""
Requires: xVals is a list of all of the values for the first random variable
	yVals is a list of all of the values for the second random variable
	meanX is the average of all of the values in xVals
	meanY is the average of all of the values in yVals
Modifies: nothing
Effects: returns the sample covariance between xVals and yVals
"""
def singlePopulationCovariance(xVals, yVals, meanX, meanY):
	varianceX = 0.0
	varianceY = 0.0
	product = 0.0
	covariance = 0.0
	total = 0.0
	step = 0
	for value in xVals:
		varianceX = value - meanX
		varianceY = yVals[step] - meanY
		step += 1
		product = varianceX * varianceY
		total += product
	covariance = total / (len(xVals))
	return covariance


"""
Requires: dictionary is a dictionary built by parseCSVFile
		inclusionList is the same length as all of the entries in dictionary
		for each entry in inclusionList, the value is 1 if that entry is to be
			included in the correlation matrix, and 0 if it is not
Modifies: nothing
Effects: returns a list of lists, holding the correlation matrix for the
	selected entries
"""
def correlationMatrix(dictionary, inclusionList):
	matrix = [] #holds the retrieved data
	index = 0
	for indicator in inclusionList:
		if indicator == 1: #1 indicated inclusion
			matrix.append(eecsCsv.retrieveEntireAttribute(dictionary, index))
		index += 1
	corrMatrix = [] #holds the correlation values between two data sets
	#holds the correlation values for a row of the correlation matrix
	rowList = []
	indexRow = 0 #used to index the first list
	indexColumn = 0 #used to index the second list
	for indexRow in range(len(matrix)): #does rows
		for indexColumn in range(len(matrix)): #does columns
			cell = singlePopulationCovariance(matrix[indexRow],
											  matrix[indexColumn],
											  measures.mean(matrix[indexRow]),
											  measures.mean(matrix[indexColumn]))
			cell = cell / (measures.stdev(matrix[indexRow]) *
						   measures.stdev(matrix[indexColumn]))
			rowList.append(cell)
		corrMatrix.append(rowList)
		rowList = []
	return corrMatrix



# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__diagnostics__":
	main(sys.argv)
