from Function import CrunchBaseRequest
import requests
import json

def process(outFile):
    numOfRequested = 0
    numOfMerged = 0
    listOfJson = []
    
    url = CrunchBaseRequest.getRequestUrl()
    requestBody = CrunchBaseRequest.getRequestBody()
    
    print("Send request to: \n\t", url, "\n")
    response = getResponse(url, requestBody)
    
    jsonResponse = response.json()

    totalNumOfRecord = int(jsonResponse["count"])
    print("\nTotal number of available result: ", totalNumOfRecord)
    numOfRequested = len(jsonResponse["entities"])
    numOfMerged += numOfRequested
    updateRequestBody(jsonResponse, numOfRequested, requestBody)
    
    while numOfMerged < totalNumOfRecord:
        print("Already receive ", numOfMerged, " / ", totalNumOfRecord, "records...", end = "")
        newResponse = requests.post(url, json=requestBody)
        newEntities = newResponse.json()["entities"]
        numOfRequested = len(newEntities)
        updateRequestBody(newResponse.json(), numOfRequested, requestBody)
        for entity in newEntities:
            jsonResponse["entities"].append(entity)
        print("Merge into JSON complete.")
        numOfMerged += numOfRequested
    print("Already receive ", numOfMerged, " / ", totalNumOfRecord, "records.\n")
    
    return jsonResponse

def updateRequestBody(jsonResponse, numOfRequested, requestBody):
    uuid = getLastUuid(jsonResponse, numOfRequested)
    requestBody['after_id'] = uuid

def getResponse(url, requestBody):
    response = requests.post(url, json=requestBody)
    checkResponseStatus(response)

    return response

def getLastUuid(js, requestNum):
    #print(js)
    entities = js["entities"]
    lastEntity = js["entities"][requestNum-1]
    uuid = lastEntity["uuid"]
    #print("new uuid: ", uuid)
    
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
