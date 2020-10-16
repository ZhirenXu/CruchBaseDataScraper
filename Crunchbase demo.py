import requests
import sys
import csv
import json
from Function import CrunchBaseRequest

def main():
    url = CrunchBaseRequest.getRequestUrl()
    requestBody = CrunchBaseRequest.getRequestBody()
    crediential = {}
    browser = ()
    i = 0
    twitter = "null"
    companyName = "null"
    outFile = ""
    entityData = []
    totalData = []
    
    print(url)
    response = requests.post(url, json=requestBody)
    if response.status_code == 200:
        print("API Authentication Success.")
        print("Please wait while the program building json data...")
    else:
        print("API Authentication Fail!")
        print(response.json())
    json_response = response.json()
    print(json_response)
    with open("venture2.json", 'w') as outFile:
        json.dump(json_response, outFile)
    #print(requestBody["field_ids"])
    csvHeader = requestBody["field_ids"]
    print("Dump json success")
    outFile.close()
    
            
def getCSVOutput():
    print("Please enter output file name (with .csv): ")
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
