# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: calculates statistical measures of our data set
# Description: takes in a list holding numerical data and returns statistical measures including the mean, variance,
# 			   standard deviation and median.

import sys
import math
import eecsCsv
import diagnostics
import generation

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the average of the numbers in data
"""
def mean(data):
	total = 0.0
	count = 0
	mean = 0.0
	if len(data) == 0:
		return "List contains no data"
	else:
		for number in data:
			total += number
			count += 1
		mean = total / count
	return mean

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the variance of the numbers in data. an explanation of how to
	calculate variance is in the spec
"""
def variance(data):
	count = 0
	total = 0.0
	diff = 0.0
	square = 0.0
	var = 0.0
	if len(data) == 0:
		return "List contains no data"
	else:
		for number in data:
			diff = number - mean(data)
			square = diff ** 2
			total += square
			count += 1
		var = total / count
		return var

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the standard deviation of the numbers in data
"""
def stdev(data):
	dev = 0.0;
	if len(data) == 0:
		return "List contains no data"
	else:
		dev = math.sqrt(variance(data))
		return dev

"""
Requires: data is a list of numbers
Modifies: data
Effects: returns the median of the numbers in data. be careful that when you use
	this function, that the order of the objects in data will be modified.
	therefore, any lists that are passed to data must be able to be changed
"""
def median(data):
	data.sort()
	middle = len(data) / 2
	med = 0.0
	if len(data) == 0:
		return "List contains no data"
	else:
		data.sort()
		middle = len(data) / 2
		if len(data) % 2 == 0:
			med = (data[middle] + data[middle-1]) / 2.0
		else:
			med = data[len(data) / 2]
		return med




# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__measures__":
	main(sys.argv)


