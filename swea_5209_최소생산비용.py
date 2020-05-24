def backtrack(level, cost):
    global min_cost
    if level == N:
        min_cost = min(cost, min_cost)
        return

    for i in range(N):
        if not visited[i]:
            prod_cost = table[level][i]
            if prod_cost + cost >= min_cost:
                continue
            else:
                visited[i] = True
                backtrack(level+1, cost+prod_cost)
                visited[i] = False


for tc in range(1, int(input())+1):
    #number of items
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    #visited for factories
    visited = [False]*N
    min_cost = 987654321
    backtrack(0,0)
    print("#{} {}" .format(tc, min_cost))