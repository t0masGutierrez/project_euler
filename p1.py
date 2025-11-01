def solution(multiples, N):
    """
    Find the sum of all the multiples below N.

    Parameters
    ----------
    multiples : list
        List of integers being multiplied
    N : int
        The maximum multiple

    Returns
    -------
    sum : int
        The sum of the multiples
    """
    sum = 0
    for i in range(N):
        for m in multiples:
            if i % m == 0:
                sum += i
                break
    return sum

def main():
    y = solution([3, 5], 1000)
    print(y)

if __name__ == "__main__":
    main()
