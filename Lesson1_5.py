prib = int(input('Введите прибыль предприятия - '))
ubit = int(input('Введите издержки предприятия - '))
pu=prib-ubit

if pu>0 :
    rent=int((pu/prib)*100)
    print(f"Ура! Денюжкав прибыло! Прибыль предприятия составляет: {rent}%")
    FTE_100 = float(input("Укажите численность сотрудников: "))
    FTE_50 = float(input("Укажите численность сотрудников с 50%: "))
    FTE_1000=FTE_50/2
    FTE=FTE_100+FTE_1000
    pribfull=pu/FTE
    print(F"Прибыль на одного сотрудника= {pribfull}")
else :
    print(f"Нафаня, сундук украли. Мы работаем в убыток.")
