import json
import requests
from prettytable import PrettyTable
api_url="http://localhost:58000/api/v1/host"
headers={"X-Auth-Token":"NC-156-631605b311d84697a9b6-nbi"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()
hosts = response_json["response"]

table=PrettyTable(["HOSTNAME","HOST IP","HOST MAC", "CONNECTED INTERFACENAME"])


for host in hosts:
    table.add_row([host["hostName"],host["hostIp"],host["hostMac"],host["connectedInterfaceName"]])

print(table)

