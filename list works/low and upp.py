lst=[2,3,4,6]
element=10
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]

    if element==cur_sum:
        print(f"pairs{lst[upp]},{lst[low]}")
        break
    elif cur_sum > element:
        upp-=1
    elif cur_sum < element:
        low+=1
