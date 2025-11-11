# 0-1 Knapsack Problem using Dynamic Programming

def knapsack_01(values, weights, capacity):
    n = len(values)
    # Create DP table of size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Find items included in knapsack
    w = capacity
    items_taken = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items_taken.append(i)  # item i is included
            w -= weights[i-1]

    items_taken.reverse()  # optional: to show items in input order
    return dp[n][capacity], items_taken

# -------- Main Program --------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = []
    weights = []

    for i in range(n):
        v = int(input(f"Enter value of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        values.append(v)
        weights.append(w)

    capacity = int(input("Enter capacity of knapsack: "))

    max_value, items_taken = knapsack_01(values, weights, capacity)

    print(f"\nMaximum value in 0-1 Knapsack = {max_value}")
    print("Items included in the knapsack:", items_taken)
