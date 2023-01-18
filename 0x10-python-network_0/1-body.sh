#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sI  --stderr /dev/null "$1" | head -1 | cut -d' ' -f2
