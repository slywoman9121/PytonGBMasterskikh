user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
str_z_list = list(['str_zapros', 555, 'd', 8, 8.9])
print(f"The list that we will consider - {str_z_list}")
for elem in str_z_list[::1]:
    dd=type(elem)
    print(f"Type {elem} - {dd}")