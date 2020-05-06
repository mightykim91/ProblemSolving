#Brute Force
def dfs(curr,dist):
    global min_ans
    visited[curr[0]][curr[1]] = True
    dist += arr[curr[0]][curr[1]]
    if dist > min_ans:
        return

    elif curr[0] == N-1 and curr[1] == N-1:
        if dist < min_ans:
            min_ans = dist
        return

    for i in range(2):
        ny = curr[0] + dy[i]
        nx = curr[1] + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            dfs([ny,nx], dist)
            visited[ny][nx] = False


for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    dx = [1,0]
    dy = [0,1]
    min_ans = 987654321

    dfs([0,0],0)
    print("#{} {}" .format(tc,min_ans))