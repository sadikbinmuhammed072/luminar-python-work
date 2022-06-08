lst=[5,3,4,6]

sum=9

for i in range(len(lst)):
    for j in range((i+1),len(lst)):
        cur_sum=lst[i]+lst[j]
        if cur_sum==sum:
            print(f"pairs {lst[i]},{lst[j]}")
            break