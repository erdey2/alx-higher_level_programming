#!/usr/bin/python3
""" a module to post data """
from sys import argv
import requests


if __name__ == "__main__":
    value = {"email": argv[2]}
    r = requests.post(argv[1], data = value)
    print(r.text)
