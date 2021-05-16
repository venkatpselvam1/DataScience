====================================================================================================================================
Seaborn intro
====================================================================================================================================
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#Check the number of null values in the columns
plt.hist(inp1["Rating"])
plt.show()

import seaborn as sns
sns.distplot(inp1["Rating"], kde=True, bins=15, horizontal=False)
plt.show()
====================================================================================================================================
sns.distplot(inp1["Rating"], kde=True, bins=15, color="red")
plt.title("Distibution of app rating", fontdict={"fontweight":20,"fontsize":25, "color":"red"})
plt.show()
====================================================================================================================================
import seaborn as sns
#sns.set_style("whitegrid")
plt.style.use("ggplot")
sns.distplot(inp1["Rating"], kde=True, bins=15, color="red")
plt.title("Distibution of app rating", fontdict={"fontweight":20,"fontsize":25, "color":"red"})
#print(plt.style.available)
plt.show()
====================================================================================================================================
inp1["Content Rating"].value_counts().plot.bar()
plt.show()
inp1["Content Rating"].value_counts().plot.barh()
plt.show()
====================================================================================================================================
plt.scatter(inp1["Size"],inp1["Rating"])
plt.show()
sns.jointplot(inp1["Price"], inp1["Rating"], kind="reg")
plt.show()
sns.pairplot(inp1[["Rating","Price", "Size","Reviews"]])
plt.show()
====================================================================================================================================
#inp1.groupby(["Content Rating"])["Rating"].sum().plot.bar()
#sns.barplot(data=inp1, x="Content Rating", y="Rating", estimator=np.median)
#sns.barplot(data=inp1, x="Content Rating", y="Rating", estimator=lambda x: np.quantile(x, 0.05))
plt.show()
====================================================================================================================================
Top4 Genres
====================================================================================================================================
top4=inp1["Genres"].value_counts()[:4].index
#print(list(top4))
print(inp1.shape)
inp2=inp1[inp1["Genres"].isin(top4)]
print(inp2.shape)
sns.barplot(data=inp2, x="Genres", y="Rating",estimator= lambda x: np.quantile(x, 0.05))
plt.show()
====================================================================================================================================
inp1["Size Bucket"]=pd.qcut(inp1["Size"], [0,0.2,0.4,0.6,0.8,1],["A","B","C","D","E"])
res=pd.pivot_table(data=inp1, index="Content Rating", columns="Size Bucket", values="Rating", aggfunc=lambda x:np.quantile(x, 0.2))
sns.heatmap(res)
plt.show()
sns.heatmap(res, cmap="Greens", annot=True)
plt.show()
====================================================================================================================================
datetimr=pd.DatetimeIndex( inp1["Last Updated"])
inp1["month"]=datetimr.month
#inp1.head()
plt.figure(figsize=[7,7])
inp1.groupby("month")["Rating"].mean().plot()
plt.show()
====================================================================================================================================
res1=pd.pivot_table(data=inp1, index="month",columns="Content Rating", values="Installs", aggfunc=np.median)
res1.plot(kind="bar", stacked=True, figsize=[10,6])
res2=res1[["Everyone", "Everyone 10+", "Mature 17+", "Teen"]].apply(lambda x : x/x.sum(), axis=1)
res2.plot(kind="bar", stacked=True, figsize=[10,6])
====================================================================================================================================
