import numpy as np

Lst = [13, 4, 20, 15, 6, 20, 20]

Lst = np.array(Lst)
print("Su vector es" .center(50, "-"))
print()
print(Lst)
print()
n = int(input("Indique el numero del vector que quiera encontrar: "))
result = np.where(Lst == n)
print()
print("Su nuemro del vector indicado se encnetra:", result[0])