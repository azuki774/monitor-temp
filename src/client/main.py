import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import remo
import openweather
import sys

REMOTE_HOST = os.environ['INFLUXDB_HOST']
ORG = os.environ['INFLUXDB_ORG']
BUCKET = os.environ['INFLUXDB_BUCKET_NAME']
TOKEN = os.environ['INFLUXDB_TOKEN']

def main():
    args = sys.argv
    if len(args) != 2:
        print("invalid args")
        sys.exit(1)
    
    target = args[1]
    client = InfluxDBClient(url=REMOTE_HOST, token=TOKEN, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    pointList = []

    print(target)
    if target == 'remo':
        pointList = remo.remo_main()
    elif target == 'open':
        pointList = openweather.open_main()
    else:
        print("unknown args")
        sys.exit(1)

    for p in pointList:
        write_api.write(bucket=BUCKET, record=p)

if __name__ == "__main__":
    main()
