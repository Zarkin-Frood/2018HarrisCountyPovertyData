import requests
import pandas as pd


# api-endpoint
URL = "https://api.census.gov/data/timeseries/poverty/saipe"

# defining a params dict for the parameters to be sent to the API
PARAMS = {"get":"NAME,SAEPOV0_17_PT,SAEPOVALL_PT,SAEMHI_PT",
          'GEOID':"48201","YEAR":2018}

  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)


# extracting data in json format. format is list of lists where first list are col headers
df = pd.DataFrame.from_records(r.json()[1:],columns = r.json()[0])

renamedcols = {'SAEMHI_PT':'Estimate of the median household income',
               'SAEPOVALL_PT':'Estimate of the number of people of any age in poverty',
               'SAEPOV0_17_PT':'Estimate of the number of people under the age of 18 in poverty',
               'NAME':'County'}


# keep only the prospective renamed columns in reverse list
df = df.loc[:,[i for i in renamedcols.keys()][::-1]]

# rename columns in dataframe
df.rename(columns = renamedcols,inplace = True)

# output to csv
df.to_csv('censusdata.csv',index = False)


