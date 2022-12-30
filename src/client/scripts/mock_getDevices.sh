#!/bin/bash -e
TOKEN=$1
CURRENT=$(cd $(dirname $0);pwd)
cat "${CURRENT}/mockdata/getDevices.mock" | jq ".[]"
