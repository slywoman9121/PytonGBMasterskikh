user_name = input('Hi, what is your name? - ')
print(f"Hi, {user_name}")
str_w = input('Enter the value of the list separated by a space - ').split()
#print (str_w)
#d_str_w = len(str_w)
#print(d_str_w)
indx = 0
if d_str_w > 1 :
    while indx<d_str_w-1 :
        tt = str_w[indx]
        str_w[indx]=str_w[indx+1]
        str_w[indx+1]=tt
        indx=indx+2
print (list(str_w))