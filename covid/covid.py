import requests 
import pandas as pd
import csv 


#PULLS JSON DATA STORES IN PYTHON DICT
JSON_URL = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(JSON_URL, headers={"Accept":"application/json"}).json()
data = response[0]
cov = data 



#TRANSFORMS PYTHON DICT INFO AND PORTS INTO DAILY CSV FILE
def to_csv(cov):
    CSV_URL = 'https://api.covidtracking.com/v1/us/current.csv'
    req = requests.get(CSV_URL)
    url_content = req.content
    csv_file = open('new_data.csv', 'wb')
    #PERHAPS USE .writerow() here
    csv_file.write(url_content)
    csv_file.close()
to_csv(cov)

# EITHER WRITE AN ADDITIONAL FUNCTION TO JUST ADD A NEW ROW TO THE CSV
#OR ADD THIS CAPABILITY INTO THE ABOVE FUNCTION ( I'D ADD IT INTO ABOVE FUNCTION )




    


