def solution(N):
    """
    The collatz sequence is defined by the following rules:
        If n is even then n -> n / 2
        If n is odd then n -> 3n + 1
    Find the starting number, below N, with the longest collatz sequence.

    Parameters
    ----------
    N: int
        The maximum starting number

    Returns
    -------
    longest_collatz : int
        The starting number with the longest collatz sequence 
    """    
    start = 1
    longest_collatz = 1
    for n in range(1, N):
        n_start = n
        collatz_len = 1
        while n_start != 1:
            if n_start % 2 == 0:
                n_start /= 2
            else:
                n_start = 3 * n_start + 1
            collatz_len += 1

        if collatz_len > longest_collatz:
            start = n
            longest_collatz = collatz_len
    return start

def main():
    y = solution(1000000)
    print(y)

if __name__ == "__main__":
    main()
