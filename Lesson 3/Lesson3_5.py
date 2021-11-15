def summar (spis, symvol):
    summ = 0
    for elem in spis:
        if elem != symvol :
            summ = summ + int*(elem)
        else :
            break
str_w = input('Введи список знаечений - ').split()
stop_slovo = input('Введи стоп-слово - ')
res = summar(str_w, stop_slovo)
