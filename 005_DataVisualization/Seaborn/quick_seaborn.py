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
