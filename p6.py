def solution(N):
    """
    Find the difference between the square of the sum and sum of the squares of the first N natural numbers. 

    Parameters
    ----------
    N: int
        The maximum natural number

    Returns
    -------
    diff : int
        The difference between square of sum and sum of squares
    """
    sum_squares = 0
    squared_sum = 0
    for i in range(1, N+1):
        sum_squares += i ** 2
        squared_sum += i

    squared_sum **= 2
    diff = squared_sum - sum_squares
    return diff

def main():
    y = solution(100)
    print(y)

if __name__ == "__main__":
    main()
