user_number = int(input('Введите целое положительное число? - '))
#print (user_number)
big=0
while user_number > 0 :
    prom = user_number % 10
    user_number = user_number // 10
    if prom>big:
        big=prom
print(big)
print("Program ended")