def my_del(nomerraz, nomerdva):
    #res = 1
    if nomerdva != 0:
     res = nomerraz/nomerdva
     print(res)
    else:
       return "Введите второе число отличное от нуля"

user_name = input('Привет, как тебя зовут - ')
raz = float(input("Введите первое число - "))
dva = float(input("Введите второе число - "))
stroka = my_del(raz, dva)
print (stroka)


