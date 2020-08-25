import requests
from urllib.parse import urlencode, urlparse, quote_plus
import json
# import 

# API REQUEST AND RESPONSE WRITTEN TO A PYTHON DICTIONARY
url = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(
    url,
    headers={"Application": "application/json"}
).json()
data = response[0]
input_data = data

# FORMAT FOR HUMANS





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

        
        

cov = Covid(data)


def fetch_h():
    print(cov.hash)
fetch_h()
  
def fetch_d():
    print(cov.date)   
fetch_d()
    
def fetch_s():
    print(cov.states)
fetch_s()
    
def fetch_p():
    print(cov.positive)
fetch_p()
    
def fetch_hc():
    print(cov.hospitalizedCumulative)
fetch_hc()

def fetch_r():
    print(cov.recovered)
fetch_r()
    
def fetch_dc():
    print(cov.dateChecked)
fetch_dc()
  
def fetch_dt():
    print(cov.death)
fetch_dt()
    
def fetch_lm():
    print(cov.lastModified)
fetch_lm()
    
def fetch_t():
    print(cov.total)
fetch_t()
    
def fetch_di():
    print(cov.deathIncrease)   
fetch_di()
    
#def save_to_db(fetch_di, fetch_t, fetch_lm,
#               fetch_dt, fetch_dc, fetch_r,
#               fetch_hc, fetch_p, fetch_s,
#               fetch_d,fetch_h ):
#    
#    print("this is going todb ")
# save_to_db()