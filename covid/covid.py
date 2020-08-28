import requests 
import os 
import pandas as pd
import csv 


#PULLS JSON DATA STORES IN PYTHON DICT
JSON_URL = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(JSON_URL, headers={"Accept":"application/json"}).json()
data = response[0]
cov = data 



#TRANSFORMS PYTHON DICT INFO AND PORTS INTO DAILY CSV FILE also creates copy
def to_csv(cov):
    CSV_URL = 'https://api.covidtracking.com/v1/us/current.csv'
    req = requests.get(CSV_URL)
    url_content = req.content
    csv_file = open('new_data.csv', 'wb')
    #PERHAPS USE .writerow() here
    csv_file.writerows(url_content)
    csv_file.close()
#to_csv(cov) 

# THE UPDATE FUNCTION WORKS AND UPDATES THE LOG FILE
def to_string(cov):
    with open('new_info.csv', 'wb'):
        #csv_writer = newt
        CSV_URI = 'https://api.covidtracking.com/v1/us/current.csv'
        reg = requests.get(CSV_URI)
        new_line = reg.content
        new_line.writerows(new_line)
        new_line.close()
#to_string(cov)




with open('log.csv', 'a', newline='') as fd:
    fieldnames = ['date','states','positive','negative','pending',
              'hospitalizedCurrently','hospitalizedCumulative','inIcuCurrently',
              'inIcuCumulative','onVentilatorCurrently','onVentilatorCumulative',
              'recovered','dateChecked','death','hospitalized','lastModified','total',
              'totalTestResults','posNeg','deathIncrease','hospitalizedIncrease',
              'negativeIncrease','positiveIncrease','totalTestResultsIncrease','hash'
              ]
    writer = csv.DictWriter(fd, fieldnames=fieldnames)
    writer.writerow(cov)
#to_string(cov)  


    


