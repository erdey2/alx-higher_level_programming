#!/usr/bin/python3
""" A module to fetch url"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print('- type: ', type(html))
    print('- content: ', (html))
    print('- utf8 content: ', (html.decode('utf-8')))
