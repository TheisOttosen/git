#imports
from random import randint

print("Double Terninge Kast Simulation")
simnum = input("hvor mange simulationer: ")

#simulation
summer = []
for i in range(int(simnum)):
    terning1 = randint(1,6)
    terning2 = randint(1,6)
    sum = terning1 + terning2
    summer.append(sum)

#optælling
to = 0
tre = 0
fire = 0
fem = 0
seks = 0
syv = 0
otte = 0
ni = 0
ti = 0
elleve = 0
tolv = 0
for i in range(int(simnum)):
    if summer[i] == 2:
        to += 1
    if summer[i] == 3:
        tre += 1
    if summer[i] == 4:
        fire += 1
    if summer[i] == 5:
        fem += 1
    if summer[i] == 6:
        seks += 1
    if summer[i] == 7:
        syv += 1
    if summer[i] == 8:
        otte += 1
    if summer[i] == 9:
        ni += 1
    if summer[i] == 10:
        ti += 1
    if summer[i] == 11:
        elleve += 1
    if summer[i] == 12:
        tolv += 1

#udprint
print("to'ere: ", to)
print("tre'ere: ", tre)
print("fire're: ", fire)
print("fem'ere: ", fem)
print("seks'ere: ", seks)
print("syv'ere: ", syv)
print("otte're: ", otte)
print("ni'ere: ", ni)
print("ti'ere: ", ti)
print("elleve're: ", elleve)
print("tolv'ere: ", tolv)