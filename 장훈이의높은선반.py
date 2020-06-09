for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    p_heights = []
    smallest = 987654321

    for i in range(1 << N):
        height = 0
        for j in range(N):
            if i&(1<<j):
                height += heights[j]
        if B <= height <= smallest:
            smallest = height

    print("#{} {}" .format(tc, smallest-B))


#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
