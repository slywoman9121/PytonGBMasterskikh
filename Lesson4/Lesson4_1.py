from Script4_1 import zp
user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
virab = float(input("Введите выработку в часах - "))
stavka = float(input("Введите ставку за час - "))
premia = float(input("Введите премию - "))

print(zp(virab,stavka,premia))