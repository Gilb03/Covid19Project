import requests
from urllib.parse import urlencode, urlparse, quote_plus
import json
import csv

# API REQUEST AND RESPONSE WRITTEN TO A PYTHON DICTIONARY
url = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(
    url,
    headers={"Application": "application/json"}
).json()

# FORMAT FOR HUMANS

data = response[0]



#  CREATE CLASS TO STORE DICTIONARY DATA IN K,V PAIRS

class Covid:

    def __init__(self, input_data):
        self.hash = input_data['hash']
        self.date = input_data['date']
        self.states = input_data['states']
        self.positive = input_data['positive']
        self.hospitalizedCumulative = input_data['hospitalizedCumulative']
        self.recovered = input_data['recovered']
        self.dateChecked = input_data['dateChecked']
        self.death = input_data['death']
        self.lastModified = input_data['lastModified']
        self.total = input_data['total']
        self.deathIncrease = input_data['deathIncrease']

    def args_str(self, url_args):
        if self.params:
            for k, v in self.params.items():
                url_args[k] = v
            return urlencode(url_args)


cov = Covid(data)
print(cov.hash)
print(cov.date)
print(cov.states)
print(cov.positive)
print(cov.hospitalizedCumulative)
print(cov.recovered)
print(cov.dateChecked)
print(cov.death)
print(cov.lastModified)
print(cov.total)
print(cov.deathIncrease)