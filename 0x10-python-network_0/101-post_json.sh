#!/bin/bash
# To post json file
curl -sX POST "$1" -H 'Content-Type: application/json' -d @"$2"
