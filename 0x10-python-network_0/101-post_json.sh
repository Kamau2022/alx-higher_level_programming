#!/bin/bash
# To post json file
curl -X POST "$1" -H 'Content-Type: application/json' -d @"$2"
