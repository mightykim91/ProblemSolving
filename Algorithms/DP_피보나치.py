dp_bu = [0,1]

def topdown(n, dp):
    if n == 0: return 0
    if n == 1: return 1
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = topdown(n-1, dp) + topdown(n-2, dp)
    return dp[n]


def bottomup(n):
    for i in range(2, n+1):
        dp_bu.append(dp_bu[i-1] + dp_bu[i-2])
    return dp_bu[n]

if __name__ == "__main__":
    answer = bottomup(100)
    print("answer", answer)

    n = 100
    dp_td = [-1]*(n+1)
    answer_td = topdown(n, dp_td)
    print("td_answer", answer_td)
    
    