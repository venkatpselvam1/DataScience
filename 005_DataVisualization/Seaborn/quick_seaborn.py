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
