"""
This module is used for tests only.

Sends several "POST HTTP Requests" to a URL (in this case, the url used to
start/end calls).
"""


import urllib.request
import json


def test_data_insert(body):
    # Default request parameters
    request_url = "http://localhost:5000/call"
    req = urllib.request.Request(request_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return response.read()

def main():
    # Opening JSON sample file
    with open('samples.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        for item in data:
            print(test_data_insert(item))


# Calling the main function
main()
