# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:44:57 2022

@author: Russell J Adams
"""

def find_nth_prime(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    # A value in prime[i] will finally be
    # false if i is Not a prime, else true.
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False
    p = 2
    primes = []  # list to store the prime numbers
    while (p * p <= n):

        # If prime[p] is not changed, then it
        # is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False

        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

    # return the 10001st prime number
    return primes[10000]

# Test the function
print(find_nth_prime(200000))