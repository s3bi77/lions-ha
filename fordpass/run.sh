#!/bin/bash

CONFIG_PATH=/data/options.json

if [[ -r "$CONFIG_PATH" ]]
then
    fordpassuser="$(jq --raw-output '.fordpassuser // empty' $CONFIG_PATH)"
    fordpasspassword="$(jq --raw-output '.fordpasspassword // empty' $CONFIG_PATH)"
    fordpassvin="$(jq --raw-output '.fordpassvin // empty' $CONFIG_PATH)"
    mqtthost="$(jq --raw-output '.mqtthost // empty' $CONFIG_PATH)"
    mqttuser="$(jq --raw-output '.mqttuser // empty' $CONFIG_PATH)"
    mqttpassword="$(jq --raw-output '.mqttpassword // empty' $CONFIG_PATH)"
fi

export fordpassuser="${fordpassuser}"
export fordpasspassword="${fordpasspassword}"
export fordpassvin="${fordpassvin}"
export mqtthost="${mqtthost}"
export mqttuser="${mqttuser}"
export mqttpassword="${mqttpassword}"

exec python3 /fordpass.py