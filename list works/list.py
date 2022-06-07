lst=[10,11,12,13,14,15,16,17]
element=11
flag=0
for num in lst:
    if element==num:
        flag=1
        break

print("print element found" if flag!=0 else "not found")
