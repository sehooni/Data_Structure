'''LCS with DP'''

# 문자열 입력 받기
m = '' + input()
n = '' + input()

# 빈 수열 만들기
dp = [[0]*(len(n)+1) for i in range(len(m)+1)]

# [0]행과 [0]열은 0으로 두고 나머지 부분 DP 진행

for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        if m[i-1] == n[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1     # 대각선 방향 값으로 +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
# print(dp)