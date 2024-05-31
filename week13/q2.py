n = int(input('多少階梯? '))

dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp)
print(f"Step: {dp[n]}")
