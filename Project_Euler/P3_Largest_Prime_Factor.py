def largest_prime_factor(n):
    # Initialize the largest prime factor to be 1
    largest_prime_factor = 1
    
    # Start from 2, and check if each number is a factor of n
    for i in range(2, n+1):
        # If i is a factor of n, divide n by i until it is not divisible by i anymore
        while n % i == 0:
            # Update the value of n and the largest prime factor
            n = n / i
            largest_prime_factor = i
    
    # Return the largest prime factor
    return largest_prime_factor
    
    