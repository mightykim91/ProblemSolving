from collections import deque

def bfs(n):
    global count
    q = deque([[n, 0]])
    while q:
        number, cnt = q.popleft()
        if number == M:
            count = cnt
            return

        for i in range(4):
            if i == 0 and 0 < number+1 <= 1000000 and counts[number+1] != 1:
                q.append([number + 1, cnt+1])
                counts[number + 1] = 1
            elif i == 1 and 0 < number-1 <= 1000000 and counts[number-1] != 1:
                q.append([number - 1, cnt+1])
                counts[number - 1] = 1
            elif i == 2 and 0 < number*2 <= 1000000 and counts[number*2] != 1:
                q.append([number * 2, cnt+1])
                counts[number * 2] = 1
            elif i == 3 and 0 < number+10 <= 1000000 and counts[number-10] != 1:
                q.append([number - 10, cnt+1])
                counts[number - 10] = 1

for tc in range(1,int(input())+1):
    counts = [0]*1000001
    count = 0
    N, M = map(int, input().split())
    counts[N] = 1
    bfs(N)
    print("#{} {}".format(tc, count))

