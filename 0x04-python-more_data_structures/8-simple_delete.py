#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
        if key != i:
            return a_dictionary
        else:
            del a_dictionary[key]
    return a_dictionary
