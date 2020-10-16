import requests
import sys
import csv
import json
from Function import CrunchBaseRequest_strict

def main():
    url = CrunchBaseRequest_strict.getRequestUrl()
    requestBody = CrunchBaseRequest_strict.getRequestBody()
    crediential = {}
    browser = ()
    i = 0
    twitter = "null"
    companyName = "null"
    outFile = ""
    entityData = []
    totalData = []

    outFile = getCSVOutput()
    print(url)
    response = requests.post(url, json=requestBody)
    if response.status_code == 200:
        print("API Authentication Success.")
        print("Please wait while the program building json data...")
    else:
        print("API Authentication Fail!")
        print(response.json())
    json_response = response.json()
    #print("The length of JSON: ", len(json_response))
    with open(outFile, 'w') as outFile:
        json.dump(json_response, outFile, indent=4)
    #print(requestBody["field_ids"])
    csvHeader = requestBody["field_ids"]
    print("Dump json success")
    outFile.close()
    print("The josn file is in the same folder. Press enter to exit.")
    input()
    sys.exit(0)
    
    
            
def getCSVOutput():
    print("Please enter output json file name (with .json): ")
    fileOut = input()
 
    return fileOut

def writeCSV(dataList, outputFile):
    try:
        csvWriter = csv.writer(outputFile)
        csvWriter.writerow(dataList)
        print("Write into CSV success.")
    except:
        print("Fail to write into CSV!")

def sysExit(fileOut):
    print("The program is finished. The output file is: ", fileOut, " . It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
    
def getValue(json):
    attribs = json.keys()
    for attrib in attribs:
         if attrib == "entities":
             uuid = json[attrib]["uuid"]
             
    pass

def getEntities(json):
    uuid = json["entities"]["uuid"]
    company_type = json["entities"]["company_type"]
    #permalink = json["entities"][

if __name__ == "__main__":
    main()
