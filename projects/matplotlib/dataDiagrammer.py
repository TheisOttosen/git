from matplotlib import pyplot as plt

x = [1, 5, 7, 10]
y = [5, 10, 11, 15]
z = [16, 12, 11, 6]

plt.plot(x, y) # laver linjer
plt.plot(x, z) # laver linjer
plt.title("Test plot") # sætter titel på
plt.xlabel("X") # sætter navn på x dimensionen
plt.ylabel("Y and Z") # sætter navn på y dimensionen
plt.legend(["this is y", "this is z"]) # fortæller hvilken linje der er hvad
plt.show() # viser det hele


