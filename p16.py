def solution(N):
    """
    Find the sum of the digits of the number 2 raised to the power of N

    Parameters
    ----------
    N: int
        The power

    Returns
    -------
    sum : int
        The sum of digits
    """
    product = 2 ** N
    sum = 0
    for n in str(product):
        sum += int(n)
    return sum

def main():
    y = solution(1000)
    print(y)

if __name__ == "__main__":
    main()
