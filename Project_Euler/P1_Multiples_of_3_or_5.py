def sum_multiples(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print(sum_multiples(1000))  # Output: 233168
