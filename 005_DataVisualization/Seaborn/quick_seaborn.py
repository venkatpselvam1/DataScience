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
