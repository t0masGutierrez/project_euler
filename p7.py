from matplotlib import pyplot as plt

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
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
