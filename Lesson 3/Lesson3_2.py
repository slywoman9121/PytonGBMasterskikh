def infot (name:str, family:str, gr:int, gp:str, e_mail:str, tel:int):

    kort = (name, family, gr, gp, e_mail, tel)
    print(kort)
#user_name = input('Привет, как тебя зовут - ')
name1 = input("Введите имя - ")
family1 = input("Введите фамилию - ")
gr1 = input("Введите год рождения - ")
gp1 = input("Введите город рождения- ")
e_mail1 = input("Введите e-mail - ")
tel1 = input("Введите номер телефона - ")
stroka = infot(name1, family1, gr1, gp1, e_mail1, tel1)
print(stroka)