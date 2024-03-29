#!/usr/bin/python3
""" A module to fetch url using requests """
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
