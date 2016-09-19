# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: This file is used to predict stocks
# Description: Contains the function to predict, select, and create lists
import sys
import measures
import diagnostics
import printer
"""
Requires: nothing
Modifies: nothing
Effects: returns the header
"""

def stockSelect(symbol, percent, dictionary):
    listOfTickers = tickerList(dictionary)
    tickerCheck = False
    for tickerName in listOfTickers:
        if symbol == tickerName:
            tickerCheck = True
        if symbol == "S&P":
            tickerCheck = False
    if tickerCheck:
        prediction = stockPredictor(symbol, percent, dictionary)
        printer.printPrediction(prediction, percent, symbol)
    elif symbol == "quit":
        pass
    else:
        print "\nInvalid command, try again"


def stockPredictor(symbol, percent, dictionary):
    all = []
    listOfChange = []
    sp = []
    all = dictionary[symbol]
    for each in all:
        listOfChange.append(each[6])
    listOfBase = []
    sp = dictionary["S&P"]
    for each in sp:
        listOfBase.append(each[6])
    changeMean = measures.mean(listOfChange)
    baseMean = measures.mean(listOfBase)
    changeStandDev = measures.stdev(listOfChange)
    baseStandDev = measures.stdev(listOfBase)
    covariance = diagnostics.singlePopulationCovariance(listOfBase,
                                                        listOfChange,
                                                        baseMean,
                                                        changeMean)
    correlation = float(covariance / (changeStandDev * baseStandDev))
    prediction = changeMean + (correlation * percent)
    return prediction

def tickerList(dictionary):
    key = []
    for tick in dictionary:
        key.append(tick)
    return key


if __name__ == "__stockCsv__":
    main(sys.argv)

   