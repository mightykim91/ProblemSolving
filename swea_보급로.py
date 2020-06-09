from collections import deque

def isValid(y,x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def bfs(y,x):
    q = deque([(y,x)])
    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]
    while q:
        curr_y, curr_x = q.popleft()
        for i in range(4):
            ny = curr_y + dy[i]
            nx = curr_x + dx[i]
            if isValid(ny,nx):
                if visited[ny][nx] == inf:
                    visited[ny][nx] = visited[curr_y][curr_x] + arr[ny][nx]
                    q.append((ny, nx))
                else:
                    if visited[ny][nx] > visited[curr_y][curr_x] + arr[ny][nx]:
                        visited[ny][nx] = visited[curr_y][curr_x] + arr[ny][nx]
                        q.append((ny, nx))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    #print(arr)
    inf = float('inf')
    visited = [[inf]*N for _ in range(N)]
    visited[0][0] = 0
    bfs(0,0)
    print("#{} {}" .format(tc, visited[-1][-1]))
    #print(visited)
