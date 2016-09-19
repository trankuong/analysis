# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: Store all large prints
# Description: Hold the function to print header, closer, and menu

import sys
import stockParseCSV

"""
Requires: nothing
Modifies: nothing
Effects: prints the header
"""
def header():
    print "========================================================"
    print "               Welcome to Stock Predictor               "
    print "========================================================\n"
    pass

"""
Requires: nothing
Modifies: nothing
Effects: prints the closer
"""
def closer():
    print "\n========================================================"
    print "            Thanks for using Stock Predictor            "
    print "========================================================"
    pass

"""
Requires: nothing
Modifies: nothing
Effects: prints the stock menu
"""
def printStocks():
    print ""
    print "Company Name:             Ticker Symbol:"
    print "-------------             --------------"
    dict = stockParseCSV.parseCSVFile('stockdata.csv')
    for each in dict:
        if each != 'S&P':
            print '{0:26s}{1}{2}' .format(dict[each][0][-1], ': ', dict[each][0][0])

def printPrediction(prediction, percent, symbol):
    print "\nGiven that you believe the S&P 500 index will have a return of",
    print str(percent) + "%"
    print str(symbol) + " is estimated to return " + str(prediction) + (
        "% the next trading day.")


if __name__ == "__printer__":
	main(sys.argv)