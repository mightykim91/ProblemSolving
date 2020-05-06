#Brute Force
def dfs(prev_point, consumption):
    global min_consumption

    if consumption > min_consumption:
        return

    elif False not in visited:
        consumption += consume_table[prev_point-1][0]
        if consumption < min_consumption:
            min_consumption = consumption
            return

    for area in areas:
        if not visited[area-1]:
            visited[area-1] = True
            dfs(area, consumption+consume_table[prev_point-1][area-1])
            visited[area-1] = False


for tc in range(1,int(input())+1):
    N = int(input())
    consume_table = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*N
    visited[0] = True
    areas = [x+1 for x in range(1,N)]
    min_consumption = 987654321
    dfs(1,0)
    print("#{} {}" .format(tc,min_consumption))


