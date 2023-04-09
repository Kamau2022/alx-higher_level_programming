#!/bin/bash
# This script takes in a URL, sends a GET request to that URL, and displays the body of the response
curl "$1" -H "X-School-User-Id: 98"
