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
#data.head()
#print(data[data.IsRainy == "Rainy"])
#print(data.describe())
print(data.head())
data[["Location", "Rainfall"]].groupby("Location").sum()
#print(data)


