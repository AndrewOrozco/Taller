# Saber si numero seleccionado es inpar o par

print("Sleccion de numero ingresado para la verificacion de numero par o inpar")

numero = int(input("Profavor ingresar un número: "))

if numero % 2 == 0:
    print("El numero es par".center(30,"-"))
else:
    print("El numero es impar".center(30,"-"))

