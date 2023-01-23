#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
   to the URL and displays the body of the response.
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print("Index")
    else:
        print("Error code: ", end='')
        print(r.status_code)
