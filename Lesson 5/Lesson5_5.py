user_name = input('What is your name? - ')
print(f"Hi, {user_name}")
summ = open("FiveFile.txt", "w+")
with open("FiveFile.txt", "a") as str:
    summ1 = ("3 57 24 29")
    sss = summ1.split()
    # print(sss)
    tra = 0
    for elem in sss:
        tra += int(elem)
    print(tra)
    str.write(f"List of numbers - {summ1}")
    str.write(f"\nSumma - {tra}")