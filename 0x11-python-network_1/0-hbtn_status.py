#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/'
                                'status') as response:
        data = response.read()
        encoding = response.info().get_content_charset()
        html = data.decode(encoding)
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {} ".format(data))
        print("\t- utf8 content: {}".format(html))
