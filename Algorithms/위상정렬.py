import sys
from collections import deque

sys.stdin = open("Algorithms/위상정렬.txt","r")


n = 7
graph = [[0]*n for _ in range(n)]
q = deque()
in_degree = [0]*n
answer = []

for i in range(6):
    a, b = input().split(" ")
    a, b = int(a), int(b)
    graph[a][b] = 1
    in_degree[b] += 1

for i in range(1,n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    answer.append(current)
    for i in range(1,n):
        if graph[current][i] == 1:
            in_degree[i] -= 1
            graph[current][i] = 0
            if in_degree[i] == 0:
                q.append(i)

print("answer", answer)
