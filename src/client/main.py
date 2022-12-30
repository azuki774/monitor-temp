import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import fetch
import time

REMOTE_HOST = os.environ['INFLUXDB_HOST']
ORG = os.environ['INFLUXDB_ORG']
BUCKET = os.environ['INFLUXDB_BUCKET_NAME']
TOKEN = os.environ['INFLUXDB_TOKEN']
TARGET = os.environ['TARGET']

def remo_main():
    remoValues = fetch.fetchRemo()
    p1 = Point("measurement").tag("source", "remo").field("hu", remoValues["hu"]["val"])
    p2 = Point("measurement").tag("source", "remo").field("il", remoValues["il"]["val"])
    p3 = Point("measurement").tag("source", "remo").field("mo", remoValues["mo"]["val"])
    p4 = Point("measurement").tag("source", "remo").field("te", float(remoValues["te"]["val"]))

    return [p1,p2,p3,p4]


def open_main():
    openValues = fetch.fetchOpen()

    p1 = Point("measurement").tag("source", "open").field("temp", float(openValues["temp"]))
    p2 = Point("measurement").tag("source", "open").field("pressure", int(openValues["pressure"]))
    p3 = Point("measurement").tag("source", "open").field("humidity", int(openValues["humidity"]))
    p4 = Point("measurement").tag("source", "open").field("feels_like", float(openValues["feels_like"]))
    p5 = Point("measurement").tag("source", "open").field("clouds", int(openValues["clouds"]))

    return [p1,p2,p3,p4,p5]

def main():
    client = InfluxDBClient(url=REMOTE_HOST, token=TOKEN, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    pointList = []

    print(TARGET)
    if TARGET == 'remo':
        pointList = remo_main()
    elif TARGET == 'open':
        pointList = open_main()
    else:
        pointList = []

    for p in pointList:
        write_api.write(bucket=BUCKET, record=p)

if __name__ == "__main__":
    main()
