from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1

    visited = [False]*(N+1)
    q = deque([(1,0)])
    visited[1] = True
    cnt = 0
    while q:
        curr, level = q.popleft()
        for i in range(N+1):
            if arr[curr][i] == 1 and not visited[i]:
                cnt += 1
                visited[i] = True
                if level < 1:
                    q.append((i,level+1))


    print("#{} {}".format(tc,cnt))

