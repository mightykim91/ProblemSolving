def find(x):
    global p
    if p[x] == x:
        return x
    else:
        return find(p[x])


def union(x,y):
    global p
    p[find(y)] = find(x)


def kruskal(datas):
    global p
    min_weight = 0

    for data in sorted(datas, key=lambda x:x[2]):
        s, e, weight = data
        start = find(s)
        end = find(e)
        if start != end:
            union(start,end)
            min_weight += data[2]

    print('#{} {}' .format(tc,min_weight))

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    data = []
    p = [x for x in range(V+1)]
    for i in range(E):
        start, end, edge = map(int, input().split())
        data.append([start, end, edge])

    kruskal(data)
