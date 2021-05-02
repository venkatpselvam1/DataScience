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

# All imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file 
sales = pd.read_excel('sales.xlsx')
sales = pd.read_excel('sales.xlsx', index_col=[0, 1])
print(sales.head())
print(sales.head(3))#print(sales.tail())
print(sales.head())
print(sales.info())
print(sales.describe())
print(sales["Profit"])
print(sales[["Profit", "Sales"]])
sales[["Profit", "Sales", "No_of_Orders"]].plot(kind="box", subplots=True)
plt.show()

#slicing and manipulation
sales = pd.read_excel('sales.xlsx', index_col = [1])
#print(sales[["Sales", "Profit"]])
#print(sales.loc[0])
#print(sales.loc[0,"Profit"])
#print(sales.iloc[0, 3])
#print(sales.loc[:,["Profit","Sales"]])
#print(sales.iloc[3:9,2])
#print(sales.iloc[3])
#print(sales.Sales > 30000)
#print(sales[sales.Sales > 30000])
#print(sales[ sales.Market.isin(["Africa", "USCA"]) & (sales.Sales > 30000) ])
#sales.Sales= sales.Sales.floordiv(1000)
print(sales.head())
sales.rename(columns={"Sales":"Sales in 1000s"}, inplace=True)
print(sales.head())
#print(sales.Profit.sum())
total= sales.Profit.sum()
#print(total)
sales["test"]=sales.Profit.apply(lambda x: x/total*100)
#sales.loc[sales.Profit < 0,"Profit"]=np.nan
#print(sales.head())
#sales.reset_index(inplace=True)
sales.reset_index(inplace=True)
print(sales.head())
sales.sort_index()
sales.set_index(["Market", "Region"], inplace=True)
sales.head(10)
sales.loc[(["Africa", "Europe"]), ["Profit", "test"]]
