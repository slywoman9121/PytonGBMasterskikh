user_name = input('What is your name? - ')
print(f"Hi, {user_name}")
with open("FourthFile.txt", "r") as str:
    for line in str:
        print(line.strip())
        rr = line.split("-")
        rr[-1] = rr[-1].strip()
        # print(rr)
        with open("FourthFile_1.txt", "w") as str2:
            if rr[0] == 'One':
                rr[0] = 'Один'
            elif rr[0] == 'Two':
                rr[0] = 'Два'
            elif rr[0] == 'Three':
                rr[0] = 'Три'
            elif rr[0] == 'Four' :
                rr[0] = 'Четыре'
            with open("FourthFile_1.txt", "a") as str3:
                str3.write(f"\n{rr}")