import pandas as pd
from matplotlib import pyplot as plt

sampleData = pd.read_csv("sample_data.csv")
print(sampleData)

columnA = sampleData.column_a
columnB = sampleData.column_b
columnC = sampleData.column_c

X = columnA
Y = columnB
Y_2 = columnC
plt.plot(X, Y)
plt.plot(X, Y_2)
plt.legend(["Y", "Y2"])
plt.show()


