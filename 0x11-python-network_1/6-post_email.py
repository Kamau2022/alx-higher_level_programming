#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
   to the URL and displays the value of the X-Request-Id
   variable found in the header of the response.
"""
import requests
import sys
if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    data = response.content.decode()
    print(data)
