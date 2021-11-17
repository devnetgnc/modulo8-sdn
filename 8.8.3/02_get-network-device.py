import json
import requests
from prettytable import PrettyTable
api_url="http://localhost:58000/api/v1/network-device"
headers={"X-Auth-Token":"NC-156-631605b311d84697a9b6-nbi"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()
networkDevices = response_json["response"]

table=PrettyTable(["HOSTNAME","PLATFORMID","MANAGEMENT IP ADD"])


for networkDecice in networkDevices:
    table.add_row([networkDecice["hostname"],networkDecice["platformId"],networkDecice["managementIpAddress"]])
print(table)

