# All imports
import numpy as np
import pandas as pd
dct = {"name":["venkat", "test"], "age":[12, 13],"country":["India", "US"]}
#print(dct)
dct_dta_frame = pd.DataFrame(dct)
print(dct_dta_frame)
print(dct_dta_frame.columns)
dct_dta_frame.columns=["Full name", "DOB", "Place"]
print(dct_dta_frame.columns)
dct_dta_frame

##REad csv
cars_data_frame = pd.read_csv("cars.csv")
print(cars_data_frame)
cars_data_frame = pd.read_csv("cars.csv", header=None)
print(cars_data_frame)
cars_data_frame.columns = ["District", "Country code", "Country", "Count", "Drive Rigth"]
print(cars_data_frame)

### set single index
cars_data_frame = pd.read_csv("cars.csv", header=None)
print(cars_data_frame.index)
cars_data_frame = pd.read_csv("cars.csv", header=None, index_col=0)
cars_data_frame.columns = ["country code", "country", "count", "rght"]
print(cars_data_frame)
print(cars_data_frame.index)
cars_data_frame.index.name="Index column"
print(cars_data_frame)
### set mulitple index
cars_data_frame = pd.read_csv("cars.csv", header=None)

cars_data_frame.columns= ['country_code','region','country','cars_per_cap','drives_right']
print(cars_data_frame)
cars_data_frame.set_index(["region", "country_code"], inplace=True)
print(cars_data_frame)
