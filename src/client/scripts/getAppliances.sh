#!/bin/bash -e
TOKEN=$1
curl -X GET "https://api.nature.global/1/appliances" -H "accept: application/json" -k --header "Authorization: Bearer ${TOKEN}" | jq ".[]"
