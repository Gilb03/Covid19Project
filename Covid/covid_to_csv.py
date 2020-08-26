# the file I will use to 

import csv 
import requests


#    def create_csv_file():
#        records = [
    #            {""}
    #         ]
#CSV_URL = 'https://api.covidtracking.com/v1/us/current.json'

#req = requests.get(CSV_URL)
#url_content = req.content
#csv_file = open("downloaded.csv", "w", newline='')

#csv_file.write(url_content)
#csv_file.close()

def create_csv_file():
        covids = [{
             "date":20200825,"states":56,"positive":5749803,
             "negative":67266976,"pending":4091,"hospitalizedCurrently":38762,
             "hospitalizedCumulative":362452,"inIcuCurrently":7851,"inIcuCumulative":16920,
             "onVentilatorCurrently":2163,"onVentilatorCumulative":1789,"recovered":2053699,
             "dateChecked":"2020-08-25T00:00:00Z","death":170353,"hospitalized":362452,
             "lastModified":"2020-08-25T00:00:00Z","total":73020870,"totalTestResults":73016779,
             "posNeg":73016779,"deathIncrease":1147,"hospitalizedIncrease":1999,"negativeIncrease":597782,
            "positiveIncrease":36679,"totalTestResultsIncrease":634461,"hash":"47bc6a8573ef4910963a04ced9452b12544d48a6"}
            ]
csv_writer = csv.writer(open("covid_data.csv", "w"), delimiter=",")
csv_writer.writerow(["date", "states","positive","negative","pending", "hospitalizedCurrently", "hospitalizedCumulative","inIcuCurrently",
                     "inIcuCumulative","onVentilatorCurrently","onVentilatorCumulative", "recovered","dateChecked", "death", "hospitalized", 
                     "lastModified", "total","totalTestResults", "posNeg", "deathIncrease", "hospitalizedIncrease", "negativeIncrease", 
                     "positiveIncrease", "totalTestResultsIncrease", "hash" ])
for covid in covids:
    csv_writer.writerow([
       covid["date"],covid["states"],covid["positive"],covid["negative"],covid["pending"],covid["hospitalizedCurrently"], covid["hospitalizedCumulative"],covid["inIcuCurrently"],
                     covid["inIcuCumulative"],covid["onVentilatorCurrently"],covid["onVentilatorCumulative"], covid["recovered"],covid["dateChecked"], covid["death"], covid["hospitalized"], 
                     covid["lastModified"], covid["total"], covid["totalTestResults"], covid["posNeg"], covid["deathIncrease"], covid["hospitalizedIncrease"], covid["negativeIncrease"], 
                    covid["positiveIncrease"], covid["totalTestResultsIncrease"], covid["hash"] 
    ])
def read_csv_file():
    for row in csv,reader(open(covid_data.csv), 'r', delimiter=','):
        print(row)
        
def update_csv():
    csv_writer = csv.writer(open("covid_data.csv", "a"), delimiter=",")
    csv_writer.writerow([0])
    
if __name__ == "__main__":
    update_csv()