#!/usr/bin/python3
""" a module to find request id """
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        body = response.read()
        print(dict(response.headers).get('X-Request-Id'))
