# Fractional Knapsack using Greedy Method

# Function to solve Fractional Knapsack
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    # Step 1: Calculate value/weight ratio
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Step 2: Sort items based on ratio in decreasing order
    ratio.sort(key=lambda x: x[0], reverse=True)
    
    total_value = 0.0
    fractions = [0] * n  # Fraction of each item taken

    for i in range(n):
        val, value, weight = ratio[i]
        if capacity >= weight:
            # Take full item
            capacity -= weight
            total_value += value
            fractions[i] = 1
        else:
            # Take fraction of item
            fraction = capacity / weight
            total_value += value * fraction
            fractions[i] = fraction
            break  # Knapsack is full

    return total_value, ratio, fractions

# -------- Main Program --------
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    values = []
    weights = []

    for i in range(n):
        v = float(input(f"Enter value of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        values.append(v)
        weights.append(w)

    capacity = float(input("Enter capacity of knapsack: "))

    max_value, ratio, fractions = fractional_knapsack(values, weights, capacity)

    print("\nItem\tValue\tWeight\tFraction taken")
    for i in range(n):
        if i < len(ratio):
            print(f"{i+1}\t{ratio[i][1]}\t{ratio[i][2]}\t{fractions[i]:.2f}")
        else:
            print(f"{i+1}\t{values[i]}\t{weights[i]}\t0.00")

    print(f"\nMaximum value in Knapsack = {max_value:.2f}")
