#!/usr/bin/python3
""" a module to post data """
from sys import argv
from urllib import request
from urllib import parse


if __name__ == "__main__":
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode('ascii')
    with request.urlopen(argv[1], data) as response:
        body = response.decode('utf-8')
        print(body)
