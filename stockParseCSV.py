# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: This file is used to parse the CSV data file
# Description: Defines functions to break the data up and collect
#              desired information.
import sys
'''
Converts a list to have the appropriate values and returns it.
The new list is in form str str float float float float int
'''
def addList(lister):
    #makes a list
    allData = []
    #makes all floats
    opening = float(lister[2])
    high = float(lister[3])
    low = float(lister[4])
    close = float(lister[5])
    percentChange = float(lister[6])
    #make the correct list style and returns
    allData = [lister[0], lister[1], opening, high, low, close, percentChange, lister[7]]
    return allData
'''
Makes a csv file into a dictionary
The stock ticker is the key
Makes a list of a list for the days of that stock
'''
def parseCSVFile(fileName):
    dataValues = {}
    listings = []
    allData = []
    obj = []
    ticker = ' '
    obj = open(fileName, 'r')#.read().split('\r')
    #makes 2d array of every line
    for each in obj:
        listings = each.split(',')
        allData.append(listings)
    for lists in allData:
        lists.pop() #would remove endline if comma at end of each line
        if ticker != lists[0]:
            ticker = lists[0]
            dataValues[ticker] = []
            dataValues[ticker].append(addList(lists))
        else:
            dataValues[ticker].append(addList(lists))
    return dataValues
"""
This function retrieves an entry from the list of entries in the dictionary
for a given key and position in the list for the key.
Requires: dictionary is the dictionary built in parseCSVFile, key is the
key from which we want to fetch values, and entry is the index of the
entry we wish to fetch
Modifies: nothing
Effects: retrieves a single entry from the list of entries in the dictionary
such that entry holds the position in the list of entries, and that key
is the key from which we wish to fetch it
"""
def retrieveValue(dictionary, key, entry):
    data = dictionary[key]
    spot = data[entry]
    return spot
"""
Requires: dictionary holds a dictionary created by parseCSVFile
columnNo holds the index of the attribute we wish to create a list from
Modifies: nothing
Effects: returns a list of the values in the column specified by columnNo
"""
def retrieveEntireAttribute(dictionary, columnNo):
    values = []
    for line in dictionary:
        key = line
        listing = dictionary[key]
    #adds column of list in list
    for each in listing:
        values.append(each[columnNo])
    return values

# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__stockParseCSV__":
    main(sys.argv)