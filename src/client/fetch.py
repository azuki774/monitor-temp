import os
import subprocess
import json

def fetchRemo():
    SHELL_PATH = '/app/scripts/getDevices.sh'
    REMO_TOKEN = os.environ['REMO_TOKEN']
    resultValue = subprocess.run([SHELL_PATH, REMO_TOKEN], capture_output=True, text=True)
    res_json = json.loads(resultValue.stdout)
    return res_json["newest_events"]

def fetchOpen():
    SHELL_PATH = '/app/scripts/getOpenWeather.sh'
    OPEN_TOKEN = os.environ['OPEN_TOKEN']
    LAT = os.environ['OPEN_LAT']
    LON = os.environ['OPEN_LON']
    resultValue = subprocess.run([SHELL_PATH, LAT, LON, OPEN_TOKEN], capture_output=True, text=True)
    res_json = json.loads(resultValue.stdout)
    return res_json["current"]
