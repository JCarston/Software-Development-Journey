import requests
import datetime
import pytz
import tzlocal
import json
import re
teamlist=["085b1325-e4ed-439b-bd8f-ad38dd99a473 | Problem Management Team",
"186c3134-b1b0-484e-ac57-54327a3030c7 | Contact Center",
"1a0d038a-ac62-42c8-a759-261da6aa5ea1 | Vice Presidents Task Force",
"1ac9058b-8f33-4785-8e20-65d93819a433 | Quality Engineering",
"1c14191c-25e4-477b-93e0-c478d0d7192f | Platform Innovation",
"1d1a445d-d5fe-465d-bb40-3bdcfbd9cc84 | IO Integrations OnBase",
"2044f685-f40b-4dca-8d99-3aca117a03f6 | Registration",
"236cd609-35c3-4f32-aaae-001a968ab9ae | Service Desk Leadership",
"238537b4-66f0-471d-bd0d-917f3430f060 | Specialized Student Services Crisis Response",
"25b80f3f-be7d-4d71-8147-9e14e602195a | IT Service Delivery",
"25c1b80c-9b7e-43e8-a40f-736378e4144d | Ed Tech Training",
"2946ccf1-88bc-44bd-8dd9-61ce616247a1 | SEF Faculty Support",
"2d98b23f-5e72-4f79-8b5f-3e9b2342abe0 | CMLX",
"3216a276-d04f-4bb7-ab72-9f41e3d21e47 | Neo",
"32abe147-d056-42f4-b5f1-d76dae7d4166 | IO Network Operations",
"3358f189-4a79-4507-9d8d-2157a5c28fad | ServiceNow Development Testing",
"376dde19-d7f2-4ef1-b0a6-f680fcb033a0 | SJE - Field Experience",
"3d597caf-1051-4170-83ed-6484ba9d46f4 | Neo-Databricks",
"447edb0d-cecd-46c9-a49e-922975944534 | DAMS",
"4f13a6cd-e8d5-43c9-8440-958ae7a804aa | ServiceNow",
"500ef090-9900-4884-a02a-3156a44d3c24 | Auth and Access - Team MT",
"5070196f-e640-4d7a-aade-cd2f728d6f6d | QE-Test",
"50a2651f-d790-434c-8959-29a87f05ea3e | Enrollment",
"512b4fa2-7196-45de-a641-35fc5f940cb9 | SF Foundations",
"570fa090-f7aa-4d5a-a053-f356f72365a8 | Program Planning",
"5c8553de-ee9d-4312-b0ff-74da07a3024f | PDLA-LearningManagement",
"61faaaf8-6f04-40ad-8811-eb4d0e211f39 | AppSec",
"626abe66-5770-43b4-bf27-dd418365dee4 | Site Outage",
"62fc70f6-3655-4efa-b925-174a091a4da1 | IO DBA",
"65d0c590-501c-4d6e-805c-3ad6595b87a6 | IO Integrations Applications",
"65d48afa-8d32-454f-9dc1-72e95b04ece1 | IO Integrations - Self-Service Appointment Scheduling",
"6657eae7-6e9f-40eb-898b-39e4a26155c6 | Examity Integrations Team",
"6bbe9f2f-95dd-4128-8055-50bbdbc642b7 | Platform Team",
"6d838970-d860-4874-bc27-1e2377a7b1bd | NOC",
"7033fe59-06f6-4501-8f40-f441a7cc7e12 | Ed Tech Communication",
"79e94319-88fa-4633-bd54-21610f1c051e | DigitalX",
"7eb29fd9-4abc-4fd8-85f0-c1ede542512d | Auth and Access - Team 401",
"7f80cdf1-582c-47b7-9850-2f4f63e9d948 | Site Security",
"80eae948-f179-4057-afc6-8a88a359a4a7 | Platform Enablement",
"81a38ecf-4db8-4151-9f65-607ecb319233 | IO Portfolio",
"831ea752-882e-461d-ba31-f761bcab34c4 | DirectorsTeam",
"843a18d0-8b89-4274-99b2-0d53165cc3f6 | Assessment Integrations",
"85c57817-f8fc-4a5e-ae3c-cd899e26ce37 | PrincipalTeam",
"8cdd663a-5457-42ee-956f-f1c6d636464a | IO Collaboration",
"9238f668-fc61-469f-8ec9-bf3cb196d64a | AV Team",
"930459b1-4aed-4c31-8d63-12b996b9f7e5 | CMDB Administrators",
"946f404d-bacf-40fc-942f-2f2cc93e3fd4 | Business Systems - Salesforce Platform",
"959046cb-4e08-4d65-b6d1-545510530c1d | PDLA Assessments",
"990429b8-e083-42f2-b500-099e7fe08b46 | IR",
"993946c8-7cea-4866-bbd3-7100c660cba6 | SharedApps",
"a06b84ba-f195-4c4d-8afe-5e40756f6a28 | Jira",
"a1319ea0-53bd-4a22-9e51-8ea080b29ee8 | Mobile",
"a33dbdd4-827c-41ec-913e-5de0a741e108 | Curriculum Architecture",
"a47293da-03ad-4f18-b57f-c7925851db08 | Platform Pipelines",
"ac154cda-51e5-4aa2-b6ed-1ee39d081559 | FinancialServices",
"add46883-4189-4e70-9d6a-cdb1b708ee93 | COC-Admissions",
"b152bc34-8798-4a3b-8eee-00d32df518d5 | Marketing Team - EdTech",
"b993e398-3846-4900-bf74-67c945797626 | WGU-Labs Affiliates Team",
"bec9e4ba-fa58-4dac-ba0a-038a6daae921 | COC-SocialAndComms",
"c1984f30-922d-4091-ad7c-1a762442a33f | CCS",
"c844a794-5800-485d-948a-eed89cec8ef9 | CLR",
"cb1d673e-27c0-4ae6-817a-590eb73306c9 | Auth and Access - Team Apollo",
"cb2cd60a-43cc-4b9a-adfd-4facc33504fb | Marketing Business",
"cfc06595-93cd-4e21-8b27-a23a31843b34 | Borg - EMA",
"d41c0d16-8c4f-4621-b73e-19f8343840ee | Kernel",
"d80ab25e-b617-440a-bed8-efac8a7eabe6 | WGU Academy",
"de28636c-abd4-44db-9efe-e9656d8ed863 | Security Operation Center",
"e4f88711-0c78-46bc-bef8-cd99f9c7dac3 | Vendor Portfolio Management",
"e7c08669-937c-4fd8-91cc-fb4c21ff1c4d | IO Server",
"ed34453a-11ed-415f-8875-22736e38d861 | IO Server Testing",
"eea0ee09-19fa-497d-875f-0d1b0381a160 | Diamond",
"f0329f40-adcf-4571-b99e-c6fe92c70bac | App Support",
"f59e5f09-9c4a-43ab-9124-e303ea5c6724 | BannerCloudReadiness",
"f96f2e05-213d-4b8d-8dcc-88e14c39a2dc | Workday",
"fea89695-ccb2-4d12-9595-7748dba555c4 | SecOps"]
id_list = []
alert_detail_api_url = []   
dynatrace_event_data = {
    "Availability": [],
    "Error": [],
    "Miscellaneous": [],
    "NewRelic":[],
    "Slowdown": [],
    "Resource": []
}

