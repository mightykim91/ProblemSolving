def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x,y):
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = [x for x in range(N+1)]
    data = list(map(int, input().split()))
    sets = []
    for i in range(M):
        union(data[i*2],data[(i*2)+1])

    for i in range(1,len(p)):
        sets.append(find_set(i))

    print("#{} {}".format(tc,len(set(sets))))



