import requests 
import csv 


CSV_URL = 'https://api.covidtracking.com/v1/us/current.json'
req = requests.get(CSV_URL)
url_content = req.content
csv_file = open('downloaded.json', 'wb')
csv_file.write(url_content)
csv_file.close()

#Now I need a function to just stack 
        