import os
import subprocess
import json
from influxdb_client import Point

def fetch_remo():
    mock_mode = os.getenv('MOCK_MODE', default='')

    if mock_mode == "mock":
        print("USE mock")
        SHELL_PATH = '/app/scripts/mock_getDevices.sh'
    else:
        SHELL_PATH = '/app/scripts/getDevices.sh'
    REMO_TOKEN = os.environ['REMO_TOKEN']
    resultValue = subprocess.run([SHELL_PATH, REMO_TOKEN], capture_output=True, text=True)
    res_json = json.loads(resultValue.stdout)
    return res_json["newest_events"]

def remo_main():
    remoValues = fetch_remo()
    p1 = Point("measurement").tag("source", "remo").field("hu", remoValues["hu"]["val"])
    p2 = Point("measurement").tag("source", "remo").field("il", remoValues["il"]["val"])
    p3 = Point("measurement").tag("source", "remo").field("mo", remoValues["mo"]["val"])
    p4 = Point("measurement").tag("source", "remo").field("te", float(remoValues["te"]["val"]))

    return [p1,p2,p3,p4]
