# coding: utf-8
import datetime # import datetime # $ pip install DateTime
from datetime import timedelta
import json # Built in module
import requests# $ pip install requests
import pytz    # $ pip install pytz
import tzlocal # $ pip install tzlocal
import time # $ pip install time
# JSON that will be passed to Service Now
nrjsondata = {
    "APM": [
    ],
    "Synthetic": [
    ],
    "Miscellaneous": [
    ],
    "Infrastructure": [
    ]
}
# Empty aray for alerts to be formatted into a list 
alertidlist =[]
# New Relic Location for synthetics
locationspart1 = [
    "Portland, OR, USA: AWS_US_WEST_2",
    "Washington, DC, USA: AWS_US_EAST_1",
    "Columbus, OH, USA: AWS_US_EAST_2",
    "San Francisco, CA, USA: AWS_US_WEST_1",
    "WGU Internal Minions: 1876829-wgu_internal_minions-E22",
    "aws_ops_oregon: 1876829-aws_ops_oregon-4D1"]
# Master list of all Opsgenie team IDs 
teamlist=["085b1325-e4ed-439b-bd8f-ad38dd99a473 | Problem Management Team",
        "186c3134-b1b0-484e-ac57-54327a3030c7 | Contact Center",
        "1a0d038a-ac62-42c8-a759-261da6aa5ea1 | Vice Presidents Task Force",
        "1ac9058b-8f33-4785-8e20-65d93819a433 | Quality Engineering",
        "1d1a445d-d5fe-465d-bb40-3bdcfbd9cc84 | IO Integrations OnBase",
        "2044f685-f40b-4dca-8d99-3aca117a03f6 | Registration",
        "236cd609-35c3-4f32-aaae-001a968ab9ae | Service Desk Leadership",
        "238537b4-66f0-471d-bd0d-917f3430f060 | Assessment Support Crisis Response",
        "25b80f3f-be7d-4d71-8147-9e14e602195a | IT Service Delivery",
        "25c1b80c-9b7e-43e8-a40f-736378e4144d | Ed Tech Training",
        "2946ccf1-88bc-44bd-8dd9-61ce616247a1 | SEF Faculty Support",
        "2d98b23f-5e72-4f79-8b5f-3e9b2342abe0 | CLD - Legacy",
        "3216a276-d04f-4bb7-ab72-9f41e3d21e47 | Neo",
        "32abe147-d056-42f4-b5f1-d76dae7d4166 | IO Network Operations",
        "3358f189-4a79-4507-9d8d-2157a5c28fad | ServiceNow Development Testing",
        "3d597caf-1051-4170-83ed-6484ba9d46f4 | Neo-Databricks",
        "447edb0d-cecd-46c9-a49e-922975944534 | DAMS",
        "4f13a6cd-e8d5-43c9-8440-958ae7a804aa | ServiceNow",
        "50a2651f-d790-434c-8959-29a87f05ea3e | Enrollment",
        "512b4fa2-7196-45de-a641-35fc5f940cb9 | SEF Foundations",
        "570fa090-f7aa-4d5a-a053-f356f72365a8 | Program Planning",
        "5c8553de-ee9d-4312-b0ff-74da07a3024f | PDLA-LearningManagement",
        "60dc2301-e638-4d15-ae30-4a13c166ac1a | SRE",
        "619a8bf2-5bb9-4b65-a835-48e8f743ebe7 | Joel Test Team",
        "61faaaf8-6f04-40ad-8811-eb4d0e211f39 | AppSec",
        "626abe66-5770-43b4-bf27-dd418365dee4 | Site Outage",
        "62fc70f6-3655-4efa-b925-174a091a4da1 | IO DBA",
        "65d0c590-501c-4d6e-805c-3ad6595b87a6 | IO Integrations Applications",
        "65d48afa-8d32-454f-9dc1-72e95b04ece1 | IO Integrations - Self-Service Appointment Scheduling",
        "6657eae7-6e9f-40eb-898b-39e4a26155c6 | Examity Integrations Team",
        "6bbe9f2f-95dd-4128-8055-50bbdbc642b7 | Platform Team",
        "6d838970-d860-4874-bc27-1e2377a7b1bd | NOC",
        "79e94319-88fa-4633-bd54-21610f1c051e | DigitalX",
        "7eb29fd9-4abc-4fd8-85f0-c1ede542512d | Auth and Access - Team 401",
        "81a38ecf-4db8-4151-9f65-607ecb319233 | Director - Infrastructure",
        "831ea752-882e-461d-ba31-f761bcab34c4 | DirectorsTeam",
        "843a18d0-8b89-4274-99b2-0d53165cc3f6 | Assessment Integrations",
        "85c57817-f8fc-4a5e-ae3c-cd899e26ce37 | PrincipalTeam",
        "8cdd663a-5457-42ee-956f-f1c6d636464a | IO Collaboration",
        "9238f668-fc61-469f-8ec9-bf3cb196d64a | AV Team",
        "947472c4-e659-4a64-9050-0f28df5fe944 | OverwatchTestTeam",
        "959046cb-4e08-4d65-b6d1-545510530c1d | Product Blueprint Assessment",
        "990429b8-e083-42f2-b500-099e7fe08b46 | IR",
        "993946c8-7cea-4866-bbd3-7100c660cba6 | ShareApps",
        "a06b84ba-f195-4c4d-8afe-5e40756f6a28 | Jira",
        "a1319ea0-53bd-4a22-9e51-8ea080b29ee8 | Mobile",
        "a78b8653-9ebe-4458-a4b3-c0f4014c9835 | COC-Finance-NGP",
        "ac154cda-51e5-4aa2-b6ed-1ee39d081559 | Finance-Team FIrefly",
        "add46883-4189-4e70-9d6a-cdb1b708ee93 | COC-Admissions",
        "b152bc34-8798-4a3b-8eee-00d32df518d5 | Marketing",
        "bec9e4ba-fa58-4dac-ba0a-038a6daae921 | COC-SocialAndComms",
        "c1984f30-922d-4091-ad7c-1a762442a33f | CCS",
        "c844a794-5800-485d-948a-eed89cec8ef9 | CLR",
        "cb1d673e-27c0-4ae6-817a-590eb73306c9 | Auth and Access - Team Apollo",
        "cb2cd60a-43cc-4b9a-adfd-4facc33504fb | Marketing Business",
        "cfc06595-93cd-4e21-8b27-a23a31843b34 | Borg - EMA",
        "d41c0d16-8c4f-4621-b73e-19f8343840ee | Kernel",
        "e4f88711-0c78-46bc-bef8-cd99f9c7dac3 | Vendor Portfolio Management",
        "e7c08669-937c-4fd8-91cc-fb4c21ff1c4d | IO Server",
        "eea0ee09-19fa-497d-875f-0d1b0381a160 | Diamond",
        "f0329f40-adcf-4571-b99e-c6fe92c70bac | App Support",
        "f59e5f09-9c4a-43ab-9124-e303ea5c6724 | SIS - Banner",
        "f96f2e05-213d-4b8d-8dcc-88e14c39a2dc | Workday",
        "fea89695-ccb2-4d12-9595-7748dba555c4 | SecOps"]
