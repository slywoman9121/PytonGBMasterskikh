user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
mon = int(input('Enter the month number - '))
print(mon)
zima="Winter"
vesna="Spring"
leto="Summer"
osen="Autumn"
if mon < 12 :
    god = {1:zima, 2:zima, 3:vesna,
           4:vesna, 5:vesna, 6:leto,
           7:leto, 8:leto, 9:osen,
           10:osen, 11:osen, 12:zima}
    godl=[zima, zima, vesna, vesna, vesna, leto, leto, leto, osen, osen, osen, zima]
    print(godl[int(mon)-1])
else:
    print("Enter the correct month")
