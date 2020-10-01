def main():
    for pair in json_response["entities"]:
        #print("Pair: ", pair)
        #print(pair['properties'].keys())
        companyName = pair['properties']['identifier']['permalink']
        print("name: ", companyName)
        if 'twitter' in pair['properties'].keys():
            twitter = pair["properties"]["twitter"]["value"]
            print("twitter Link: ", twitter)
        else:
            print("twitter Link: Null")
            twitter = "null"
        entityData.append(companyName)
        entityData.append(twitter)
        totalData.append(entityData)
        entityData = []

    fileOut = getCSVOutput()
    outFile = open(fileOut, 'w', encoding = 'utf8', newline='')
    writeCSV(["company name", "Twitter"], outFile)
    for entity in totalData:
        writeCSV(entity, outFile)
    outFile.close()
    sysExit(fileOut)
