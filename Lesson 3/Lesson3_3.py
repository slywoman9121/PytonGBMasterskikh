def my_func(nomerraz:int, nomerdva:int, nomertri:int):
    n1=nomerraz+nomerdva
    n2=nomerraz+nomertri
    n3=nomerdva+nomertri
    maxi=max(n1, n2, n3)
    if maxi == n1 :
        print(f"Сумма первых двух чисел наибольшая, она равна - {maxi}")
    elif maxi == n2 :
        print(f"Сумма первого и третьего чисел наибольшая, она равна - {maxi}")
    else :
        print(f"Сумма второго и третьего чисел наибольшая, она равна - {maxi}")


n11 = int(input("Введите первое число - "))
n22 = int(input("Введите второе число - "))
n33 = int(input("Введите третье число - "))

res = my_func(n11, n22, n33)
print(res)
