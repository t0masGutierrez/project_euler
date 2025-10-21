"""
Find the sum of all the primes below two million.
"""

sum = 2
for n1 in range(3, 2000000):
    if n1 % 2 == 0:
        continue
    else:
        root = int(n1 ** 0.5)
        is_prime = True
        for n2 in range(3, root+1, 2):
            if n1 % n2 == 0:
                is_prime = False
                break
        if is_prime:
            sum += n1
print(sum)