def opsgenie_list_view():
    ''' 
    Opsgenie API call to gather alerts ID and store them in a list to be ran through the "opsgenie_alert_detail_api" function. 
    - API is limited to 100 requests.
    - Offsets option shifts the starting point.
    - More options: https://docs.opsgenie.com/docs/alert-api
    '''
    try:
        opsgenie = 'SOMETHINGWASHERE'
        get_Opsgenie_URL = 'https://api.opsgenie.com/v2/alerts?query=status%3Aclosed&limit=6&offset=0&sort=updatedAt&order=desc'
        getHeaders = {"Authorization": "GenieKey " + opsgenie, "Content-Type": "application/json"}
        getRequest = requests.get(get_Opsgenie_URL, headers=getHeaders)
        getRequest.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("An exception occured with the service_now_noce_creation function: {}".format(e)) 
    
    list_data = getRequest.json()
    for item in list_data["data"]:
        alertid = item['id']
        id_list.append(alertid)
        

def opsgenie_alert_detail_url_formatter(alert_id_list):
    ''' 
    Modifies the Opsgenie URL with the alert ID to find the specific alert.
    '''
    for alert_details in alert_id_list:
        alert_detail_url = (f'https://api.opsgenie.com/v2/alerts/{alert_details}?identifierType=id') 
        alert_detail_api_url.append(alert_detail_url)  

def opsgenie_alert_time_adjustment(alert_timestamp):
    ''' 
    Adjusts the alert date/time from UTC to the users local time.
    '''
    local_timezone = tzlocal.get_localzone()
    utc_time = datetime.datetime.strptime(alert_timestamp,'%Y-%m-%dT%H:%M:%S.%fZ')
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    local_time = str(local_time)[:-16]
    return(local_time)

def opsgenie_team_name(teamID):
    ''' 
    Search through the "teamlist" list for all Opsgenie team neams and their ID's. 
    - Excludes alerts from Crisis Support team. 
    '''
    for opsgenie_team_name in teamlist:
        if teamID == "":
            team_name = "Null"
            return team_name
        # This team needs to be excluded from the MHC
        if opsgenie_team_name.__contains__(teamID):
            team_name = str(opsgenie_team_name)[39:]
            if team_name.__contains__("Specialized Student Services Crisis Response"):
                team_name = "REMOVE THIS ALERT"
            return team_name
        else:
            pass

