import requests
import sys
import csv
import json
from Function import CrunchBaseRequest
from Function import Greeting
from Function import Run

##TODO: get into run and use the uuid to generate new request body
def main():
    Greeting.showInfo()
    outFileName = Run.getJsonOutput()
    jsonResponse = Run.process(outFileName)
    with open(outFileName, 'a') as outFile:
        print("Dumping JSON... The time is around 3-5 mins depend on file size.")
        json.dump(jsonResponse, outFile, indent=4)
    print("Dump json success.")
    Greeting.sysExit(outFileName)    

if __name__ == "__main__":
    main()
