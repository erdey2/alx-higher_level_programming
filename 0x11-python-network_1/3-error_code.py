#!/usr/bin/python3
""" a module to post data """
from sys import argv
from urllib import request
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: ', e.code)