def opsgenie_alert_detail_api(alert_detail_url_list):
    ''' Function argument comes from "opsgenie_list_view". 
    - Makes an API call and parse on the required information.
    - Creates key attribute variables.
    - Parses API response by Opsgenie integration type.
    - Organizes data into 5 different key/values objects found in "dynatrace_event_data".
    '''
    for whole_alert_info in alert_detail_url_list:
        try:
            opsgenie = 'SOMETHINGWASHERE'
            whole_alert_headers = {"Authorization": "GenieKey " + opsgenie, "Content-Type": "application/json"}
            whole_alertRequest = requests.get(whole_alert_info, headers=whole_alert_headers)
            whole_alert_data = whole_alertRequest.json()
            whole_alertRequest.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("An exception occured with the service_now_noce_creation function: {}".format(e)) 
            
        alert_id = whole_alert_data['data']['id']
        alert_id_url = (f'https://westerngovernorsuniversity.app.opsgenie.com/alert/detail/{alert_id}/details') 
        message = whole_alert_data['data']["message"]
        createdAt = whole_alert_data['data']["createdAt"]
        priority = whole_alert_data['data']["priority"]
        ownerTeamId = whole_alert_data['data']["ownerTeamId"]
        description = whole_alert_data['data']['description']
        integration_used = whole_alert_data['data']["integration"]["type"]
        created_timestamp = opsgenie_alert_time_adjustment(createdAt)
        opsgenie_team = opsgenie_team_name(str(ownerTeamId))
        
        # Description adjustments /remove excess HTML / Format the response for easier understanding
        description_noHTML = re.sub('<.*?>', '', str(description))
        seperator = '<a target="_blank"'
        formatted_description = description_noHTML.split(seperator, 1)[0].replace("impacted infrastructure", "\n\nImpacted Infrastructure: \n - ").replace("Root cause", "\n\nRoot Cause: \n - ").replace("impacted application", "\n\nImpacted Application: \n - ").replace("impacted serviceWeb", "\n\nImpacted Service Web: \n - ").replace("Problem detected at:", "\n\nProblem Detected At: \n - ").replace("Problem P-", "Problem:\n - P-").replace("Open in Browser", "")
        # Strips the Dynatrace URL from the description
        description_urls = re.findall('"((http)s?://.*?)"', str(description))
        dynatrace_url = str(description_urls).split(",")[0].replace("[(", "").replace("'", "")
        if opsgenie_team != 'Null':
            try:
                if (integration_used == "Ruxit") and ("APPLICATION" in message) or ("Browser monitor" in message): 
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": opsgenie_team,"priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Availability'].append(availability_json_data)
                    
                elif opsgenie_team == "REMOVE THIS ALERT":
                    pass
                
                elif (integration_used == "NewRelicV2") or (integration_used == "NewRelic"):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": opsgenie_team,"priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['NewRelic'].append(availability_json_data)
                
                elif (integration_used == "Ruxit") and ("SERVICES" in message):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": opsgenie_team,"priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Slowdown'].append(availability_json_data)
                
                elif (integration_used == "Ruxit") and ("INFRASTRUCTURE" in message):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": opsgenie_team,"priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Resource'].append(availability_json_data)
                else:
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": opsgenie_team,"priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Miscellaneous'].append(availability_json_data)
            except BaseException as error:
                print("An exception offured: {}".format(error)) 
        else:
            try:
                if (integration_used == "Ruxit") and ("APPLICATION" in message) or ("Browser monitor" in message): 
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": "No Team Found","priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Availability'].append(availability_json_data)
                
                elif (integration_used == "NewRelicV2") or (integration_used == "NewRelic"):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": "No Team Found","priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['NewRelic'].append(availability_json_data)
                
                elif (integration_used == "Ruxit") and ("SERVICES" in message):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": "No Team Found","priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Slowdown'].append(availability_json_data)
                
                elif (integration_used == "Ruxit") and ("INFRASTRUCTURE" in message):
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": "No Team Found","priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Resource'].append(availability_json_data)
                else:
                    availability_json_data={"message": message,"alert_url": alert_id_url,"dynatrace_url": dynatrace_url,"description": formatted_description,"createdAt": created_timestamp,"ownerID": "No Team Found","priority": priority,"integration_used": integration_used}
                    dynatrace_event_data['Miscellaneous'].append(availability_json_data)
            except BaseException as error:
                print("An exception occured: {}".format(error)) 
    console_data_output = json.dumps(dynatrace_event_data, indent=4)
    print(console_data_output)
    
def service_now_noce_creation():
    """
    Sends over formatted "dynatrace_event_data" into ServiceNow to be injected into a NOCE. 
    - Append newly created NOCE to the ServiceNow API URL.
    - Makes API call to ServiceNow. Documentation "Rest Explorer" API: "https://docs.servicenow.com/bundle/vancouver-api-reference/page/integrate/inbound-rest/concept/use-REST-API-Explorer.html"
    - Injects "dynatrace_event_data" into the API body.
    """
    try:
        validbody = json.dumps(dynatrace_event_data)
        servicenow_url = 'https://wgu.service-now.com/api/wegu/noc_morning_health_check/createAlerts/NOCE0003981'
        headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }
        response = requests.post(servicenow_url, auth=("SOMETHINGWASHERE", "SOMETHINGWASHERE"), headers=headers, data=validbody )
        print(response.json())
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("An exception occured with the service_now_noce_creation function: {}".format(e)) 

opsgenie_list_view()
opsgenie_alert_detail_url_formatter(id_list)
opsgenie_alert_detail_api(alert_detail_api_url)
service_now_noce_creation()
