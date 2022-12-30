import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import remo
import openweather
import time

REMOTE_HOST = os.environ['INFLUXDB_HOST']
ORG = os.environ['INFLUXDB_ORG']
BUCKET = os.environ['INFLUXDB_BUCKET_NAME']
TOKEN = os.environ['INFLUXDB_TOKEN']
TARGET = os.environ['TARGET']

def main():
    client = InfluxDBClient(url=REMOTE_HOST, token=TOKEN, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    pointList = []

    print(TARGET)
    if TARGET == 'remo':
        pointList = remo.remo_main()
    elif TARGET == 'open':
        pointList = openweather.open_main()
    else:
        pointList = []

    for p in pointList:
        write_api.write(bucket=BUCKET, record=p)

if __name__ == "__main__":
    main()
