import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv ('log/log.csv')
hc = df 

hc['hospitalizedCurrently'].hist()
plt.show()

hc['deathIncrease'].hist()
plt.show()

#this is gonna be the jupyter notebook