def solve_knapsack(N, C, weights, values):
    # 创建动态规划表
    dp = [[0] * (C + 1) for _ in range(N + 1)]
    
    # 填充dp表
    for i in range(1, N + 1):
        for w in range(C + 1):
            if weights[i-1] <= w:
                # 可以放入当前物品
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # 不能放入当前物品
                dp[i][w] = dp[i-1][w]
    
    return dp[N][C]

# 测试
N, C = 4, 10
weights = [1, 1, 9, 3]
values = [3, 4, 10, 6]

result = solve_knapsack(N, C, weights, values)
print(result)  # 应该输出9，因为我们可以选择商品1和3（总重量=2，总价值=7）
