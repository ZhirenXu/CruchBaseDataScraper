import requests
import sys
import csv
import json
from Function import CrunchBaseRequest
from Function import Greeting
from Function import Run

##TODO: get into run and use the uuid to generate new request body
def main():
    outFile = Run.getJsonOutput()
    jsonResponse = Run.process()
    with open(outFile, 'w') as outFile:
        json.dump(jsonResponse, outFile, indent=4)
    print("Dump json success.")
    outFile.close()
    numOfRecord = len(jsonResponse["entities"])
    print("This request contains ", numOfRecord, "entities")
    Greeting.sysExit(outFile)    

if __name__ == "__main__":
    main()
