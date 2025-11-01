def solution(N):
    """
    Find the sum of all the primes below N.

    Parameters
    ----------
    N: int
        The maximum prime number

    Returns
    -------
    sum : int
        The sum of the prime numbers
    """
    sum = 2
    for n1 in range(3, N):
        if n1 % 2 != 0:
            MAX_PRIME_FACTOR = int(n1 ** 0.5)
            is_prime = True
            for n2 in range(3, MAX_PRIME_FACTOR+1, 2):
                if n1 % n2 == 0:
                    is_prime = False
                    break
            if is_prime:
                sum += n1
    return sum

def main():
    y = solution(2000000)
    print(y)

if __name__ == "__main__":
    main()