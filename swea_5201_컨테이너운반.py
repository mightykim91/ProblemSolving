def sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst


for tc in range(1,int(input())+1):
    num_containers, num_trucks = map(int,input().split())
    weights = list(map(int,input().split()))
    capability = list(map(int,input().split()))
    loaded = [False]*num_trucks
    sort(weights)
    sort(capability)
    transferred = 0
    for i in range(num_containers):
        for j in range(num_trucks):
            if weights[i] <= capability[j] and not loaded[j]:
                loaded[j] = True
                transferred += weights[i]
                break

    print("#{} {}" .format(tc,transferred))



