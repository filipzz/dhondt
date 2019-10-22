import json

with open('results2019.json') as f:
    data = json.load(f)

with open('results2015.json') as ff:
    dataf = json.load(ff)

for row in data:
    num = row["field1"]
    name = row["field2"]
    namef =
