#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    data = response.content
    html = data.decode('utf-8')
    print("Body response:")
    print("\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
