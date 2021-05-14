================================================================================================================
Bar Graph
================================================================================================================
import numpy as np
import matplotlib.pyplot as plt

x_axis = np.array(["A","B","C"])
y_axis = np.array([10,7,6])
print(x_axis)
print(y_axis)
plt.bar(x_axis, y_axis, width=0.5, align="center", edgecolor="yellow", color="pink")
plt.title("test\n", fontdict={'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
plt.xlabel("names\n", fontdict={'fontsize': 15, 'fontweight' : 5, 'color' : 'red'})
plt.ylabel("values\n", fontdict={'fontsize': 15, 'fontweight' : 5, 'color' : 'red'})
ticks=np.arange(1,15,0.5)
label_ticks = ["{:.2f}".format(x) for x in ticks]
plt.yticks(ticks, label_ticks)
plt.show()
================================================================================================================
Scatter Graph
================================================================================================================
import numpy as np
import matplotlib.pyplot as plt

================================================================================================================
