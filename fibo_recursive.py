def fibonacci(n):      
    if n == 1:
        return 1

    elif n == 2:
        return 1  

    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input('Final de la secuencia de Fibonnacci: '))

for i in range(1,n):
    m = fibonacci(i)
    print(i, ':', m)

