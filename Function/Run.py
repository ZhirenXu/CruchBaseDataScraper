from Function import CrunchBaseRequest
import requests
import json

def process():
    url = CrunchBaseRequest.getRequestUrl()
    requestBody = CrunchBaseRequest.getRequestBody()
    
    print(url)
    response = requests.post(url, json=requestBody)
    checkResponseStatus(response)
    
    jsonResponse = response.json()
    totalNumOfRecord = int(jsonResponse["count"])
    numOfRequested = len(jsonResponse["entities"])
    if numOfRequested < totalNumOfRecord:
        uuid = getLastUuid(jsonResponse, numOfRequested)
    
    return jsonResponse

def getLastUuid(js, requestNum):
    entities = js["entities"]
    lastEntity = js["entities"][requestNum-1]
    uuid = lastEntity["uuid"]

    return uuid

def checkResponseStatus(post):
    if post.status_code == 200:
        print("API Authentication Success.")
        print("Please wait while the program building json data...")
    else:
        print("API Authentication Fail!")
        print(post.json())
        print("Press enter to exit.")
        input()
        sys.exit(0)
    
def getJsonOutput():
    print("Please enter output json file name (with .json): ")
    fileOut = input()
 
    return fileOut
