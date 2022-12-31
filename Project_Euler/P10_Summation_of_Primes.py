def sieve(n):
    primes = {}
    for i in range(1,n+1):
        primes[i] = True
    primes[1] = False
    for i in range(2,n+1):
        for j in range(i+i, n+1, i):
            primes[j] = False
    return primes

# get the sum of all primes below 2,000,000
p = sieve(2000000)
total = 0
for i in range(1,2000000):
    if p[i]:
        total+=i
print(total)

    
