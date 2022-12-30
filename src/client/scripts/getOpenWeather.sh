#!/bin/bash -e
LAT=$1
LON=$2
APPID=$3
curl "https://api.openweathermap.org/data/2.5/onecall?lat=${LAT}&lon=${LON}&units=metric&lang=ja&appid=${APPID}"
