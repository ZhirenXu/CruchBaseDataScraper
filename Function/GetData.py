import json

# @return
#       A single list contain all data, data is pure string
def getData(json, header):
    propertyDict = json["entities"]["properties"]
    if propertyDict.has_key("acquirer_identifier"):
        acquirerList = locals getAcquirer(json)
    else:
        acquirerList = ["null"]
    if propertyDict.has_key("aliases"):  
        aliasList = getAlias(json)
    else:
        aliasList = ["null"]
    if propertyDict.has_key("categories"):
        categoryList = getCategories(json)
    else:
        categoryList = ["null"]
    if propertyDict.has_key("category_groups"):
        categoryGroupList = getCategoryGroup(json)
    else:
        categoryGroupList = ["null"]
    if propertyDict.has_key("closed_on"):
        closedOnList = getClosedOn(json)
    else:
        closedOnList = ["null"]
    if propertyDict.has_key("company_type"):
        companyTypeList = getCompanyTypeList(json)
    else:
        companyTypeList = ["null"]
    print(acquirerList, "\n", aliasList, "\n", categoryList)

def getAlias(data):
    aliases = json["entities"]["properties"]["aliases"]
    
    
