#!/usr/bin/env python3
"""
pretty prints swagger/openapi json files to the console.
Useful when static human readble output is required, eg. reporting.
"""

import json
import sys
import os

try:
    FILENAME = sys.argv[1]
except IndexError:
    print("Error: no input file specified")
    exit(1)

if not os.path.isfile(FILENAME):
    print("Error: Problem with input file - check file/path and try again")
    exit(1)


with open(FILENAME, "r") as API_DATA_RAW:
    API_DATA = json.load(API_DATA_RAW)

for path in API_DATA["paths"]:
    print("Path: {}".format(path))
    for method in API_DATA["paths"][path]:
        if method not in ["get", "put", "patch", "post", "delete", "head"]:
            continue
        print("Method: {}".format(method))
        try:
            print("Summary: {}".format(API_DATA["paths"][path][method]["summary"]))
        except KeyError:
            print("Summary: None")
        try:
            print(
                "OperationId: {}".format(API_DATA["paths"][path][method]["operationId"])
            )
        except KeyError:
            print("OperationId: Unknown")
        try:
            for param in API_DATA["paths"][path][method]["parameters"]:
                print("Parameters: {}".format(param))
        except KeyError:
            print("Parameters: None")
        try:
            for rbody in API_DATA["paths"][path][method]["requestBody"]:
                print(
                    "RequestBody: {} - {}".format(
                        rbody, API_DATA["paths"][path][method]["requestBody"][rbody]
                    )
                )
        except KeyError:
            print("RequestBody: None")
        try:
            for response in API_DATA["paths"][path][method]["responses"]:
                print(
                    "Response: {} - {}".format(
                        response,
                        API_DATA["paths"][path][method]["responses"][response][
                            "description"
                        ],
                    )
                )
        except KeyError:
            print("Responses: None")
        print()
