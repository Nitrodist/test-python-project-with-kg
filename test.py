#!/usr/bin/env python

import json

with open('account_mapping.json') as file_object:
        data = json.load(file_object)
print(data)

vendor_name = "Joe Blow vendor"

print data[vendor_name]

if data[vendor_name] != None:
    print "Found " + str(data[vendor_name]) + "!"
else:
    print "vendor '" + vendor_name + "' not found"
