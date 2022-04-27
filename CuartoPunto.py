# Hallar el promedio de n números.
numero = int(input("Ingrse la cantidad de numeros a promediar: ".center(30)))
suma = 0
i = 1

while i <= numero :
    print("Ingrese el numero: ", i)
    nota = float(input())
    suma = suma+nota
    i += 1
    promedio = suma/numero
    print("El pormedio de numeros es: ".center(40, "-"))
    print(format(promedio, '=^30'))