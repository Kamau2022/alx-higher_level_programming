#!/bin/bash
# This script takes in a URL, sends a GET request to that URL, and displays the body of the response
curl -sI "$1" | grep -i HTTP | awk '{print $2}'
