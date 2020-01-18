import pandas as pd
from matplotlib import pyplot as plt

countryData = pd.read_csv("countryData.csv")
print(countryData)

dk = countryData[countryData.country == "Denmark"]
angola = countryData[countryData.country == "Angola"]

print(dk)
print(angola)

dktime = dk.year
angolatime = angola.year
dkpop = dk.population / 10**6
angolapop = angola.population / 10**6

print(dktime)
print(angolatime)
print(dkpop)
print(angolapop)

X = dktime
X_2 = angolatime
Y = dkpop # / dkpop.iloc[0] * 100
Y_2 = angolapop # / angolapop.iloc[0] * 100

plt.plot(X, Y)
plt.plot(X_2, Y_2)
plt.title("Samligning af Danmarks og Angolas befolkningstal")
plt.xlabel("Tid")
plt.ylabel("Befolkningstal")
plt.legend(["Danmark", "Angola"])
plt.show()
