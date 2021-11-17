user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
str_w = [30, 2, 13, 45, 23, 2, 3, 1, 34]
print(str_w)
znach = [str_w[i] for i in range (len(str_w)) if str_w[i] > str_w[i-1]]
print(znach)