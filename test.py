#!/usr/bin/env python

import json
import re
import csv

with open('account_mapping.json') as file_object:
        json_data = json.load(file_object)
print(json_data)

with open('transactions.csv') as file_object:
        csv_reader = csv.reader(file_object, delimiter=',')
        csv_data = for x in csv_reader:
            x

for row in csv_data:
    print row


#result = re.search('CDN TIRE STORE STORE [0-9][0-9][0-9]', probably_matching_value)
#
#print result.group(0)
