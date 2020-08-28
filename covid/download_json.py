import requests 
import pandas as pd
import csv 

# DOWNLOADS THE JSON DATA INTO A NEWLY CREATED FILE DESIGNATED 'DOWNLOADED'
#CSV_URL = 'https://api.covidtracking.com/v1/us/current.json'
# req = requests.get(CSV_URL)
# url_content = req.content
# csv_file = open('downloaded.json', 'wb')
# csv_file.write(url_content)
# csv_file.close()

#==================================#
#==================================#
#==================================#
#==================================#




#==================================#
# CREATE A CLASS CALLED COVID 
#==================================#





    
    #==================================#
    # FUNCTION 1 
    # This function should pull the json data and store it in a python dictionary 
    #==================================#
JSON_URL = 'https://api.covidtracking.com/v1/us/current.json'
response = requests.get(JSON_URL, headers={"Accept":"application/json"}).json()
data = response[0]
#cov = data 

#print(data)

cov = data
#cov.items()

def format_cov(cov):
    print(cov['date'])
    print(cov['states'])
    print(cov['positive'])
    print(cov['negative'])
    print(cov['pending'])
    print(cov['hospitalizedCurrently'])
    print(cov['hospitalizedCumulative'])
    print(cov['inIcuCurrently'])
    print(cov['inIcuCumulative'])
    print(cov['onVentilatorCurrently'])
    print(cov['onVentilatorCumulative'])
    print(cov['recovered'])
    print(cov['dateChecked'])
    print(cov['death'])
    print(cov['hospitalized'])
    print(cov['lastModified'])
    print(cov['total'])
    print(cov['totalTestResults'])
    print(cov['posNeg'])
    print(cov['deathIncrease'])
    print(cov['hospitalizedIncrease'])
    print(cov['negativeIncrease'])
    print(cov['positiveIncrease'])
    print(cov['totalTestResultsIncrease'])
    print(cov['hash'])
#format_cov(cov)


    
def tester(cov):
    for item in cov.items():
        print(item)
#tester(cov)


#TRANSFORMS JSON DATA INTO CSV 
def to_csv(cov):
    CSV_URL = 'https://api.covidtracking.com/v1/us/current.csv'
    req = requests.get(CSV_URL)
    url_content = req.content
    csv_file = open('data.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
to_csv(cov)




    


