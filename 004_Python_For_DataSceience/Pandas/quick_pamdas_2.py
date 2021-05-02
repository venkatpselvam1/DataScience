import numpy as np
import pandas as pd
data = pd.read_csv("weatherdata.csv", header =0)
#data.head()
#data[(data.Sunshine > 4) & (data.MaxTemp> 35)]
dataInd = pd.DatetimeIndex(data.Date)

data["Year"]=dataInd.year
data["Month"]=dataInd.month
data["DAyofMonth"]=dataInd.day
data["MaxTemp_f"] = data.MaxTemp * 9/ 5 +32
data["IsRainy"]=data.Rainfall.apply(lambda x : "Rainy" if x > 50 else "Not rainy")
data.head()
print(data[data.IsRainy == "Rainy"])
print(data.describe())
print(data.head())
data[["Location", "Rainfall"]].groupby("Location").sum()
print(data.head())
data_location = data.groupby(by="Location").mean()
data_location.sort_values("Rainfall", ascending=False).head()
data_location.head()
data_cold = data.groupby(by="Month").mean()
data_cold.sort_values("MinTemp").head()
𝑊𝐶𝐼=(10∗𝑣⎯⎯√−𝑣+10.5).(33−𝑇𝑚)
data["WCI"]=(10*np.sqrt(data.WindGustSpeed)- data.WindGustSpeed+10.5)*(33-data.MinTemp)
def funce(x):
    wind = x.WindGustSpeed
    minTemp = x.MinTemp
    return (10*np.sqrt(wind)- wind+10.5)*(33-minTemp)
#data["WCI"]=data.apply(funce, axis=1)
print(data.head())
data_cold_wci = data.groupby(by="Month").mean()
data_cold_wci.sort_values("WCI").head()
print(data.groupby(by="Month"))
