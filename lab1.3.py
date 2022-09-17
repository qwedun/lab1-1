fib1 = 0                                    #Вывод: мы смогли создать программу, которая считывает число и определяет, является ли оно числом Фибоначчи
fib2 = 1
fib_sum = 1
n = int(input())
if n == fib1 or n == fib2:
    print('Yes')
elif n != fib_sum:
    while fib_sum < n:
        fib1 = fib2
        fib2 = fib_sum
        fib_sum = fib1 + fib2
    if n == fib_sum:
        print("Yes")
    else:
        print("No")
