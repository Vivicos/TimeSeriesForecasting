
n = int(input("Numero de la serie de Fibonacci: "))
# n = 8
m = 0
p = 0

# print(fibo(n))

for i in range(1,n):
    if m == 0:
        p = m
        print('0 : ', p)
        m = m + 1
        print('1 : ', m)
        
    elif m == 1:
        p = m
        m = m + p
        print(i, ':',m)

    else:
        
        m = m + p
        p = m - p
        print(i, ':',m)


print("Secuencia de Fibonacci completada.")
