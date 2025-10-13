"""
What is the largest prime factor of the number 600851475143?
"""

n = 600851475143
max = int(n ** 0.5)
prime_factors = []

for i in range(2, max):
    divisible = n % i == 0
    multiple = False

    for p in prime_factors:
        if i % p == 0:
            multiple = True

    if divisible and not multiple:
        prime_factors.append(i)

largest_prime_factor = prime_factors[-1]

print(prime_factors)
print(f"largest prime factor = {largest_prime_factor}")