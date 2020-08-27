import pandas as pd
#TRANSFORMS DATA INTO CSV 
statusObj = pd.read_json('downloaded.json', orient='columns')
statusObj.to_csv('data.csv', index=False)







