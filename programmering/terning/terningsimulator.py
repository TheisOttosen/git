from random import randint

terninger = int(input("Hvor mange terninger: "))
simulationer = int(input("Hvor mange simulationer: "))


slag = []
for i in range(terninger):
    slag.append(randint(1,6))

