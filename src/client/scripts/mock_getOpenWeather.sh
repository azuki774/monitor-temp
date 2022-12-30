#!/bin/bash -e
LAT=$1
LON=$2
APPID=$3
CURRENT=$(cd $(dirname $0);pwd)
cat "${CURRENT}/mockdata/getOpenWeather.mock" | jq '.current'
