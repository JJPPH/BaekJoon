n, m = map(int, input().split())

dp = [0] * 101
dp[0] = 1
dp[1] = 1
for i in range(2, 101):
    dp[i] = i * dp[i - 1]

if dp[n] % dp[n - m] == 0:
    print((dp[n] // (dp[n - m]) // dp[m]))
else:
    print((dp[n] // (dp[m]) // dp[n - m]))
