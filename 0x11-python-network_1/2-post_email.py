#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the email
   as a parameter, and displays the body of the response
   (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]})
    email = email.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], email) as response:
        html = response.read()
        print(html.decode('utf-8'))
