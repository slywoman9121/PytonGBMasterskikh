def step (x, y):
    if x == 0 :
         return "Введите первое число отличное от нуля"
    elif y == 0:
         return "Введите второе число отличное от нуля"
    step1 = 1/(x ** y)
    return step1
raz = float(input("Введите первое целое число - "))
dva = int(input("Введите второе целое число - "))
rez = step(raz, dva)
print(rez)