lst1=[10,11,12,13,14]
lst2=[11,14,15,16,17]

#print common numbers from these two list

dup_lst=[]
for num in lst1:
    if num in lst2:
        dup_lst.append(num)
print(dup_lst)
