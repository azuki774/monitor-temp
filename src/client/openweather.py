import os
import subprocess
import json

def fetch_open():
    SHELL_PATH = '/app/scripts/getOpenWeather.sh'
    OPEN_TOKEN = os.environ['OPEN_TOKEN']
    LAT = os.environ['OPEN_LAT']
    LON = os.environ['OPEN_LON']
    resultValue = subprocess.run([SHELL_PATH, LAT, LON, OPEN_TOKEN], capture_output=True, text=True)
    res_json = json.loads(resultValue.stdout)
    return res_json["current"]

def open_main():
    openValues = fetch_open()

    p1 = Point("measurement").tag("source", "open").field("temp", float(openValues["temp"]))
    p2 = Point("measurement").tag("source", "open").field("pressure", int(openValues["pressure"]))
    p3 = Point("measurement").tag("source", "open").field("humidity", int(openValues["humidity"]))
    p4 = Point("measurement").tag("source", "open").field("feels_like", float(openValues["feels_like"]))
    p5 = Point("measurement").tag("source", "open").field("clouds", int(openValues["clouds"]))

    return [p1,p2,p3,p4,p5]
