import json
import datetime

data = {
    "NOCE_Details": [
        {
            "NOCE Number": "Something was here",
            "Created By": "Something was here",
            "Date of Event": "Something was here",
            "Short Description": "Something was here",
            "Notify Major Incident": "Something was here",
            "Notify Service Desk": "Something was here",
            "MTTD/I": "Something was here",
        },
        {
            "NOCE Number": "Something was here",
            "Created By": "Something was here",
            "Date of Event": "Something was here",
            "Short Description": "Something was here",
            "Notify Major Incident": "Something was here",
            "Notify Service Desk": "Something was here",
            "MTTD/I": "Something was here",
        },
        {
            "NOCE Number": "Something was here",
            "Created By": "Something was here",
            "Date of Event": "Something was here",
            "Short Description": "Something was here",
            "Notify Major Incident": "Something was here",
            "Notify Service Desk": "Something was here",
            "MTTD/I": "Something was here",
        },
        {
            "NOCE Number": "Something was here",
            "Created By": "Something was here",
            "Date of Event": "Something was here",
            "Short Description": "Something was here",
            "Notify Major Incident": "Something was here",
            "Notify Service Desk": "Something was here",
            "MTTD/I": "Something was here",
        },
        {
            "NOCE Number": "Something was here",
            "Created By": "Something was here",
            "Date of Event": "Something was here",
            "Short Description": "Something was here",
            "Notify Major Incident": "Something was here",
            "Notify Service Desk": "Something was here",
            "MTTD/I": "Something was here",
        }
    ],
    "MTTD_I": [
        "{'NOCE Number': 'Something was here', 'Created By': 'Something was here', 'MTTD/I': '0:14:11'}",
        "{'NOCE Number': 'Something was here', 'Created By': 'Something was here', 'MTTD/I': '0:04:00'}",
        "{'NOCE Number': 'Something was here', 'Created By': 'Something was here', 'MTTD/I': '0:01:00'}",
        "{'NOCE Number': 'Something was here', 'Created By': 'Something was here', 'MTTD/I': '0:14:00'}",
        "{'NOCE Number': 'Something was here', 'Created By': 'Something was here', 'MTTD/I': '0:09:00'}"
    ]
}

data = json.dumps(data) #Forces dictionary into String
loaded_data = json.loads(data) #Forces string into dictionary
print(type(loaded_data))
# with open("noce_api.json") as f:
#     data = json.load(f)


date_list = []

for i in loaded_data['MTTD_I']:
    something = i.split("'MTTD/I':", 1) [-1]
    something = something.split("}", 1)[0]
    something = something.replace("'", "")
    something = something.replace(" ", "0")
    something = something[:-3][-2:]
    date_list.append(int(something))    
print(date_list)
total = sum(date_list)
final = total / len(date_list)
print(total)
print(final)