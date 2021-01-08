import requests 
from os import path
import csv 

 
JSON_URL = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(JSON_URL, headers={"Accept":"application/json"}).json()
cov = response[0]


file_path = path.relpath("data/log.csv")
with open(file_path, 'a', newline='') as fd:
    fieldnames = ['date','states','positive','negative','pending',
              'hospitalizedCurrently','hospitalizedCumulative','inIcuCurrently',
              'inIcuCumulative','onVentilatorCurrently','onVentilatorCumulative',
              'recovered','dateChecked','death','hospitalized','lastModified','total',
              'totalTestResults','posNeg','deathIncrease','hospitalizedIncrease',
              'negativeIncrease','positiveIncrease','totalTestResultsIncrease','hash'
              ]
    writer = csv.DictWriter(fd, fieldnames=fieldnames)
    writer.writerow(cov) 


    


