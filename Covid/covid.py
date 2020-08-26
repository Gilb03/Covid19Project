import requests
from urllib.parse import urlencode, urlparse, quote_plus
import json
import csv

# API REQUEST AND RESPONSE WRITTEN TO A PYTHON DICTIONARY
url = "https://api.covidtracking.com/v1/us/current.csv"
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

        
    
        
    
cov = Covid(data)
     
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



#def scrape_covid(url):
#    url = 'https://api.covidtracking.com/v1/us/current.json'
#    response = requests.get(
#   url,headers={"Application": "application/json"}).json()
#    data = response[0]
#    covid = []
#    all_covid = []
#     for covid in all_covid:
#       covid_info = ( fetch_h, fetch_d, fetch_s, fetch_p, fetch_hc, fetch_r, fetch_dc,
#                     fetch_dt, fetch_lm, fetch_t, fetch_di)

  
  
# SAVES INFORMATION TO THE DB
#def save_to_db():
#    conn = sqlite3.connect('covid_db')
#    c = conn.cursor()
#    c.execute(''' CREATE TABLE covid_stats 
            #(hash INTEGER, date DATE, states TEXT, positive INTEGER,
            #hostpitalizedCumulative INTEGER, recovered INTEGER, 
            #death INTEGER,lastModified DATE, total INTEGER, 
            #deathIncrease INTEGER )
#          ''')
# conn.commit()
# conn.close()


    
