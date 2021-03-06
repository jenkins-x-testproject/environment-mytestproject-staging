import requests
import sys
import time
import json


projectId = "ZUcmXXXXXXEa2UgtQ"
jobId = "uSh9YXXXXXXX0NrBQ"
apiKey = "OeyCmOn4XXXXXXXXXPq1lhvIijNS81"
agentId = "ZEBXXXXXXXXb5s8xTgVeg"
apiUrl = "https://api.testproject.io/"
url = apiUrl + 'v2/projects/' + projectId + '/jobs/' + jobId + '/run'

headers = {
    "accept": "application/json",
    "Authorization": apiKey,
    "Content-Type": "application/json; charset=utf-8"
}
body = {
    "agentId": agentId,
    "browsers": [
        "Chrome"
    ],
    "queue": True
}

print("Before execution", url)
executionId = requests.post(url, json=body, headers=headers).json()["id"]


url = apiUrl + 'v2/projects/' + projectId + '/jobs/' + jobId + '/executions/'+ executionId + '/state'

headers = {
    "accept": "application/json",
    "Authorization": apiKey,
}

print("Execution States", url)
executionState = requests.get(url, headers=headers).json()["state"]

count = 0
while count < 10:
    executionState = requests.get(url, headers=headers).json()["state"]
    print(executionState)
    if executionState == 'Passed':
        exit(1)
    time.sleep(2)
    count += 1
exit(0)
