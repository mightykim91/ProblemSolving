import math
import time

def dajikstra(graph, start):
    #create list to save nodes in path
    cost = 0
    visited = [False]*(N+1)
    visited[start] = True
    path = [start]

    #create list to save distance info from start
    distance = [math.inf]*(N+1)
    for i in range(len(distance)):
        distance[i] = graph[start][i]
    distance[start] = 0

    for i in range(N):
        min_node = 0
        min_distance = 11

        #find closest node
        for j in range(len(distance)):
            if distance[j] == 0:
                continue
            else:
                if min_distance > distance[j] and not visited[j]:
                    min_distance = distance[j]
                    min_node = j

        #add min_node to path and mark it as visited and update distance travelled
        visited[min_node] = True
        path.append(min_node)
        cost = min_distance

        #end search when target is reached
        if min_node == N:
            return cost

        #update distance data
        for k in range(len(distance)):
            if not visited[k]:
                if distance[min_node]+graph[min_node][k] < distance[k]:
                    distance[k] = distance[min_node] + graph[min_node][k]

    return cost

for tc in range(1, int(input())+1):
    #b = time.time()
    N, E = map(int, input().split())

    #make graph
    graph = [[math.inf]*(N+1) for _ in range(N+1)]
    data = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        data.append([start, end, weight])

    #insert input data into graph
    for i in range(len(data)):
        graph[data[i][0]][data[i][1]] = data[i][2]

    print("#{} {}" .format(tc,dajikstra(graph, 0)))
    #print(time.time()-b)
