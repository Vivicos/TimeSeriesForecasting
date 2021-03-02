# def fibo(n):

#     if m == 0:
#         p = m
#         print(p)
#         m = m + 1
#         print(m)
        
#     elif m == 1:
#         p = m
#         m = m + p
#         print(m)

#     else:
        
#         m = m + p
#         p = m - p
#         print(m)    

# 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 1 2 3 5 8 13 21 34 55 89

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