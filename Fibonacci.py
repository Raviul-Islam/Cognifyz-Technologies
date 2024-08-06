def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    
    return sequence

n = int(input("Enter the number of terms: "))
sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms:")
print(sequence)