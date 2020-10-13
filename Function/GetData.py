import json

class Organization:
    acquirer: dict
    alias: list
    category: list
    categoryGroup: list
    closedOn: dict
    compantType: str
    contactEmail: str
    createdAt: str
    delistedOn: dict
    demoDays: bool
    description: str
    diversitySpotlights: list
    entityDefID: str
    equityFundingTotal: dict
    exitedOn: dict
    facebook: dict
    facetIDs: list
    foundedOn: dict
    founderIDs: list
    fundingStage: str
    fundingTotal: dict
    hubTags: list
    imageID: str
    imageUrl: str
    investorIDs: list
    investorStage: list
    investorType: list
    ipoStatus: str
    lastEquityFundingTotal: dict
    lastEquityFundingType: str
    lastFundingAt: str
    lastFundingTotal: dict
    lastFundingType: str
    lastKeyEmployeeChangeDate: str
    layoutID: str
    legalName: str
    linkedin: dict
    listedStockSymbol: str
    locationGroupIDs: list
    locationIDs: list
    name: str
    numAcquisitions: int
    numAlumni: int
    numArticles: int
    numCurrentAdvisorPositions: int
    numCurrentPositions: int
    numDiversitySpotlightInvestments: int
    numEmployeeEnum: str
    numEnrollments: str
    numEventAppearance: int
    numExits: int
    numExitsIPO: int
    numFounderAlumni: int
    numFounder: int
    numFundingRound: int
    numFunds: int
    numInvestments: int
    numInvestors: int
    numLeadInvestments: int
    numLeadInvestors: int
    numPastPositions: int
    numPortfolioOrg: int
    numSubOrg: int
    operatingStatus: str
    overrideLayoutID: str
    ownerID: dict
    permalink: str
    permaAliases: list
    phoneNum: str
    programApplicationDeadline: str
    programDuring: int
    programType: str
    rankDelta30: float
    rankDelta7: float
    rankDelta90: float
    rankOrg: int
    rankPrincipal: int
    revenueRange: str
    schoolMethod: str
    schoolProgram: str
    schoolType: str
    shortDescription: str
    status: str
    stockExchangeSymbol: str
    stockSymbol: dict
    twitter: dict
    updateAt: str
    uuid: str
    valuation: dict
    valuationDate: str
    website: dict
    websiteUrl: str
    wentPublicOn: str
    
    def getAcquirer

    class EntityIdentifier:
        uuid: str
        permalink: str
        value: str
        imageID: str
        entityDefID: str

        def __init__(self):
            uuid = ""
            permalink = ""
            value = ""
            imageID = ""
            entityDefID = ""
        
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
    if propertyDict.has_key("contact_email"):
        emailList = getContactEmail(json)
    else:
        emailList = ["null"]
    if propertyDict.has_key("created_at"):
        createTime = getCreateTime(json)
    else:
        createTime = ["null"]
    if propertyDict.has_key("delisted_on"):
        delistDate = getDelistDate(json)
    else:
        delistDate = ["null"]
    if propertyDict.has_key("demo_days"):
        hasDemo = getDemoDay(json)
    else:
        hasDemo = ["null"]
    if propertyDict.has_key("description"):
        description = getDescription(json)
    else:
        description = ["null"]
    if propertyDict.has_key("diversity_spotlights"):
        diversity = getDiversity(json)
    else:
        diversity = ["null"]
    if propertyDict.has_key("entity_def_id"):
        entityDef = getEntityDef(json)
    else:
        entityDef = ["null"]
    if propertyDict.has_key("equity_funding_total"):
        entityFunding = getEntityFunding(json)
    else:
        entityDef = ["null"]
    if propertyDict.has_key("exited_on"):
        exitDate = getExitDate(propertyDict["exited_on"])
    else:
        exitDate = ["null"]
    if propertyDict.has_key("facebook"):
        facebook = getFacebook(propertyDict["facebook"])
    else:
        facebook = ["null"]
    if propertyDict.has_key("facet_ids"):
        facet = getFacet(propertyDict["facet_ids"])
    else:
        facet = ["null"]
    if propertyDict.has_key("founded_on"):
        foundDate = getFoundDate(propertyDict["founded_on"])
    else:
        foundDate = ["null"]
    if propertyDict.has_key("founder_identifiers"):
        founderID = getFounderID(propertyDict["founder_identifiers"])
    else:
        founderID = ["null"]
    if propertyDict.has_key("funding_stage"):
        fundingStage = getFundingStage(propertyDict["funding_stage"])
    else:
        fundingStage = ["null"]
    if propertyDict.has_key("funding_total"):
        funding_total = getFundingTotal(propertyDict["funding_total"])
    else:
        funding_total = ["null"]
    if propertyDict.has_key("hub_tags"):
        hubTag = getHubTag(propertyDict["hub_tags"])
    else:
        hubTag = ["null"]
    if propertyDict.has_key("identifier"):
        identifierList = getIdentifier(propertyDict["identifier"])
    else:
        identifierList = ["null"]
    if propertyDict.has_key("image_id"):
        imageID = getImageID(propertyDict["image_id"])
    else:
        imageID = ["null"]
    if propertyDict.has_key("image_url"):
        imageUrl = getImageUrl(propertyDict["image_url"])
    else:
        imageUrl = ["null"]
    if propertyDict.has_key("investor_identifiers"):
        investerIDList = getInvesterID(propertyict["investor_identifiers"])
    else:
        investerIDList = ["null"]
    if propertyDict.has_key("investor_stage"):
        investorStage = getInvestorStage(propertyDict["investor_stage"])
    else:
        invetorStage = ["null"]
    if propertyDict.has_key("investor_type"):
        investorType = getInvestorType(propertyDict["investor_type"])
    else:
        investorType = ["null"]
    if propertyDict.has_key("ipo_status"):
        ipo = getIPOStatus(propertyDict["ipo_status"])
    else:
        ipo = ["null"]
    if propertyDict.has_key("last_equity_funding_total"):
        equityFundTotal = getEquityFundTotal(propertyDict["last_equity_funding_total"])
    else:
        equityFundTotal = ["null"]
    if propertyDict.has_key("last_equity_funding_type"):
        equityFundType = getEquityFundType(propertyDict["last_equity_funding_type"])
    else:
        equityFundType = ["null"]
    if propertyDict.has_key("last_funding_at"):
        lastFundAt = getLastFundAt(propertyDict["last_funding_at"])
    else:
        lastFundAt = ["null"]
    if propertyDict.has_Key("last_funding_total"):
        lastFundTotal = getLastFundTotal(propertyDict["last_finding_total"])
    else:
        lastFundTotal = ["null"]
    if propertyDict.has_Key("last_funding_type"):
        lastFundType = getLastFundType(propertyDict["last_funding_type"])
    else:
        lastFundType = ["null"]
    if propertyDict.has_key("last_key_employee_change_date"):
        keyEmployeeChange = getKeyEmployeeChange(propertyDict["last_key_employee_change_date"])
    else:
        keyEmployeeChange = ["null"]
    if propertyDict.has_key("layout_id"):
        layoutID = getLayoutID(propertyDict["layout_id"])
    else:
        layoutID = ["null"]
    if propertyDict.has_key("legal_name"):
        legalName = getLegalName(propertyDict["legal_name"])
    else:
        legalName = ["null"]
    if propertyDict.has_key("linkedin"):
        linkedin = getLinkedin(propertyDict["linkedin"])
    else:
        linkedin = ["null"]
    if propertyDict.has_key("listed_stock_symbol"):
        stockSym = getStockSym(propertyDict["listed_stock_symbol"])
    else:
        stockSym = ["null"]
    if propertyDict.has_key("location_group_identifiers"]):
        locationGroupID = getLocationGroupID(propertyDict["location_group_identifiers"])
    else:
        locationGroupID = ["null"]
    if propertyDict.has_key("location_identifiers"):
        locationID = getLocationID(propertyDict["location_identifiers"])
    else:
        locationID = ["null"]
    if propertyDict.has_key("name"):
        name = getName(propertyDict["name"])
    else:
        name = ["null"]
    if propertyDict.has_key("num_acquisitions"):
        acqNum = getAcqNum(propertyDict["num_acquisitions"])
    else:
        acqNum = ["null"]
    if propertyDict.has_key("num_alumni"):
        AlumniNum = getAlumniNum(propertyDict["num_alumni"])
    else:
        AlumniNum = ["null"]
    
    print(acquirerList, "\n", aliasList, "\n", categoryList)

def getAlias(data):
    aliases = json["entities"]["properties"]["aliases"]
    
    
