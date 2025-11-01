def solution(N):
    """
    Find the sum of all the even terms in the Fibonacci sequence that do not exceed N.

    Parameters
    ----------
    N : int
        The maximum sum

    Returns
    -------
    sum : int
        The sum of the even terms
    """
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] <= N:
        fibonacci_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(fibonacci_num)

    sum = 0
    for n in fibonacci_seq[:-1]:
        if n % 2 == 0:
            sum += n
    return sum

def main():
    y = solution(4000000)
    print(y)

if __name__ == "__main__":
    main()
