#!/usr/bin/python3
"""add program args module"""
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

import sys
import os.path

args = sys.argv[1:]
list1 = []

if os.path.exists("./add_item.json"):
    list1 = load("add_item.json")
save(list1 + args, "add_item.json")
