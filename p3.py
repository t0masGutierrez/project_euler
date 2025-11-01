def solution(N):
    """
    Find the largest prime factor of N.

    Parameters
    ----------
    N : int
        The number being prime factorized

    Returns
    -------
    largest_prime_factor : int
        The largest prime factor
    """
    MAX_PRIME_FACTOR = int(N ** 0.5)
    prime_factors = []
    for i in range(2, MAX_PRIME_FACTOR):
        divisible = N % i == 0
        multiple = False
        for p in prime_factors:
            if i % p == 0:
                multiple = True

        if divisible and not multiple:
            prime_factors.append(i)

    largest_prime_factor = prime_factors[-1]
    return largest_prime_factor

def main():
    y = solution(600851475143)
    print(y)

if __name__ == "__main__":
    main()
