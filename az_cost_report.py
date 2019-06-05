import os
import json
json_string = os.popen('az account management-group list').read()
datastore = json.loads(json_string)
print(datastore)