def opsgenielistview():
    # Opsgenie API Token for HTTPS request
    opsgenie = 'SOMETHINGWASHERE'
    # URL that contains the syntax of the qurey
    postURL = ' https://api.opsgenie.com/v2/alerts?query=status%3Aclosed&limit=7&sort=updatedAt&order=desc'
    # API authorization
    postHeaders = {"Authorization": "GenieKey " + opsgenie, "Content-Type": "application/json"}
    postRequest = requests.get(postURL, headers=postHeaders)
    data = json.loads(postRequest.text)
    # Searches JSON response on and parse out the data via a for loop
    for item in data['data']:
        # Gather specific sections
        alertid = item['id']
        # Appened the ID reults into the empty array
        alertidlist.append(alertid)
opsgenielistview()
def alertcycle(list):
    url = "https://api.newrelic.com/graphql"
    NewRelic_APIKey = 'SOMETHINGWASHERE'
    headers = {
                'x-api-key': NewRelic_APIKey,
                'Content-Type': 'text/plain'
                }
    local_timezone = tzlocal.get_localzone() # get pytz tzinfo
    for x in list:
        time.sleep(2)
        # Make API call to Opsgenie for each alert in alertidlist
        opsgenie = 'SOMETHINGWASHERE'
        alertINFOURL = 'https://api.opsgenie.com/v2/alerts/'+x+'?identifierType=id'
        alertINFOHeaders = {"Authorization": "GenieKey " + opsgenie, "Content-Type": "application/json"}
        alertINFORequest = requests.get(alertINFOURL, headers=alertINFOHeaders)
        alertINFOdata = alertINFORequest.json()
        # Key Variables/Items pulled from the Opsgenie alert itself
        alertMessage = alertINFOdata['data']["message"]
        alertCreatedAt = alertINFOdata['data']["createdAt"]
        alertTeam = alertINFOdata['data']["ownerTeamId"]
        alertPriority = alertINFOdata['data']["priority"]
        alertID = alertINFOdata['data']["id"]
        alertDescription = alertINFOdata['data']["description"]
        alertIntegration = alertINFOdata['data']["integration"]['type']
        # Formats the alert create date 
        utc_time = datetime.datetime.strptime(alertCreatedAt,'%Y-%m-%dT%H:%M:%S.%fZ')
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
        # Removes the milliseconds from the local time and forces the local_time to string.
        newLocal_time = str(local_time)[:-16]
        alertMessageString = str(alertMessage)
        # Gather/format alert failure window (failure of alert and 30 mins after) / Local_time is the alert failure time
        time_change = timedelta(minutes=30)
        failurewindow = local_time + time_change
        failurewindow30min = str(failurewindow)[:-13]
        # Checks the description of the alert for lower enviroment key words 
        keywordExcemptList = ['Stage','stage','QA','qa','Qa']
        if any(x in alertMessageString for x in keywordExcemptList):
            print('This alert is not a production alert')
        else:
            pass
        # Checks for a New Relic integration
        if alertIntegration != "NewRelicV2":
            print("New Relic Integration was not used")
            print('https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details')
            print (alertMessage +" | "+ newLocal_time)
            miscellaneousteam = ""
            if alertTeam == "":
                print('No alert ID')
            else:
                # Opsgenie Team Assignment
                for e in teamlist:
                    if e not in teamlist:
                        print('No team')
                    else:
                        pass
                    if e.startswith(alertTeam): 
                        miscellaneousteam += str(e)[39:]
                        print(miscellaneousteam +" | "+ alertPriority)
            miscellaneous = {
            "message": alertMessage,
            "createdAt": newLocal_time,
            "ownerID": miscellaneousteam,
            "priority": alertPriority,
            "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details'
            }
            nrjsondata["Miscellaneous"].append(miscellaneous)
        else:
            print (alertMessage +" | "+ newLocal_time)
            print('https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details')
            try:
                alertTargetLink = alertDescription.split("Target Link")[1]
                alertTargetURL = alertTargetLink.split("\n")[0]
                finalTargetURL = alertTargetURL[2:]
                alertTargetLinkstring = str(alertTargetLink)[3:]
                print (alertTargetLinkstring)
            except IndexError:
                alertTargetLink = 'null'
        # Checks for Target Type of Infrastructure from the Opsgenie alert
        infrastructureKeyword = ['Target Type : Host']
        if any(x in alertDescription for x in infrastructureKeyword):
            alertProductType = alertDescription.split("Target Type") [1]
            alertProductTypeResult = alertProductType.split(': ') [1]
            print (alertProductTypeResult)
            # Checks Opsgenie description to pull the hostname
            hostnameKeyword = ["fullHostname"] 
            if any (x in alertDescription for x in hostnameKeyword):
                alertHostname = alertDescription.split("fullHostname") [1]
                alertHostnameResult = alertHostname.split(',') [0]
                alertHostnametring = str(alertHostnameResult)[1:]
                print (alertHostnametring)
                print (newLocal_time +" | "+failurewindow30min)
                # Takes Infrastructure information and passes it into NRQL | NRQL window is 40 minutes
                infra_utc_time = datetime.datetime.strptime(alertCreatedAt,'%Y-%m-%dT%H:%M:%S.%fZ')
                infra_time_afterwindow = datetime.timedelta(minutes=30)
                infra_time_afterdifference = infra_utc_time + infra_time_afterwindow
                infra_time_beforewindow = datetime.timedelta(minutes=-10)
                infra_time_beforedifference = infra_utc_time + infra_time_beforewindow
                infrapayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"from SystemSample select average(memoryUsedBytes)/average(memoryTotalBytes)*100 as 'Memory Usage (%)', average(cpuPercent) as 'CPU (%)', average(diskUsedPercent) as 'Disk Usage (%)', average(loadAverageFiveMinute) as 'LAFM' where fullHostname = '"+alertHostnametring+"' since '"+str(infra_time_beforedifference)+"' UNTIL '"+str(infra_time_afterdifference)+"'\") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
                infrarequest = requests.get(url, headers=headers, data=infrapayload)
                infrarequestJSON = infrarequest.json()
                # Validate the API response then continues to parse JSON
                if infrarequest.status_code != 200:
                    print(infrarequest.status_code)
                else:
                    try:
                        nrErrorResult = infrarequestJSON['data']['actor']['account']['nrql']['results']
                        for item in nrErrorResult:
                            nrCPU = item.get('CPU (%)',0)
                            print(nrCPU)
                            nrDiskUsage = item.get('Disk Usage (%)',0)
                            nrMemUsage = item.get('Memory Usage (%)',0)
                            nrLAFM = item.get('LAFM',0)
                            print('CPU: '+ str(nrCPU)[:-12] + '%\nDisk Usage: ' +str(nrDiskUsage)[:-12]+ '%\nMemory Usage: ' +str(nrMemUsage)[:-12]+'%')
                    except TypeError:
                        nrDiskUsage = "0"
                        nrMemUsage = "0"
                        nrLAFM = "0"
                        nrCPU = "0"
                infrateam = ""
                if alertTeam == "":
                    print('No alert ID')
                else:
                    # Opsgenie Team Assignment
                    for e in teamlist:
                        if e not in teamlist:
                            print('No team')
                        if e.startswith(alertTeam):
                            infrateam = str(e)[39:]
                            print(infrateam +" | "+ alertPriority)
                            print("----------")
                            print("----------")
                infrabody = {
                "message": alertMessage,
                "createdAt": newLocal_time,
                "ownerID": infrateam,
                "priority": alertPriority,
                "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                "description": finalTargetURL,
                "InfraCPU": nrCPU,
                "InfraDiskUsage": nrDiskUsage,
                "InfraMemUsage": nrMemUsage,
                "InfraLoadAverageFiveMinutes": nrLAFM
                }
                nrjsondata["Infrastructure"].append(infrabody)
            else:
                # global miscinfrateam
                miscinfrateam = ""
                if alertTeam == "":
                    print('No alert ID')
                else:
                    # Opsgenie Team Assignment
                    for e in teamlist:
                        if e not in teamlist:
                            print('No team')
                        else:
                            pass
                        if e.startswith(alertTeam): 
                            miscinfrateam += str(e)[39:]
                            print(miscinfrateam +" | "+ alertPriority)
                            print("----------")
                            print("----------")
                miscellaneous = {
                "message": alertMessage,
                "createdAt": newLocal_time,
                "ownerID": miscinfrateam,
                "priority": alertPriority,
                "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                "description": finalTargetURL
                }
                nrjsondata["Miscellaneous"].append(miscellaneous)
        else:
            pass
        # Checks for Target Type of Query from the Opsgenie alert
        infrastructureKeyword = ['Target Type : Query']
        if any(x in alertDescription for x in infrastructureKeyword):
            quereyTeam = ""
            # Opsgenie Team Assignment
            for e in teamlist:
                if e not in teamlist:
                    print('No team')
                else:
                    pass
                if e.startswith(alertTeam): 
                    quereyTeam += str(e)[39:]
                    print(quereyTeam +" | "+ alertPriority)
                    print("----------")
                    print("----------")
            miscellaneous = {
            "message": alertMessage,
            "createdAt": newLocal_time,
            "ownerID": quereyTeam,
            "priority": alertPriority,
            "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
            "description": finalTargetURL
            }
            nrjsondata["Miscellaneous"].append(miscellaneous)
        else:
            pass
            # Checks for Target Type of Synthetics from the Opsgenie alert
        syntheticKeyword = ['Target Product : SYNTHETICS']
        if any(x in alertDescription for x in syntheticKeyword):
            # Key Synthetic Variables pulled from the Opsgenie alert itself
            alertsyntheticName = alertDescription.split("Target Name") [1]
            syntheticName = alertsyntheticName.split(": ") [1]
            syntheticNamesplit = syntheticName.replace('\nTarget Type ', "")
            print(syntheticNamesplit)
            synth_utc_time = datetime.datetime.strptime(alertCreatedAt,'%Y-%m-%dT%H:%M:%S.%fZ').replace(microsecond=0)
            synth_time_afterwindow = datetime.timedelta(minutes=5)
            synth_time_afterdifference = synth_utc_time + synth_time_afterwindow
            synth_time_beforewindow = datetime.timedelta(minutes=-10)
            synth_time_beforedifference = synth_utc_time + synth_time_beforewindow
            keywordExcemptList = ['Stage','stage','QA','qa','Qa']
            if any(x in alertMessageString for x in keywordExcemptList):
                print("None Production synthetic")      
            else:
                # Formatted the alert message to grab the monitor location
                keywordLocationExcemption = 'or more '
                if keywordLocationExcemption in alertMessageString:
                    miscellaneousteam = ""
                    synthpayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"From SyntheticCheck Select error where monitorName = '"+syntheticNamesplit+"'  and error  LIKE '%%' and result = 'FAILED' since '"+str(synth_time_beforedifference)+"' UNTIL '"+str(synth_time_afterdifference)+"'\") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
                    multi_requestFacet = requests.get(url, headers=headers, data=synthpayload)
                    multi_facetJSON = multi_requestFacet.json()
                    if multi_requestFacet.status_code != 200:
                        print(multi_requestFacet.status_code)
                    else:
                        try:
                            multi_facetJSONResult = multi_facetJSON['data']['actor']['account']['nrql']['results']
                            for x in multi_facetJSONResult:
                                json.dumps(multi_facetJSON, indent=4)
                                multi_nrfacetResult = x.get('error')
                                # Parses information to show the failure of the synthetic
                        except TypeError:
                           multi_nrfacetResult = "Null"
                    # Opsgenie Team Assignment
                    if alertTeam == "":
                        print('No alert ID')
                    else:
                        for e in teamlist:
                            if e not in teamlist:
                                print('No team')
                            else:
                                pass
                            if e.startswith(alertTeam): 
                                miscellaneousteam += str(e)[39:]
                                print(miscellaneousteam +" | "+ alertPriority)
                                print("----------")
                                print("----------")
                    synthbody = {
                    "message": alertMessage,
                    "createdAt": newLocal_time,
                    "ownerID": synthteam,
                    "priority": alertPriority,
                    "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                    "description": finalTargetURL,
                    "synthlocation": "",
                    "syntherror": multi_nrfacetResult
                    }
                    nrjsondata["Miscellaneous"].append(miscellaneous)
                else:
                    firstmessagesplit = alertMessageString.split("[New Relic] Monitor failed for location ")[1]
                    finalmessagesplit = firstmessagesplit.split(" on")[0]
                    # Comparing synthetic location to list and just NRQL to that specific location
                    for x in locationspart1:
                        if finalmessagesplit in x:
                            # This variable needs to be global for it to be used in NRQL on line 220
                            # global locationformatted
                            # global locationformattedName
                            locationformatted = x.split(": ")[1]
                            locationformattedName = x.split(": ")[0]
                        else:
                            pass
                    # Once the location is formatted then the NRQL is update to make the API call to New Relic
                    synthpayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"From SyntheticCheck Select uniqueCount(location) where monitorName = '"+syntheticNamesplit+"' and error LIKE '%%' and result = 'FAILED' and location ='"+locationformatted+"' FACET location, error SINCE '"+str(synth_time_beforedifference)+"' UNTIL '"+str(synth_time_afterdifference)+"'\") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
                    requestFacet = requests.get(url, headers=headers, data=synthpayload)
                    facetJSON = requestFacet.json()
                    nrErrorFacet = ""
                    if requestFacet.status_code != 200:
                        print(requestFacet.status_code)
                    else:
                        try:
                            facetJSONResult = facetJSON['data']['actor']['account']['nrql']['results']
                            for x in facetJSONResult:
                                # facet = x.get('facet')
                                nrfacetResult = x.get('facet')
                                nrErrorFacet = str(nrfacetResult).replace(locationformatted,"",1).replace(''''',''','',1).replace('[',"",1).replace(']',"",1)
                                # Parses information to show the failure of the synthetic
                                print(nrErrorFacet)
                        except TypeError:
                           nrErrorFacet = "Null"
                    synthteam = ""
                    if alertTeam == "":
                        print('No alert ID')
                    else:
                        for e in teamlist:
                            if e not in teamlist:
                                print('No team')
                            if e.startswith(alertTeam):
                                synthteam = str(e)[39:]
                                print(synthteam +" | "+ alertPriority)
                                print("----------")
                                print("----------")
                    # Synthetic JSON format that will be sent to ServiceNow
                    synthbody = {
                    "message": alertMessage,
                    "createdAt": newLocal_time,
                    "ownerID": synthteam,
                    "priority": alertPriority,
                    "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                    "description": finalTargetURL,
                    "synthlocation": locationformattedName,
                    "syntherror": nrErrorFacet
                    }
                    nrjsondata["Synthetic"].append(synthbody)                
        else:
            pass
        # This is used for text message comparison to make sure Examity WGU messages are not processed 
        keywordExcemptListAPM = ['Examity']
        # Checks to make sure that Opsgenie alert is an APM
        apmKeyword = ['Target Type : Application']
        if any(x in alertDescription for x in apmKeyword):
            # Key APM Variables pulled from the Opsgenie alert itself
            apmTargetName = alertDescription.split("Target Name") [1]
            apmTargetNameresult = apmTargetName.split(": ") [1]
            apmNamesplit = apmTargetNameresult.replace('\nTarget Type ', "")
            apm_utc_time = datetime.datetime.strptime(alertCreatedAt,'%Y-%m-%dT%H:%M:%S.%fZ')
            apm_time_afterwindow = datetime.timedelta(minutes=10)
            apm_time_afterdifference = apm_utc_time + apm_time_afterwindow
            apm_time_beforewindow = datetime.timedelta(minutes=-30)
            apm_time_beforedifference = apm_utc_time + apm_time_beforewindow
            # API call to gather APM Webtransaction information and adjusts the time range of the NRQL 
            webtransactionPayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"SELECT average(apm.service.overview.web) * 1000 FROM Metric WHERE (appName = '"+apmNamesplit+"') FACET `segmentName` SINCE '"+str(apm_time_beforedifference)+"' UNTIL '"+str(apm_time_afterdifference)+"'\") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
            webtransactionRequest = requests.get(url, headers=headers, data=webtransactionPayload)
            webtransactionRequestJSON = webtransactionRequest.json()
            overviewAverageRounded = ""
            if 'result' not in webtransactionRequestJSON:
                print ("No JSON data")
            else:
                # Checks the excemption list for the Examity WGU | Webtransaction
                if any(x in alertMessageString for x in keywordExcemptListAPM):
                    pass
                else:
                    try:
                        for item in webtransactionRequestJSON['data']['actor']['account']['nrql']['results']:
                            facet = item.get('facet')
                            overviewAverage = item.get ('average.apm.service.overview.web*1.0e3')
                            overviewAverageRounded = str(round(overviewAverage, 2))
                            print(str(facet), overviewAverageRounded +" ms")
                    except TypeError:
                        overviewAverageRounded = "0"
            # API call to gather APM Throughput information and adjusts the time range of the NRQL 
            # Throughput (Requests per minute)
            throughputPayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"SELECT rate(count(apm.service.transaction.duration), 1 minute) as 'Web throughput' FROM Metric WHERE (appName = '"+apmNamesplit+"') AND (transactionType = 'Web') SINCE '"+str(apm_time_beforedifference)+"' UNTIL '"+str(apm_time_afterdifference)+"'\") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
            throughputRequest = requests.get(url, headers=headers, data=throughputPayload)
            throughputRequestJSON = throughputRequest.json()
            if 'result' not in throughputRequestJSON:
                print ("No JSON data")
            else:
                # Checks the excemption list for the Examity WGU | Throughput
                apmThroughputRounded =""
                if any(x in alertMessageString for x in keywordExcemptListAPM):
                    pass
                else:
                    try:
                        for item in throughputRequestJSON['data']['actor']['account']['nrql']['results']:
                            apmThroughput = item.get('Web throughput')
                            apmThroughputRounded = str(round(apmThroughput, 2))
                            print(apmThroughputRounded + " rpm")
                    except TypeError:
                        apmThroughputRounded = '0'
            # API call to gather APM Error Rate/Percent information and adjusts the time range of the NRQL 
            errorRatePayload = "{\r\n  actor {\r\n    account(id: 1876829) {\r\n      name\r\n      nrql(query: \"SELECT filter((count(apm.service.error.count) / count(apm.service.transaction.duration)), where transactionType = 'Web') as 'Web errors', count(apm.service.error.count) / count(apm.service.transaction.duration) AS 'All errors' FROM Metric WHERE (appName = '"+apmNamesplit+"') since '"+str(apm_time_beforedifference)+"' UNTIL '"+str(apm_time_afterdifference)+"' \") {\r\n        results\r\n      }\r\n    }\r\n  }\r\n}"
            errorRateRequest = requests.get(url, headers=headers, data=errorRatePayload)
            errorRateRequestJSON = errorRateRequest.json()
            if 'result' not in errorRateRequestJSON:
                    print ("No JSON data")
            else:
                # Checks the excemption list for the Examity WGU  | Errors
                apmAllErrors = ""
                apmWebErrors = ""
                if any(x in alertMessageString for x in keywordExcemptListAPM):
                    pass
                else:
                    try:
                        for item in errorRateRequestJSON['data']['actor']['account']['nrql']['results']:
                            apmAllErrors = item.get('All errors')
                            apmWebErrors = item.get('Web errors')
                            print(str(apmAllErrors) + " %\n" + str(apmWebErrors) + " %") 
                    except TypeError:
                        apmWebErrors = '0'
                        apmAllErrors = '0'
            # Opsgenie Team Assignment
            apmteam = ""
            if alertTeam == "":
                    print('No alert ID')
            else:
                for e in teamlist:
                    if e not in teamlist:
                        print('No team')
                    if e.startswith(alertTeam):
                        apmteam = str(e)[39:]
                        print(apmteam +" | "+ alertPriority)
                        print("----------")
                        print("----------")
            # JSON Validation, confirming that all JSON's are formatted correct.
            if 'result' not in (webtransactionRequestJSON,errorRateRequestJSON,throughputRequestJSON, webtransactionRequestJSON):
                apmbody = {
                "message": alertMessage,
                "createdAt": newLocal_time,
                "ownerID": apmteam,
                "priority": alertPriority,
                "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                "description": finalTargetURL
                }
                nrjsondata["APM"].append(apmbody)
            else:  
                apmbody = {
                "message": alertMessage,
                "createdAt": newLocal_time,
                "ownerID": apmteam,
                "priority": alertPriority,
                "id": 'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/'+alertID+'/details',
                "description": finalTargetURL,
                "apmAllErrors": apmAllErrors,
                "apmWebErrors": apmWebErrors,
                "apmThroughput": apmThroughputRounded,
                "webTransactionOverview": overviewAverageRounded
                }
                nrjsondata["APM"].append(apmbody)
        else:
            pass
alertcycle(alertidlist)
# Display the JSON before passing it to ServiceNow
validbody = json.dumps(nrjsondata, indent=4)
print(validbody)
# ServiceNow API call and passing New Relic JSON data
url = 'https://wgu.service-now.com/api/wegu/noc_morning_health_check/createAlerts/NOCE0002044'
headers = {
'Content-Type': "application/json",
'cache-control': "no-cache"
}
response = requests.post(url, auth=("noc.alerts", "SOMETHINGWASHERE"), headers=headers, data=validbody )
print(response.json())
