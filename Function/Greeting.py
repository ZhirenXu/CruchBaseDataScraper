import sys

## print program info
def showInfo():
    print("*******************************************")
    print("*   Crunchbase JSON Data Scrapper v1.0.1  *")
    print("*           Author: Zhiren Xu             *")
    print("*        published data: 10/29/20         *")
    print("*******************************************")

## print exit message
# @param    fileOut
#           name of output file
def sysExit(fileOut):
    print("The program is finished. The output file is: ", fileOut, " . It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
