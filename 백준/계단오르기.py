#DP 문제

import sys

steps = [0]

n = int(sys.stdin.readline())

for i in range(n):
    steps.append(int(sys.stdin.readline()))

if n == 2 or n == 1:
    print(sum(steps))

else:
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = steps[1]
    dp[2] = max(steps[1]+steps[2], steps[2])
    dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

    #점화식1
    # dp[n-3] + steps[i-1] + steps[i]

    #점화식2
    #dp[n-2] + steps[i]

    for i in range(4,n+1):
        
        dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])

    print(dp[n])



