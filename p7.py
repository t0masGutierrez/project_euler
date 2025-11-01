def solution(N):
    """
    Find the Nth prime number.

    Parameters
    ----------
    N: int
        The index of the prime number

    Returns
    -------
    Nth_prime : int
        The Nth prime number
    """
    i = 2
    primes = []
    while len(primes) < N:
        is_prime = True
        for p in primes:
            remainder = i % p
            if remainder == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1

    Nth_prime = primes[-1]
    return Nth_prime

def main():
    y = solution(10001)
    print(y)

if __name__ == "__main__":
    main()
