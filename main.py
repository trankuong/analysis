# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: Main Function
# Description: This file contains the driver for the extension

import sys
import printer
import stockCsv
import stockParseCSV

"""
Use this function as the driver for the project extension
"""
def main(argv):
    dictionary = stockParseCSV.parseCSVFile("stockdata.csv")
    printer.header()
    print "What do you expect the return of the S&P 500 index to be tomorrow?"
    percent = float(raw_input("Please enter response as a percentage point: "))

    symbol = ""
    while (symbol != "quit"):
        printer.printStocks()
        symbol = raw_input('Please enter a stock ticker'
                           ' symbol you wish to investigate or enter "quit": ')
        stockCsv.stockSelect(symbol, percent, dictionary)
    printer.closer()


# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__main__":
    main(sys.argv)
