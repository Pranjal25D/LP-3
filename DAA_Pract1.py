# Fibonacci Number Calculator
# Non-Recursive (Iterative) and Recursive Versions

# DAA Practical 1. Write a program non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity.


# -------- Iterative Fibonacci Function --------
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_seq = [0, 1]  # first two Fibonacci numbers
    for i in range(2, n):
        next_fib = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_fib)
    return fib_seq

# -------- Recursive Fibonacci Function --------
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = fibonacci_recursive(n-1)
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# -------- Main Program --------
def main():
    print("Fibonacci Number Calculator")
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    
    # Iterative Fibonacci
    iterative_result = fibonacci_iterative(n)
    print("\nIterative Fibonacci sequence:")
    print(iterative_result)
    print("Time Complexity: O(n), Space Complexity: O(n)")
    
    # Recursive Fibonacci
    recursive_result = fibonacci_recursive(n)
    print("\nRecursive Fibonacci sequence:")
    print(recursive_result)
    print("Time Complexity: O(2^n), Space Complexity: O(n) (due to recursion stack)")

if __name__ == "__main__":
    main()
