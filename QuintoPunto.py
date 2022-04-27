# Programa que me calcula numero mayor de N Entradas
numeros = []
for i in range(3):
  numero =input("Introduce el número #{}: ".format(i + 1))
  numeros.append(numero)
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("El numero Mayor es :", mayor)