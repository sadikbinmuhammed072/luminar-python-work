lst=[10,11,12,13,14,15,16,17,12,12]
evenlist=[]

for num in lst:
    if num%2==0:
        evenlist.append(num)
print(evenlist)
evenlist.sort(reverse=True)
print(evenlist)
