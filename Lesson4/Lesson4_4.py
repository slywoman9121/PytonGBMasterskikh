user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
str_w = [30, 2, 13, 45, 23, 2, 3, 1, 34, 2, 30, 1]
print(str_w)
znach = [i for i in str_w if str_w.count(i) == 1]
print(znach)