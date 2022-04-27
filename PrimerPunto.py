#Implementar un programa que muestre la 
# sucesion o serie de Fibonacci es la siguiente sucesion infinita de numeros naturales: 
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , 233 , 377 , 610 , 987 , 
# 1597

def Fibonacci_fun(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return Fibonacci_fun(n - 1) + Fibonacci_fun(n - 2)


print("Serie infinita Fibonacci".center(30, '-'))

size = 150
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
for i in range(0,size):
    if i>1:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(f'{fibonacci[i]} ',end="")
print()