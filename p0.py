def solution(N):
    """
    Find the sum of all the odd squares for the first N square numbers.

    Parameters
    ----------
    N : int
        The number of odd squares

    Returns
    -------
    sum : int
        The sum of the odd squares
    """
    sum = 0
    for i in range(N+1):
        if i % 2 != 0:
            sum += i ** 2
    return sum

def main():
    y = solution(754000)
    print(y)

if __name__ == "__main__":
    main()
