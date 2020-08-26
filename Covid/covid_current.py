import requests 
import csv 


CSV_URL = 'https://api.covidtracking.com/v1/us/current.csv'

req = requests.get(CSV_URL)
url_content = req.content
csv_file = open("downloaded.csv", "wb")

csv_file.write(url_content)
csv_file.close()


        