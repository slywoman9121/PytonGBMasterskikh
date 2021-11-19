user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
str_w = input('Enter a list of words - ').split()
for elem in str_w[::1]:
    dd=len(elem)
    if dd > 10:
        ddd=elem[:10]
print(f"Слово {ddd} - {dd}")