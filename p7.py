"""
Find the 10001st prime number. 
"""

count = 2
primes = []
while len(primes) < 10001:
    is_prime = True
    for p in primes:
        remainder = count % p
        if remainder == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(count)
    count += 1

nth_prime = primes[-1]
print(nth_prime)