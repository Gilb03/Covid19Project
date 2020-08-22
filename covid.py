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

#FORMAT FOR HUMANS

data = response[0]
for k, v in data.items():
    print(k,v)
    
   
    
#  CREATE CLASS TO STORE DICTIONARY DATA IN K,V PAIRS

class Covid:  
    data = response[0]
def __init__(self, data, hash, date, dateChecked, states, lastModified,
                 positive, death, hospitalizedCumulative, recovered, 
                 deathIncrease, total):
        self.data = data 
        self.hash= hash
        self.date = date
        self.states = states
        self.positive = positive
        self.hospitalizedCumulative = hospitalizedCumulative
        self.recovered = recovered
        self.dateChecked = dateChecked
        self.death = death
        self.lastModified = lastModified
        self.total = total
        self.deathIncrease = deathIncrease
        self.params = {k:v}
        
    
def args_str(self, url_args):
        if self.params:
            for k, v in self.params.items():
               url_args[k] = v
            return urlencode(url_args)
print(Covid)
