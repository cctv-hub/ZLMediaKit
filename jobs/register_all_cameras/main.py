import requests
import json
import sys
import yaml

HOST = sys.argv[1]
with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

# Get the list of cameras
response = requests.post(
    f'{cfg["zlm-cms"]["host"]}/v1/camera/getCamera',
    data=json.dumps(
        {
            "groupId": "p411",
            "cameraName": "cam4-zoneA"
        }
    ),
    timeout=5
)